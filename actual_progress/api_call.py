import requests as rq
import json

# 
# pkm = input("Pokemon name:\n\n")
# base_url = "https://pokeapi.co/api/v2/pokemon/"
# 
# def get_pokemon_info(pkm):
#     url = f"{base_url}{pkm}/"
#     response = rq.get(url)
#     print(f"\n\n {response}")
#     
#     if response.status_code == 200:
#         print(f"Data for {pkm} was retrieved!\n\n")
#         pokemon_data = response.json()
#         return pokemon_data
#         
#     else:
#         print("Failed to retrieve data for {pkm}")
# 
# pokemon_info = get_pokemon_info(pkm)
# 
# 
# if pokemon_info:
#     print(f"Name: {pokemon_info[\"name\"]}")
#     print(f"ID: {pokemon_info[\"id\"]}")
#     print(f"Height: {pokemon_info[\"height\"]}")
#     print(f"Weight: {pokemon_info[\"weight\"]}")
#     print("\n\n")

payload = {"model":"llama3",
           "messages": [{"role":"user", "content":"message_input"}],
           "stream": False}

url = "https://lovalhost:11434/api/chat"
response = rq.post(url,json=payload)

response_json = json.loads(response.text)

ai_reply  = response_json["message"]["content"]
print(ai_reply)