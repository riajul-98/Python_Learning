import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250102.csv")
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_squirrel, gray_squirrel, cinnamon_squirrel]
}

data = pd.DataFrame(data_dict)
data.to_csv("squirrels.csv")