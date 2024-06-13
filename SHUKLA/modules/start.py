# © @SHIVANSHDEVS

from telethon import __version__, events, Button
from config import X1

# Constants
START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/astaad_majhablock"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/panjabichatting")
    ],
    [Button.url("• ᴍᴀɴʙᴇᴇʀ •", "https://t.me/MANBEERVIRK6862")]
]

IMAGE_URL = "https://graph.org/file/90005b1183ad8c817ff12.jpg"
PYTHON_VERSION = "3.11.3"
STRANGER_VERSION = "M 1.8.31"

async def get_bot_info(event):
    SHEKHAR = await event.client.get_me()
    bot_name = SHEKHAR.first_name
    bot_id = SHEKHAR.id
    return bot_name, bot_id

def create_start_text(bot_name, bot_id, sender_name, sender_id):
    return (
        f"**ʜᴇʏ​ [{sender_name}](tg://user?id={sender_id}),\n\n"
        f"ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [MANBEER](https://t.me/MANBEERVIRK6862)**\n\n"
        f"» **ᴍᴀɴʙᴇᴇʀ V2 :** `{STRANGER_VERSION}`\n"
        f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{PYTHON_VERSION}`\n"
        f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n"
        "━━━━━━━━━━━━━━━━━"
    )

@X1.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        bot_name, bot_id = await get_bot_info(event)
        start_text = create_start_text(bot_name, bot_id, event.sender.first_name, event.sender.id)
        await event.client.send_file(
            event.chat_id,
            IMAGE_URL,
            caption=start_text,
            buttons=START_BUTTON
        )
