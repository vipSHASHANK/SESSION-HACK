import env
from Hack import bot
from Hack.helpers import MENU1, KEYBOARD1
from Hack.database import DB
from telethon import events, Button

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    id = event.sender_id
    mention = f"[{event.sender.first_name}](tg://user?id={id})"
    TEXT = (
        "ʜᴇʏ  {}, ɪ ᴀᴍ ᴀ sᴇssɪᴏɴ ʜᴀᴄᴋᴇʀ ʙᴏᴛ sᴜᴘᴘᴏʀᴛɪɴɢ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ "
        "ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ sᴛʀɪɴɢ. ᴛʏᴘᴇ /hack ᴛᴏ sᴇᴇ ᴍᴇɴᴜ"
    )
    SHUKLA = "https://files.catbox.moe/ihj4vm.jpg"
    
    BUTTON = [
        [Button.url("🍁 sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ 🍁", "https://t.me/StringSesssionGeneratorRobot")],
        [Button.url("🌿 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🌿", "https://t.me/StrangerAssociation/539")],
        [
            Button.url("⌯ ˹sʜɪᴠᴀɴsʜ ʜᴇʀᴇ˼ 🇮🇳", "https://t.me/SHIVANSHDEVS"),
            Button.url("ᴜᴘᴅᴀᴛᴇ ❄️️️", "https://t.me/StrangerAssociation"),
        ],
        [Button.url("𝆺𝅥⃝ᶦϻ‌ ˢʰⁱᵛ ≛⃝🇸𝐇𝐈𝐕𝐀𝐍⃝⃝⃪⃕𝐒𝐇❣𓆩ꭙ𝗗𓆪ꪾ🥀⃝⃪•๋๋๋๋๋๋๋๋๋๋๋๋๋•๋๋๋๋๋๋๋≛", 
                    "https://t.me/ITSZ_SHIVANSH")],
    ]
    
    # Send photo with caption and inline buttons
    await bot.send_file(
        event.chat_id,
        file=SHUKLA,
        caption=TEXT.format(mention),
        buttons=BUTTON
    )
    
    # Add user to database if DB is enabled
    if DB:
        await DB.add_user(id)
    
    # Log user in LOG_GROUP_ID if it is set
    if env.LOG_GROUP_ID:
        await bot.send_message(
            env.LOG_GROUP_ID,
            f'{mention} Has Just Started The Bot'
        )

@bot.on(events.NewMessage(pattern="/hack"))
async def hack(event):
    if not event.is_private:
        return await event.reply("You can't use me in groups.")
    await event.reply(MENU1, buttons=KEYBOARD1)
