import re
import requests

url = "https://www.havadurumu15gunluk.net/havadurumu/bursa-hava-durumu-15-gunluk.html"
site_content = requests.get(url).content.decode('utf-8')

regex_day_temp = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
regex_night_temp = '<td width="45">&nbsp;(-?\d+)°C</td>'
regex_day = '<td width="70" nowrap="nowrap">(.*)</td>'
regex_date = '<td width="75" nowrap="nowrap">(.*)</td>'
regex_description = '<img src="/havadurumu/images/trans.gif" alt="Bursa Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'

pattern_day_temp = re.compile(regex_day_temp)
pattern_night_temp = re.compile(regex_night_temp)
pattern_day = re.compile(regex_day)
pattern_date = re.compile(regex_date)
pattern_description = re.compile(regex_description)

day_temps = []
night_temps = []
days = []
dates = []
descriptions = []

for temp in re.findall(regex_day_temp, site_content):
    day_temps.append(temp)

for temp in re.findall(regex_night_temp, site_content):
    night_temps.append(temp)

for day in re.findall(regex_day, site_content):
    days.append(day)

for date in re.findall(regex_date, site_content):
    dates.append(date)

for desc in re.findall(regex_description, site_content):
    descriptions.append(desc)

print("-" * 75)
print("                         BURSA WEATHER FORECAST")
print("-" * 75)
for i in range(0, len(days)):
    print("{} {},\n\t\t\t\t\tday: {} °C\tnight: {} °C\t{}".format(dates[i], days[i], day_temps[i], night_temps[i], descriptions[i]))
    print("-" * 75)
