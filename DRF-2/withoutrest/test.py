import requests 

# 1. base url 
# 2. end point

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijsoncbv'

resp = requests.get(BASE_URL + END_POINT)

print(type(resp))
print(type(resp.json()))

data = resp.json()

print('Data from django application')
print('='*40)
print(f'Employee Number: {data['eno']}')
print(f'Employee Name: {data['ename']}')
print(f'Employee Salary: {data['esal']}')
print(f'Employee Address: {data['eaddr']}')
print('='*40)
