import sys
from pyspark import SparkConf, SparkContext

# Initialize spark configuration and context
conf = SparkConf()
sc = SparkContext(conf=conf)

# Read from text file, split each line into "words" by any whitespace (i.e. empty parameters to string.split())
lines = sc.textFile(sys.argv[1])
words = lines.flatMap(lambda line: line.split())

# Filter non-alpha characters, then convert them to lowercase
letters = words.filter(lambda letter: letter.isalpha()) \
               .map(lambda word: word[0].lower())

# Map each letter to a key-value pair, with value 1
pairs = letters.map(lambda letter: (letter, 1))

# Reduce by key, effectively summing every tuples values into a single reduction for each letter
counts = pairs.reduceByKey(lambda n1, n2: n1 + n2)

# Save to output directory, end context
counts.saveAsTextFile(sys.argv[2])
sc.stop()
