import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Initialize SparkSession and GlueContext
spark = SparkSession.builder \
    .appName(args['JOB_NAME']) \
    .getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from S3
df3 = spark.read.csv("s3://group6finalpro1/STREET/", header=True)

# Rename columns
df4 = df3.withColumnRenamed("Crime ID","CrimeID") \
         .withColumnRenamed("Month","MONTH") \
         .withColumnRenamed("Reported by","ReportedBy") \
         .withColumnRenamed("Crime type","CrimeType") \
         .withColumnRenamed("Falls within","FallsWithin") \
         .withColumnRenamed("Longitude","Longitude") \
         .withColumnRenamed("Last outcome category","LastOutcomeCategory") \
         .withColumnRenamed("Context","Contexts") \
         .withColumnRenamed("Latitude","Latitude") \
         .withColumnRenamed("Location","Locations") \
         .withColumnRenamed("LSOA code","LSOACODE") \
         .withColumnRenamed("LSOA name","LSOANAME")

# Write to Parquet
<<<<<<< HEAD
df4.coalesce(1).write.parquet("s3://group-6-datalakenew2802/street/", mode="append")
=======
df4.coalesce(1).write.parquet("s3://group-6-datalakenew23re6dlref/street/", mode="append")
>>>>>>> a1dc1ec93ae1c776f0c96759caea8df78d494032

# Fetching data from RDS
# Read data from RDS using Glue Catalog
rds_database = "new_db"
rds_table = "outcome"
rds_data_source = glueContext.create_dynamic_frame.from_catalog(database=rds_database, table_name=rds_table)

# Convert DynamicFrame to DataFrame for further processing
rds_df = rds_data_source.toDF()

# Rename columns
df2 = rds_df.withColumnRenamed("Crime ID","CrimeID") \
         .withColumnRenamed("Month","MONTH") \
         .withColumnRenamed("Reported by","ReportedBy") \
         .withColumnRenamed("Falls within","FallsWithin") \
         .withColumnRenamed("Longitude","Longitude") \
         .withColumnRenamed("Latitude","Latitude") \
         .withColumnRenamed("Location","Locations") \
         .withColumnRenamed("LSOA code","LSOACODE") \
         .withColumnRenamed("LSOA name","LSOANAME") \
         .withColumnRenamed("Outcome type","Outcometype") \
         .withColumnRenamed("crime type","crimetype") \
         .withColumnRenamed("last outcome category","lastoutcomecategory")

# Write to Parquet
<<<<<<< HEAD
df2.repartition(90).write.parquet("s3://group-6-datalakenew2802/outcomes/", mode="append")
=======
df2.repartition(90).write.parquet("s3://group-6-datalakenew23re6dlref/outcomes/", mode="append")
>>>>>>> a1dc1ec93ae1c776f0c96759caea8df78d494032

# Stop SparkSession
spark.stop()
