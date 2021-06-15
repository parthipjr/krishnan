from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⭕ Join Our Channel ⭕", url="https://t.me/filmy_beats")],
        [InlineKeyboardButton(
            "⭕ Join Our Group ⭕", url="https://t.me/moviemediazz")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info Welcome to @Fbutubebot, The Most Advanced utube Video and Audio Downloader in Telegram!
Please send any YouTube video link."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
