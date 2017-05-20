from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import csv
import operator

if not sc:
    conf = SparkConf().setAppName("Spark Project: Part 1")
    sc = SparkContext(conf=conf)
    sqlCtx = SQLContext(sc)

sc.setLogLevel("ERROR")

# Read in the csv file from HDFS
rdd = sc.textFile("/user/hduser/mw_trace50.csv")

# Filter by res_snd
rddSend = rdd.filter(lambda w: w.startswith("res_snd,"))

# Get minutes from csv file, located at the fift column. To get
# distinct values and calculate the occurence inside a minute, 
# we define a tumple with value 1 to sum up the values later
minutef = lambda x: (str(int(x.split(",")[6]) / 1000 * 60), 1)

# Execute the mapping function and reduce by key. The latter will
# sum up all the values which are grouped by one key and put them
# into a tuple -> (<min>, <occurence>)
rddDistinctMin = rddSend.map(minutef).reduceByKey(operator.add)

	
# Now we have to sum up all the occurences inside one minute and
# divide them through the minutes occurence
result = rddDistinctMin.map(lambda x: int(x[1])).reduce(operator.add)


# To get the throughput per minte, we have to calculate the difference of
# the minutes range
minTime = int(rddDistinctMin.min()[0])
maxTime = int(rddDistinctMin.max()[0])

diff = maxTime - minTime
print(result / diff)


# Write the throughput for exsiting minutes to csv file. Note: the
# minutes which does not contains any entries are not inlcuded
with open("out.csv", "wb") as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	for line in rddDistinctMin.collect():
		writer.writerow(line) 
