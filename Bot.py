import discord, os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time, json, requests
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
            elif channel.id == "465584250129743874":
                global b
                b = channel
            elif channel.id == "463785244772794370":
                global w
                w = channel
            elif channel.id == "483791168111509504" or channel.name == "╠-ranks":
                global r
                r = channel
            elif channel.id == "483801660930523146":
                global ru
                ru = channel

    h = int(time.strftime("%I"))
    m = str(time.strftime("%M"))
    time2 = (str(h+1)+":"+m+" BST")
    await bot.change_presence(game=discord.Game(name=time2, type=3))
    async for message in bot.logs_from(c, limit=1):
        await bot.delete_message(message)    
    embed=discord.Embed(title="Server Rules:", color=0xf07e00)
    embed.set_author(name="RULES: ACCEPT RULES BY CLICKING GREEN TICK")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/259028945104666637/464161871511945228/Nebula_Logo_3.png")
    embed.add_field(name="1.", value="-No Toxicity", inline=False)
    embed.add_field(name="2.", value="-No Spamming", inline=False)
    embed.add_field(name="3.", value="-No Posting DMs Without Permission", inline=False)
    embed.add_field(name="4.", value="-No Racism", inline=False)
    embed.add_field(name="5.", value="-Respect Admins", inline=False)
    embed.add_field(name="6.", value="-Respect All Members", inline=False)
    embed.add_field(name="7.", value="-No NSFW", inline=False)
    embed.add_field(name="8.", value="-Nobody Skips Africa By Toto, Or They Get Banned", inline=False)
    embed.add_field(name="9.", value="ACCEPT RULES TO GAIN A ROLE BY CLICKING GREEN TICK", inline=False)
    embed.set_footer(text="Thank You.")
    msg = await bot.send_message(c, embed=embed)
    embed=discord.Embed(title="SERVER")
    embed.add_field(name="EU", value="React With: 🇪🇺", inline=False)
    embed.add_field(name="NA", value="React With: 🇺🇸", inline=True)
    async for message in bot.logs_from(b, limit=1):
        await bot.delete_message(message)
    msg2 = await bot.send_message(b, embed=embed)
    reaction = '✅'
    reactionDJ = '🎧'
    await bot.add_reaction(msg, reaction)
    await bot.add_reaction(msg, reactionDJ)
    reactionEU = '🇪🇺'
    reactionNA = '🇺🇸'
    await bot.add_reaction(msg2, reactionEU)
    await bot.add_reaction(msg2, reactionNA)   
    for x in bot.get_all_emojis():
        if x.name == "Copper":
            emojiCop = x
        elif x.name == "Bronze":
            emojiBro = x
        elif x.name == "Silver":
            emojiSil = x
        elif x.name == "Gold":
            emojiGol = x
        elif x.name == "Plat":
            emojiPla = x
        elif x.name == "Diamond":
            emojiDia = x
        elif x.name == "C_":
            emojiC = x
        elif x.name == "B_":
            emojiB = x
        elif x.name == "S_":
            emojiS = x
        elif x.name == "G_":
            emojiG = x
        elif x.name == "P_":
            emojiP = x
        elif x.name == "D_":
            emojiD = x
    
    async for message in bot.logs_from(r, limit=50):
        await bot.delete_message(message)
    embed=discord.Embed(title="Ranks")
    embed.add_field(name="Rank:", value="React With Appropriate Reaction To Add Role", inline=False)

    msgRank = await bot.send_message(r, embed=embed)
    await bot.add_reaction(msgRank, emojiCop)
    await bot.add_reaction(msgRank, emojiBro)
    await bot.add_reaction(msgRank, emojiSil)
    await bot.add_reaction(msgRank, emojiGol)
    await bot.add_reaction(msgRank, emojiPla)
    await bot.add_reaction(msgRank, emojiDia)

    async for message in bot.logs_from(ru, limit=50):
        await bot.delete_message(message)
    embed=discord.Embed(title="Ranks")
    embed.add_field(name="Rank:", value="React With Appropriate Reaction To Add Role", inline=False)
    msgRankUS = await bot.send_message(ru, embed=embed)
    await bot.add_reaction(msgRankUS, emojiC)
    await bot.add_reaction(msgRankUS, emojiB)
    await bot.add_reaction(msgRankUS, emojiS)
    await bot.add_reaction(msgRankUS, emojiG)
    await bot.add_reaction(msgRankUS, emojiP)
    await bot.add_reaction(msgRankUS, emojiD)
    
    
    

@bot.event
async def on_member_join(member):
    for server in bot.servers:
        for channel in server.channels:
            if channel.id == "463785244772794370" and member.server.name == "Nebula eSports":
                w = channel
                print("{} Has Joined".format(member))
                embed=discord.Embed(title=str(member.name), color=0xfa9361)
                embed.set_author(name="Welcome To Nebula:")
                embed.set_thumbnail(url=member.avatar_url)
                await bot.send_message(w,embed=embed)
                role = discord.utils.get(member.server.roles, name="New")
                role2 = discord.utils.get(member.server.roles, name="⋑-Members-⋐")
                await bot.add_roles(member, role)
                await bot.add_roles(member, role2)
    
    
@bot.command(pass_context=True)
async def admin(ctx):
    admins=[]
    server = ctx.message.server
    for role in server.roles:
        #print(role)
        if "admin" in str(role) or "Admin" in str(role) or "MODS" in str(role) or "mods" in str(role) or "Mods" in str(role)or "Moderator" in str(role):
            adminRole = role
            pass
    for member in server.members:
        if adminRole in member.roles:
            #print(member.name)
            admins.append(member.name)

    embed=discord.Embed(title="Admins:", color=0xff3f06)
    for x in range(len(admins)):
        #print(admins[x])
        embed.add_field(name="{}.".format(x+1), value=str(admins[x]), inline=True)
    await bot.say(embed=embed)
    
    
@bot.event
async def on_reaction_add(reaction, user):
    if user.id != "461306582958080010":
        for x in bot.get_all_emojis():
            if x.name == 'Copper':
                emojiCop = x
            elif x.name == "Bronze":
                emojiBro = x
            elif x.name == "Silver":
                emojiSil = x
            elif x.name == "Gold":
                emojiGol = x
            elif x.name == "Plat":
                emojiPla = x
            elif x.name == "Diamond":
                emojiDia = x
            elif x.name == "C_":
                emojiC = x
            elif x.name == "B_":
                emojiB = x
            elif x.name == "S_":
                emojiS = x
            elif x.name == "G_":
                emojiG = x
            elif x.name == "P_":
                emojiP = x
            elif x.name == "D_":
                emojiD = x
        channel = reaction.message.channel
        role = discord.utils.get(user.server.roles, name="⋑-Members-⋐")
        role2 = discord.utils.get(user.server.roles, name="New")
        roleEU = discord.utils.get(user.server.roles, name="EU")
        roleNA = discord.utils.get(user.server.roles, name="NA")
        roleDJ = discord.utils.get(user.server.roles, name="DJ")
        roleCop = discord.utils.get(user.server.roles, name="Copper")
        roleBro = discord.utils.get(user.server.roles, name="Bronze")
        roleSil = discord.utils.get(user.server.roles, name="Silver")
        roleGol = discord.utils.get(user.server.roles, name="Gold")
        rolePla = discord.utils.get(user.server.roles, name="Platinum")
        roleDia = discord.utils.get(user.server.roles, name="Diamond")

        if reaction.emoji == emojiCop and channel == r:
            await bot.add_roles(user, roleCop)
        elif reaction.emoji == emojiBro and channel == r:
            await bot.add_roles(user, roleBro)
        elif reaction.emoji == emojiSil and channel == r:
            await bot.add_roles(user, roleSil)
        elif reaction.emoji == emojiGol and channel == r:
            await bot.add_roles(user, roleGol)
        elif reaction.emoji == emojiPla and channel == r:
            await bot.add_roles(user, rolePla)
        elif reaction.emoji == emojiDia and channel == r:
            await bot.add_roles(user, roleDia)

        elif reaction.emoji == emojiC and channel == ru:
            await bot.add_roles(user, roleCop)
        elif reaction.emoji == emojiB and channel == ru:
            await bot.add_roles(user, roleBro)
        elif reaction.emoji == emojiS and channel == ru:
            await bot.add_roles(user, roleSil)
        elif reaction.emoji == emojiG and channel == ru:
            await bot.add_roles(user, roleGol)
        elif reaction.emoji == emojiP and channel == ru:
            await bot.add_roles(user, rolePla)
        elif reaction.emoji == emojiD and channel == ru:
            await bot.add_roles(user, roleDia)

        elif reaction.emoji == '🎧' and channel == c:
            await bot.add_roles(user, roleDJ)
        elif reaction.emoji == '✅' and channel == c:
            await bot.add_roles(user, role)
            try:
                await bot.remove_roles(user, role2)
            except Exception:
                pass
            try:
                await bot.add_roles(user, role)
            except Exception:
                print("Failed To Add Member Role")
        elif reaction.emoji == '🇪🇺' and channel == b:
            try:
                await bot.add_roles(user, roleEU)
            except Exception:
                pass
        elif reaction.emoji == '🇺🇸' and channel == b:
            try:
                await bot.add_roles(user, roleNA)
            except Exception:
                pass
        
@bot.event
async def on_reaction_remove(reaction, user):
    if user.id != "461306582958080010":
        for x in bot.get_all_emojis():
            if x.name == 'Copper':
                emojiCop = x
            elif x.name == "Bronze":
                emojiBro = x
            elif x.name == "Silver":
                emojiSil = x
            elif x.name == "Gold":
                emojiGol = x
            elif x.name == "Plat":
                emojiPla = x
            elif x.name == "Diamond":
                emojiDia = x
            elif x.name == "C_":
                emojiC = x
            elif x.name == "B_":
                emojiB = x
            elif x.name == "S_":
                emojiS = x
            elif x.name == "G_":
                emojiG = x
            elif x.name == "P_":
                emojiP = x
            elif x.name == "D_":
                emojiD = x
        roleCop = discord.utils.get(user.server.roles, name="Copper")
        roleBro = discord.utils.get(user.server.roles, name="Bronze")
        roleSil = discord.utils.get(user.server.roles, name="Silver")
        roleGol = discord.utils.get(user.server.roles, name="Gold")
        rolePla = discord.utils.get(user.server.roles, name="Platinum")
        roleDia = discord.utils.get(user.server.roles, name="Diamond")

        if reaction.emoji == emojiCop and reaction.message.channel == r:
            await bot.remove_roles(user, roleCop)
        elif reaction.emoji == emojiBro and reaction.message.channel == r:
            await bot.remove_roles(user, roleBro)
        elif reaction.emoji == emojiSil and reaction.message.channel == r:
            await bot.remove_roles(user, roleSil)
        elif reaction.emoji == emojiGol and reaction.message.channel == r:
            await bot.remove_roles(user, roleGol)
        elif reaction.emoji == emojiPla and reaction.message.channel == r:
            await bot.remove_roles(user, rolePla)
        elif reaction.emoji == emojiDia and reaction.message.channel == r:
            await bot.remove_roles(user, roleDia)

        elif reaction.emoji == emojiC and reaction.message.channel == ru:
            await bot.remove_roles(user, roleCop)
        elif reaction.emoji == emojiB and reaction.message.channel == ru:
            await bot.remove_roles(user, roleBro)
        elif reaction.emoji == emojiS and reaction.message.channel == ru:
            await bot.remove_roles(user, roleSil)
        elif reaction.emoji == emojiG and reaction.message.channel == ru:
            await bot.remove_roles(user, roleGol)
        elif reaction.emoji == emojiP and reaction.message.channel == ru:
            await bot.remove_roles(user, rolePla)
        elif reaction.emoji == emojiD and reaction.message.channel == ru:
            await bot.remove_roles(user, roleDia)

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
async def clear(ctx, amount=50):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)+1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages Deleted.")
        #async for message in bot.logs_from(channel, limit=1):
            #time.sleep(2)
        #await bot.delete_message(message)

@bot.command(pass_context=True)
async def now(ctx, value=0):
    value=int(value)
    if value != 0 and value != 1:
        value = 0

    h = int(time.strftime("%I"))
    m = str(time.strftime("%M"))
    time2 = (str(h+1)+":"+m+" BST")
    text = "The Time Is "+time2
    await bot.send_message(ctx.message.channel, text, tts=bool(value))
        
@bot.event
async def on_message(message):
   if message.content.startswith("👏👏") or message.content.startswith("👏 👏"):
        await bot.send_message(message.channel,"***MEME REVIEW***")
   else:
   		pass
   if message.content.lower().startswith("dip dip"):
        await bot.send_message(message.channel,"🥔🍟")
   if "prodigy" in str(message.content.lower()):
        await bot.send_message(message.channel, "Fuck You ᴘʀᴏᴅɪɢʏ")
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
async def fuprodigy(ctx):
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=1):
        await bot.delete_message(message)
    await bot.send_message(channel, "Fuck You ProdIgy")


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
        h = int(time.strftime("%I"))
        m = str(time.strftime("%M"))
        time2 = (str(h+1)+":"+m+" BST")
        await bot.change_presence(game=discord.Game(name=time2, type=3))
        await asyncio.sleep(5)

    
bot.loop.create_task(timeloop())
bot.run(os.getenv('TOKEN'))
