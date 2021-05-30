# Fastgre
### FastAPI and PostgreSQL integration to simple usage

Step 1:
Check the dependencies first:

```bash
pip3 install -r requirements.txt
```

Step 2:
Configure database accesing credentials: (If you don't setup PostgreSQL yet, please check [this document](https://www.postgresql.org/docs/12/tutorial-createdb.html) out. Also you can get some informations about how to create database and tables to storage data)

```python
con = psycopg2.connect(
    host="localhost",
    database="enter_your_db_name",
    user="enter_your_database_user",
    password="enter_your_password")
```

Step 3:
Run FastAPI service:

```bash
python3 service.py
```

Step 4:
Post json request to the service with given example request.py script:
```bash
python3 request.py
```
Note: To add, delete, list and update operations you should configure this script with dictionaries given below. 

* ADD
```json
{
   "context":{
      "table_name":"tablename",
      "cols":[
         "col1",
         "col2"
      ],
      "vals":[
         "val1",
         "val2"
      ]
   }
}
```

* DELETE
```json
{
   "context":{
      "table_name":"tablename",
      "condition":"col='val'"
   }
}
```

* LIST
```json
{
   "context":{
      "table_name":"tablename",
      "cols":[
         "col1",
         "col2"
      ]
   }
}
```

* UPDATE
```json
{
   "context":{
      "table_name":"tablename",
      "cols":[
         "col1",
         "col2"
      ],
      "vals":[
         "new_val1",
         "new_val2"
      ],
      "condition":"col1='val1'"
   }
}
```
