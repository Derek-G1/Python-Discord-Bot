# Link to youtube video for code https://www.youtube.com/watch?v=SPTfmiYiuok&t=1955s&ab_channel=freeCodeCamp.org
# Added features not in the video
# Marvin The Paranoid Android Discord Bot <- Named after the character in the movie "Hitchhikers Guide to The Galaxy" ->
# https://en.wikipedia.org/wiki/Hitchhikers_Guide_to_The_Galaxy
# Import discord.py, requests,json, os, random and http.client
# from discord.channel import VoiceChannel
# from discord.ext.commands.core import command
from googleapiclient.discovery import build
import discord
import os
import requests
import json
import random
import http.client
from discord.ext import commands

# Call Bot and Declare variables
# =========================================================
#intents = discord.Intents.all()

#client = discord.Client()

bot = commands.Bot(command_prefix='!')

sadWords = ["sad", "depressed", "unhappy", "angry", "miserable",
            "depressing", "awful", "sorry", "tragic", "hate"]

tyResponse = ["Your Welcome!", "No Problem!", "Here to Help!", "Anytime!"]

userTy = ["Thank you Marvin!", "Thank you Marvin"]


starterEncouragements = ["Hey there! I'm Marvin, the paranoid android bot. I'm here to help you stay sane and happy!.", "Cheer up!", "You are a great person / bot!", "Hang in there!", "So long and thanks for all the fish", "42"
                         ]
# Functions
# ====================================================================================


@bot.command()
async def quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    await ctx.send(quote)


# joke function and


@bot.command()
async def joke(ctx):
    conn = http.client.HTTPSConnection("jokes-by-api-ninjas.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "jokes-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "5c56a95e0dmshe101134916c12e9p1f4954jsn70264f193f7d"
    }

    conn.request("GET", "/v1/jokes", headers=headers)
    res = conn.getresponse()
    data = res.read()

    joke = eval(data.decode("utf-8"))
    await ctx.channel.send(joke[0]['joke'])
    print(joke[0]['joke'])
 # Events
# ================================================================


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    # print(client.user.name)
    # print(client.user.id)

    # Welcome message


@bot.event
async def on_welcome():
    print("Welcome {0.user} to the server!")


# @bot.command()
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     msg = message.content


# # If statement for get_joke function to be called in on_message.

#     if msg.startswith("!joke"):
#         joke = get_joke()
#

    # if any(word in msg for word in sadWords):
    #     await messa.channel.send(random.choice(starterEncouragements))

# @bot.command()
# async def thanks(ctx):
#     if msg.startswith("!thanks"):
#         await ctx.send(random.choice(tyResponse))


#     if msg.startswith("!join"):
#

# Commands
# ========================================================================


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


bot.run("OTAyNzc0Nzk1NDc1NzUwOTc0.YXjUiw.FXdrnt1ZXH44Ry295Pxqf0FGEdY")
