a={"a":["s1","s2"],"b":["s1","s3"]}
d={}
for k in a:
    for v in a[k]:
        if(not v in d):
            d[v]=[]
        d[v].append(k)

print d
