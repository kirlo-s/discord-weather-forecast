import requests
import json

def getJMAWeater(pref_code):
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{pref_code}.json"
    Data = requests.get(url).json()
    return Data

def getPrefID(pref_name):
    json_open = open("util/pref.json","r")
    json_load = json.load(json_open)
    prefs = json_load["prefectures"]
    prefID = ""
    
    for pref in prefs:
        if pref["name"] == pref_name:
            prefID = pref["code"]
    
    #エラー用        
    if prefID == "":
        return "00"
    
    #北海道、沖縄、鹿児島は独自表記
    if prefID == "01":
        return prefID
    elif prefID == "46":
        return "460100"
    elif prefID == "47":
        return prefID
    else:
        return f"{prefID}0000"
        
        
