PROJECT : Kidney Stone Risk Analysis
LAYER : Gold Layer - Analytics & Insights
AUTHOR : Varnika
DATE : 28 May 2026
TOOL : PySpark + Databricks

# Databricks notebook source
df_gold = spark.sql("select * from silver_kidney_stone")

# COMMAND ----------

df_gold.groupBy("stone_present") \
    .count() \
    .orderBy("stone_present") \
    .show()

# COMMAND ----------

from pyspark.sql.functions import avg, round

df_gold.groupBy("stone_present") \
    .agg(round(avg("calcium_level"), 2).alias("avg_calcium")) \
    .show()

# COMMAND ----------

from pyspark.sql.functions import avg, round

df_gold.groupBy("stone_present") \
    .agg(
        round(avg("urine_ph"), 2).alias("avg_ph"),
        round(avg("osmolarity"), 2).alias("avg_osmolarity"),
        round(avg("urea_level"), 2).alias("avg_urea")
    ) \
    .show()

# COMMAND ----------

df_gold.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_kidney_stone")
