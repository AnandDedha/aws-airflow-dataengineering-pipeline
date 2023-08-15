
#### Data Engineering project: Extracting Weather Data from OpenWeather, Storing in S3, and Loading into Redshift using Airflow

In this project, we are creating a data pipeline in AWS using the airflow, python, spark, and AWS services. High-level architecture for the project

We set up the whole architecture using infrastructure as code (IAC). After that, we set two airflow dags . In the first Airflow dag we extract the data using weatherAPI and load into s3 . here we have two tasks 

### task 1: Extract Data from OpenWeather API

Use a Python operator to extract weather data from the OpenWeather API. You are using libraries like `requests` to make API requests and retrieve the data.

### task 2: Store Data in S3

Once the data is extracted, save it dataframe and store into an S3 bucket using  S3CreateObjectOperator. 

### Step 3: Set Up 2nd Airflow DAG

The DAG will include tasks for extracting data from s3 , applying transformation, and loading it into Redshift.

### Step 4: Task 1 - Wait for first dag to complete

### Step 5: Task 2 - ETL Data to Redshift using Glue Operator

Define another PythonOperator task that uses the GlueContext to copy data from the S3 bucket to Amazon Redshift. This can be achieved using the GlueContext.create_dynamic_frame.from_catalog() method.


### Conclusion

By following these steps, you can create an ETL pipeline that extracts weather data from OpenWeather, stores it in S3, and loads it into Redshift using Apache Airflow and Glue operators. This pipeline ensures regular and automated updates of weather data in your Redshift database.
