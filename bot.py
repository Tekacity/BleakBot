import discord
from discord.ext import commands
import logging
import requests
import json

logging.basicConfig(level=logging.INFO)

with open('token.json') as token_file:
    data = json.load(token_file)

TOKEN = data['token']


def get_prefix(bot, message):
   
    prefixes = ['b!', './']

    if not message.guild:
        
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)
    
    

bot = commands.Bot(command_prefix=get_prefix, description='BleakBot by Tek')




initial_extensions = ['cogs.moderation', 'cogs.misc']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    
    print("We have logged in as {0.user}".format(bot))

    

bot.run(TOKEN, bot=True, reconnect=True)