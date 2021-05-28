def add_query(order_type,table_name, cols, vals):
    query=""
    query+="insert into "+str(table_name)+"("
    for i in range(0, len(cols)-1):
        query+=cols[i]+","
    query+=str(cols[-1])+") values ("
    for i in range(0, len(vals)-1):
        query+="'"+vals[i]+"',"
    query+="'"+str(vals[-1])+"')"
    return query

def del_query(table_name, condition):
    query=""
    query+="delete from "+str(table_name)
    query+=" where "
    query+=str(condition)
    return query

def list_query(cols, table_name):
    query=""
    query+="select "
    if cols[0]=="*":
        query+="* from"
    else:
        for i in range(0, len(cols)-1):
            query+=cols[i]+","
        query+=str(cols[-1])
    query+=" from "+str(table_name)
    return query

def update_query(table_name, cols, vals, condition):
    query=""
    query+="update "+str(table_name)+" set "
    for i in range(0, len(cols)-1):
        query+=cols[i]+"='"+vals[i]+"',"
    query+=cols[-1]+"='"+vals[-1]+"'"
    query+=" where "+condition
    print(query)
    return query
