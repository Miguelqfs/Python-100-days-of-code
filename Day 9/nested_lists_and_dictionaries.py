capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 8,
    },
    "Germany": {
        "cities_visited":["Stuttgart", "Berlin"],
        "total_visits": 5,
    },
}

print(travel_log["Germany"]["cities_visited"][0])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict[1] = 4
print(dict)