PROJECT : Kidney Stone Risk Analysis
LAYER : Bronze Layer - Raw Data Ingestion
AUTHOR : Varnika
DATE : 28 May 2026
TOOL : PySpark + Databricks

# Databricks notebook source
dbutils.fs.ls("/Volumes/workspace/default/kidney_stone_volume/kidney-stone-dataset.csv")

# COMMAND ----------

df_bronze = spark.read\
    .format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("/Volumes/workspace/default/kidney_stone_volume/kidney-stone-dataset.csv")

# COMMAND ----------

df_bronze.show()


# COMMAND ----------

df_bronze.printSchema()

# COMMAND ----------

print(df_bronze.count())

# COMMAND ----------

df_bronze.write\
    .format("delta")\
    .mode("overwrite")\
    .saveAsTable("bronze_kidney_stone")

# COMMAND ----------

spark.sql("select * from bronze_kidney_stone").show()
