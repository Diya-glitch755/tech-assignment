import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")

plt.plot(df['month_number'], df['total_profit'])
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit of All Months")
plt.show()

plt.plot(df['month_number'], df['facecream'], label='Face Cream')
plt.plot(df['month_number'], df['facewash'], label='Face Wash')
plt.plot(df['month_number'], df['toothpaste'], label='Toothpaste')
plt.plot(df['month_number'], df['bathingsoap'], label='Bathing Soap')
plt.plot(df['month_number'], df['shampoo'], label='Shampoo')
plt.legend()
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Product Sales Data")
plt.show()

plt.bar(df['month_number'], df['facecream'], label='Face Cream')
plt.bar(df['month_number'], df['facewash'], label='Face Wash')
plt.legend()
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Face Cream vs Face Wash Sales")
plt.show()

sales_data = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(),
              df['bathingsoap'].sum(), df['shampoo'].sum()]
labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo']

plt.pie(sales_data, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Data")
plt.show()