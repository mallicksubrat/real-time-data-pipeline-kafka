# ⚡ Real-Time Data Pipeline (Kafka + Spark)

A real-time data pipeline that ingests streaming events, processes them using **Spark Structured Streaming**, performs real-time aggregations, and stores analytics-ready data.

---

## 🏗 Architecture

```
Producer → Kafka → Spark Streaming → Aggregation → Storage (Parquet)
```

---

## 🛠 Tech Stack

- Python  
- Apache Kafka  
- PySpark (Structured Streaming)  
- Docker  
- Parquet  

---

## 🎯 Project Goal

Simulate a **production-grade real-time data pipeline** using local infrastructure, focusing on streaming ingestion, transformation, and analytics.

---

## 🚀 Current Status

- ✅ Kafka cluster running via Docker  
- ✅ Producer generating real-time events  
- ✅ Spark Structured Streaming consumer implemented  
- ✅ JSON parsing with schema enforcement  
- ✅ Real-time aggregation (event counts)  
- ✅ Data stored in Parquet (analytics-ready)  

---

## ▶️ How to Run the Pipeline

### 1. Start Infrastructure

```bash
docker-compose up -d
```

---

### 2. Start Kafka Producer

```bash
python producer/producer.py
```

---

### 3. Start Spark Streaming Consumer

```bash
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \
  spark_streaming/consumer.py
```

---

### 4. Verify Output

- Real-time aggregation will appear in the terminal  
- Processed data is stored in:

```bash
/tmp/output
```

---

## 📊 Example Output

```
+----------+-----+
|event_type|count|
+----------+-----+
|click     | 42  |
|view      | 30  |
|purchase  | 5   |
+----------+-----+
```

---

## 📁 Project Structure

```
real-time-data-pipeline-kafka/
├── producer/
│   └── producer.py
├── spark_streaming/
│   └── consumer.py
├── docker-compose.yml
├── README.md
```

---

## 📌 Next Steps

- Add windowed aggregations (time-based analytics)  
- Integrate PostgreSQL for serving layer  
- Add monitoring and logging  
- Build dashboard (Streamlit / Grafana)  

---

## 🧠 What This Project Demonstrates

- Real-time data ingestion using Kafka  
- Stream processing using Spark Structured Streaming  
- Schema enforcement and JSON parsing  
- Stateful aggregations on streaming data  
- Writing analytics-ready data to storage  

---

## 🔥 Summary

This project demonstrates how to build an **end-to-end real-time data pipeline**, moving from raw event ingestion to structured analytics-ready output — a core skill in modern data engineering.
