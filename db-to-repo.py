# Databricks notebook source
from pyspark.sql.types import *

df = spark.createDataFrame([1,2,3,4,5,6], IntegerType())
display(df)
