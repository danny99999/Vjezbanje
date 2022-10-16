def funkcija3(x):
    return {y for d in x for _,y in d.items()}

print(funkcija3( [{'ip':'192.168.3.1'}, {'ip':'10.0.0.0'}, {'ip':'127.0.0.0'},
{'ip':'192.168.3.1'}]))
