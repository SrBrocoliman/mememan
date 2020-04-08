import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot listo.")

@client.event
async def on_message(message):
    if ("http" in message.content) || (len(message.embeds) > 0) :
        message.channel.send("UNO MAS!")

client.run('Njk3MTM5OTMyNTU2Mjk2Mjgz.Xo445w.f5Lew0cQmsNBNeHwlhruRktk97M')
