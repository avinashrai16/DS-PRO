import pandas as pd

#json_file_path = "C:\Users\raiavina1\Desktop\powerbi-json\main_1ea38520-3a8c-4bf4-93d2-ef6e839ebee1.fullscan.json"
dataFrameJson =  pd.read_json(r'https://api.github.com/repos/pandas-dev/pandas/issues')
print(dataFrameJson)