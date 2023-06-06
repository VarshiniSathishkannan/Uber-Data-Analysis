#! /usr/bin/python

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("GCSFilesRead").getOrCreate()

raw = "uber_data_analysis_raw_01"
stage = "uber_data_analysis_stage_01"
final = "uber_data_analysis_final_01"
input_path = f"gs://{raw}/input"
output_path = f"gs://{stage}/"

df = spark.read.parquet(input_path)

df.write.mode('overwrite').parquet(output_path)
