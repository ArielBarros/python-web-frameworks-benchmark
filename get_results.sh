# Usage: ./get_results.sh <framework> <scenario>
cd "results/$1/$2"

echo "\n[*] Latency: $1 - Scenario: $2"
cat `ls -1 | sort -V` | grep Latency | awk '{print $2}'

echo "\n[*] Latency std: $1 - Scenario: $2"
cat `ls -1 | sort -V` | grep Latency | awk '{print $3}'

echo "\n[*] Requests/sec: $1 - Scenario: $2"
cat `ls -1 | sort -V` | grep Requests/sec | awk '{print $2}'

echo "\n[*] Request/sec std: $1 - Scenario: $2"
cat `ls -1 | sort -V` | grep Req/Sec | awk '{print $3}'

echo "\n[*] Total requests timeout: $1 - Scenario: $2"
cat `ls -1 | sort -V` | grep 'Request timeouts' | awk '{print $3}'
