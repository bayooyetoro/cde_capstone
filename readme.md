# **S3 to Snowflake ETL Pipeline with DBT**

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
6. [Usage](#usage)
7. [DBT Data Models](#dbt-data-models)
8. [Screenshots](#screenshots)

---

## **Project Overview**

This project implements an **ETL (Extract, Transform, Load)** pipeline to load data from an **AWS S3 bucket** into **Snowflake**, process it, and model it using **DBT** for analytics. The pipeline is orchestrated using **Apache Airflow** and containerized with **Docker** for portability and scalability.

The pipeline processes country data, extracts essential fields, and structures it into **dimension** and **fact tables** for predictive analytics.

---

## **Architecture**

The architecture for this project is shown below:

![Architecture Diagram](https://via.placeholder.com/800x400?text=Architecture+Diagram)

1. **AWS S3**: Stores raw data in Parquet format.
2. **Snowflake**: Serves as the data warehouse for loading and querying transformed data.
3. **DBT**: Models raw data into clean, analytical tables (Fact and Dimension).
4. **Airflow**: Orchestrates the pipeline from extraction to transformation.
5. **Docker**: Containerizes the pipeline for deployment.

---

## **Features**

- **End-to-End Data Pipeline**:
  - Extracts raw data from **S3**.
  - Loads data directly into **Snowflake**.
  - Models data into analytics-ready tables using **DBT**.
- **Cloud-Native**:
  - Utilizes AWS S3 and Snowflake for scalable data processing.
- **Orchestrated Workflow**:
  - Powered by **Apache Airflow**.
- **Containerized**:
  - Fully Dockerized for easy setup and deployment.

---

## **Technologies Used**

| Technology       | Purpose                                   |
|-------------------|-------------------------------------------|
| **AWS S3**        | Cloud storage for raw data               |
| **Snowflake**     | Data warehouse for analytics             |
| **DBT**           | Data transformation and modeling         |
| **Apache Airflow**| Workflow orchestration                   |
| **Docker**        | Containerization                         |
| **Python**        | ETL logic and scripting                  |
| **pandas**        | Data manipulation                        |

---

## **Setup Instructions**

### **Prerequisites**

Ensure you have the following installed:

- **Docker**: For running the pipeline in a containerized environment.
- **Apache Airflow**: To orchestrate the pipeline.
- **Snowflake Account**: For hosting the data warehouse.
- **AWS S3**: For storing raw data.

### **Installation**

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/bayooyetoro/cde_capstone.git
    cd cde_capstone
    ```

2. **Set Up Credentials**:
    Create a `creds/config.ini` file:

    ```ini
    [aws]
    access_key = your_aws_access_key
    secret_key = your_aws_secret_key
    region = your_aws_region

    [snowflake]
    user = your_snowflake_user
    password = your_snowflake_password
    account = your_snowflake_account
    warehouse = your_snowflake_warehouse
    database = your_snowflake_database
    schema = your_snowflake_schema
    ```

3. **Build and Start Docker Containers**:

    ```bash
    docker-compose up --build
    ```

4. **Set Up Airflow**:
    - Place your DAG files in the `dags/` directory.
    - Start Airflow:

        ```bash
        airflow standalone
        ```

5. **Deploy DBT Models**:

    ```bash
    cd dbt/
    dbt run
    ```

---

## **Usage**

1. **Trigger the Airflow DAG**:
    - Access the Airflow UI at `http://localhost:8080`.
    - Trigger the `s3_to_snowflake_full_pipeline` DAG.

2. **Monitor the Workflow**:
    - Check logs and statuses of each task in the Airflow UI.

3. **Query Data in Snowflake**:
    - Verify the raw, dimension, and fact tables in Snowflake using SQL queries.

---