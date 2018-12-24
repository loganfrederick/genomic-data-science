seq='abcd'

for i in range(len(seq)+1):
        for j in range(i):
                print(seq[j:i])

print('Option A')

# i=0
# while i<len(seq) :
#       j=0
#       while(j<i) :
#                 print(seq[j:i])

print('Option B')

# i=1
# while i<len(seq) :
#       j=1
#       while(j<i) :
#                 print(seq[j:i])
#                 j=j+1
#       i=i+1

print('Option C')

# i=0
# while i<len(seq) :
#        j=0
#        while(j<i) :
#                  print(seq[j:i])
#                  j+=1
#        i+=1

print('Option D')
# i=0
# while i<len(seq)+1 :
#       j=0
#       while(j<i+1) :
#                 print(seq[j:i])
#                 j=j+1
#       i=i+1

print('Option E')
#i=1
# while i<len(seq)+1 :
#       j=1
#       while(j<i+1) :
#                 print(seq[j:i])

print('Option F')
# i=0
# while i<len(seq):
#       j=i
#       while(j>0):
#                 print(seq[j:i])
#                 j=j+1
#       i=i+1


i = 1
while i < 100:
          if i%2 == 0 : break
          i += 1
          print(i)
else:
     i=1000
     print(i)
