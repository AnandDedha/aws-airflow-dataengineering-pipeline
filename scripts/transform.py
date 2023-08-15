import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
  

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
weather_dyf = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://airflowoutputtos3bucket/raw/weather_api_data.csv"],
        "recurse": True,
    },
    transformation_ctx="weather_dyf",
)

# Script generated for node Change Schema
changeschema_weather_dyf = ApplyMapping.apply(
    frame=weather_dyf,
    mappings=[
        ("dt", "string", "dt", "string"),
        ("weather", "string", "weather", "string"),
        ("visibility", "string", "visibility", "string"),
        ("`main.temp`", "string", "temp", "string"),
        ("`main.feels_like`", "string", "feels_like", "string"),
        ("`main.temp_min`", "string", "min_temp", "string"),
        ("`main.temp_max`", "string", "max_temp", "string"),
        ("`main.pressure`", "string", "pressure", "string"),
        ("`main.sea_level`", "string", "sea_level", "string"),
        ("`main.grnd_level`", "string", "ground_level", "string"),
        ("`main.humidity`", "string", "humidity", "string"),
        ("`wind.speed`", "string", "wind", "string"),
    ],
    transformation_ctx="changeschema_weather_dyf",
)

#changeschema_weather_dyf.show()

redshift_output = glueContext.write_dynamic_frame.from_options(
    frame=changeschema_weather_dyf,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-262136919150-us-east-1/temporary/",
        "useConnectionProperties": "true",
        "aws_iam_role": "arn:aws:iam::262136919150:role/datapipeline-demo-RedshiftIamRole-1KQUQK6ZER2WH",
        "dbtable": "public.weather_data",
        "connectionName": "redshift-demo-connection",
        "preactions": "DROP TABLE IF EXISTS public.weather_data; CREATE TABLE IF NOT EXISTS public.weather_data (dt VARCHAR, weather VARCHAR, visibility VARCHAR, temp VARCHAR, feels_like VARCHAR, min_temp VARCHAR, max_temp VARCHAR, pressure VARCHAR, sea_level VARCHAR, ground_level VARCHAR, humidity VARCHAR, wind VARCHAR);",
    },
    transformation_ctx="redshift_output",
)

job.commit()
