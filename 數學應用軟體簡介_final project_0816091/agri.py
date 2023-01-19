#import json to read json file
import json
#import average function from func.py
from func import average

class Weather:
  def __init__(self,item):
    self.data=item

  def location(self):
    self.location=self.data['locationName']
    print(self.location)

  #find the date in the json file
  def date(self):
    self.date=self.data['weatherElements']['Wx']['daily']
    date=[]
    for d in self.date:
        date.append(d['dataDate'])

    print('from',date[0],'to',date[-1])

  #find the maximum weather and calculate the average
  def MaxT(self):
    self.max_weather=self.data['weatherElements']['MaxT']['daily']
    max_t=[]
    maxt=0
    for t in self.max_weather:
      max_t.append(int(t['temperature']))
      maxt=max(maxt,int(t['temperature']))

    print('highest temperature of the week:',maxt)
    print('average highest temperature of the week:',format(average(max_t),".2f") )

  # find the minimum weather and calculate the average
  def MinT(self):
    self.min_weather = self.data['weatherElements']['MinT']['daily']
    min_t = []
    mint=100
    for t in self.min_weather:
      min_t.append(int(t['temperature']))
      mint=min(mint,int(t['temperature']))

    print('lowest temperature of the week:',mint)
    print('average lowest temperature of the week:', format(average(min_t), ".2f"))

  #print the wanted result
  def print(self):
    self.location()
    self.date()
    self.MaxT()
    self.MinT()


#you can find the latest json file here: https://opendata.cwb.gov.tw/dataset/forecast/F-A0010-001
#rename the json file to agriculture.json
#open the file and encode using utf-8 and store as f
with open('agriculture.json',encoding="utf-8") as f:
  #store the file as info
  info = json.load(f)

#region is the path to the last dict before locationName(item in list)
region=info['cwbdata']['resources']['resource']['data']['agrWeatherForecasts']['weatherForecasts']['location']
#print(region)

# go through elements in region
for item in region:
  #print(item)

  # result is the name of object
  result=Weather(item)
  #call print function in class Weather
  result.print()
