import os
from pyrogram import Client, filters
from prime import *
from bookmyshow import *
# Replace with your own API ID and API Hash
API_ID = "9590156"
API_HASH = "368a346bb1b206b650f2b3b37f91e237"
BOT_TOKEN = "7346471184:AAGerFMfoKR2MljNmWIuZdj9PIlVgPifkhw"

# Create the bot client
app = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello! I'm your bot. How can I assist you?")

@app.on_message(filters.command("help"))
def handle_ask(client, message):
    if len(message.command) > 1:
        org_text = message.text.split(maxsplit=1)[1]
        message.reply(org_text)
    else:
        message.reply("Please write your query along with /ask command.")
 
@app.on_message(filters.command("amzn"))
async def handle_amzn_command(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a valid Amazon Prime Video URL after the /amzn command.")
        return
    
    url = message.command[1]
    if "primevideo.com" in url:
        covershot_url = scrape_amazon_prime_covershot(url)
        await message.reply_text(covershot_url)
    else:
        await message.reply_text("Please send a valid Amazon Prime Video URL.")

@app.on_message(filters.command("bms"))
async def handle_bms_command(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a valid BMS URL after the /bms command.")
        return
    
    url = message.command[1]
    if "bookmyshow" in url:
        poster_url = bms_poster(url)
        await message.reply_text(poster_url)
    else:
        await message.reply_text("Please send a valid BookMyShow URL.")                

if __name__ == "__main__":
    app.run()
