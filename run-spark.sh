#!/usr/bin/env bash

rm -rf output
spark-submit letter-count.py $1 $2