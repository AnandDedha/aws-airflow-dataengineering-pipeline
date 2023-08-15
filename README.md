
## Data Engineering project AWS

In this project, we're developing an AWS-based data pipeline utilizing airflow, python, spark, and AWS services. The objective is to extract Weather Data from OpenWeather, subsequently storing it in S3, and ultimately loading it into Redshift using the Airflow platform. The project's high-level architecture is as follows:

We've established the entire architecture through infrastructure as code (IAC) methodologies. Following that, we've configured two separate airflow directed acyclic graphs (DAGs).

**Setting Up the First Airflow DAG:**
This DAG encompasses tasks for data extraction via the weather API and subsequent loading into an S3 bucket.

**Task 1:** Extracting Data from OpenWeather API: Utilizing a Python operator, we retrieve weather data from the OpenWeather API. This involves leveraging libraries such as "requests" to initiate API requests and obtain the required data.

**Task 2:** Storing Data in S3: After successfully extracting the data, we structure it within a data frame and then store it within an S3 bucket. This operation is executed using the S3CreateObjectOperator.

**Setting Up the Second Airflow DAG:**
This DAG includes tasks for extracting data from S3, applying transformations, and finally loading the processed data into Redshift.

**Task 1: Waiting for Completion of the First DAG:** Before proceeding, this task ensures that the first DAG has successfully completed its operations.

**Task 2: ETL Processing to Redshift using Glue Operator:** This step involves employing the GlueContext and Spark context for Extract, Transform, Load (ETL) operations. The data, once transformed, is loaded into the Redshift database.

**Conclusion:**
By adhering to these outlined steps, a comprehensive ETL pipeline is established within AWS. This pipeline facilitates the extraction of weather data from OpenWeather, its storage within S3, and its subsequent loading into Redshift. The integration of Apache Airflow and Glue operators guarantees the automation of routine updates to the weather data in the Redshift database.
