from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageOps


import discord, os
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time, json, requests
from discord.voice_client import VoiceClient


bot=discord.Client()
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_member_join(member):

    for channel in member.server.channels:
        if channel.id == "535987415597449216" and member.server.id == "463785244772794368":
            welcomeChannel = channel
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

#https://discord.gg/qn6n3Z
bot.run("NDY0MTMyMzA5MTU1NzA4OTM4.DyP11g.sTk8lRp10HvONC1wNu_njKfxwLU")
