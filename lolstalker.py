import json
import urllib2
import time
api_key= ""
array_summoners=[ "generalblood1"]
positions = (("TOP", 1), ("MIDDLE", 2), ("JUNGLE", 3), ("BOT", 4))
roles = (("DUO", 1), ("SUPPORT", 2), ("CARRY", 3), ("SOLO", 4))


def api_call(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_json_result = json.load(response)    

    time.sleep(1)
    return the_json_result


def look_up_summoner_by_name(summoner, region="na"):
    print "Looking up: "+  summoner
        
    url = "https://%s.api.pvp.net/api/lol/%s/v1.4/summoner/by-name/%s/?%s" % (region, region, summoner, "api_key=" +  api_key) 
    summoner_id = api_call(url)[summoner]["id"]
    print "The summoner's id is "+ str(summoner_id)
    return summoner_id


def get_match_list_by_id(summoner_id, region="na"):
    url = "https://%s.api.pvp.net/api/lol/%s/v1.3/game/by-summoner/%s/recent?%s" % (region, region, summoner_id, "api_key=" +  api_key)
    match_list = api_call(url)
    return match_list


def get_champion_by_id(champ_id):
    url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/%s/?%s" % (champ_id, "api_key=" +  api_key) # + "&champData=all
    champion = api_call(url)
    return champion


def get_player_by_id(summoner_id, region="na"):
    url = "https://%s.api.pvp.net/api/lol/%s/v1.4/summoner/%s/?%s" %(region, region, summoner_id, "api_key=" +  api_key)
    summoner = api_call(url)
    return summoner


def get_spell_by_id(spell_id, region="na"):
    url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell/%s/?%s" %(spell_id, "api_key=" +  api_key) # "&spellData=all
    spell = api_call(url)
    return spell


def get_item_by_id(item_id, region="na"):
    url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/%s/?%s" %(item_id, "api_key=" +  api_key) # "&itemData=all
    item = api_call(url)
    item["description"] = item["description"].replace("<br>", "\n")
    return item


def generate_match_stats(match):
    match["champion"] = get_champion_by_id(match["championId"])
    
    if match["teamId"] == 100:
        match["team"] = "blue"
        del match["teamId"]
    else:
        match["team"] = "purple"
        del match["teamId"]
    
    match["spell1"] = get_spell_by_id(match["spell1"])
    match["spell2"] = get_spell_by_id(match["spell2"])

    if match["stats"].get("item0"):
        match["stats"]["item0"] = get_item_by_id(match["stats"]["item0"])
    if match["stats"].get("item1"):
        match["stats"]["item1"] = get_item_by_id(match["stats"]["item1"])
    if match["stats"].get("item2"):
        match["stats"]["item2"] = get_item_by_id(match["stats"]["item2"])
    if match["stats"].get("item3"):
        match["stats"]["item3"] = get_item_by_id(match["stats"]["item3"])
    if match["stats"].get("item4"):
        match["stats"]["item4"] = get_item_by_id(match["stats"]["item4"])
    if match["stats"].get("item5"):
        match["stats"]["item5"] = get_item_by_id(match["stats"]["item5"])
    if match["stats"].get("item6"):
        match["stats"]["item6"] = get_item_by_id(match["stats"]["item6"])
    
    for position in positions:
        if match["stats"]["playerPosition"] == position[1]:
            match["stats"] ["playerPosition"] = position[0]
            break
    
    for role in roles:
        if match["stats"]["playerRole"] == role[1]:
            match["stats"] ["playerRole"] = role[0]
            break

    for indice, fellow_player in enumerate(match["fellowPlayers"]):
        match["fellowPlayers"][indice]["summoner"] = get_player_by_id(fellow_player["summonerId"])
        del match["fellowPlayers"][indice]["summonerId"] 
        
        match["fellowPlayers"][indice]["champion"] = get_champion_by_id(fellow_player["championId"])
        del match["fellowPlayers"][indice]["championId"] 
        
        if fellow_player["teamId"] == 100:
            match["fellowPlayers"][indice]["team"] = "blue"
            del match["fellowPlayers"][indice]["teamId"]
        else:
            match["fellowPlayers"][indice]["team"] = "purple"
            del match["fellowPlayers"][indice]["teamId"]
    return match


def lambda_handler(event, context):


    for summoner in array_summoners:
        summoner_id = look_up_summoner_by_name(summoner)
        
        match_list = get_match_list_by_id(summoner_id)

        if isinstance(event.get("to_print"), int):

            match_list["games"][event.get("to_print")] = generate_match_stats(match_list["games"][event.get("to_print")] )
            print json.dumps(match_list["games"][event.get("to_print")], indent=4).replace("\\n", "\n\t\t\t\t")
        else:
            for index, match in enumerate(match_list["games"]):
                match_list["games"][index] = generate_match_stats(match)
                print "Match is :"+ json.dumps(match_list["games"][index], indent=4).replace("\\n", "\n\t\t\t")

    
    return "Stalked"
if __name__ == "__main__":
    lambda_handler({"to_print": 0}, None)
