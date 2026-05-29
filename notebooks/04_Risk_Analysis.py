# Databricks notebook source
df_risk = spark.sql("SELECT * FROM silver_kidney_stone")
df_risk.show()

# COMMAND ----------

from pyspark.sql.functions import when, col

df_risk = df_risk.withColumn(
    "risk_category",
    when(col("calcium_level") > 5, "High Risk")
    .when(col("calcium_level") > 3, "Medium Risk")
    .otherwise("Low Risk")
)

df_risk.show()

# COMMAND ----------

df_risk.groupBy("risk_category").count().show()

# COMMAND ----------

df_risk.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_risk_analysis")

# COMMAND ----------

corr_calcium = df_risk.stat.corr("calcium_level", "stone_present")

# pH aur Stone ka relation  
corr_ph = df_risk.stat.corr("urine_ph", "stone_present")

print(f"Calcium & Stone Correlation: {round(corr_calcium, 2)}")
print(f"pH & Stone Correlation: {round(corr_ph, 2)}")