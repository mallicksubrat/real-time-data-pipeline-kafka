# ⚡ Real-Time Data Pipeline (Kafka + Spark)

A complete real-time data pipeline that ingests streaming events, processes them using **Spark Structured Streaming**, performs real-time aggregations, and stores analytics-ready data.

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

Build a **production-style real-time data pipeline** locally that demonstrates:
- streaming ingestion  
- transformation  
- real-time analytics  
- persistent storage  

---

## 🚀 Features Implemented

- ✅ Kafka cluster running via Docker  
- ✅ Real-time event producer (Python)  
- ✅ Spark Structured Streaming consumer  
- ✅ JSON parsing with schema enforcement  
- ✅ Real-time aggregation (event counts)  
- ✅ Data stored in Parquet (analytics-ready format)  
- ✅ Windowed real-time analytics (time-based aggregation)
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
- Example:

```
-------------------------------------------
Batch: 0
-------------------------------------------
+----------+-----+
|event_type|count|
+----------+-----+
|click     | 42  |
|view      | 30  |
|purchase  | 5   |
+----------+-----+
```

---

### 5. Check Stored Data

Processed data is stored locally in:

```bash
/tmp/output
```

You can inspect files using:

```bash
ls /tmp/output
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

## 📊 What This Project Demonstrates

- Real-time data ingestion using Kafka  
- Stream processing using Spark Structured Streaming  
- Schema-based JSON parsing  
- Stateful aggregation on streaming data  
- Writing analytics-ready data to Parquet  

---

## 📚 Key Learnings

- Handling real-time streaming systems end-to-end  
- Debugging Kafka and Spark integration issues  
- Understanding Structured Streaming output modes  
- Designing clean, scalable data pipelines  
- Managing streaming state and checkpoints  

---

## 📌 Next Steps

- Add time-window based aggregations  
- Integrate PostgreSQL as a serving layer  
- Add monitoring/logging  
- Build dashboard (Streamlit / Grafana)  

---

## 🔥 Summary

This project demonstrates the ability to design, build, and debug a **real-time data pipeline** from ingestion to analytics-ready storage — a core capability in modern data engineering.
