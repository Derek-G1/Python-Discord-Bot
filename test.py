import discord
from discord.ext import commands


client = commands.Bot(command_prefix='!')


@client.command()
async def play(ctx, url: str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voiceChannel.connect()

client.run("OTAyNzc0Nzk1NDc1NzUwOTc0.YXjUiw.FXdrnt1ZXH44Ry295Pxqf0FGEdY")
