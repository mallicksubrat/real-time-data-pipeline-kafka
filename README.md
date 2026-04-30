# ⚡ Real-Time Data Pipeline (Kafka + Spark)

A real-time data pipeline that ingests streaming events, processes them using Spark Structured Streaming, and stores analytics-ready data.

---

## 🏗 Architecture
Producer → Kafka → Spark Streaming → Storage

---

## 🛠 Tech Stack
Python • Kafka • PySpark • Docker • PostgreSQL

---

## 🎯 Goal
Simulate a production-grade real-time data pipeline with local infrastructure and CI/CD workflow.

---

## 🚀 Current Status
- [x] Repository initialized  
- [x] Project structure setup  
- [x] Kafka setup  
- [x] Producer service  
- [x] Streaming consumer  
- [x] Storage integration  
- [x] CI/CD pipeline  

---

## 📌 Next Step
Set up Kafka and start streaming real-time events.

## ▶️ How to Run the Pipeline

### 1. Start infrastructure
```bash
docker-compose up -d
python producer/producer.py

spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \
  spark_streaming/consumer.py

/tmp/output
