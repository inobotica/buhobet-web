import requests
import json
import os
from utils.constants import (
    API_PATH,
    GET_MATCHES_BETWEEN_DATES_ENDPOINT,
    GET_LEAGUE_INFO_ENDPOINT,
    GET_TEAM_INFO_ENDPOINT
)

def generic_request(url_: str, query_params:dict=None)->json:
    """_summary_

    Args:
        url_ (str): API endpoint
        query_params (dict, optional): Query parameters. Defaults to None.

    Returns:
        json: Request result
    """
    print('Requesting info from:', url_)
    
    PARAMS = {'api_token': 'eAquVUhxieIpktGdlFUxJ9LQIg90lr4XOQRwVh96alISKedpXWLyFSgMDTBS'}
    
    if query_params:
        PARAMS.update(query_params)
    response = requests.get(url=url_, params=PARAMS,)
    json_response = response.json()
    print(json_response)
    
    return json_response
    
def get_league_info(league_id: int)->json:
    """Get league info

    Args:
        league_id (int): League id

    Returns:
        dict: Information of league
    """
    
    url = API_PATH + GET_LEAGUE_INFO_ENDPOINT
    url = url.format(**locals())
    
    response = generic_request(url)
    return response

def get_team_info(team_id:int)->json:
    """Gets team info

    Args:
        team_id (int): ID of team

    Returns:
        json: Informatio about the team
    """
    
    url = API_PATH + GET_TEAM_INFO_ENDPOINT
    url = url.format(**locals())
    
    response = generic_request(url)
    return response