PROJECT : Kidney Stone Risk Analysis
LAYER : Silver Layer - Data Cleaning 
AUTHOR : Varnika
DATE : 28 May 2026
TOOL : PySpark + Databricks

# Databricks notebook source
df_silver = spark.sql("select * from bronze_kidney_stone")

# COMMAND ----------

df_silver = df_silver.drop("_c0")
df_silver.show()

# COMMAND ----------

from pyspark.sql.functions import col, sum
df_silver.select([sum(col(c).isNull().cast("int")).alias(c) for c in df_silver.columns]).show()


# COMMAND ----------

df_silver = df_silver.withColumnRenamed("gravity", "urine_gravity")
df_silver = df_silver.withColumnRenamed("ph", "urine_ph")
df_silver = df_silver.withColumnRenamed("osmo", "osmolarity")
df_silver = df_silver.withColumnRenamed("cond", "conductivity")
df_silver = df_silver.withColumnRenamed("urea", "urea_level")
df_silver = df_silver.withColumnRenamed("calc", "calcium_level")
df_silver = df_silver.withColumnRenamed("target", "stone_present")

df_silver.show()

# COMMAND ----------

df_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_kidney_stone")
