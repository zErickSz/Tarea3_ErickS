# 📊 Tarea 3 - Procesamiento de Datos con Apache Spark (Batch)

## 👤 Autor

* Nombre: [Tu Nombre]
* Curso: Big Data
* Universidad: UNAD

---

## 🎯 Descripción del proyecto

Este proyecto tiene como objetivo implementar un proceso de análisis de datos utilizando **Apache Spark en modo batch**, aplicando técnicas de procesamiento sobre un conjunto de datos en formato CSV.

El análisis permite obtener información relevante a partir de los datos mediante operaciones de transformación, filtrado y agregación.

---

## 🧱 Tecnologías utilizadas

* Apache Spark
* Python
* Ubuntu (Máquina Virtual)

---

## 📂 Estructura del proyecto

* `datos.csv` → Dataset utilizado para el análisis
* `batch_tarea3.py` → Script de procesamiento de datos en batch

---

## ⚙️ Procesamiento en Batch

En esta fase se realiza:

* Carga del dataset desde un archivo CSV
* Exploración de la estructura de los datos
* Identificación de valores nulos
* Generación de estadísticas descriptivas
* Agrupación de datos por ciudad
* Cálculo de promedios de temperatura y humedad
* Identificación de valores máximos y mínimos
* Filtrado de registros según condiciones específicas

---

## ▶️ Ejecución del proyecto

Para ejecutar el análisis en batch, se utiliza el siguiente comando:

```bash
spark-submit batch_tarea3.py
```

---

## 📊 Resultados obtenidos

A partir del análisis realizado se obtuvieron los siguientes resultados:

* Promedio de temperatura por ciudad
* Promedio de humedad por ciudad
* Conteo de registros por ciudad
* Identificación de temperaturas altas
* Análisis general del comportamiento de los datos

---

## 🧠 Conclusiones

* Apache Spark permite procesar datos de manera eficiente en modo batch
* El uso de DataFrames facilita el análisis y manipulación de datos
* Las operaciones de agregación permiten obtener información útil rápidamente
* El análisis de datos permite identificar patrones y comportamientos relevantes

---

## 📚 Referencias

* Documentación oficial de Apache Spark
* Guía de aprendizaje UNAD
* Material de apoyo del curso Big Data

---
