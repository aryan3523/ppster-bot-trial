import os
from pyrogram import Client, filters
from 
# Replace with your own API ID and API Hash
API_ID = "9590156"
API_HASH = "368a346bb1b206b650f2b3b37f91e237"
BOT_TOKEN = "6032731588:AAHjrlORAsAc7uyk1RRduStbk33mh-6RRf"

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
        
@app.on_message(filters.text)
def echo(client, message):
    message.reply(f"You said: {message.text}")

if __name__ == "__main__":
    app.run()