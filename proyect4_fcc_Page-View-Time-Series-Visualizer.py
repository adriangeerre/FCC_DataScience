import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
df = df[(df['value'] > (df['value'].quantile(0.025))) &
        (df['value'] < (df['value'].quantile(1-0.025)))]


def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(16,9))
    plt.plot('date','value', data=df, color="red")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month_name()

    # Draw bar plot
    fig,ax = plt.subplots(figsize=(12,9))
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    sns.barplot(data=df_bar, y="value", x="year", hue="month", ci=None, palette="pastel", hue_order=months)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc=2, title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    print(1)
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['month'] = pd.DatetimeIndex(df_box['date']).month_name()
    df_box["month"] = df_box["month"].str[0:3]

    print(2)
    # Draw box plots (using Seaborn)
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,9))
    sns.boxplot(data=df_box, y="value", x="year", palette="pastel", ax=ax1)
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Page Views')
    ax1.set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(data=df_box, y="value", x="month", palette="pastel", ax=ax2, order=months)
    ax2.set_xlabel('Months')
    ax2.set_ylabel('Page Views')
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    print(3)
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig