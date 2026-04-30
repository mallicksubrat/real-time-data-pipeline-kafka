from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("RealTimeAnalyticsPipeline") \
    .getOrCreate()

# Kafka read
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
).select("data.*")

# Query 1: STORE RAW STRUCTURED DATA (parquet)
query1 = df_struct.writeStream \
    .format("parquet") \
    .option("path", "/tmp/output") \
    .option("checkpointLocation", "/tmp/checkpoint1") \
    .start()

# Query 2: REAL-TIME ANALYTICS (console)
df_agg = df_struct.groupBy("event_type").count()

query2 = df_agg.writeStream \
    .format("console") \
    .outputMode("complete") \
    .start()

# Keep both running
query1.awaitTermination()
query2.awaitTermination()
