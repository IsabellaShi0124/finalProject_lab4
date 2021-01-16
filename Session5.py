#Isabella Shi Session 5


#11 Mortal Fibonacci Rabbits
'''
Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
----------------------------
Sample Dataset: 6 3
Sample Output: 4
'''

def mortalRabbits(n, m):
  rabbits = [1, 1]
  months = 2
  while months < n: 
    #different situations depending on m
    if months < m:
      rabbits.append(rabbits[-2] + rabbits[-1])
    elif months == m:
      rabbits.append(rabbits[-2] + rabbits[-1] - 1)
    else: 
      rabbits.append(rabbits[-2] + rabbits[-1] - rabbits[-(m + 1)])
    months += 1
  totalPairs = rabbits[-1]
  return totalPairs

print(mortalRabbits(6, 3))
#works!
print(mortalRabbits(80, 17))



#12 Overlap Graphs
'''
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
----------------------------
Sample Dataset:
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
Sample Output:
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
'''



#13 Calculating Expected Offspring
'''
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond 
to the number of couples in a population possessing each genotype pairing for a given factor. 
In order, the six given integers represent the number of couples having the following genotypes:

1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
under the assumption that every couple has exactly two offspring.
----------------------------
Sample Dataset: 1 0 0 1 0 1
Sample Output: 3.5
'''
def dominantPhenotype(a, b, c, d, e, f):
  '''
  a = # of AA-AA pairs
  b = # of AA-Aa pairs
  c = # of AA-aa pairs
  d = # of Aa-Aa pairs
  e = # of Aa-aa pairs
  f = # of aa-aa pairs
  '''
  #the possibility of having dominant phenotype offspring. 
  aProb = 1
  bProb = 1
  cProb = 1
  dProb = 0.75
  eProb = 0.5
  fProb = 0

  #num of dominant phenotype offspring in each situation
  aNum = aProb * a
  bNum = bProb * b
  cNum = cProb * c
  dNum = dProb * d
  eNum = eProb * e
  fNum = fProb * f

  #total number
  dominantPhenotypeNum = (aNum + bNum + cNum + dNum + eNum + fNum) * 2

  return dominantPhenotypeNum

print(dominantPhenotype(1, 0, 0, 1, 0, 1))
#works! 
print(dominantPhenotype(19412, 16131, 17431, 19005, 18790, 18576))