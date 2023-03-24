import requests

# Set up the API endpoint and parameters
url = 'http://10.10.12.103/sql-request.do'

params = {
    'response_type': 'application/json',
    'sql_statement': 'SELECT * FROM timeline_stream LIMIT 10;'
}

# Make the API request
response = requests.post(url, data=params)

# Check for errors in the response
if response.status_code != 200:
    print(f'Request failed with error code {response.status_code}')
    exit()

# Parse the response data as JSON
data = response.json()

# Check for errors in the response
if data[0]['error']:
    print(f'Request failed with error: {data[0]["error"]}')
    exit()

# Extract the data from the response
rows = data[0]['data']
for row in rows:
    print(row)
