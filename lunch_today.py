import requests
from datetime import datetime

def menu_list(lunch_data, today):
    day_data = [ d for d in lunch_data['days'] if d['date'] == today.strftime('%Y-%m-%d') ] 
    if len(day_data) == 0:
       return []
    return day_data[0]['menu_items']
    
def menu_item_text(day_data):
    food = day_data['food']
    if food is None:
        return None
    return food["name"]

def menu_choices(lunch_data, today):
    mlist = menu_list(lunch_data, today)
    menu_choices = []
    current_choice = None
    for item in mlist:
        if not item['no_line_break']:
            if current_choice is not None:
                menu_choices.append(current_choice[:-1])
            current_choice = ""
        if item['food'] is None:
            current_choice = current_choice + item['text'] + " "
        else:
            current_choice = current_choice + item['food']['name'] + " "
    return menu_choices
        
def get_data(today = datetime.now()):
    resp = requests.get(url(today))
    return resp.json()

def url(today = datetime.now()):
    host= "https://worthington.nutrislice.com"
    path = "menu/api/weeks/school/evening-street-elementary-school/menu-type/lunch"
    params = f'{today.year}/{today.month}/{today.day}/'
    return f'{host}/{path}/{params}'

if __name__ == "__main__":
    today = datetime.now()
    print(menu_choices(get_data(today), today))