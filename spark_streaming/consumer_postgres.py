from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, to_timestamp
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("PostgresSink") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

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

# Parse
df_json = df.selectExpr("CAST(value AS STRING)")

df_struct = df_json.select(
    from_json(col("value"), schema).alias("data")
).select("data.*") \
.withColumn("timestamp", to_timestamp(col("timestamp")))

# Window aggregation
df_windowed = df_struct \
    .withWatermark("timestamp", "1 minute") \
    .groupBy(
        window(col("timestamp"), "10 seconds"),
        col("event_type")
    ).count()

df_final = df_windowed.select(
    col("window.start").alias("window_start"),
    col("window.end").alias("window_end"),
    col("event_type"),
    col("count")
)
# Write to Postgres
def write_to_postgres(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/analytics") \
        .option("dbtable", "event_counts") \
        .option("user", "analytics") \
        .option("password", "analytics") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

query = df_final.writeStream \
    .outputMode("update") \
    .foreachBatch(write_to_postgres) \
    .start()

query.awaitTermination()
