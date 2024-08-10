import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(13,9))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue")

    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(years_extended, years_extended*slope1 + intercept1, "-r")

    # Create second line of best fit
    recent_df = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(2000,2051))
    ax.plot(years, years*slope2 +intercept2, "-y")

    # Add labels and title
    ax.set(xlabel="Year", ylabel="Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()