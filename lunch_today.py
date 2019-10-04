import requests
from datetime import datetime

def lunch_today():
    today = datetime.now()
    day = [ d for d in get_data()['days'] if d['date'] == today.strftime('%Y-%m-%d') ] 
    return list(map( food_today, day[0]['menu_items']))

def food_today(day_data):
    food = day_data['food']
    if food is None:
      return "Nothing"
    return food["name"]
def get_data(today = datetime.now()):
    resp = requests.get(url(today))
    return resp.json()

def url(today = datetime.now()):
    host= "https://worthington.nutrislice.com"
    path = "menu/api/weeks/school/evening-street-elementary-school/menu-type/lunch"
    params = f'{today.year}/{today.month}/{today.day}/'
    return f'{host}/{path}/{params}'

if __name__ == "__main__":
    print(lunch_today())