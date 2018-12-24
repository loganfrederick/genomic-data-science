import random
def create_dna(n, alphabet='acgt'):
    return ''.join([random.choice(alphabet) for i in range(n)])
dna = create_dna(1000000)

print(len(dna))

# def count1(dna, base):
#    i = 0
#    for c in dna:
#            if c == base:
#        i += 1
#    return i

# def count2(dna, base):
#     i = 0
#     for j in range(len(dna)):
#         if dna[j] == base:
#             i += 1
#     return i

def count3(dna, base):
    match = [c == base for c in dna]
    return sum(match)

print(count3('abcdabcd','a'))

def count4(dna, base):
    return dna.count(base)

print(count3('abcdabcd','a'))

# def count5(dna, base):
#     return len([i for i in range(len(dna)) if dna[i] == base])

# def count6(dna,base):
#    return sum(c == base for c in dna)
