import requests

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
opentdb_data = response.json()

question_data = opentdb_data["results"]
