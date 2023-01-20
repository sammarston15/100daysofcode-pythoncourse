import requests
from datetime import datetime

TOKEN = "asdflkjasdflkasdf"
USERNAME = "sammarston15"
GRAPH_ID = "graph1"


pixela_base_url = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

""" create user (COMPLETED) """
# response = requests.post(pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)


""" create graph """
graph_endpoint = f"{pixela_base_url}/{USERNAME}/graphs"


headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km", 
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# response.raise_for_status()
# print(response.text)


""" post a pixel """
pixel_creation_endpoint = f"{pixela_base_url}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How far did you go today?\n"),
}

response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
if response.status_code == 503:
    print("   ")
    print('Oops! Try again...')
    print("   ")
    print(response.text)
    print("   ")

elif response.status_code == 200:
    print("   ")
    print("Success:")
    print("   ")
    print(response.text)
    print("   ")



""" update a pixel """
pixel_update_endpoint = f"{pixela_base_url}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5",
}

# response = requests.put(pixel_update_endpoint, json=new_pixel_data, headers=headers)
# response.raise_for_status()
# print(response.text)


""" delete a pixel """
pixel_delete_endpoint = f"{pixela_base_url}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(pixel_delete_endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)



