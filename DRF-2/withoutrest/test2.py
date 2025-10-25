import requests 

# 1. base url 
# 2. end point

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijsoncbv2'

resp1 = requests.get(BASE_URL + END_POINT)
data1 = resp1.json()

resp2 = requests.post(BASE_URL + END_POINT)
data2 = resp2.json()

resp3 = requests.put(BASE_URL + END_POINT)
data3 = resp3.json()

resp4 = requests.delete(BASE_URL + END_POINT)
data4 = resp4.json()

print('='*40)
print(data1)
print('='*40)

print('*'*60)

print('='*40)
print(data2)
print('='*40)

print('*'*60)

print('='*40)
print(data3)
print('='*40)

print('*'*60)

print('='*40)
print(data4)
print('='*40)