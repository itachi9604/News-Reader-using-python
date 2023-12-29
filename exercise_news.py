
import json
import requests
import pyttsx3
import datetime
import os

def readn(nstr):
    engine = pyttsx3.init()

    engine.setProperty('voice', "english+f5")
    engine.setProperty('rate', 120)

    engine.say(nstr)
    engine.runAndWait()
    engine.stop()



url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=<API_KEY>"
r=requests.get(url)
r1=r.text
parsed_news=json.loads(r1)
print(parsed_news)
arts=parsed_news["articles"]
os.chdir("/home/itachi/Documents/news")
todays_date=str(datetime.date.today())
date_file_name=todays_date+".txt"
fl=open(date_file_name,'w')

for itms in arts:

    fl.write(itms["title"])
    fl.write("\n")
    print(itms["title"])
    readn(itms["title"])
fl.close()

# there can be two options_ read news and create newspaper
# readn(parsed_news)
