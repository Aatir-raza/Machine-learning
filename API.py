import requests
import pandas as pd

# API fetch
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=15)

# Check  request successful or  not
response.raise_for_status()


data = response.json()


df = pd.DataFrame(data)

print(df.head())
print(df.columns)