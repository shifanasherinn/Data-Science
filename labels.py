import pandas as pd
data={
         'name': ['shifaa', 'sheri', 'haris', 'mk'],
         'age': [20, 20, 25, 20],
         'marks':[85,90,78,88]
}
df=pd.DataFrame(data)
print("original DataFrame")
print(df)
print("\nStudents with marks greater than 80:")
print(df[df['marks']>80])
print("\nSelected data using loc:")
print(df.loc[0:2,['name','marks']])