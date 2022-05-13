#%%
import pandas as pd   #Importar pandas API
import seaborn as sns #Importar seaborn

sns.set_theme(style="white")
#%%
df = pd.read_csv("Ulabox/Ulabox.csv")   # Cargar dataset
#%%
# Obtenemos el numero de filas y columnas
count_row = df.shape[0]  # Numero de filas
count_col = df.shape[1]  # Numero de columnas

(count_col, count_row)  #Imprimir valores
# %%
# Analisis de las variables (Nombres largos porque no son finales :v)
customer_number = df['customer'].max() +1       #Numero de clientes, se le suma 1 porque se cuenta el cliente 0
most_orders_customer = df['customer'].mode()    #Cliente con mas ordenes
items_per_order = df['total_items'].mean()      #Promedio de cantidad de objetos por orden
discounts = df['discount%'].mean()              #Promedio de descuento por ordern
most_sales_day = df['weekday'].mode()           #Dia con mas ventas
most_sales_hour = df['hour'].mode()             #Hora con mas ventas

                                                #Porciento de ventas de cada tipo de producto
food = df['Food%'].mean()                       
fresh = df['Fresh%'].mean()
drinks = df['Drinks%'].mean()
home = df['Home%'].mean()
beauty = df['Beauty%'].mean()
health = df['Health%'].mean()
baby = df['Baby%'].mean()
pets = df['Pets%'].mean()

(customer_number, most_orders_customer,items_per_order, discounts, most_sales_day, most_sales_hour, food, fresh, drinks, home, beauty, health, baby, pets)

# %%
sns.displot(x='total_items', data = df) #Tabla de numero objetos por orden
# %%
