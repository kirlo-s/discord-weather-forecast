from random import choices
import discord
from discord import Option
import os
from dotenv import load_dotenv
from util import getdata
from discord.ext import pages ,commands
import attachments

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = discord.Bot()
GUILD_IDS = [530296819935084564]  # ← BOTのいるサーバーのIDを入れます



@bot.event
async def on_ready():
    print(f"{bot.user} On ready")


@bot.slash_command(description="天気予報", guild_ids=GUILD_IDS)
async def weather(
    ctx: discord.ApplicationContext,
    prefecture: Option(str, required=True, description="都道府県を入力(-県)"),
    date: Option(str,required = False,description="天気を取得する日(更新5:00)",choices=["今日","明日","明後日"])
):  

    if date == None:
        date = "今日"

    pref_code = getdata.getPrefID(prefecture)
    if pref_code == "00" :
        await ctx.send("存在しない地域です")
    elif pref_code == "01":
        await ctx.send("未対応")
    elif pref_code == "47":
        await ctx.send("未対応")
    else:
        weather = attachments.JMAWeatherEmbed(prefecture,pref_code,date)
        paginator = pages.Paginator(pages = weather)
        await paginator.respond(ctx.interaction, ephemeral=False)


bot.run(TOKEN)