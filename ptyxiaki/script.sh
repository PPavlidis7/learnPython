#!/bin/bash
echo started, gn!
sleep 2h
echo now i can run 

for i in 5000 7000 9000 11000 13000 15000 17000 19000 21000 23000
do
    echo $i start
    python generator.py $i
	python CSR.py $i
	python CSR.py $i
	python CSR.py $i
	python CSR.py $i
	python CSR.py $i
done
