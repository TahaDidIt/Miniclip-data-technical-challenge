# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:48:27 2024

@author: Taha
"""
##### SET-UP
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import norm



#Loading datasets into a Pandas dataframe
csvPathActivity = "C:/Taha/projects/Data Science Fundamentals with Python and SQL/Miniclip analysis task working directory/data_activity.csv"
csvPathIAP = "C:/Taha/projects/Data Science Fundamentals with Python and SQL/Miniclip analysis task working directory/data_in_app_purchases.csv"
csvPathMatches = "C:/Taha/projects/Data Science Fundamentals with Python and SQL/Miniclip analysis task working directory/data_matches.csv"
csvPathVP = "C:/Taha/projects/Data Science Fundamentals with Python and SQL/Miniclip analysis task working directory/data_virtual_purchase.csv"

activityData = pd.read_csv(csvPathActivity)
IAPData = pd.read_csv(csvPathIAP)
matchesData = pd.read_csv(csvPathMatches)
VPData = pd.read_csv(csvPathVP)



### Deriving more convenient datasets

#activity data without duplicate user_ids
#Note: now activity date is the latest activity
userData = activityData.drop_duplicates(subset = "user_id", keep = "last")

"""NOTE: Users in activity and transactions tables are not all the same-
    many users will not be filled in for below"""
#Merging userData and IAP and VP data
#grouping IAP by user
totalIAPSpend = IAPData.groupby("user_id")["dollar_purchase_value"].sum().reset_index()
#merge with userData
userIAPs = pd.merge(userData, totalIAPSpend, on = "user_id", how = "left")
#grouping VP by user
totalVPSpend = VPData.groupby("user_id")["gold_spend"].sum().reset_index()
#Now merge with userIAPs to get full user spend record
userSpend = pd.merge(userIAPs, totalVPSpend, on = "user_id", how = "left")
#fill null values where a user has never spent
userSpend["dollar_purchase_value"] = userSpend["dollar_purchase_value"].fillna(0)
userSpend["gold_spend"] = userSpend["gold_spend"].fillna(0)

#Calculating winrate and matches played data
#total matches played by each user
matchesPlayed = matchesData.groupby("user_id")["n_matches"].sum().reset_index()
#total wins of each user
winsRecord = matchesData.loc[matchesData["finish_position"] == 1, ["user_id", "n_matches"]].reset_index()
totalWins = winsRecord.groupby("user_id")["n_matches"].sum().reset_index()

userRecord = pd.merge(totalWins, VPData, on = "user_id", how = "inner")



"""
userRecord = pd.DataFrame({
    "user_id"
    })
"""


"""
userData.to_csv("userData.csv")
"""





##### ANALYSIS
"""
Descriptive
"""
def platformActivity():
    #Get unique users
    userData = activityData.drop_duplicates(subset = "user_id", keep = "last")
    ax = sns.countplot(x = "platform", data = userData)
    ax.set_title("Players by Platform")
    plt.show()


"""
Distributions
"""



"""
Tests
"""






##### MAIN MENU


### Analysis index
plotFunctions = {}

### Menu
menuChoice = ""
while menuChoice != "0":
    #Time and spacer for ease of reading
    print("")
    print("")
    print("")
    print("########## ", "Current Time: ", datetime.now().strftime("%H:%M:%S"))
    print("")
    #Menu choices
    print("Main Menu:")
    for i in plotFunctions:
        print(i, ": ", plotFunctions[i])
    
    menuChoice = input("Please select a number from the options: ")
    if menuChoice == "0":
        pass
    elif int(menuChoice) in plotFunctions:
        print("")
        plotFunctions[int(menuChoice)]()
    else:
        print("Invalid choice, please try again.")
    