"""
Assume you're given a table containing information on Facebook user actions.
Write a query to obtain number of monthly active users (MAUs) in July 2022,
including the month in numerical format "1, 2, 3".
"""

# Write your code here

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("active_user_retention").getOrCreate()
df = spark.read.csv("/workspaces/pyspark_learning/src/data/Active_User_Retention.csv",header=True)
df.show()

input("Press Enter to exit...")

