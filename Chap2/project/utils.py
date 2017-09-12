import ast
import json
import csv

def load_json_file(file):
    """load json file and return data_dict
    :param file json file format
    """
    with open(file, "r", encoding="utf-8-sig") as file:
        data_dict = ast.literal_eval(file.read())
        #jsn = json.dumps(data_dict)
    return data_dict

def parse_json(json_data, **required_data):
    extracted_data = {}
    for key, data in required_data.items():
        tmp = json_data
        if ("." in data):
            temp_keys = data.split(".")
            for temp_key in temp_keys:
                tmp = tmp[temp_key]
            extracted_data[key] = tmp
        else:
            extracted_data[key] = json_data[data]
    return extracted_data

def parse_json_dot(json_data, **required_data):
    from objectjson import ObjectJson as objson
    extracted_data = {}
    j = objson(json_data)
    for key, data in required_data.items():
        extracted_data[key] = getattr(j, data)
    return extracted_data

def read_file(filename, mode, buffer, encoding=None):
    with open(filename, mode, buffer, encoding) as file:
        return file.read()

def show_history(history):
    if (len(history) == 0):
        print("Not history records are found, please do some search and retry")
    else:
        for k, v in history.items():
            print(f"{k}\n{v}")

def city_exists(city, json_data):
    status = json_data['status']
    if status == "ok":
        return True, status
    else:
        return False, status

def cmd_exists(cmd, commands):
    for command in commands:
        if type(command) == type("str"):
            command = [command]
        if cmd in command:
            return True
        else:
            continue
    return False

def show_weather(city, weather_info):
    city_weather = ""
    for k, v in weather_info.items():
        city_weather += f"{k}:{v}\n"
        # set to Unknown if weather is empty from the source data
        if city_weather == "":
            city_weather = "未知天气"
    return city_weather

def load_schedule_from_config(config_file):
    json_data = load_json_file(config_file)
    city = json_data['city']
    frequency = json_data['frequency']
    fixed_time = json_data['fixed_time']
    print(
    f"Your current schedule setting is:\ncity: {city}\nfrequency: {frequency}\nfixed_time:{fixed_time}"
    )
    if not city:
        print("You haven't specified a city, please reset")
    if not any(frequency, fixed_time):
        print(
        "You have to specify either a frequency or a fixed time, if both set, by default frequency will be used; please reset"
        )
    return json_data

def schedule(config_file):
    # load current settings from config file
    json_data = load_schedule_from_config(config_file)
    frequency = '' #json_data['frequency']
    fixed_time = '' #json_data['fixed_time']
    # ask user if he wants to update the settings
    mark_for_change = input("  > Do you want to change these settings(y/n)?")
    if mark_for_change == "y":
        city = input("    >> enter the city name: ")
        run_on = input(
        "    >> do you want to run at specified time or at frequencies? (s/f): "
        )
        if run_on == "s":
            fixed_time = input(
            "        >> enter a datetime (2017/8/20 15:10:00): "
            )
        else:
            frequency = input(
            "        >> enter a frequency(1h for 1 hour,1m for 1 minute, 1s for 1 second): "
            )
        #print({'city':city, "fixed_time": fixed_time,"frequency":frequency})
        json_data['city'] = city
        json_data['frequency'] = frequency
        json_data['fixed_time'] = fixed_time
        # write new setting back to config file
        with open(config_file, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_data))
        print(
        f"Your new schedule setting is:\n city: {city} \n frequency:{frequency} \n fixed time: {fixed_time}\n"
        )
    return json_data

def switch():
    mode = input("    > Please select a mode(m for manual, a for auto):")
    return mode

def convert_tuple_to_list(t, list_=[]):
    for item in t:
        if  isinstance (item, tuple):
            list_ = convert_tuple_to_list(item, list_)
        else:
            list_.append(item)
    return list_

def load_all_cities_from_csv(filename, *colnames):
    cities = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for col in colnames:
                cities.append(row[col])
    return cities
