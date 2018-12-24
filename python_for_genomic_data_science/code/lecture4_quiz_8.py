mylist=[1,2,2,3,4,5]

d = {}
result = False
for x in mylist:
    if x in d:
       result=True
       break
    d[x] = True
print(d)

d = {}
result = False
for x in mylist:
    if not x in d:
       d[x]=True
       continue
    result = True
print(d)
