done = function(summary, latency, requests)
   io.write(string.format("\nSocket connection errors: %s\n", summary.errors.connect))
   io.write(string.format("Socket read errors: %s\n", summary.errors.read))
   io.write(string.format("Socket write errors: %s\n", summary.errors.write))
   io.write(string.format("HTTP status errors: %s\n", summary.errors.status))
   io.write(string.format("Request timeouts: %s\n", summary.errors.timeout))
end
