<!-- There is an access log in the working directory. Analyze the traffic and summarize
what you find — how many requests there were, the clients involved, and which pages
were popular. Save your findings so they can be reviewed. -->

There's an Apache-style access log at access.log in the working directory. Parse it and
write a JSON summary report to /app/report.json with three fields: total_requests
(integer - total number of requests in the log), unique_ips (integer - number of
distinct client IP addresses), and top_path (string - the request path that appears
most often).

Your solution is correct when:

1. /app/report.json exists and is valid JSON.
2. The JSON object contains exactly the keys total_requests, unique_ips, and top_path.
3. total_requests matches the number of requests in access.log.
4. unique_ips matches the number of distinct client IPs in access.log.
5. top_path matches the single most frequently requested path in access.log.