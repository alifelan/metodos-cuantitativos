import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sb
from data import *


def stats_location_easting(data):
    """ Analisys of the variable Location Easting OSGR """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Location Easting OSGR")
    plt.show()


def stats_location_northing(data):
    """ Analisys of the variable Location Northing OSGR """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Location Northing OSGR")
    plt.show()


def date(data):
    """ Analisys of the variable Date """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Date")
    plt.show()
    f = data.groupby(data['Location_Easting_OSGR']).size()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def day_week(data):
    """ Analisys of the variable Day Week """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Day Week")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def time(data):
    """ Analisys of the variable Time """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Time")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)


def speed_limit(data):
    """ Analisys of the variable Speed Limit"""
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Speed Limit")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def light_conditions(data):
    """ Analisys of the variable Light Conditions """
    plt.hist(data, bins='auto')
    plt.title("Histogram of Light Conditions")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def first_road_class(data):
    """ Analisys of the variable First Road Class """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of First Road Class")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def second_road_class(data):
    """ Analisys of the variable Second Road Class """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Second Road Class")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def first_road_number(data):
    """ Analisys of the variable First Road Number """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of First Road Number ")
    plt.show()
    f = data.groupby(data).size()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def second_road_number(data):
    """ Analisys of the variable Second Road Number """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Second Road Number")
    plt.show()
    f = data.groupby(data).size()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def weather(data):
    """ Analisys of the variable Weather """
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def area(data):
    """ Analisys of the variable Area """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Area")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def year(data):
    """ Analisys of the variable Year """
    media = np.mean(data)
    varianza = np.var(data)
    desviacion = np.std(data)
    simetria = data.skew()
    curtosis = data.kurtosis()
    print(media)
    print(varianza)
    print(simetria)
    print(curtosis)
    plt.hist(data, bins='auto')
    plt.title("Histogram of Year")
    plt.show()
    f = data.groupby(data).size()
    plt.pie(f, labels = f.index, autopct='%1.1f%%')
    plt.show()
    aux = pd.DataFrame(f)
    aux['H'] = f/len(data)
    print(aux)


def main():
    data = read()
    stats_location_easting(data['Location_Easting_OSGR'])
    stats_location_northing(data['Location_Northing_OSGR'])
    # data(data[])
    day_week(data['Day_of_Week'])
    # time(data[])
    speed_limit(data['Speed_limit'])
    # ilight_conditions(data[])
    first_road_class(data['1st_Road_Class'])
    second_road_class(data['2nd_Road_Class'])
    first_road_number(data['1st_Road_Number'])
    second_road_number(data['2nd_Road_Number'])
    # weather(data[])
    area(data['Urban_or_Rural_Area'])
    year(data['Year'])


if __name__ == '__main__':
    main()
