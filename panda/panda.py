import pandas as pd
import matplotlib.pyplot as plt

data={
    "Count":[45376783,45808747,46234838,46654581,47067641,47473760,47873268,48266524,48653385,49033678,49407265],
    "Year":[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]
}

df=pd.DataFrame(data)

print(df)

df.to_csv("file.csv",encoding="utf-8",index=False)

x=df.Year
y=df.Count

plt.scatter(x,y,color="hotpink")

plt.show()