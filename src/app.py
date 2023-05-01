"""Main app to retrieve football odds"""
from flask import Flask, render_template
import requests
from utils.side_requests import get_league_info, get_team_info
app = Flask(__name__)

@app.route('/')
def index():
    start_date = '2023-04-28'
    end_date = '2023-05-05'
    
    URL = f'https://soccer.sportmonks.com/api/v2.0/fixtures/between/{start_date}/{end_date}'
    response = requests.get(url=URL, params={'api_token': 'eAquVUhxieIpktGdlFUxJ9LQIg90lr4XOQRwVh96alISKedpXWLyFSgMDTBS'},)
    json_response = response.json()
    
    if json_response and 'data' in json_response:
        for row in json_response['data']:
            # League info
            league_info = get_league_info(row['league_id'])
            if league_info:                
                print('League name', league_info['data']['name'])
                
            # Team info
            lteam_info = get_team_info(row['localteam_id'])
            vteam_info = get_team_info(row['visitorteam_id'])
            if lteam_info and vteam_info:
                print('Local:{} Visitor:{}'.format(lteam_info['data']['name'], vteam_info['data']['name']))
                
    return render_template('index.html')

    