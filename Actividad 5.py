import matplotlib.pyplot as plt

years=[2019,2020,2021,2022]
sales_a=[14,18,23,32]
sales_b=[11,12,26,32]

plt.plot(years,sales_a,color='blue',linewidth=3,label='EMPRESA A')
plt.plot(years,sales_b,color='red',linewidth=3,label='EMPRESA B')
         
plt.title("DIAGRAMA DE LINEA")
plt.ylabel('Sales')
plt.xlabel('Years')
plt.xticks(years)

plt.legend()
plt.grid()
plt.show()
