from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import csv
import operator

if not sc:
    conf = SparkConf().setAppName("Spark Project: Part 2")
    sc = SparkContext(conf=conf)
    sqlCtx = SQLContext(sc)

sc.setLogLevel("ERROR")

# Read in the client csv file from HDFS
rdd = sc.textFile("/user/hduser/client_trace50.csv")
rdd = rdd.filter(lambda x: not x.startswith("code,"))

# Defines mapping function for combined key (client_id and loc_ts).
# As value we are using the timestamp
def mapf(x):
    fields = x.split(",")
    return (fields[1] + "_" + fields[2], int(fields[6]))

# Map the function above and reduce by combined key to get the diff
# between two corresponding request and response entries
rddReqResp = rdd.map(mapf)
rddReqRespTimeDiff = rddReqResp.reduceByKey(lambda x,y: y - x) 

# To get the 
rddReqMinute = rddReqResp.reduceByKey(lambda x,y: x / 1000 * 60)
rddReqMinuteSum = rddReqMinute.reduceByKey(operator.add)


# Write the throughput for exsiting minutes to csv file. Note: the
# minutes which does not contains any entries are not inlcuded
with open("out.csv", "wb") as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	for line in rddReqMinute.collect():
		writer.writerow(line) 
