import json
import csv
import urllib.request
base_url = 'https://fantasy.premierleague.com/drf/bootstrap-static'
offline_url = r'bootstrap-static.json'


def Data_Viewer():

    file = open(offline_url, encoding='utf-8')
    data = json.load(file)
    for item in data["elements"]:
        if item["id"] < 10:
            print(item["id"], "-", item["web_name"])
    file.close()


def JSON_Edit():
    file = open(offline_url, encoding='utf-8')
    data = json.load(file)
    Pos_List = ['GK', 'Def', 'Mid', 'For']
    for x in Pos_List:
        fx = x + '_Data.json'
        outfile = open(fx, 'w+')
        Elem_Check = {'GK': 1, 'Def': 2, 'Mid': 3, 'For': 4}
        Elem_Type = Elem_Check[x]
        i = 1
        for item in data["elements"]:
            if item["element_type"] == Elem_Type:
                item["id"] = i
                json.dump(item, outfile)
                i += 1
        outfile.close()
        JSON_Decorate(x)
        JSON_to_CSV(x)

    file.close()
    outfile.close()


def JSON_Decorate(x):
    fx1 = x + '_Data.json'
    with open(fx1, 'r') as file1:
        data = file1.read()
        newdata = data.replace('}{', '},{')

    with open(fx1, 'w') as file1:
        file1.write('[')
        file1.write(newdata)
        file1.write(']')


def JSON_to_CSV(x):

    file = open(offline_url, encoding='utf-8')
    fx = x + '_Data.json'
    fx2 = x + '_Data.csv'
    outfile1 = open(fx, 'r')
    data = json.load(file)
    for item in data["elements"]:
        fn = list((item.keys()))
        print("%s successful" % (x))
        break
    rows = json.load(outfile1)
    with open(fx2, 'w+', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['id', 'photo', 'web_name', 'team_code', 'status', 'code', 'first_name', 'second_name', 'squad_number', 'news', 'now_cost', 'news_added', 'chance_of_playing_this_round', 'chance_of_playing_next_round', 'value_form', 'value_season', 'cost_change_start', 'cost_change_event', 'cost_change_start_fall', 'cost_change_event_fall', 'in_dreamteam', 'dreamteam_count', 'selected_by_percent', 'form', 'transfers_out', 'transfers_in',
                                                    'transfers_out_event', 'transfers_in_event', 'loans_in', 'loans_out', 'loaned_in', 'loaned_out', 'total_points', 'event_points', 'points_per_game', 'ep_this', 'ep_next', 'special', 'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index', 'ea_index', 'element_type', 'team'])
        dict_writer.writeheader()
        dict_writer.writerows(rows)

    file.close()
    outfile1.close()


# def Label_Dict_Map():
#     file = open(offline_url, encoding='utf-8')
#     data = json.load(file)
#     global Label_Dict
#     Dict = {}
#     for item in data["stats"]["headings"]:
#         k = item["field"]
#         v = item["label"]
#         Label_Dict[k] = v
#     file.close()


def Team_Dict_Map():
    file = open('Team_Data.json', encoding='utf-8')
    data = json.load(file)
    global Team_Dict
    Team_Dict = {}
    i = 0
    while i < len(data):
        li = []
        item = data[i]
        var = ["name", "short_name"]
        for x in var:
            li.append(item[x])
        Team_Dict[item["code"]] = li
        i += 1
    file.close()


def Editor(x):
    JSON_Edit()
    JSON_to_CSV(x)


def Data_Update(url1):
    urllib.request.urlretrieve(url1, offline_url)
    JSON_Edit()

if (input("Is network available : ")).lower() == "y":
    Data_Update(base_url)
else:
    JSON_Edit()
