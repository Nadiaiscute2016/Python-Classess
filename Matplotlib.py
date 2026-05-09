import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 200, 170]
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()