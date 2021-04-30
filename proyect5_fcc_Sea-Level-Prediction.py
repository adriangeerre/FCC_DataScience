import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')

    # Create scatter plot
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df, color="black")

    # Create first line of best fit
    years=list(range(1880,2050))
    lm = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    pred1=[]
    for year in years:
        pred1.append(lm.intercept + lm.slope*year)
    plt.plot(years, pred1, 'blue', label="1st fit")

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    df2 = df2[["Year","CSIRO Adjusted Sea Level"]]

    years=list(range(2000,2050))
    lm2 = linregress(df2) # 2nd Linear model
    
    pred2=[]
    for year in years:
        pred2.append(lm2.intercept + lm2.slope*year)
 
    # Include line 2nd fit
    plt.plot(years, pred2, 'red', label="2nd fit")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()