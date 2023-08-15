
## Data Engineering project AWS

In this project, we are creating a data pipeline in AWS using the airflow, python, spark, and AWS services where we are extracting Weather Data from OpenWeather, Storing it in S3, and Loading it into Redshift using Airflow. High-level architecture for the project

We set up the whole architecture using infrastructure as code (IAC). After that, we set two airflow dags. 

#### Set Up 1st Airflow DAG
The DAG will include tasks to extract the data using weather API and load it into s3

Task 1: Extract Data from OpenWeather API - Use a Python operator to extract weather data from the OpenWeather API. You are using libraries like `requests` to make API requests and retrieve the data.

Task 2: Store Data in S3- Once the data is extracted, save it data frame and store it in an S3 bucket using  S3CreateObjectOperator. 

#### Set Up 2nd Airflow DAG
The DAG will include tasks for extracting data from s3, applying the transformation, and loading it into Redshift.

Task 1 - Wait for the first dag to complete

Task 2 - ETL Data to Redshift using Glue Operator. This can be achieved using the GlueContext and Spark context


### Conclusion

By following these steps, you can create an ETL pipeline in AWS that extracts weather data from OpenWeather, stores it in S3, and loads it into Redshift using Apache Airflow and Glue operators. This pipeline ensures regular and automated updates of weather data in your Redshift database.
