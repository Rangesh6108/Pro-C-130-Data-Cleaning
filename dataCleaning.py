import csv
import pandas as pd

dataframe=pd.read_csv("total_stars.csv")
print("The initial rows and columns of the csv: ",dataframe.shape)
del dataframe["Unnamed: 0"]
del dataframe["Luminosity"]
del dataframe["Unnamed: 6"]
del dataframe["star_name"]
del dataframe["distance"]
del dataframe["mass"]
del dataframe["radius"]
print('')
print(list(dataframe))
print('')
print("The final rows and columns of the csv: ",dataframe.shape)

dataframe=dataframe.to_csv('cleaned.csv')

