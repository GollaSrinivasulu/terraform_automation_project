from pyspark.sql import SparkSession
from pyspark.sql.functions import min
import os, shutil
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("DeptSalaryPipeline") \
    .master("local[*]") \
    .getOrCreate()

# -------------------
# Read CSV Files
# -------------------

df1 = spark.read.csv("data1.csv", header=True, inferSchema=True)
df2 = spark.read.csv("data2.csv", header=True, inferSchema=True)

# -------------------
# Transformations
# -------------------

joindf = df1.join(df2, df1["dept_id"] == df2["dept_id1"], "left")

seldf = joindf.select("emp_id","name","dept_name","salary").orderBy("salary")

expdf = (
    seldf
    .groupBy("dept_name")
    .agg(min("salary").alias("salary"))
)

finaldf = expdf.join(df1, ["salary"], "inner").drop("dept_id")

resultdf = finaldf.select("emp_id","name","dept_name","salary").orderBy(col("emp_id").asc())

# Show result in logs
resultdf.show()

# -------------------
# Write Output
# -------------------

resultdf.coalesce(1).write.mode("overwrite").option("header", True).csv("temp_output")

for file in os.listdir("temp_output"):
    if file.endswith(".csv"):
        shutil.move(f"temp_output/{file}", "cleaned_data.csv")

shutil.rmtree("temp_output")

print("Pipeline completed. Output saved as cleaned_data.csv")

spark.stop()
