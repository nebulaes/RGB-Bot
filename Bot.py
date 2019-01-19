import discord, os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time, json, requests
from discord.voice_client import VoiceClient

from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image, ImageOps

bot=discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready")
    for server in bot.servers:
        for channel in server.channels:
            if channel.id == "463789709341097984" or channel.name == "╠-rules":
                global c
                c = channel
            elif channel.id == "465584250129743874" or channel.name == "╠-server":
                global b
                b = channel
            elif channel.id == "463785244772794370" or channel.name == "╔-welcome":
                global w
                w = channel
            elif channel.id == "483791168111509504" or channel.name == "╠-ranks":
                global r
                r = channel

    h = int(time.strftime("%I"))
    m = str(time.strftime("%M"))
    time2 = (str(h+1)+":"+m+" BST")
    await bot.change_presence(game=discord.Game(name=time2, type=3))
    async for message in bot.logs_from(c, limit=3):
        await bot.delete_message(message)    
    embed=discord.Embed(title="Server Rules:", color=0xf07e00)
    embed.set_author(name="RULES: ACCEPT RULES BY CLICKING GREEN TICK")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/369932731687370752/536000092738682890/RedCrop.png")
    embed.add_field(name="1.", value="-No Toxicity", inline=False)
    embed.add_field(name="2.", value="-No Spamming", inline=False)
    embed.add_field(name="3.", value="-No Posting DMs Without Permission", inline=False)
    embed.add_field(name="4.", value="-No Racism", inline=False)
    embed.add_field(name="5.", value="-Respect Admins", inline=False)
    embed.add_field(name="6.", value="-Respect All Members", inline=False)
    embed.add_field(name="7.", value="-No NSFW", inline=False)
    embed.add_field(name="8.", value="-No Posting Server Invite Without Permission", inline=False)
    embed.add_field(name="9.", value="-ACCEPT RULES TO GAIN A ROLE BY CLICKING GREEN TICK", inline=False)
    embed.set_footer(text="Thank You.")
    msg = await bot.send_message(c, embed=embed)
    embed=discord.Embed(title="SERVER")
    embed.add_field(name="EU", value="React With: 🇪🇺", inline=False)
    embed.add_field(name="NA", value="React With: 🇺🇸", inline=True)
    async for message in bot.logs_from(b, limit=3):
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
    
    embed=discord.Embed(title="SERVER")
    embed.add_field(name="Ranked", value="React With: ✅", inline=False)
    msg3 = await bot.send_message(b, embed=embed)
    await bot.add_reaction(msg3, reaction)
    
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

    
    
    

@bot.event
async def on_member_join(member):

    for channel in member.server.channels:
        if channel.id == "535987415597449216" and member.server.id == "463785244772794368":
            welcomeChannel = channel
        elif channel.id == "495362269736075273":
            zc = channel
        elif channel.id == "495363675830616073" and member.server.name == "Nebula eSports Community":
            bc = channel
        elif channel.id == "495367099024277515" and member.server.name == "Nebula eSports Community":
            tc = channel
        
    img = Image.open("Welcome.png")
    W, H = (800,300)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    tfont = ImageFont.truetype("libel-suit-rg.ttf", 50)
    # draw.text((x, y),"Sample Text",(r,g,b))
    msg = member.name
    w,h = tfont.getsize(msg)
    draw.text((80, 120), msg, font=tfont, fill="white")
    print(member.avatar_url)
    if(member.avatar_url == ""):
        cacheImg = Image.open("noImg.png")
        img_w, img_h = cacheImg.size
        bg_w, bg_h = img.size
        offset = ((bg_w - img_w) // 2 + 192, (bg_h - img_h) // 2)
        img.paste(cacheImg, offset, cacheImg)
        img.save('Message.png')
        await bot.send_file(welcomeChannel,"Message.png")

    elif(".gif" in member.avatar_url):
        cacheImg = requests.get(member.avatar_url[:-4]+"256")
        open("cache.gif", 'wb').write(cacheImg.content)
        cacheImg = Image.open("cache.gif")
        img_w, img_h = cacheImg.size
        bg_w, bg_h = img.size
        offset = ((bg_w - img_w) // 2 + 192, (bg_h - img_h) // 2)
        img.paste(cacheImg, offset)
        img.save('Message.png')
        await bot.send_file(welcomeChannel,"Message.png")
    
    else:
        cacheImg = requests.get(member.avatar_url[:-4]+"256")
        open("cache.png", 'wb').write(cacheImg.content)
        cacheImg = Image.open("cache.png")
        img_w, img_h = cacheImg.size
        bg_w, bg_h = img.size
        offset = ((bg_w - img_w) // 2 + 192, (bg_h - img_h) // 2)
        img.paste(cacheImg, offset, cacheImg)
        img.save('Message.png')
        await bot.send_file(welcomeChannel,"Message.png")

    role = discord.utils.get(member.server.roles, name="New")
    role2 = discord.utils.get(member.server.roles, name="⋑-Members-⋐")
    await bot.add_roles(member, role)
    await bot.add_roles(member, role2)


    t = 0
    b = 0
    for i in member.server.members:
        t += 1
        if i.bot == True:
            b +=1
    h = t - b
    await bot.edit_channel(channel = tc, name="╔-total-﹝{}﹞".format(t))
    await bot.edit_channel(channel = zc, name="╠-members-﹝{}﹞".format(h))
    await bot.edit_channel(channel = bc, name="╚-bots-﹝{}﹞".format(b))
                
                
@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        h = 0
        if channel.id == "495362269736075273" and member.server.id == "463785244772794368":
            zc = channel
        elif channel.id == "495363675830616073" and member.server.id == "463785244772794368":
            bc = channel
        elif channel.id == "495367099024277515" and member.server.id == "463785244772794368":
            tc = channel

    t = 0
    b = 0
    for i in member.server.members:
        t += 1
        if i.bot == True:
            b +=1
    h = t - b
    await bot.edit_channel(channel = tc, name="╔-total-﹝{}﹞".format(t))
    await bot.edit_channel(channel = zc, name="╠-members-﹝{}﹞".format(h))
    await bot.edit_channel(channel = bc, name="╚-bots-﹝{}﹞".format(b))

                
@bot.command(pass_context=True)
async def memberCount(ctx):
    for channel in ctx.message.server.channels:
        if channel.id == "495362269736075273":
            zc = channel
        elif channel.id == "495363675830616073":
            bc = channel
        elif channel.id == "495367099024277515":
            tc = channel
                
            t = 0
            b = 0
            for i in ctx.message.server.members:
                t += 1
                if i.bot == True:
                    b +=1
            h = t - b
            await bot.edit_channel(channel = tc, name="╔-total-﹝{}﹞".format(t))
            await bot.edit_channel(channel = zc, name="╠-members-﹝{}﹞".format(h))
            await bot.edit_channel(channel = bc, name="╚-bots-﹝{}﹞".format(b))
    
    
@bot.command(pass_context=True)
async def admin(ctx):
    admins=[]
    server = ctx.message.server
    for role in server.roles:
        #print(role)
        if "admin" in str(role) or "Admin" in str(role) or "MODS" in str(role) or "mods" in str(role) or "Mods" in str(role)or "Moderator" in str(role):
            adminRole = role
            pass
        if "♕-Owners-♕" == role.name:
            ownerRole = role
            pass
    for member in server.members:
        if ownerRole in member.roles:
            admins.append(member.name)
        if adminRole in member.roles and ownerRole not in member.roles:
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
        roleRanked = discord.utils.get(user.server.roles, name="Ranked")

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
        elif reaction.emoji == '✅' and channel == b:
            await bot.add_roles(user, roleRanked)
        
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

        roleCop = discord.utils.get(user.server.roles, name="Copper")
        roleBro = discord.utils.get(user.server.roles, name="Bronze")
        roleSil = discord.utils.get(user.server.roles, name="Silver")
        roleGol = discord.utils.get(user.server.roles, name="Gold")
        rolePla = discord.utils.get(user.server.roles, name="Platinum")
        roleDia = discord.utils.get(user.server.roles, name="Diamond")
        roleRanked = discord.utils.get(user.server.roles, name="Ranked")
        
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
        elif reaction.emoji == '✅' and reaction.message.channel == b:
            await bot.remove_roles(user, roleRanked)

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
async def timeout(ctx, m : discord.Member, i : int = 30):
    try:
        server = ctx.message.server
        for role in server.roles:
            #print(role)
            if "admin" in str(role) or "Admin" in str(role) or "MODS" in str(role) or "mods" in str(role) or "Mods" in str(role) or "Moderator" in str(role):
                adminRole = role
                pass
        if adminRole in ctx.message.author.roles:
            if int(i) >= 300:
                await bot.say("Cannot Timeout Above 300 Seconds")
                pass
            else:
                await bot.server_voice_state(m, mute=True)
                await count(int(i))
                await bot.server_voice_state(m, mute=False)
                async for message in bot.logs_from(channel, limit=1):
                    await bot.delete_message(message)
        else:
            await bot.say("You Must Be An Admin To Use This Command!")
            pass
    except Exception:
        await bot.say("Error Has Occured")
        pass

async def count(m):
    seconds = m
    while seconds > 0:
        seconds -= 1
        await asyncio.sleep(1)
       



@bot.command(pass_context=True)
async def logo(ctx):
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=1):
            await bot.delete_message(message)
    await bot.send_file(channel,"Logo.png")
   
@bot.command(pass_context=True)
async def clear(ctx, amount=5):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)+1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages Deleted.")
    async for message in bot.logs_from(channel, limit=1):
        time.sleep(0.5)
    await bot.delete_message(message)

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
        

@bot.command(pass_context=True)
async def rules(ctx):
    message = ctx.message
    channel = ctx.message.channel
    async for message in bot.logs_from(channel, limit=1):
        await bot.delete_message(message)
    msg = await bot.say("RULES \n -No Toxicity \n -No Spamming \n -No Posting DMs \n -No Racism \n -No Posting or using Faces (Even Blurred) Without Permission \n -If You Join A Call And Are Asked To Mute Your Mic, Mute It \n -If Moved Out A Chat, Don't Move Back \n -Respect All Members \n -Respect Admins And Listen To Them \n -No NSFW")
    print(msg)

async def timeloop():
    await bot.wait_until_ready()
    while not bot.is_closed:
        h = int(time.strftime("%I"))
        m = str(time.strftime("%M"))
        time2 = (str(h)+":"+m+" GMT")
        await bot.change_presence(game=discord.Game(name=time2, type=3))
        await asyncio.sleep(5)

    
bot.loop.create_task(timeloop())
bot.run(os.getenv('TOKEN'))
