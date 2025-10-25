import json,requests 
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'




# def delete_resource(id):
#     data = {
#         'id':id
#     }

#     resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())

# delete_resource(2)






def update_resource(id):
    new_emp = {
        'id':id,
        'ename':'salman khan',
        'esal':97000,
    }

    resp = requests.put(BASE_URL + END_POINT, data=json.dumps(new_emp))

    print(resp.status_code)
    print(resp.json())
update_resource(3)













# def create_resource():
#     new_emp = {
#         'eno':105,
#         'ename':'Rohit',
#         'esal':190000,
#         'eaddr':'Delhi',
#     }

#     resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json)
 

# create_resource()



# def get_resource(id = None):
#     data = {}

#     if id is not None:
#         data = {
#             'id': id
#         }

#     resp = requests.get(BASE_URL + END_POINT, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
    
# get_resource(2)