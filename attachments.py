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
    for i in range(len(data[0]["timeSeries"][0]["areas"])):
        area = data[0]["timeSeries"][0]["areas"][i]
        title = prefname+"/"+ area["area"]["name"]
        embed = discord.Embed(title=title,description = area["weathers"][date],url=f"https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code={pref}")
        weatherCode = area["weatherCodes"][date]
        #日付変換
        d = dt.datetime.fromisoformat(data[0]["timeSeries"][0]["timeDefines"][date])
        
        print(f"https://www.jma.go.jp/bosai/forecast/img/{weatherCode}.png")
        embed.set_thumbnail(url=f"https://www.jma.go.jp/bosai/forecast/img/{weatherCode}.png")
        embed.set_footer(text=f"{d.strftime('%Y年%m月%d日')}")
        #気温
        t_times = list()
        for t_time in data[0]["timeSeries"][2]["timeDefines"]:
            t_times.append(dt.datetime.fromisoformat(t_time))
            
        t_root = data[0]["timeSeries"][2]["areas"][i]
        
        tmp = ""
        for i in range(len(t_root["temps"])):
            if t_times[i].day == d.day:
                time = t_times[i].strftime('%H時')
                str = t_root["temps"][i]
                tmp += f"{time}:{str}℃\n"
        
        if tmp != "":
            embed.add_field(name="気温:thermometer:",value=tmp)
        
        #湿度
        p_times = list()
        for p_time in data[0]["timeSeries"][1]["timeDefines"]:
            p_times.append(dt.datetime.fromisoformat(p_time))
            
        p_root = data[0]["timeSeries"][1]["areas"][i]
        
        tmp = ""
        for i in range(len(p_root["pops"])):
            if p_times[i].day == d.day:
                time = p_times[i].strftime('%H時')
                str = p_root["pops"][i]
                tmp += f"{time}:{str}%\n"
        
        if tmp != "":
            embed.add_field(name="降水確率:umbrella:",value=tmp)
        #セット
        embeds.append(embed)
    return embeds

