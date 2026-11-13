# telegram-chat-to-pdf

Convert a Telegram Desktop chat export (`result.json`) into a clean, printable HTML file, then save it as PDF from your browser. Offline, no upload, one Python file, no dependencies.

Handles single-chat exports and full-account exports, formatted text, photos/files/stickers (shown as placeholders) and service messages.

## Usage

1. In Telegram Desktop: open the chat, then *⋮ > Export chat history*, choose **Format: Machine-readable JSON**. You get `result.json`.
2. Run:

```bash
python3 telegram_to_html.py result.json > chat.html
```

3. Open `chat.html` in a browser and use *Print > Save as PDF*.

## Need it as evidence?

For court, HR, insurance, landlord or police files, the free script is not enough: you usually need numbered messages, a cover sheet, page numbers and a hash so the document can be shown to be unaltered.

**[ChatExhibit](https://martincrescenzo-dotcom.github.io/chatexhibit/)** does that in the browser (nothing is uploaded): numbered transcript, cover sheet, page "x of y", SHA-256 of the original export. Also supports WhatsApp, Signal, Messenger, Instagram, Discord, Slack, Google Chat, LINE and KakaoTalk. Preview free, €9 one-time for the full PDF.

See also: [whatsapp-chat-to-pdf](https://github.com/martincrescenzo-dotcom/whatsapp-chat-to-pdf), [discord-chat-to-pdf](https://github.com/martincrescenzo-dotcom/discord-chat-to-pdf).

## License

MIT
