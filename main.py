import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

# a dataframe is a 2d labeled data structure that has multiple columns
df = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 107\data.csv')
fig = px.scatter(df,x='student_id',y='level', color='attempt', size='attempt')
fig.show()
