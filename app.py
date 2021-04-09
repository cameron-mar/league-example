import json
import requests
import os

api_key = os.environ["API_KEY"]
base_url = "https://na1.api.riotgames.com/lol"

def get(url, headers):
    """
    Makes a get call to the riot api
    """
    default_headers = {"X-Riot-Token": api_key}
    default_headers.update(headers)
    response = requests.get(url, headers=default_headers)
    response_json = response.json()
    return response_json

def get_champion_mastery(summoner_id):
    champion_mastery_url = f"{base_url}/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"
    mastery = get(champion_mastery_url, ())
    return mastery

def get_champion_rotation():
    champion_rotation_url = f"{base_url}/platform/v3/champion-rotations"
    champion_rotation_response = get(champion_rotation_url, ())
    return champion_rotation_response["freeChampionIds"]

def get_summoner_info(summoner_name):
    summoner_url = f"{base_url}/summoner/v4/summoners/by-name/{summoner_name}"
    summoner_info = get(summoner_url, ())
    return summoner_info

def run():
    champion_rotation_ids = get_champion_rotation()
    summoner_info = get_summoner_info("blahty13")
    summoner_id = summoner_info["id"]
    summoner_puuid = summoner_info["puuid"]
    mastery = get_champion_mastery(summoner_id)

if __name__ == "__main__":
    run()