import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("Superstore.xls")

# NORMALIZAR NOMBRES DE COLUMNAS
df.columns = (
    df.columns
      .str.lower()
      .str.replace(" ", "_")
)

# VISUALIZACION DEL TIPO DE DATO, CANTIDAD DE COLUMNAS Y FILAS
df.info()

# Exploracion y transformacion de tipo de datos
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

duplicados = df.duplicated().sum()
print("Filas duplicadas exactas:", duplicados)

nulos = df.isnull().sum()
print("Filas con nulos:", nulos)


df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()

df["order_processing_days"] = (df["ship_date"] - df["order_date"]).dt.days


# Manejo de graficas para entender datos

# Outliers
plt.figure(figsize=(10,5))
sns.boxplot(data=df[["sales", "profit"]])
plt.title("Outliers en Sales y Profit")
plt.show()

# Grafica de barras de ventas por categoria
sales_by_category = df.groupby("category")["sales"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=sales_by_category, x="category", y="sales")
plt.title("Ventas por Categoría")
plt.show()

# Grafico de lineas de ventas mensuales
monthly_sales = df.groupby(["year", "month"])["sales"].sum().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x="month", y="sales", hue="year")
plt.title("Ventas Mensuales")
plt.show()

# Correlación
plt.figure(figsize=(5,4))
sns.heatmap(df[["sales", "quantity", "discount", "profit"]].corr(), annot=True)
plt.title("Correlación de variables")
plt.show()


# Exportamos nuestro dataset limpio
df.to_csv("sales_clean.csv", index=False)

