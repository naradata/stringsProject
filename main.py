print("COUNTER-STRIKE PRO STATS".center(78, "="))
print()

player_name = "zywoo"
age = 25
country = "france"
role = "awper"
hltv_rating = 1.30

print("Featured Player")
print("-" * 78)
print(f"Name: {player_name.upper()}")
print(f"Age: {age}")
print(f"Country of Origin: {country.title()}")
print(f"Role: {role.upper()}")
print(f"HLTV Rating: {hltv_rating:.2f}")
print()

players = [
    {
        "name": "m0nesy",
        "age": 21,
        "country": "russia",
        "role": "awper",
        "hltv_rating": 1.27,
    },
    {
        "name": "donk",
        "age": 19,
        "country": "russia",
        "role": "rifler",
        "hltv_rating": 1.35,
    },
    {
        "name": "ropz",
        "age": 26,
        "country": "estonia",
        "role": "lurker",
        "hltv_rating": 1.10,
    },
    {
        "name": "niko",
        "age": 29,
        "country": "bosnia and herzegovina",
        "role": "rifler",
        "hltv_rating": 1.18,
    },
]

print("Player Table")
print("-" * 78)
print(f"{'Name':<14}{'Age':<8}{'Country':<26}{'Role':<16}{'Rating':>8}")
print("-" * 78)

for player in players:
    name = player["name"].upper()
    country = player["country"].title()
    role = player["role"].title()
    rating = player["hltv_rating"]

    print(f"{name:<14}{player['age']:<8}{country:<26}{role:<16}{rating:>8.2f}")

print("-" * 78)

total_rating = 0

for player in players:
    total_rating += player["hltv_rating"]

average_rating = total_rating / len(players)
best_player = max(players, key=lambda player: player["hltv_rating"])

summary = (
    f"The average HLTV rating is {average_rating:.2f}. "
    f"The highest-rated sample player is {best_player['name'].upper()} "
    f"with a rating of {best_player['hltv_rating']:.2f}."
)

print()
print(summary)
