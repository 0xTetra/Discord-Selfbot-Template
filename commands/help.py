"""
This file contains an example command, which is a command that will display all other commands;
also known as the `help` command.

You can use this file as a base idea to create other commands,
because they are all structured similarly.
"""

import discord
from discord.ext import commands

import sys
from datetime import datetime

from utils import prefix


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(title='Command List', color=0xfffff,
        description=f'Prefix: {prefix}')
        helpEmbed.add_field(name='Category 1', value='`command1` `command2` `command3`')
        helpEmbed.add_field(name='Category 2', value='`command1` `command2` `command3`')
        helpEmbed.add_field(name='Category 3', value='`command1` `command2` `command3`')
        helpEmbed.timestamp = datetime.now()

        await ctx.send(embed=helpEmbed)


def setup(bot):
    bot.add_cog(Help(bot))
