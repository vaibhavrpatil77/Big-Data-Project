import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

jdbc_url = "jdbc:mysql://dbt6.c7tpympilpcm.us-east-1.rds.amazonaws.com:3306/crime"
properties = {
    "user": "admin",
    "password": "qwertyuiop",
    "driver": "com.mysql.cj.jdbc.Driver"
}
table_name = "outcomes"
df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=properties)

# Reading data from MySQL table "your_table_name"
df = spark.read.jdbc(url=jdbc_url, table="outcome", properties=jdbc_pro)

# Transformations or data processing if needed
# df_transformed = df.withColumn(...)

# Define the number of partitions
num_partitions = 149

# Repartition the DataFrame
df = df.repartition(num_partitions)

# Writing data to S3 with partitions

output_path = "s3://g624datalake/outcomes-datalake/"

df.write \
    .mode("append") \
    .parquet(output_path)

job.commit()


