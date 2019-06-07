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
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
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


def accidents_by_wheather(df):
    """Groups accidents by wheater conditions and counts them."""
    plt.figure(1, figsize=(7, 7))
    accidents = df['Weather_Conditions'].groupby(df['Weather_Conditions']).count()
    accidents.plot(kind="bar", title="Accidents caused by Wheather")
    plt.xlabel('Causes')
    plt.ylabel('Accidents')
    plt.show()


def accidents_by_day_and_hour(df, day=2):
    """Graphs accidents grouped by hour on day received."""
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    accidents = df[df['Day_of_Week'] == day].groupby(
        pd.Grouper(freq='1H', key='Time'))['Accident_Index']
    accidents.count().plot(kind='bar', title=f'Accidents on {days[day-1]}')
    plt.xlabel('Hour')
    plt.ylabel('Accidents')
    hours = []
    for key in accidents.groups:
        hours.append(key.strftime('%H:%M'))
    plt.xticks(np.arange(24), tuple(hours))
    plt.show()
