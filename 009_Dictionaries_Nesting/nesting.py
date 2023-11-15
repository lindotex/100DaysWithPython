libr = {
    "key":["list","of","data"],
    "key2": {
        "brazil":"brasilia",
        "france":"paris",
    }
}
print(libr["key2"])
print(libr["key2"]["brazil"])
print(libr["key"])
print(libr["key"][2])

# Nesting a list into a Dictionary:
travel_log = {
    "france": ["Paris", "Lille", "Dijon"]
}
for key in range(0, len(travel_log["france"])):
    print(travel_log["france"][key])

# Nesting a Dictionary into a Dictionary:

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visit, list_of_cities):
    new_country = {}
    new_country["country"] = country
    new_country["visit"] = visit
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)

add_new_country("brazil", 4, ["Rio de Janeiro", "Sao paulo", "Salvador", "Ilheus",])
print(travel_log)

print(f"I've been to {travel_log[2]["country"]} {travel_log[2]["visit"]} times ")
print(f"My favorite city was {travel_log[2]["cities"][0]}")