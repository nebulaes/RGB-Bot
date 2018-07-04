import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time, json, ranks as data, requests
from discord.voice_client import VoiceClient

bot=discord.Client()
bot = commands.Bot(command_prefix="!")

startup_extensions = ["Music"]

@bot.event
async def on_ready():
    print("Ready")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot
        
##
##@client.command(pass_context=True)
##async def spam(ctx, name, x=5):
##    print(ctx)
##    channel = ctx.message.channel
##    async for message in client.logs_from(channel, limit=1):
##        await client.delete_message(message)
##    try:
##        x = int(x)
##    except Exception:
##        pass
##    while x >= 1:
##        await client.say(str(name))
##        async for message in client.logs_from(channel, limit=1):
##            await client.delete_message(message)
##        x -= 1


@bot.command(pass_context=True)
async def banner(ctx):
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=1):
            await bot.delete_message(message)
    await bot.send_file(channel,"NebulaRender3.jpg")

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)+1):
        messages.append(message)
    try:
        await bot.delete_messages(messages)
        await bot.say("Messages Deleted.")
        async for message in client.logs_from(channel, limit=1):
            time.sleep(2)
        await bot.delete_message(message)
    except:
        await bot.say("An Error Has Occured. Please Try Again")
        async for message in bot.logs_from(channel, limit=1):
            time.sleep(2)
        await bot.delete_message(message)

@bot.command(pass_context=True)
async def rank(ctx, name):
    n = str(name)
    url = "https://api.r6stats.com/api/v1/players/%s/seasons?platform=uplay" % name
    r = requests.get(url)
    player = json.loads(r.text)
    if 'status' in player.keys() and 'failed' in player['status']:
        return False
    elif not player['seasons']:
        return 'Bronze'
    rank = data.ranks[player['seasons'][list(player['seasons'].keys())[0]]['emea']['ranking']['rank'] - 1]['label']
    if n == "tamarix.brt" or n == "Tamarix.brt" or n == "tamarix-brt" or n == "Tamarix-brt" or n == "tamarix_yt":
        await bot.say("Gold")
    elif n == "hitman._." or n == "Hitman._.":
        await bot.say("Never Diamond")
    else:
        await bot.say(rank)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to Load Extension')
        
bot.run(os.getenv('TOKEN'))
