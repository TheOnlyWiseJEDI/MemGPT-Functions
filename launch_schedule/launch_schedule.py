from datetime import datetime, timezone, timedelta
import requests
import json
import os

create_files = True
docs_dir = os.path.join(os.path.expanduser("~"), "Documents")

def launch_schedule(self):
    global create_files
    """
        Gets the Rocket Launch schedule for Ron and makes him happy. Set heartbeat = True
        
        Args:
            No arguments required
            
        Returns:
            str: Launch Schedule in text format
            
    """

    print("Retrieving Rocket Launch Schedule..")
    
    api_key = "&key=YOUR-API-KEY"
    api_url = "https://fdo.rocketlaunch.live/json/"
    location = "launches?state_abbr=FL&limit=1"

    def convert_utc_to_est(utc_timestamp):
        utc_time = datetime.utcfromtimestamp(utc_timestamp).replace(tzinfo=timezone.utc)
        est_time = utc_time.astimezone(timezone(timedelta(hours=-1)))
        return est_time.strftime('%Y-%m-%d %H:%M:%S')

    def convert_sort_dates(json_data):
        for launch in json_data['result']:
            utc_timestamp = int(launch['sort_date'])
            launch_date = convert_utc_to_est(utc_timestamp)
            launch['launch_date'] = launch_date
        return json_data

    def get_schedule():
        url = api_url + location + api_key 
        response = requests.get(url)
        
        try:
            json_data = response.json()
            updated_json = convert_sort_dates(json_data)
            return updated_json 
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return

    def format_launch_info(launch):
        return (
            f"Launch ID: {launch['id']}\n"
            f"Name: {launch['name']}\n"
            f"Provider: {launch['provider']['name']}\n"
            f"Vehicle: {launch['vehicle']['name']}\n"
            f"Launch Pad: {launch['pad']['name']}, {launch['pad']['location']['statename']}, {launch['pad']['location']['country']}\n"
            f"Mission: {launch['missions'][0]['name']}\n"
            #f"Launch Description: {launch['launch_description']}\n"
            #f"Window Open: {launch['win_open']}\n"
            #f"T0: {launch['t0']}\n"
            #f"Window Close: {launch['win_close']}\n"
            #f"Estimated Date: {launch['est_date']['month']}-{launch['est_date']['day']}-{launch['est_date']['year']}\n"
            f"Launch Date: {launch['launch_date']}\n"  # New field
            f"Tags: {', '.join(tag['text'] for tag in launch['tags'])}\n"
        )

    def json_to_readable_text(updated_data):
        output = ""
        output += f"Valid Authentication: {updated_data['valid_auth']}\n"
        output += f"Count: {updated_data['count']}\n"
        output += f"Limit: {updated_data['limit']}\n"
        output += f"Total: {updated_data['total']}\n"
        output += f"Last Page: {updated_data['last_page']}\n\n"
        
        output += "Launch Schedule:\n\n"
        
        for launch in updated_data['result']:
            output += format_launch_info(launch)
            output += "\n"

        return output

    if create_files:
        def write_to_text_file(text, filename= (docs_dir + "/launch_schedule.txt")):
            with open(filename, "w") as file:
                file.write(text)
                
        def write_to_json_file(data, filename= (docs_dir + "/launch_schedule.json")):
            with open(filename, "w") as file:
                # json.dump(data, file, indent=2) # with line feeds
                json.dump(data, file, separators=(',', ':')) # without line feeds
            
    updated_data = get_schedule()
    write_to_json_file(updated_data)
    if updated_data:
        formatted_text = json_to_readable_text(updated_data)
        write_to_text_file(formatted_text)

    return formatted_text


