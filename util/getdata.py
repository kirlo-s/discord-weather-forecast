import requests


def getJMAweater(pref):
    url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{pref}.json"
    Data = requests.get(url).json()
    print(Data)


getJMAweater(260000)