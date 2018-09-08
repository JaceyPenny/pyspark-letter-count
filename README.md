# PySpark: Letter Count

A simple PySpark program to count the occurrences of words that start with each character of the 26 letter English alphabet.

## Execute

Have a text file handy. To execute the program, you do either of the following:

```bash
spark-submit letter-count.py TEXT_FILE OUTPUT_DIRECTORY
```

OR

```bash
chmod +x run-spark.sh # only need to do this once 
./run-spark.sh TEXT_FILE OUTPUT_DIRECTORY
```


## Output

The output will come in `part-*` files in the output directory of your choosing.
Each line in a `part-*` file will contain a string in the following format:

```
(LETTER, COUNT)
```

For example:
```
('c', 19618)
```

If your text file contains words such that every letter in the alphabet occurs as the first character of some word, then
you should expect a total of 26 unique key-value pairs in these `part-*` files.
