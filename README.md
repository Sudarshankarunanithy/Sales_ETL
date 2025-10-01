# Sales_ETL (PySpark + Docker + HDFS)

A prototype **ETL pipeline** built using **PySpark, Docker, HDFS, and Shell scripting**.  
This project demonstrates how raw sales data can be ingested, transformed, and stored efficiently using a modern data engineering stack.

---

## Project Overview
The purpose of this project is to simulate a real-world **ETL workflow**:

1. **Extract** – Load raw input files (CSV/JSON).
2. **Transform** – Clean, process, and enrich data using PySpark.
3. **Load** – Write the final dataset into HDFS (and as CSV output).

---

## Tech Stack
- **PySpark** – Data processing and transformations  
- **Docker + Docker Compose** – Containerized environment for Spark & HDFS  
- **HDFS** – Distributed storage layer  
- **Shell Scripts** – Automation for running ETL jobs  
- **Git** – Version control  

---

## Project Structure
```bash
Sales_ETL/
│
├── input/                  # Raw input data
│   ├── products.json
│   └── sales.csv
│
├── logs/                   # Log files (ignored in .gitignore)
│   └── sales_etl.log
│
├── scripts/                # PySpark scripts
│   └── sales_etl_job.py
│
├── shell/                  # Shell automation
│   └── run_sales.sh
│
├── .gitignore
├── README.md               # Project documentation
└── docker-compose.yml      # (if added for Spark + HDFS setup)
---
```
## Setup & Run

### 1️ Clone the Repository
```bash
git clone git@github.com:Sudarshankarunanithy/Sales_ETL.git
cd Sales_ETL
```
2️ Build & Start Docker Services
```bash
docker-compose up -d
```
3️ Submit the ETL Job
```bash
sh shell/run_sales.sh
```
---

## This will:

- Run the PySpark job inside Docker
- Process raw input files
- Save results into HDFS/output folder
---
##  Sample ETL Flow

- **Input**: sales.csv + products.json
- **Transformations**: cleaning, joining, aggregating
- **Output**: processed sales summary dataset
---
## Features

- Automated job execution with shell script
- Logs generated for every ETL run
- Dockerized Spark cluster (portable setup)
- Modular codebase for easy extensions
---
## Future Enhancements

- Add data validation & quality checks
- Store processed data into a relational DB (Postgres/SQL Server)
- Build a visualization layer (Power BI / Tableau)
- Implement CI/CD for automated runs
---
## Author

Sudarshan Karunanithy
sudarshankarunanithy7@gmail.com

---

✅ This is now a **clean, properly formatted Markdown block**.  
Would you like me to also add a **table of contents** at the top (with links to sections like Overview, Tech Stack, Setup, Features, etc.) for even more polish?
