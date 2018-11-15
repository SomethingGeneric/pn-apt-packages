import discord
from discord.ext import commands
import asyncio
import random
from time import sleep
import os
import subprocess

bot = commands.Bot(command_prefix='Alexa ', description="Alexa bot")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(description="Imma parrot")
async def echo(text=""):
    """Imma parrot"""
    await bot.say(text)

bot.run(input("Token: "))
