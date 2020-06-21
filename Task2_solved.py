from datetime import datetime
import time
import requests
import json
import numpy as np
import argparse


def get_data_from_web():
    """Sends a request to web, gets a result and parses it"""
    response = requests.get('http://ir.eia.gov/ngs/wngsr.json')
    response_json = json.loads(response.content)
    return response_json


def parse_json_data_from_web(data):
    """Parses received from the WEB JSON-data"""
    net_changes = []
    for data_series in data['series']:
        name = data_series['name']
        calculated_net_change = data_series['calculated']['net_change']
        if 'total' in name:
            print(f'\nTotal net change: {calculated_net_change}')
        else:
            net_change = int(data_series['calculated']['net_change'])
            net_changes.append(net_change)
    average_net_change = np.average(net_changes)
    print(f'Average meaning of net changes is {average_net_change}')


def get_time_to_start_and_run_script():
    """Picks start time and starts parser"""
    current_time = datetime.now().time().strftime('%H:%M')
    start_time = "08:16"

    parser = argparse.ArgumentParser()
    parser.add_argument("--starts", help="changes start time")
    args = parser.parse_args()
    if args.starts:
        start_time = args.starts

    print(f'Parsing starts at {start_time}')
    while current_time != start_time:
        current_time = datetime.now().time().strftime('%H:%M')
        time.sleep(1)
    else:
        try:
            data_json = get_data_from_web()
            parse_json_data_from_web(data_json)
        except (ValueError, KeyError):
            print('Something went wrong!')


def main():
    get_time_to_start_and_run_script()


if __name__ == '__main__':
    main()
