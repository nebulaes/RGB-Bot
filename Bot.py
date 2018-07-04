import discord, os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time, json, ranks as data, requests
from discord.voice_client import VoiceClient

bot=discord.Client()
bot = commands.Bot(command_prefix="!")

##startup_extensions = ["Music"]

@bot.event
async def on_ready():
    print("Ready")
    for server in bot.servers:
        for channel in server.channels:
            if channel.id == "463789709341097984":
                c = channel

    await bot.change_presence(game=discord.Game(name="This Server"))
    async for message in bot.logs_from(c, limit=10):
        await bot.delete_message(message)
    await bot.send_file(c,"NebulaRender3.jpg")
    embed=discord.Embed(title="Server Rules:", color=0xf07e00)
    embed.set_author(name="RULES")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/259028945104666637/464161871511945228/Nebula_Logo_3.png")
    embed.add_field(name="1.", value="-No Toxicity", inline=True)
    embed.add_field(name="2.", value="-No Spamming", inline=True)
    embed.add_field(name="3.", value="-No Posting DMs Without Permission", inline=True)
    embed.add_field(name="4.", value="-No Racism", inline=True)
    embed.add_field(name="5.", value="-Respect Admins", inline=True)
    embed.add_field(name="6.", value="-Respect All Members", inline=True)
    embed.set_footer(text="Thank You.")
    msg = await bot.send_message(c, embed=embed)
    reaction = '✅'
    await bot.add_reaction(msg, reaction)



@bot.event
async def on_reaction_add(reaction, user):
    print("Added")
    role = discord.utils.get(user.server.roles, name="New")
    if reaction.emoji == '✅':
        await bot.add_roles(user, role)


##class Main_Commands():
##    def __init__(self, bot):
##        self.bot = bot
        
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
        await bot.delete_messages(messages)
        await bot.say("Messages Deleted.")
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

@bot.command(pass_context=True)
async def rules(ctx):
    message = ctx.message
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=1):
        await bot.delete_message(message)
    msg = await bot.say("RULES \n -No Toxicity \n -No Spamming \n -No Posting DMs \n -No Racism \n -No Posting or using Faces (Even Blurred) Without Permission \n -If You Join A Call And Are Asked To Mute Your Mic, Mute It \n -If Moved Out A Chat, Don't Move Back \n -Respect All Members \n -Respect Admins And Listen To Them")
    print(msg)
    reaction = '✅'
    await bot.add_reaction(msg, reaction)



##    reactors = cache_msg.get_reaction_users(react)
##    print(reactors)
##    for reactor in reactors:
##        await bot.add_roles(reactor, role)
##        print("added")
                    


            
##if __name__ == "__main__":
##    for extension in startup_extensions:
##        try:
##            bot.load_extension(extension)
##        except Exception as e:
##            exc = '{}: {}'.format(type(e).__name__, e)
##           print('Failed to Load Extension')
bot.run("NDYxMzA2NTgyOTU4MDgwMDEw.Dh5neA.i9OAI9ZECs0kyW8xhokaCQ7Fjq8")       
#bot.run(os.getenv('TOKEN'))
