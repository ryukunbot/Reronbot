from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='r?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('おはよ')

@bot.command()
async def おやすみ(ctx):
    await ctx.send('おやすみ')

    
bot.run(token)
