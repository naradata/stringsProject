player_name = 'zywoo'
country = 'france'
role = 'awper'
age = 25
hltv_rating = 1.30

print('COUNTER-STRIKE PLAYER PROFILE')


players = [
    {
        'name': 'zywoo',
        'country': 'france',
        'role': 'awper',
        'age': '25',
        'hltv_rating': 1.30,
    },
    {
        'name': 'donk',
        'country': 'russia',
        'age': '19',
        'role': 'rifler',
        'hltv_rating': 1.35,
    
    },
]

print(players[0]['name'])
print(players[1]['name'])

for player in players:
    print(f"PLAYER PROFILE: {player['name'].upper()}")
    print('-' * 32)
    print(f"Name: {player['name'].upper()}")
    print(f"Country: {player['country'].title()}")
    print(f"Role: {player['role'].upper()}")
    print(f"Age: {player['age']}")
    print(f"HLTV Rating: {player['hltv_rating']:.2f}")
    print("-" * 32)
    print()
