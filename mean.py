import csv
import pandas as pd
import plotly.figure_factory as px


df = pd.read_csv('yes.csv')


graph = px.create_distplot([df['height'].tolist()], ['height'])

graph.show()