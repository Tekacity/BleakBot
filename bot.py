import discord
from discord.ext import commands
import logging
import requests
import json

logging.basicConfig(level=logging.DEBUG)
bot = commands.Bot(command_prefix='./')

with open('token.json') as token_file:
    data = json.load(token_file)

TOKEN = data['token']


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))





    

bot.run(TOKEN)