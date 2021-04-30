import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = np.where(df['weight'] / ((df['height']/100)**2) < 25, 0, 1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = np.where(df['gluc']>1, 0, 1)
df['cholesterol'] = np.where(df['cholesterol']>1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df[['cholesterol','gluc','smoke','alco','active','overweight']])

    # Group and reformat the data to split it by 'cardio'. 
    # Show the counts of each feature. 
    # You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.melt(df, value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"], id_vars="cardio")
    
    # Draw the catplot with 'sns.catplot()'
    # fig = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")
    fig = sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")
    fig.set(xlabel='variable', ylabel='total')
    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
      (df['ap_lo'] <= df['ap_hi']) & 
      (df['height'] >= (df['height'].quantile(0.025))) &
      (df['height'] <= (df['height'].quantile(0.975))) &
      (df['weight'] >= (df['weight'].quantile(0.025))) &
      (df['weight'] <= (df['weight'].quantile(0.975)))
    ]
    
    # Calculate the correlation matrix
    corr = round(df_heat.corr(), 1)

    # Generate a mask for the upper triangle
    mask = np.triu(corr) 

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, linewidths = 1, square= True, mask = mask)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig