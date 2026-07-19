An Apache-style access log is at /app/access.log in the working directory. Parse every non-empty line and produce a JSON summary report at /app/report.json with exactly these fields:

  - "total_requests" (integer): number of log lines parsed
  - "unique_ips" (integer): count of distinct client IP addresses
  - "top_path" (string): the URL path that appears most often in requests

Write the JSON file to /app/report.json with no extra fields and no trailing commas.

Success criteria:

1. /app/report.json exists and contains valid JSON.
2. "total_requests" equals the total number of non-empty lines in the access log.
3. "unique_ips" equals the number of distinct IP addresses across all log lines.
4. "top_path" equals the URL path with the highest request count (ties broken by first occurrence).
