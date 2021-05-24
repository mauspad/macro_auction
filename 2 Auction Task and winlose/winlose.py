# -*- coding: utf-8 -*-
"""
Usage: Change file name on line 13 before running. And change items too if you want I guess.

feb 25 2021
@author: mauspad
"""
# import packages
import pandas as pd
from numpy import random

# turn csv into dataframe
df = pd.read_csv("data/test_macro_auction_2021_Apr_07_1330.csv") #change!

# set index
df.set_index("image_file", inplace=True)

#make dataframe with only bids on possible snacks
result = df.loc[["ImageFiles_Cropped/FruitSnacks_120_cropped.jpg", "ImageFiles_Cropped/CheeseAndCrackers_120_cropped.jpg", "ImageFiles_Cropped/PeanutbutterAndCrackers_120_cropped.jpg", "ImageFiles_Cropped/Pretzels_120_cropped.jpg"],["Bid"]]

#choose randomly from these
chosen = result.sample(n=1)
chosenname = str((chosen.index.values)[0])
print("Item chosen: " + chosenname)
subjectbid = (float(chosen.iloc[0]["Bid"]) / 200)
print("Participant bid " + str(subjectbid))

#generate computer bid
compbid = random.uniform(0,5)
print("Computer bids " + str(compbid))

#compare bids
if compbid < subjectbid:
	print("Participant wins! Give " + chosenname + " and $" + str(5 - subjectbid) + " after task")
	
else:
	print("Computer wins! Too bad ;)")

