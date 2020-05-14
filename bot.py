from config import *
from twitchio.ext import commands
import random

bot = commands.Bot(
    irc_token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=CHANNEL
)

@bot.event
async def event_ready():
    print(f"{BOT_NICK} is online!")
    ws = bot._ws

@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == BOT_NICK.lower():
        return
    await bot.handle_commands(ctx)
    print(f'{ctx.channel} - {ctx.author.name}: {ctx.content}')

@bot.command(name='roll')
async def roll(ctx):
    rollNum = ctx.content.split(' ')
    print(rollNum)
    if len(rollNum) > 1 and rollNum[1].isnumeric():
        print(rollNum[1])
        await ctx.channel.send(f"{ctx.author.name} rolled a {random.randrange(0,int(rollNum[1]),1)}!")
    elif len(rollNum) > 1 and rollNum[1].lower() == 'help':
        await ctx.channel.send(f"{ctx.author.name}, you can specify a number to roll between 0 and the number specified. If you do not specify a number, you will roll 100.")
    elif len(rollNum) > 1 and rollNum[1].lower() != 'help':
        await ctx.channel.send(f"{ctx.author.name}, you did not select a number to roll")
    else:
        await ctx.channel.send(f"{ctx.author.name} rolled a {random.randrange(0,100,1)}!")

if __name__ == "__main__":
    bot.run()