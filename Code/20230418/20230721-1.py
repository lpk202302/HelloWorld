import os
os.environ["SPARK_HOME"] = r"D:\CDA\data\week6\2022-03-12\spark-3.0.3-bin-hadoop2.7\spark-3.0.3-bin-hadoop2.7"
os.environ["HADOOP_HOME"] = r"D:\CDA\data\week6\2022-03-12\winutils-master\winutils-master\hadoop-2.7.1"

from pyspark.sql import SparkSession

#初始化spark上下文
spark = (
    SparkSession
         .builder
         .master("local[4]") ## 如果有集群，这里填写集群资源信息。例如：spark://192.168.2.123:7077
         .appName("SparkCoreDemo")
         .getOrCreate()
        )