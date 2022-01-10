from discord.ext import commands
from os import getenv
import traceback
import disordbot

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_ready(): # botが起動したときに動作する処理
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="with discord.py", type=1))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
