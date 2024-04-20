import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

pd.set_option("display.max_colwidth",50)
pd.set_option("display.max_columns",50)

df = pd.read_csv("Travel.csv")
print(df.columns)

print(df.head())
