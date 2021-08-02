import datetime
import discord
from discord.ext import commands

TOKEN = open("token.txt", "r", encoding="utf-8").read()
activity = discord.Activity(type=discord.ActivityType.watching, name="Your Exam")
prefix = "!"
bot = commands.Bot(command_prefix=prefix, activity=activity)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


def calculate():
    now = datetime.datetime.now()
    dday = datetime.datetime.strptime(
        "2021-10-12 09:00:00.000000", "%Y-%m-%d %H:%M:%S.%f"
    )
    return (dday - now).days


@bot.command(name="exam")
async def exam(ctx):
    embedVar = discord.Embed(
        title="**Second Semester 1st Exam Info**",
        color=0xC3B9D6,
        timestamp=datetime.datetime.utcnow(),
    )
    embedVar.set_footer(
        text=ctx.message.author,
        icon_url=ctx.message.author.avatar_url,
    )
    embedVar.add_field(name="** **", value=f"D - {calculate()}", inline=False)
    embedVar.add_field(name="** **", value="** **", inline=False)
    await ctx.send(embed=embedVar)


bot.run(TOKEN)
