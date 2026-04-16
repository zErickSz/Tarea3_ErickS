from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count, when, col, desc

# Crear sesión de Spark
spark = SparkSession.builder.appName("AnalisisBatchTarea3").getOrCreate()

# Cargar el archivo CSV
df = spark.read.csv("datos.csv", header=True, inferSchema=True)

print("\n========== 1. ESQUEMA DEL DATASET ==========")
df.printSchema()



print("\n========== 2. DATOS CARGADOS ==========")
df.show(truncate=False)



print("\n========== 3. TOTAL DE REGISTROS ==========")
print(f"Total de registros: {df.count()}")



print("\n========== 4. VALORES NULOS POR COLUMNA ==========")
df.select([
    count(when(col(c).isNull(), c)).alias(c) for c in df.columns
]).show()



print("\n========== 5. ESTADÍSTICAS GENERALES ==========")
df.describe().show()



print("\n========== 6. PROMEDIO DE TEMPERATURA Y HUMEDAD POR CIUDAD ==========")
df.groupBy("ciudad").agg(
    avg("temperatura").alias("promedio_temperatura"),
    avg("humedad").alias("promedio_humedad")
).show()



print("\n========== 7. TEMPERATURA MÁXIMA Y MÍNIMA POR CIUDAD ==========")
df.groupBy("ciudad").agg(
    max("temperatura").alias("temp_max"),
    min("temperatura").alias("temp_min")
).show()



print("\n========== 8. REGISTROS CON TEMPERATURA MAYOR A 30 ==========")
df.filter(col("temperatura") > 30).show()



print("\n========== 9. REGISTROS CON HUMEDAD MAYOR A 70 ==========")
df.filter(col("humedad") > 70).show()



print("\n========== 10. CIUDADES ORDENADAS POR TEMPERATURA PROMEDIO ==========")
df.groupBy("ciudad").agg(
    avg("temperatura").alias("promedio_temperatura")
).orderBy(desc("promedio_temperatura")).show()



print("\n========== 11. CANTIDAD DE REGISTROS POR CIUDAD ==========")
df.groupBy("ciudad").count().show()

print("\n========== FIN DEL ANÁLISIS BATCH ==========")

spark.stop()