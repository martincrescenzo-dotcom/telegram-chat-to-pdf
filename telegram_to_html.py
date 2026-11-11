#!/usr/bin/env python3
"""Convert a Telegram Desktop chat export (result.json) to printable HTML.

Usage: python3 telegram_to_html.py result.json > chat.html
Then open chat.html in a browser and Print > Save as PDF. Offline, no dependencies.
"""
import html, json, sys


def text_of(msg):
    t = msg.get("text", "")
    if isinstance(t, list):
        t = "".join(p if isinstance(p, str) else p.get("text", "") for p in t)
    extra = []
    for k, label in (("photo", "photo"), ("file", "file"), ("sticker_emoji", "sticker")):
        if msg.get(k):
            extra.append(f"[{label}]")
    if msg.get("media_type") and not extra:
        extra.append(f"[{msg['media_type']}]")
    return (t + (" " if t and extra else "") + " ".join(extra)).strip()


def main(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    chats = data["chats"]["list"] if "chats" in data else [data]
    out = ["<!doctype html><meta charset='utf-8'><title>Telegram chat</title>",
           "<style>body{font:14px/1.45 system-ui,sans-serif;max-width:800px;margin:2em auto}"
           ".m{margin:.35em 0;page-break-inside:avoid}.d{color:#666;font-size:12px}"
           ".n{font-weight:600}.s{color:#888;font-style:italic}h2{margin-top:2em}</style>"]
    for chat in chats:
        out.append(f"<h2>{html.escape(chat.get('name') or 'Chat')}</h2>")
        for m in chat.get("messages", []):
            date = html.escape(m.get("date", "").replace("T", " "))
            body = html.escape(text_of(m)).replace("\n", "<br>")
            if m.get("type") == "service":
                action = html.escape(m.get("action", "service"))
                out.append(f"<div class='m s'><span class='d'>{date}</span> {html.escape(m.get('actor') or '')} {action}</div>")
                continue
            name = html.escape(m.get("from") or "")
            out.append(f"<div class='m'><span class='d'>{date}</span> <span class='n'>{name}:</span> {body}</div>")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
