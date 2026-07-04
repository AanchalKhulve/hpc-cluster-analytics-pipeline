# HPC Cluster Analytics Pipeline

## Overview

A real-time data engineering project that simulates HPC scheduler events and processes them using Kafka and Apache Spark.

The pipeline demonstrates event streaming, distributed data processing, workflow orchestration, and analytics.

---

## Architecture

Python Producer
        ↓
Kafka Topic
        ↓
Spark Structured Streaming
        ↓
Parquet Files
        ↓
SQL Analytics

---

## Technologies

- Python
- Apache Kafka
- Apache Spark
- Docker
- Airflow (coming soon)
- SQL

---

## Project Structure

producer/
spark/
sql/
airflow/
data/
architecture/

---

## Features

- Simulated scheduler events
- Real-time event streaming
- Spark Structured Streaming
- Analytics using SQL
- Containerized environment

---

## Future Improvements

- Airflow DAGs
- Grafana Dashboard
- Kubernetes deployment

---

## Author

## Architecture

```text
                    +----------------------+
                    |  Python Producer     |
                    | (scheduler events)   |
                    +----------+-----------+
                               |
                               |
                               v
                    +----------------------+
                    |      Kafka Topic     |
                    |   cluster-events     |
                    +----------+-----------+
                               |
                               |
                               v
              +-------------------------------+
              | Spark Structured Streaming    |
              | Parse + Aggregate + Transform |
              +---------------+---------------+
                              |
                              |
                              v
                  +-------------------------+
                  |   Parquet Files         |
                  |  (Analytics Dataset)    |
                  +------------+------------+
                               |
                               |
                               v
                    +----------------------+
                    | SQL / Dashboard      |
                    | Future: Airflow      |
                    +----------------------+
```


Aanchal Khulve
