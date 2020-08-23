import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(data_frame=df, x="date", y="cases", color="country", title="COVID-19 Cases")

fig.show()