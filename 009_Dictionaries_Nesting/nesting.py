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

travel_log = {
    "france": {
        "Paris": {
            "visits": "2",
        }, 
        "Lille": {
            "visits": "4",
        }, 
        "Dijon": {
            "visits": "6",
        }, 
    },
}

print(travel_log["france"]["Paris"]["visits"])
print(travel_log["france"]["Lille"]["visits"])
print(travel_log["france"]["Dijon"]["visits"])