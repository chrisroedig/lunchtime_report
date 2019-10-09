import lunch_today
import json
from datetime import datetime
from datetime import timedelta

def get_api_data():
    return json.load(open('nutrislice_example.json'))

def find_start_date(api_data):
    return datetime.strptime(api_data['start_date'], '%Y-%m-%d')

API_DATA = get_api_data()
START_DATE = find_start_date(API_DATA)

def test_menu_list():    
    subject = lunch_today.menu_list(API_DATA, START_DATE)
    assert isinstance(subject, list)
    for item in subject:
      assert isinstance(item, dict)

def test_menu_list_week():
    for i in range(0,8):
      date = START_DATE + timedelta(days=i)
      subject = lunch_today.menu_list(API_DATA, date)
      print(subject)
      assert isinstance(subject, list)

def test_menu_choices():
    subject = lunch_today.menu_choices(API_DATA, START_DATE)
    assert isinstance(subject, list)
    for item in subject:
        assert isinstance(item, str)

if __name__ == '__main__':
    print(test_menu_choices())