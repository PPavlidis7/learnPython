#!/bin/bash
echo started!

for i in 5000 7000 9000 11000 13000 15000 17000 19000 21000 23000
do
    echo $i start
	python comprese_v2.py $i
	python comprese_v2.py $i
	python comprese_v2.py $i
	python comprese_v2.py $i
	python comprese_v2.py $i

	python comprese_v3.py $i
	python comprese_v3.py $i
	python comprese_v3.py $i
	python comprese_v3.py $i
	python comprese_v3.py $i
done

$echo start diagonal

for i in 5000 7000 9000 11000 13000 15000
do
    echo $i start
	python diagonal_v2.py $i

done