from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import handler
import psycopg2

# connect to the db
con = psycopg2.connect(
    host="localhost",
    database="template1",
    user="postgres",
    password="test123")

app = FastAPI()

class RequestBody(BaseModel):
    context: dict

@app.post("/add", status_code = 200)
async def add(rb:RequestBody):
    cur = con.cursor()

    table_name=rb.context["table_name"]
    cols=rb.context["cols"]
    vals=rb.context["vals"]

    query=handler.add_query("add", table_name, cols, vals)
    
    cur.execute(query)
    con.commit()
    #close the cursor
    cur.close()
    return {"status": "OK"}

@app.post("/del", status_code = 200)
async def delete(rb:RequestBody):
    cur = con.cursor()
    table_name=rb.context["table_name"]
    condition=rb.context["condition"]
    query=handler.del_query(table_name, condition)
    cur.execute(query)
    con.commit()
    #close the cursor
    cur.close()
    return {"status": "OK"}

@app.post("/list", status_code = 200)
async def list(rb:RequestBody):
    cur = con.cursor()
    table_name=rb.context["table_name"]
    cols=rb.context["cols"]
    query=handler.list_query(cols,table_name)
    cur.execute(query)
    result = cur.fetchall()

    con.commit()
    #close the cursor
    cur.close()
    return {"result":result}

@app.post("/update", status_code = 200)
async def update(rb:RequestBody):
    cur = con.cursor()
    table_name=rb.context["table_name"]
    cols=rb.context["cols"]
    vals=rb.context["vals"]
    condition=rb.context["condition"]
    query=handler.update_query(table_name, cols, vals,condition)
    cur.execute(query)
    con.commit()
    #close the cursor
    cur.close()
    return {"status": "OK"}

if __name__ == '__main__':  
    uvicorn.run(app, host="0.0.0.0", port=8000)