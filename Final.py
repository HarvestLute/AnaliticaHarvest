#%%
import pandas as pd   #Importar pandas API
import seaborn as sns #Importar seaborn
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder 
import matplotlib.pyplot as plt
from kneed import KneeLocator

sns.set_theme(style="white")
#%%
df = pd.read_csv("Ulabox/Ulabox.csv")   # Cargar dataset
#%%
# Obtenemos el numero de filas y columnas
count_row = df.shape[0]  # Numero de filas
count_col = df.shape[1]  # Numero de columnas

(count_col, count_row)  #Imprimir valores
# %%
# Analisis de las variables 
customer_number = df['customer'].max() +1       #Numero de clientes, se le suma 1 porque se cuenta el cliente 0
orders_per_customer = df['customer'].mean
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
#%%
sns.displot(x='total_items', data = df) #Tabla de numero objetos por orden
#%%
df_ord_per_day = df.groupby('weekday')['weekday'].count()
df_ord_per_day.head
sns.barplot(x = df_ord_per_day.index, y = df_ord_per_day.values) 
#%%
df_ord_per_hour = df.groupby('hour')['hour'].count()
df_ord_per_hour.head
sns.barplot(x=df_ord_per_hour.index, y=df_ord_per_hour.values)
#(customer_number, most_orders_customer,items_per_order, discounts, most_sales_day, most_sales_hour, food, fresh, drinks, home, beauty, health, baby, pets)
#%%
df_orders = df.groupby('weekday').agg({'hour': ['mean'], 'total_items': ['mean'], 'discount%': ['mean']})
df_orders.head(7)
#%%
sns.scatterplot(data=df, x='total_items', y='discount%')
#%%
df_clus = df[["total_items", "discount%"]]
df_clus.head()
#%%
ssd=[]
ks = range (1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(df_clus)
    ssd.append(km.inertia_)
kneedle = KneeLocator(ks, ssd, S=1.0,curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()
k = round(kneedle.knee)
print(f"numero de clusters sugerido por knee:{k}")
# %%
kmeans = KMeans(n_clusters=k).fit(df[["total_items", "discount%"]])
sns.scatterplot(data=df, x="total_items", y="discount%", hue=kmeans.labels_)
plt.show()
#%%
from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier()
tree.fit(df[["weekday", "total_items", "discount%"]], kmeans.labels_)
print(export_text(tree, feature_names=["weekday", "total_items", "discount%"]))

# %%
