import csv
import numpy as s
import pandas as pd
import plotly.express as px

df = pd.read_csv("Correlation.csv")
fig = px.scatter(df, x="Days Present", y="Marks In Percentage",size_max=60)
fig.show()
        

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : days_present, "y": marks_in_percentage}

def findCorrelation(datasource):
    correlation = s.corrcoef(datasource["x"], datasource["y"])
    print("Correlation Between Marks In Percentage And Days Present Is :-   \n--->",correlation[0,1])

def setup():
    data_path  = "./Correlation.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()