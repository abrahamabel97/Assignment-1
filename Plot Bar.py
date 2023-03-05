# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 00:10:04 2023

@author: abrah
"""
import pandas as pd
import matplotlib.pyplot as plt

def bargraph(df):
    """
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    plt.figure(figsize = (22,10))
    plt.bar(df.index, df["Value"])
    
    # setting values and text size
    plt.xticks(df.index, fontsize = 15)
    plt.yticks(fontsize = 15)
    
    # setting the limits on x-axis
    plt.xlim(1995, 2006)
    
    # labelling
    plt.xlabel("Years", fontsize = 20)
    plt.ylabel("Subscriptions (per 100 inhabitants)", fontsize = 20)
    
    # titling the plot
    plt.title("Mobile-cellular Telephone Subscriptions", fontsize = 30)
    
    # saving as png
    plt.savefig("bargraph.png")
    
    plt.show()
    
    return

df_subscriptions = pd.read_csv("mobile_subscriptions.csv", index_col = 0)
# calling bargraph with dataframe
bargraph(df_subscriptions)





