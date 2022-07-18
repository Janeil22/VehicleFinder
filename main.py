import requests

model = 'civic'

for i in range(10):
    year = 2010
    api_url = 'https://api.api-ninjas.com/v1/cars?year={}&limit=30'.format(model)
    year+=1
response = requests.get(api_url, headers={'X-Api-Key': 'satQ5cAvuZnDLaHo6QNHhA==be21RIxCh11f66As'})
data = response.json()
print(data[0])
for i in data:
    print(i['year'])