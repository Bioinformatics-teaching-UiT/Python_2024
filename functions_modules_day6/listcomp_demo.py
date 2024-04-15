# -*- coding: utf-8 -*-
"""
List comprehensions


[<expression> for item in iterable <if condition>]
"""

# old way to put numbers in a list
emptylist = []
for i in range(5):
    emptylist.append(i) 
print(emptylist)

# with a list comprehension
numlist = [i+10 for i in range(5)]
print(numlist)

# full way to write out list comprehension
numlist = []
addtentome = 0
for i in range(5):
    numlist.append(i+10)
    addtentome += 10 # addtentome = addtentome + 10
    
# given a list of numbers, return another 
# list with only odd numbers
# use list comprehension!

findoddnumlist = [0, 2, 5, 7, 8, 12, 11]

oddlist = [num for num in findoddnumlist if num % 2 == 1]

# counting nucleotides in a sequence with a list comprehension
# rosalind_count_nucleotides.py
# 20 21 12 17
ourseq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

countslist = []
A_count = 0
C_count = 0

for nucl in ourseq:
    if nucl == 'A':
        A_count += 1
    if nucl == 'C':
        C_count += 1
        
ourseq.count('A')
ourseq.count('T')
ourseq.count('C')
ourseq.count('G')

countslist = [ourseq.count(base) for base in ['A', 'T', 'C', 'G']]

countslist = [ourseq.count(base) for base in 'ATCG']  

rosalind_output = '-'.join([str(basecount) for basecount in countslist])

countslist = ' '.join([str(ourseq.count(base)) for base in 'ATCG'])  

    
    


