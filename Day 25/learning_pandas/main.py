import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250509.csv")

fur_color_list = data["Primary Fur Color"].tolist()

gray = 0
cinnamon = 0
black = 0

for color in fur_color_list:
    match color:
        case "Gray":
            gray += 1
        case "Cinnamon":
            cinnamon += 1
        case "Black":
            black += 1

data_dict = {
    "Fur color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray, cinnamon, black],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
