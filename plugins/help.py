from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"An easy youtube video downloader telegram bot made by Papy"
    await message.reply_text(helptxt)
