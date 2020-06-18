import schedule
from datetime import datetime
import time
import requests
import json
import numpy as np


def get_data_from_web_and_parses_it():
    '''Sends a request to web, gets a result and parses it'''
    print()
    try:
        response = requests.get('http://ir.eia.gov/ngs/wngsr.json')
        response_text_raw = response.text.replace('ï»¿', '')
        response_json = json.loads(response_text_raw)
        net_changes = []
        for data_series in response_json['series']:
            name = data_series['name']
            calculated_net_change = data_series['calculated']['net_change']
            if 'total' in name:
                print(f'Total net change: {calculated_net_change}')
            else:
                net_change = int(data_series['calculated']['net_change'])
                net_changes.append(net_change)
        average_net_change = np.average(net_changes)
        print(f'Average meaning of net changes is {average_net_change}')
    except Exception:
        print('Something went wrong!')


def get_time_to_start_and_run_script():
    '''Picks start time and run parser'''
    current_time = datetime.now().time().strftime('%H:%M')
    start_time = "11:53"

    user_choice = input('''Would like to pick time to start: 1.Yes
                                  2.No ''')
    print()

    if user_choice == '1':
        start_time = input('Pick time you want to start(format: HH:MM) ')
        print(f'Script starts at {start_time}')
    elif user_choice == '2':
        print(f'Script starts at {start_time}')
    else:
        print(f'Incorrect input. Script starts at {start_time}')

    while current_time != start_time:
        current_time = datetime.now().time().strftime('%H:%M')
        time.sleep(1)
    else:
        get_data_from_web_and_parses_it()


def main():
    get_time_to_start_and_run_script()


if __name__ == '__main__':
    main()
