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


#Deriving more convenient datasets
#activity data without duplicate user_ids, now activity date is latest activity
userData = activityData.drop_duplicates(subset = "user_id", keep = "last")


userData.to_csv("userData.csv")





##### ANALYSIS
"""
Descriptive
"""
def platformActivity():
    #Get unique users
    userData = activityData.drop_duplicates(subset = "user_id", keep = "last")
    ax = sns.countplot(x = "platform", data = userData)
    ax.set_title("Players by Platform")
    plt.show


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
    