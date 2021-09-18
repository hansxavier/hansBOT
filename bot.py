import os
import discord
import requests
import json

from discord.ext import commands

from main_cog import main_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/')

bot.remove_command('help')

bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))

token  = os.getenv('TOKEN')
bot.run(token)