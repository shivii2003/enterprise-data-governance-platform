def validate(rows,required):
    return [(i,key) for i,row in enumerate(rows) for key in required if row.get(key) in (None,'')]
def authorize(role,classification):
    return classification=='public' or role in {'admin','data_steward'}
