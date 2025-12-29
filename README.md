📊 Análisis de Ventas y Performance (Superstore)
📌 Descripción

Link del dataSet utilizado: 
https://www.kaggle.com/datasets/amirmotefaker/superstore-sales-dataset

Este proyecto analiza el desempeño de ventas, rentabilidad y eficiencia operativa de una empresa de retail utilizando el dataset Superstore.
Se cubre todo el flujo de trabajo: limpieza de datos → análisis exploratorio → visualización en Power BI → generación de insights de negocio.

🧾 Dataset

Fuente: Superstore

Registros: 9.994

Columnas: 21

Variables principales:

Ventas, ganancias, cantidad y descuento

Fechas de pedido y envío

Categoría, segmento y región

Información de clientes y productos

 Limpieza y Preparación de Datos
✔ Normalización

Estandarización de nombres de columnas a minúsculas y snake_case.

✔ Tipos de datos

Conversión de fechas (order_date, ship_date) a tipo datetime.

✔ Valores nulos y duplicados

Revisión de duplicados exactos.

No se encontraron nulos críticos para el análisis de ventas.

✔ Feature Engineering

year

month

month_name

order_processing_days (días entre pedido y envío)

✔ Outliers

Analizados en ventas y ganancias.

No se eliminaron, ya que representan transacciones reales de alto valor.

 Análisis Realizado

Distribución de ventas y ganancias

Ventas por categoría

Tendencias temporales (mensual y anual)

Análisis de correlación entre variables

 Insights Clave

Technology es la categoría con mayor ingreso.

Existen clientes con alto volumen de ventas pero baja o negativa ganancia.

Se observa estacionalidad en las ventas.

Tiempo promedio de entrega cercano a 4 días.

📊 Dashboard (Power BI)

El dashboard incluye:

KPIs de ventas y ganancias

Análisis por categoría y producto

Tendencia temporal

Análisis por región

🔗 Dashboard público:
https://app.powerbi.com/view?r=eyJrIjoiYTY4NjBjNTMtZTIxMS00ZjViLTg2NjUtMjJjZTE2NTI2MDg1IiwidCI6IjhkMzY4MzZlLTZiNzUtNGRlNi1iYWI5LTVmNGIxNzc1NDI3ZiIsImMiOjR9


🛠️ Herramientas

Python (Pandas, Matplotlib, Seaborn)

Power BI

Git / GitHub

📌 Nota

El dataset original no se incluye debido a su tamaño.
El repositorio se enfoca en el proceso de análisis y visualización.

🎯 Conclusión

Este proyecto demuestra un flujo completo de análisis de datos orientado a la toma de decisiones de negocio.

