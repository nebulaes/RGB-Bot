import discord, os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time, json, ranks as data, requests
from discord.voice_client import VoiceClient

bot=discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready")
    for server in bot.servers:
        for channel in server.channels:
            if channel.id == "463789709341097984":
                global c
                c = channel

    time2 =str(time.strftime("%I:%M")+" GMT")
    await bot.change_presence(game=discord.Game(name=time2))
    async for message in bot.logs_from(c, limit=1):
        await bot.delete_message(message)
    embed=discord.Embed(title="Server Rules:", color=0xf07e00)
    embed.set_author(name="RULES: ACCEPT RULES BY CLICKING GREEN TICK")
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
    channel = reaction.message.channel
    role = discord.utils.get(user.server.roles, name="⋑-Members-⋐")
    role2 = discord.utils.get(user.server.roles, name="New")
    if reaction.emoji == '✅' and channel == c:
        try:
            await bot.add_roles(user, role)
        except Exception:
            pass
        try:
            await bot.remove_roles(user, role2)
        except Exception:
            pass

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
async def now(ctx, text):
    ttsvalue = str(text)
    if ttsvalue.lower() == "yes" :
        ttsvalue = "True"
    if ttsvalue.lower() == "no":
        ttsvalue = "False"
    else:
        ttsvalue = "False"
    

    time2 = time.strftime("%I %M")
    text = "The Time Is "+time2
    await bot.send_message(ctx.message.channel, text, tts=bool(ttsvalue))
        
@bot.event
async def on_message(message):
   if message.content.startswith("👏👏") or message.content.startswith("👏 👏"):
        await bot.send_message(message.channel,"***MEME REVIEW***")
   else:
   		pass
   try:
        await bot.process_commands(message)
   except Exception:
        pass

@bot.command(pass_context=True)
async def hmm(ctx):
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=1):
        await bot.delete_message(message)
    await bot.send_message(channel, "HmmMmMMMmmmMmMmMMMmmmMm")
    


@bot.command(pass_context=True)
async def rules(ctx):
    message = ctx.message
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=1):
        await bot.delete_message(message)
    msg = await bot.say("RULES \n -No Toxicity \n -No Spamming \n -No Posting DMs \n -No Racism \n -No Posting or using Faces (Even Blurred) Without Permission \n -If You Join A Call And Are Asked To Mute Your Mic, Mute It \n -If Moved Out A Chat, Don't Move Back \n -Respect All Members \n -Respect Admins And Listen To Them")
    print(msg)

async def timeloop():
    await bot.wait_until_ready()
    while not bot.is_closed:
        time2 =str(time.strftime("%I:%M")+" GMT")
        await bot.change_presence(game=discord.Game(name=time2, type=3))
        await asyncio.sleep(1)
        await bot.change_presence(game=discord.Game(name=time2, type=3))
        await asyncio.sleep(15)
        await bot.process_commands(message)
    
bot.loop.create_task(timeloop())
bot.run(os.getenv('TOKEN'))
