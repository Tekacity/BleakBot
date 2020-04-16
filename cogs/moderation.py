import discord
from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member):
      role = discord.utils.get(member.guild.roles, name="/dev/null")
      await member.add_roles(role)
      embed=discord.Embed(description="{0} has been muted by {1}".format(member, ctx.message.author))
      embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name="**Reason:**", value="T", inline=False)
  
      await ctx.send(embed=embed)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member):
      role = discord.utils.get(member.guild.roles, name="/dev/null")
      await member.remove_roles(role)
      embed=discord.Embed(description="{0} has been unmuted by {1}".format(member, ctx.message.author))
      embed.set_thumbnail(url=member.avatar_url)
      await ctx.send(embed=embed)
    
    
def setup(bot):
  bot.add_cog(Moderation(bot))
  
  
  
  
  