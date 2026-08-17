import pandas as pd
data={
         'name': ['shifaa', 'sheri', 'haris', 'mk'],
         'age': [20, 20, 25, 20],
         'marks':[85,90,78,88]
}
df=pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nSummary statistics:")
print(df.describe())
print("\nBasic Information:")
print(df.info())