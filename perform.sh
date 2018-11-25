#!/bin/bash

CONNECTIONS=(100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000)

for connections in "${CONNECTIONS[@]}"; do
	echo "[*] Testing: $connections connections"
	wrk -t4 -c"$connections" -d20s http://127.0.0.1:5000/ > "results/$1/$connections.txt"
done
