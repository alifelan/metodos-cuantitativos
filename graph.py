import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def corr_heatmap(df):
    """ This creates a heatmap based in the correlation of each variable with the rest"""
    corr = df.corr()
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)
    plt.show()


def accidents_per_day(df):
    """Groups accidents by week day and counts them."""
    accidents = df.groupby(['Day_of_Week'])['Accident_Index'].count()
    accidents.plot(kind='bar', title='Accidents by day')
    plt.xlabel('Day')
    plt.ylabel('Accidents')
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    plt.xticks(np.arange(7), days)
    plt.show()


def casualties_ratio(df):
    """Graphs the ratio between casualties and ammount of crashes grouped by
    pedestrian facilities."""
    grouped_casualties = df.groupby(
        ['Pedestrian_Crossing-Physical_Facilities'])['Number_of_Casualties']
    casualties = grouped_casualties.sum()
    crashes = grouped_casualties.count()
    ratio = casualties / crashes
    ratio.plot(kind='bar')
    plt.show()
