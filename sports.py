sports = {'A' : ['s1','s2','s3'],'B' : ['s2','s4'],'C' : ['s3'],'D' : ['s1','s4','s5']}
def invert(a):
    result = {}
    for k in a:
        for v in a[k]:
            if(not v in result):
                result[v] = []
            result[v].append(k)
    return result
print invert(sports)
