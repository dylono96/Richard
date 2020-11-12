import discord
from discord.ext import commands
import os

client = commands.Bot(commands.when_mentioned_or('pp '))
token = os.getenv("DISCORD_BOT_TOKEN")


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='Dylan'))
    print('Richard is er klaar voor!')


client.run(token)
