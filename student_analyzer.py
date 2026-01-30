import pandas as pd
data=pd.read_csv('students.csv')
data["Total"]=data["Math"]+data["English"]+data["Science"]
data["Average"]=data["Total"]/3
data["Result"]=data["Average"].apply(lambda x:"Pass" if x>= 50 else "Fail")
topper = data.loc[data["Average"].idxmax()]

print(topper["Name"], "-", topper["Average"])

print("\n Final Report")
print(data)
data.to_csv("result.csv", index=False)