from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_ready():
    print("Botは正常に起動しました！")
    print(bot.user.name)  # Botの名前
    print(bot.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await bot.change_presence(activity=discord.Game(name=f"TEST{len(bot.guilds)}"))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
