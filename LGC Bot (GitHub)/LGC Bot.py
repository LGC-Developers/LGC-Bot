import discord
from discord.ext import commands
from discord import client


print("Il bot si sta avviando...")
token = ""
client = commands.Bot(command_prefix=("g!"))

@client.event

async def on_ready():
   print(client.user,"é ora ONLINE","(ID ",client.user.id,")")

@client.event

async def on_message(message):
   if message.content == "g!Hello":
      await message.channel.send("Welcome to the server!")


client.run(token)
