user = 'john'
prefix = 'request_rate_limiter.' + user

# Use the prefix in rate limiting or other operations
rate_limit_key = prefix + '.api_endpoint'
# rate_limit_key would be 'request_rate_limiter.john.api_endpoint'
