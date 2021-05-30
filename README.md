# Fastgre
### FastAPI and PostgreSQL integration to simple usage

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