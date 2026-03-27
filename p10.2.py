import pandas as pd


data = {
    "State": ["Maharashtra", "Gujarat", "Karnataka", "Rajasthan", "Punjab"],
    "Area": [307713, 196024, 191791, 342239, 50362],   # in sq km
    "Population": [112374333, 60439692, 61095297, 68548437, 27743338]
}

df = pd.DataFrame(data)


print("\n--- State Information ---")
print(df)


print("\nState with Largest Area:")
print(df.loc[df['Area'].idxmax(), 'State'])


print("\nState with Largest Population:")
print(df.loc[df['Population'].idxmax(), 'State'])


df['Density'] = df['Population'] / df['Area']
print("\nPopulation Density:")
print(df[['State', 'Density']])


print("\nState with Highest Population Density:")
print(df.loc[df['Density'].idxmax(), 'State'])