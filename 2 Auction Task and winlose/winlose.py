# -*- coding: utf-8 -*-
"""
Better and messier than ever!!

March 8 2022
@author: mauspad
"""
# import packages
import pandas as pd
from numpy import random
import glob
import os.path

# get ready to save results

# grab latest output file
folder_path = r'data'
file_type = r'\*csv'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
print("Output file chosen: " + max_file)

#get ready to save log
max_filename = max_file.replace(".csv", "")
f = open(max_filename + "_winlose.txt", "a")

# turn csv into dataframe
df = pd.read_csv(max_file)

# set index
df.set_index("image_file", inplace=True)

#make dataframe with only bids on possible snacks
result = df.loc[["ImageFiles_Cropped/FruitSnacks_120_cropped.jpg", "ImageFiles_Cropped/CheeseAndCrackers_120_cropped.jpg", "ImageFiles_Cropped/PeanutbutterAndCrackers_120_cropped.jpg", "ImageFiles_Cropped/Pretzels_120_cropped.jpg"],["Bid"]]

#choose randomly from possible snacks
chosen = result.sample(n=1)
chosenname = str((chosen.index.values)[0])
chosenname = chosenname.replace("ImageFiles_Cropped/", "")
chosenname = chosenname.replace("_120_cropped.jpg", "")
print("Item chosen: " + chosenname, file=f)
print("Item chosen: " + chosenname)
subjectbid = (float(chosen.iloc[0]["Bid"]) / 200)
subjectbid = round(subjectbid, 2)
print("Participant bid " + "{:.2f}".format(subjectbid), file=f)
print("Participant bid " + "{:.2f}".format(subjectbid))

#generate computer bid
compbid = random.uniform(0,5)
compbid = round(compbid, 2)
print("Computer bids " + "{:.2f}".format(compbid), file=f)
print("Computer bids " + "{:.2f}".format(compbid))

#compare bids
if compbid < subjectbid:
	print("Participant wins! Give " + chosenname + " and $" + "{:.2f}".format(5 - subjectbid) + " after task", file=f)
	print("Participant wins! Give " + chosenname + " and $" + "{:.2f}".format(5 - subjectbid) + " after task")
else:
	print("Computer wins! Too bad ;)", file=f)
	print("Computer wins! Too bad ;)")

#close log
f.close()

