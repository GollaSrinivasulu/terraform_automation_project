# 🚀 Terraform Automated Spark Data Pipeline

## 📌 Project Overview

This project demonstrates an **end-to-end Data Engineering pipeline** using:

- Apache Spark (PySpark) for data processing  
- Docker for containerized execution  
- Terraform for automated pipeline orchestration  

It simulates how real-world data pipelines are built, deployed, and triggered in cloud environments — matching modern Data Engineer hackathon and interview expectations.

---

## 🏗️ Project Architecture

Terraform orchestrates the complete workflow:

Terraform → Docker Build → Docker Run → Spark Job → Output CSV

---

## 📂 Project Structure

terraform_automation_project/
│
├── app.py              # Spark transformation logic  
├── data1.csv           # Employee dataset  
├── data2.csv           # Department mapping dataset  
├── Dockerfile          # Spark container definition  
│
└── terraform/
    └── main.tf         # Terraform automation script  

---

## 📊 Input Data

### data1.csv

emp_id,name,dept_id,salary  
1,A,A,1000000  
2,B,A,2500000  
3,C,G,500000  
4,D,G,800000  
5,E,W,9000000  
6,F,W,2000000  

### data2.csv

dept_id1,dept_name  
A,AZURE  
G,GCP  
W,AWS  

---

## ⚙️ Spark Transformation Logic

1. Read both CSV files into Spark DataFrames  
2. Join employee and department data  
3. Compute minimum salary per department  
4. Join back to find employees with minimum salary per department  
5. Generate final curated dataset  

### ✅ Final Output

emp_id | name | dept_name | salary  
3 | C | GCP | 500000  
1 | A | AZURE | 1000000  
6 | F | AWS | 2000000  

---

## 🐳 Docker Setup

The pipeline runs inside an official Apache Spark container.

Dockerfile:

FROM apache/spark:3.5.1  

WORKDIR /opt/app  

COPY app.py .  
COPY data1.csv .  
COPY data2.csv .  

CMD ["/opt/spark/bin/spark-submit", "/opt/app/app.py"]

---

## 🌍 Terraform Automation

Terraform automatically:

- Builds Docker image  
- Runs Spark container  
- Executes Spark job  
- Copies output file to host  

One command triggers everything:

terraform apply

---

## ▶️ How to Run

Step 1 — Go to terraform folder  

cd terraform  

Step 2 — Initialize Terraform (first time only)

terraform init  

Step 3 — Run pipeline

terraform apply  

Type **yes** when prompted.

---

## 📁 Output Files

After execution:

cleaned_data.csv  → Final processed dataset  
terraform/infra_ready.txt → Terraform execution confirmation  

---

## 🧠 Key Concepts Demonstrated

- Apache Spark DataFrame transformations  
- Joins and aggregations  
- Dockerized Spark execution  
- Infrastructure-as-Code using Terraform  
- Fully automated data pipeline  

---

## 💡 Real-World Relevance

This project reflects how enterprise data pipelines are:

- Containerized with Docker  
- Executed with Spark  
- Orchestrated using Terraform  
- Reproducible and automated  

---

## 👤 Author

Srinivas Yadav  
GitHub: https://github.com/GollaSrinivasulu  

---

### 🚀 One Command Execution

terraform apply
