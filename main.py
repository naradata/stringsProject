player_name = 'zywoo'
country = 'france'
role = 'awper'
age = 25
hltv_rating = 1.30

print('COUNTER-STRIKE PLAYER PROFILE')
print()


players = [
    {
        'name': 'zywoo',
        'country': 'france',
        'role': 'awper',
        'age': '25',
        'hltv_rating': 1.30,
        'team': 'vitality',
    },
    {
        'name': 'donk',
        'country': 'russia',
        'age': '19',
        'role': 'rifler',
        'hltv_rating': 1.35,
        'team': 'spirit',
    
    },
    {
        'name': 'niko',
        'country': 'bosnia and herzegovina',
        'age': '29',
        'role': 'rifler',
        'hltv_rating': 1.18,
        'team': 'falcons',
    },
    {
        'name': 'kyousuke',
        'country': 'russia',
        'age': '19',
        'role': 'rifler',
        'hltv_rating': 1.15,
        'team': 'falcons',
    },
    {
        'name': 'xkacpersky',
        'country': 'poland',
        'age': '19',
        'role': 'rifler',
        'hltv_rating': 1.09,
        'team': 'ninjas in pajamas',
    },
{
        'name': 'blitz',
        'country': 'mongolia',
        'age': '24',
        'role': 'igl',
        'hltv_rating': 1.02,
        'team': 'the mongolz',
    },
{
        'name': 'm0nesy',
        'country': 'russia',
        'age': '21',
        'role': 'awper',
        'hltv_rating': 1.27,
        'team': 'falcons',
    },
{
        'name': 'sh1ro',
        'country': 'russia',
        'age': '24',
        'role': 'awper',
        'hltv_rating': 1.17,
        'team': 'spirit',
    },
{
        'name': 'hunter',
        'country': 'bosnia and herzegovina',
        'age': '30',
        'role': 'igl',
        'hltv_rating': 1.06,
        'team': 'g2',
    },
{
        'name': 'rntu',
        'country': 'united states of america',
        'age': '21',
        'role': 'rifler',
        'hltv_rating': 1.27,
        'team': '99w9',

    },
]

while True:
    search_name = input("Enter a player name, or type quit to stop: ")
   
    if search_name.strip().lower() == "quit":
        break
    
    found_player = False



    for player in players:
        if search_name.strip().lower() == player['name'].lower():
            found_player = True
    
            print()
            print(f"PLAYER PROFILE: {player['name'].upper()}")
            print('-' * 32)
            print(f"Name: {player['name'].upper()}")
            print(f"Age: {player['age']}")
            print(f"Country: {player['country'].title()}")
            print(f"Role: {player['role'].upper()}")
            print(f"Team: {player['team'].upper()}")
            print(f"HLTV Rating: {player['hltv_rating']:.2f}")
            print("-" * 32)
            print()

    if found_player == False:
        print("Player not found.")
    