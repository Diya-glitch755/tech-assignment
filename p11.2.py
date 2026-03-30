import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'Amdocs']
recruitments = [120, 150, 180, 90, 110, 130, 100]

plt.bar(companies, recruitments)
plt.title("Recruitments Bar Chart")
plt.show()

plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitments Pie Chart")
plt.show()

plt.pie(recruitments, labels=companies, autopct='%1.1f%%', startangle=90)
plt.title("Customized Pie Chart")
plt.show()

plt.pie(recruitments, labels=companies, autopct='%1.1f%%', wedgeprops=dict(width=0.4))
plt.title("Doughnut Chart")
plt.show()

labels = ['IBM', 'Amdocs']
values = [90, 100]

plt.bar(labels, values)
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.show()