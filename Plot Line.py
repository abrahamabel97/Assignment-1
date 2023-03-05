# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:45:19 2023

@author: abrah
"""

import pandas as pd
import matplotlib.pyplot as plt

def lineplot(df, headers):
    """

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.
    headers : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
   
    
    plt.figure(figsize = (17, 6.5))
    
    # plotting each head
    for head in headers:
        plt.plot(df.columns, df.loc[head], label=head)
        
    # increasing size of ticks
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    
    # labelling the axes
    plt.xlabel("Year", fontsize = 17)
    plt.ylabel("Growth Percentage", fontsize = 17)
    
    # titling the plot
    plt.title("GDP Growth from 2010 to 2020", fontsize = 25)
    
    plt.legend(fontsize = 17)
 
    #saving as png
    plt.savefig("lineplot.png")
    
    plt.show()
    
    return

# creating dataframe from the data
df_population = pd.read_excel("gdp_growth.xlsx", index_col = 0)


hd = df_population.index.tolist()
lineplot(df_population, hd)
