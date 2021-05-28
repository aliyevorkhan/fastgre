import requests
'''
context = {"context": {"table_name": "users", "cols": [
    "username", "password"], "vals": ["oskhs", "1234"]}}

context={"context":{"table_name":"users", "condition":"username='orkhan'"}}

context = {"context": {"table_name": "users", "cols": [
    "username", "password"]}}
'''
context = {"context": {"table_name": "users", "cols": [
    "username", "password"], "vals": ["ali", "5555"], "condition":"username='eeee'"}}

# "condition":"username=orkhan"
r = requests.post('http://127.0.0.1:8000/update', json=context)
print(r.json())
