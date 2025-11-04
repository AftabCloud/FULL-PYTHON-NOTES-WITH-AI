from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, when

# ===================================
# 1️⃣ Initialize Spark session
# ===================================
spark = SparkSession.builder \
    .appName("SalesDataCleaningAndTransformation") \
    .getOrCreate()

# ===================================
# 2️⃣ Load data from S3
# ===================================
input_path = "s3://aftab-emr-practice-bucket/sales_data_dirty.csv"
output_path = "s3://aftab-emr-practice-bucket/output/clean_data"

df = spark.read.option("header", True).csv(input_path)

print("=== 🧾 Original Data ===")
df.show(truncate=False)

# ===================================
# 3️⃣ Data Cleaning & Transformation
# ===================================

# 🔹 Trim spaces and standardize text cases
df = df.withColumn("region", trim(upper(col("region")))) \
       .withColumn("product", trim(upper(col("product")))) \
       .withColumn("sales", trim(col("sales")))

# 🔹 Handle null or empty sales values
df = df.withColumn(
    "sales",
    when((col("sales").isNull()) | (col("sales") == ""), None).otherwise(col("sales"))
)

# 🔹 Convert sales column to integer safely
df = df.withColumn("sales", col("sales").cast("int"))

# 🔹 Drop rows where essential fields are missing
df_cleaned = df.dropna(subset=["region", "sales", "product"])

# 🔹 Remove duplicate records
df_cleaned = df_cleaned.dropDuplicates()

# ===================================
# 4️⃣ Optional Extra Transformations
# ===================================

# Remove negative sales (if any)
df_cleaned = df_cleaned.filter(col("sales") >= 0)

# Replace any unknown or missing region/product names
df_cleaned = df_cleaned.withColumn("region", when(col("region") == "", "UNKNOWN").otherwise(col("region")))
df_cleaned = df_cleaned.withColumn("product", when(col("product") == "", "UNKNOWN").otherwise(col("product")))

# ===================================
# 5️⃣ Save Final Cleaned Data (Single File)
# ===================================

# Coalesce(1) ensures only one CSV file (clean_data.csv)
df_cleaned.coalesce(1) \
    .write.mode("overwrite") \
    .option("header", True) \
    .csv(output_path)

print("✅ Data cleaned and transformation completed successfully!")
print(f"📁 Cleaned file saved to: {output_path}")

# ===================================
# 6️⃣ Stop Spark session
# ===================================
spark.stop()
