import csv
import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("data.csv")
histogram = ff.create_distplot([data["Avg Rating"].tolist()],["Mobile Brand"])
histogram.show()