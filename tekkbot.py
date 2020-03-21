import discord
from discord.ext import commands
import logging
import requests
import json

logging.basicConfig(level=logging.DEBUG)
client = commands.Bot(command_prefix='t!')

with open('token.json') as tokenFile:
    data = json.load(tokenFile)

TOKEN = data['token']


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.command()
async def avatar(ctx, member: discord.User):
    ctx.message.au
    authorName = ctx.message.author
    authorUrl = ctx.message.author.avatar_url
    avatarUrl = member.avatar_url
    memberName = member 
    embed = discord.Embed(
        title = memberName,
        colour = discord.Color.blue() 
                    
    )
    embed.set_image(url=avatarUrl)
    embed.set_footer(text="Avatar requested by {}".format(authorName))  
    await ctx.send(embed=embed)

@client.command()
async def inspiro(ctx):
    inspiroGen = requests.get("https://inspirobot.me/api?generate=true")
    embed = discord.Embed(
       
        colour = discord.Color.green()
    )
    
    embed.set_image(url=inspiroGen.text)
    embed.set_footer(text="Image generated by InspiroBot", icon_url="https://inspirobot.me/favicon.ico")

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="/dev/null")
    await member.add_roles(role)
    embed=discord.Embed(description="{0} has been muted by {1}".format(member, ctx.message.author))
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="**Reason:**", value="T", inline=False)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="/dev/null")
    await member.remove_roles(role)
    embed=discord.Embed(description="{0} has been unmuted by {1}".format(member, ctx.message.author))
    embed.set_thumbnail(url=member.avatar_url)
    

    
 
    await ctx.send(embed=embed)

    

client.run(TOKEN)