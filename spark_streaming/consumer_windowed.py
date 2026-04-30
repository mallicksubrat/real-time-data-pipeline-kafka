from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, to_timestamp
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("WindowedAnalytics") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test-topic") \
    .load()

# Schema
schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("event_type", StringType()) \
    .add("page", StringType()) \
    .add("timestamp", StringType())

# Parse JSON
df_json = df.selectExpr("CAST(value AS STRING)")

df_struct = df_json.select(
    from_json(col("value"), schema).alias("data")
).select("data.*") \
.withColumn("timestamp", to_timestamp(col("timestamp")))

# Windowed aggregation
df_windowed = df_struct \
    .withWatermark("timestamp", "1 minute") \
    .groupBy(
        window(col("timestamp"), "10 seconds"),
        col("event_type")
    ).count()

# Output
query = df_windowed.writeStream \
    .format("console") \
    .outputMode("update") \
    .start()

query.awaitTermination()
