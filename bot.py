"""
This file will register the bot, it's prefix, load all of the commands, then run it using your discord account token.
To get your discord token, open developer tools (F12)
Storage -> Local Storage -> CTRL + F5 to refresh -> Scroll to the bottom and copy the "token" value.

If you have any questions regarding this template, contact me via Discord. - Tetra#4357
"""

import discord
from discord.ext import commands

import os
from commands.utils import token, prefix


bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')


for command in os.listdir('./commands'):
    if command.endswith('.py'):
        bot.load_extension(f'commands.{command[:-3]}')


bot.run(token, bot=False)
