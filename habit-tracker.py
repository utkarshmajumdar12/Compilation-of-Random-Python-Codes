import requests
from datetime import datetime

TOKEN ="wh7nwindi902m"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token":TOKEN,
    "username":"utkarsh27",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

'''response = requests.post(url = PIXELA_ENDPOINT, json = user_params )
print(response.text)'''

'''graph_endpoint = "https://pixe.la/v1/users/utkarsh27/graphs"
graph_params = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"Min",
    "type":"float",
    "color":"momiji",
}
headers = {
    "X-USER-TOKEN":TOKEN
}

response =  requests.post(url=graph_endpoint, json=graph_params, headers= headers)
print(response.text)'''
today = datetime.now()

post_pixel_endpoint = "https://pixe.la/v1/users/utkarsh27/graphs/graph1"

pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"4",
}

headers = {
    "X-USER-TOKEN":TOKEN,
}
response  = requests.post(url= post_pixel_endpoint, json= pixel_params, headers=headers)
print(response.text)