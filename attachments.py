from pydoc import describe
from unicodedata import name
import discord 
from util import getdata
import numpy as np 
import datetime  as dt

def JMAWeatherEmbed(prefname,pref,date):
    
    if date == "今日":
        date = 0
    elif  date == "明日":
        date = 1
    elif date  == "明後日":
        date = 2

    embeds = list()
    data = getdata.getJMAWeater(pref)
    for area in data[0]["timeSeries"][0]["areas"]:
        title = prefname+" "+ area["area"]["name"]
        embed = discord.Embed(title=title,description = area["weathers"][date])
        weatherCode = area["weatherCodes"][date]
        #日付変換
        d = dt.datetime.fromisoformat(data[0]["timeSeries"][0]["timeDefines"][date])
        
        print(f"https://www.jma.go.jp/bosai/forecast/img/{weatherCode}.png")
        embed.set_thumbnail(url=f"https://www.jma.go.jp/bosai/forecast/img/{weatherCode}.png")
        embed.set_footer(text=f"{d.strftime('%Y年%m月%d日')}")
        embeds.append(embed)
    return embeds

