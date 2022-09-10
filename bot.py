# Done! Congratulations on your new bot. You will find it at t.me/klaipeda_molas_kite_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 5401619222:AAGK7MWUB8IzxhLyyYUuiYoX-JDDSuCljPY
# Keep your token secure and store it safely, it can be used by anyone to control your bot.

import logging

import telegram
import telegram.ext

import klaipeda_port_api_service
from klaipeda_port_api_service import get_data_from_api, ApiMethods

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# The API Key we received for our bot
API_KEY = "5401619222:AAGK7MWUB8IzxhLyyYUuiYoX-JDDSuCljPY"
# Create an updater object with our API Key
updater = telegram.ext.Updater(API_KEY)
# Retrieve the dispatcher, which will be used to add handlers
dispatcher = updater.dispatcher


# The entry function
def start(update_obj, context):
    update_obj.message.reply_text(klaipeda_port_api_service.build_message())
    return telegram.ext.ConversationHandler.END


def cancel(update_obj, context):
    # get the user's first name
    update_obj.message.reply_text("im feel bad, se you")
    return telegram.ext.ConversationHandler.END


# Create our ConversationHandler, with only one state
handler = telegram.ext.ConversationHandler(
    entry_points=[telegram.ext.CommandHandler('start', start)],
    states={
    },
    fallbacks=[telegram.ext.CommandHandler('cancel', cancel)],
)
# add the handler to the dispatcher
dispatcher.add_handler(handler)


# start polling for updates from Telegram
updater.start_polling()
# block until a signal (like one sent by CTRL+C) is sent
updater.idle()
