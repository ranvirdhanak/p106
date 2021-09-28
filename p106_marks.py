import csv
import numpy as np
import plotly.express as px

def setup():
    data_path = 'Students_marks.csv'
    datasource = getDatasource(data_path)
    cor = np.corrcoef(datasource['x'],datasource['y'])
    print(cor)

def getDatasource(data_path):
    rollNo = []
    percentage = []
    with open (data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            rollNo.append(float(row["Roll No"]))
            percentage.append(float(row["\tRoll No of the students"]))
    return {'x':rollNo,'y':percentage}
setup()

with open ("Students_marks.csv") as f:
        csv_reader = csv.DictReader(f)
        fig = px.scatter(csv_reader,x = "Roll No",y = "\tRoll No of the students")
        fig.show()