import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df["value"] <= df["value"].quantile(0.975)) & (df["value"] >= df["value"].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(23,15))
    ax.plot(df.index, df["value"], linewidth=2, color="red")
    xticks = pd.to_datetime(["2016-07", "2017-01", "2017-07", "2018-01", 
                         "2018-07", "2019-01", "2019-07", "2020-01"])
    ax.set_xticks(xticks)
    ax.set_xticklabels([date.strftime("%Y-%m") for date in xticks])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set(xlabel="Date", ylabel="Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year.rename("Year"),df.index.strftime("%B").rename("Month")])["value"].mean().reset_index()

    # Draw bar plot
    months_order = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
    df_bar["Month"] = pd.Categorical(df_bar["Month"], categories=months_order, ordered=True)
    df_bar = df_bar.dropna()
    fig, ax = plt.subplots(figsize=(11,9))
    sns.barplot(df_bar, x="Year", y="value", hue="Month", ax=ax, palette="tab10", width=0.4)
    ax.set(xlabel="Years", ylabel="Average Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box["month"] = pd.Categorical(df_box["month"], categories=months_order, ordered=True)
    fig, (ax1,ax2) = plt.subplots(1,2,figsize= (18,13))
    sns.boxplot(df_box, x="year", y="value",ax= ax1)
    sns.boxplot(df_box, x="month", y="value",ax= ax2)
    ax1.set(xlabel="Year", ylabel="Page Views")
    ax2.set(xlabel="Month", ylabel="Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
