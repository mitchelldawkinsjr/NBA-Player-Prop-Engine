import requests
import pandas as pd
import json
import math
import argparse
import time

# API keys
API_KEY = "{API_KEY_HERE}"
BASE_URL = "https://api.sportradar.com"

# Function to pull player stats by season and team
def get_player_stats(team_id, season, league="nba"):
    # url = f"{BASE_URL}/{league}/trial/v8/en/players/{player_id}/profile.json?api_key={API_KEY}"
    url = f"{BASE_URL}/{league}/trial/v8/en/seasons/{season}/REG/teams/{team_id}/statistics.json?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve player stats:", response.status_code)

# Function to pull probability of specific stats
def poisson_probability_at_least_k(lambda_value, k, stat_name, percent):
    """
    Calculate the probability of getting at least k occurrences
    in a Poisson distribution with mean (lambda_value).
    
    Parameters:
    - lambda_value: Average number of occurrences (e.g., rebounds)
    - k: The threshold number of occurrences

    Returns:
    - Probability of at least k occurrences as a percentage
    """
    # Calculate cumulative probability for P(X < k)
    cumulative_probability = sum(
        (math.exp(-lambda_value) * (lambda_value ** i)) / math.factorial(i)
        for i in range(k)
    )

    # Calculate the probability of getting at least k occurrences
    probability_at_least_k = 1 - cumulative_probability
    
    # Calculate the percentage
    probability = probability_at_least_k * 100

    if (probability > percent) :
        response = f"Probability of {k} {stat_name} is: {probability:.2f}%"
        return (response)
    else :
        return ''

def main(season_year, points, rebounds, assists, percent):
    avg_rebounds = 0;
    avg_points = 0;
    avg_assists = 0;

    print(f"Season: {season_year}")

    teams = [
        ("583ec8d4-fb46-11e1-82cb-f4ce4684ea4c",'wizards'),
        ("583ecb3a-fb46-11e1-82cb-f4ce4684ea4c",'rockets'),
        ("583ece50-fb46-11e1-82cb-f4ce4684ea4c",'jazz'),
        ("583ecefd-fb46-11e1-82cb-f4ce4684ea4c",'bucks'),
        ("583ecae2-fb46-11e1-82cb-f4ce4684ea4c",'lakers'),
        ("583eccfa-fb46-11e1-82cb-f4ce4684ea4c",'celtics'),
        ("583eca2f-fb46-11e1-82cb-f4ce4684ea4c",'wovles'),
        ("583ed102-fb46-11e1-82cb-f4ce4684ea4c",'nuggets'),
        ("583ec9d6-fb46-11e1-82cb-f4ce4684ea4c",'nets'),
        ("583ed0ac-fb46-11e1-82cb-f4ce4684ea4c",'kings'),
        ("583ecc9a-fb46-11e1-82cb-f4ce4684ea4c",'pelicans'),
        ("583ecf50-fb46-11e1-82cb-f4ce4684ea4c",'mavs'),
        ("583ec97e-fb46-11e1-82cb-f4ce4684ea4c",'hornets'),
        ("583ec825-fb46-11e1-82cb-f4ce4684ea4c",'warriors'),
        ("583ecdfb-fb46-11e1-82cb-f4ce4684ea4c",'clippers'),
        ("583ecfa8-fb46-11e1-82cb-f4ce4684ea4c",'suns'),
        ("583ecb8f-fb46-11e1-82cb-f4ce4684ea4c",'hawks'),
        ("583ecea6-fb46-11e1-82cb-f4ce4684ea4c",'heat'),
        ("583ec70e-fb46-11e1-82cb-f4ce4684ea4c",'knicks'),
        ("583ed157-fb46-11e1-82cb-f4ce4684ea4c",'magic'),
        ("583ec87d-fb46-11e1-82cb-f4ce4684ea4c",'sixers'),
        ("583ecda6-fb46-11e1-82cb-f4ce4684ea4c",'raptors'),
        ("583ec5fd-fb46-11e1-82cb-f4ce4684ea4c",'bulls'),
        ("583ec773-fb46-11e1-82cb-f4ce4684ea4c",'cavs'),
        ("583ec7cd-fb46-11e1-82cb-f4ce4684ea4c",'pacers'),
        ("583ecfff-fb46-11e1-82cb-f4ce4684ea4c",'thunder'),
        ("583ecd4f-fb46-11e1-82cb-f4ce4684ea4c",'spurs')
    ]

    for team, team_name in teams:
        # Sleep for 1/2 second after each team stats have been pulled
        time.sleep(.500)
        print("==================================================", "\n")
        team_data = get_player_stats(team, season_year, "nba")
        # Sleep for 1/2 second after each team stats have been pulled
        time.sleep(.500)

        if team_data is None:
            continue
            # print(f"Error: No data returned for team {team}. \n")
        else:
            for player in team_data['players']:
                if player["full_name"] and player["average"]["minutes"] >= 25:
                    rp = poisson_probability_at_least_k(player["average"]["rebounds"], rebounds, 'Rebounds', percent)
                    pp = poisson_probability_at_least_k(player["average"]["points"], points, 'Points', percent)
                    ap = poisson_probability_at_least_k(player["average"]["assists"], assists, 'Assists', percent)
                    tpp = poisson_probability_at_least_k(player["average"]["three_points_made"], 2, 'Three points made', percent)
                    bp = poisson_probability_at_least_k(player["average"]["blocks"], 1, 'Blocks', percent)
                    sp = poisson_probability_at_least_k(player["average"]["steals"], 1, 'Steals', percent)
                   
                    if (rp or pp or ap or tpp or bp or sp) :
                        print(player["full_name"], " | ", team_name)
                        print()
                        if rp:
                            print(rp)
                        if pp:
                            print(pp)
                        if ap:
                            print(ap)
                        if tpp:
                            print(tpp)
                        if bp:
                            print(bp)
                        if sp:
                            print(sp)
if __name__ == "__main__":

    #season - points - rebounds - assists - percent
    main(2024, 20, 6, 6, 85)
