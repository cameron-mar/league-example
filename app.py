import json
import requests
import os

def run():
    api_key = os.environ["API_KEY"]
    url = "https://na1.api.riotgames.com/lol/platform/v3/champion-rotations"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    free_champion_ids = response_json["freeChampionIds"]


if __name__ == "__main__":
    run()