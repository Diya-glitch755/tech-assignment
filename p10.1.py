import pandas as pd


df = pd.read_csv("books.csv")


print("\n--- Complete Book Report ---")
print(df)


author = input("\nEnter author name: ")
print("\nBooks by author:")
print(df[df['author'] == author])


publisher = input("\nEnter publisher name: ")
print("\nBooks by publisher:")
print(df[df['publisher'] == publisher])


print("\nCheapest Book:")
print(df.loc[df['price'].idxmin()])

print("\nCostliest Book:")
print(df.loc[df['price'].idxmax()])


print("\nBooks sorted by Year:")
print(df.sort_values(by='year'))