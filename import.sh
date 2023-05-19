#!bin/bash

echo 'hello'

for i in {1..9};
do
    cd /home/neeleshmgr/input
    wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2009-0$i.parquet
done