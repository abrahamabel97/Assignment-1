# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:13:58 2023

@author: abrah
"""

import pandas as pd
import matplotlib.pyplot as plt

def piechart(df):
    """
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    plt.figure(figsize = (20, 10))
    
    plt.subplot(1, 2, 1)
    plt.pie(df[1990], labels = df.index,
            autopct = '%1.0f%%', textprops = {'fontsize': 20})
    
    plt.title("Population (1990)", fontsize = 25)
    
    plt.subplot(1, 2, 2)
    plt.pie(df[2020], labels = df.index,
            autopct = '%1.0f%%', textprops = {'fontsize' : 20})
    
    plt.title("Population (2020)", fontsize = 25)
    
    plt.savefig("piechart.png")
    
    plt.show()
    
    return

df_population = pd.read_excel("population_growth.xlsx", index_col = 0)

piechart(df_population)
    
    