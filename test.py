import pandas as pd

def objChanger(df):
  df["A"][0] = "HELLO"


df = pd.DataFrame({"A":[1,2,3]})
objChanger(df)
print(df)