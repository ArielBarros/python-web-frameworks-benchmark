#!/bin/bash

# Usage: ./perform.sh <framework> <scenario>

# Create results directory hierarchy
mkdir -p results/{flask,bottle,falcon}/{hello,template,database}

CONNECTIONS=(100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000)
case "$2" in
	hello)
		for connections in "${CONNECTIONS[@]}"; do
			echo "[*] Testing [Hello] using: $connections connections"
			wrk -t4 -c"$connections" -d20s -s scripts/report.lua http://127.0.0.1:5000/ > "results/$1/$2/$connections.txt"
		done
		;;
	template)
		for connections in "${CONNECTIONS[@]}"; do
			echo "[*] Testing [Template] using: $connections connections"
			wrk -t4 -c"$connections" -d20s -s scripts/report.lua http://127.0.0.1:5000/template > "results/$1/$2/$connections.txt"
		done
		;;
	database)
		for connections in "${CONNECTIONS[@]}"; do
			echo "[*] Testing [Database] using: $connections connections"
			wrk -t4 -c"$connections" -d20s -s scripts/redis.lua http://127.0.0.1:5000/database > "results/$1/$2/$connections.txt"
		done
		;;
	*)
		echo "Invalid option: $@"
		;;
esac

