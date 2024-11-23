import env
from Hack import bot
from Hack.helpers import MENU1, KEYBOARD1
from Hack.database import DB
from telethon import events, Button

# Handler for the /start command
@bot.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    try:
        id = event.sender_id
        mention = f"[{event.sender.first_name}](tg://user?id={id})"
        TEXT = (
            "ʜᴇʏ  {}, ɪ ᴀᴍ ᴀ sᴇssɪᴏɴ ʜᴀᴄᴋᴇʀ ʙᴏᴛ sᴜᴘᴘᴏʀᴛɪɴɢ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ "
            "ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ sᴛʀɪɴɢ. ᴛʏᴘᴇ /hack ᴛᴏ sᴇᴇ ᴍᴇɴᴜ"
        )
        SHUKLA = "https://files.catbox.moe/ihj4vm.jpg"
        
        # Define inline buttons
        BUTTON = [
            [Button.url("▪️sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ▪️", "https://t.me/StringSesssionGeneratorRobot")],
            [Button.url("▪️ғʀᴇᴇ ɪᴅ ᴜsᴇʀ-ʙᴏᴛ▪️", "https://t.me/Shukla_op_clone1bot")],
            [
                Button.url("▪️sᴜᴘᴘᴏʀᴛ▪️", "https://t.me/SHIVANSHDEVS"),
                Button.url("▪️ᴜᴘᴅᴀᴛᴇ▪️", "https://t.me/StrangerAssociation"),
            ],
            [Button.url("▪️sʜɪᴠᴀɴsʜ-xᴅ▪️",
                        "https://t.me/ITSZ_SHIVANSH")],
        ]
        
        # Send photo with caption and buttons
        await bot.send_file(
            event.chat_id,
            file=SHUKLA,
            caption=TEXT.format(mention),
            buttons=BUTTON
        )
        
        # Add user to the database if DB is configured
        if DB:
            await DB.add_user(id)
        
        # Log the user in the LOG_GROUP_ID if it is configured
        if env.LOG_GROUP_ID:
            await bot.send_message(
                env.LOG_GROUP_ID,
                f"{mention} Has Just Started The Bot"
            )
    except Exception as e:
        print(f"Error in /start command: {e}")

# Handler for the /hack command
@bot.on(events.NewMessage(pattern="^/hack$"))
async def hack(event):
    try:
        if not event.is_private:
            return await event.reply("You can't use me in groups.")
        await event.reply(MENU1, buttons=KEYBOARD1)
    except Exception as e:
        print(f"Error in /hack command: {e}")
