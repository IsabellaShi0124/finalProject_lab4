#Isabella Shi Session 3


#6 Counting Point Mutations
'''
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
----------------------------
Sample Dataset: 
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output: 
7
'''

def mutationCount(s, t):
  #count the difference
  numCount = 0
  for i in range(0, len(s)):
    if s[i] == t[i]:
      continue
    else:
      numCount += 1
  return numCount

s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
print(mutationCount(s, t))

s = 'TTCTCAAGGGGTAGAGTAATAGACAAGGCCTCACTGGTGCCCGCGTCGTCGTGAAGCGACGGTTGTTTGCCACGTAAACGTATGCACCGTACTTCCATTTTGGATCATTCGAGGGTTGAGCGCATGCTAACATAGCCAAAGATGGCCCAGGAAGCATGCGGGCCGATGTCTTTTCCAATGGGACTCCGATGGGGTCGGGGTCCCATAACGATGCCGCGAGTGAGGGAGTTCGCTCTTCCCTCGCTGCGGGCTTAACGGTACACTCACGAAATCAAAATTCGCTACTGATAAAATACATATCTATCCGTGCGCCGATTCTAAGCCCGACGTCGCAAATACTCGCGGTAGTGCGTGAGTTGTATTAAGCGTGAAAATGGGCAACAGGAAAGATCAGTCTAAGACGGATCTACATTGGTAAGCTTATACAGAAGCGTGGGGTGGATGCGCCGAGGGTGAATGAGTTAAGGGGAAGTTACGGGAGCTCGTTAGTTGCGTGGGCACAAGATGTTTGTACTCCTCTATGTTACCGACCTCGAACAAGGGCGTTACTAACACTTTCCGGCAGAATCTCGTACACAATAGAGTTACGTTACATAAATCCTCCTAAAAATTCCCGCCCCTGTCTCGGTTTGGAACGTGGTATACTAGGAGCCCTGATGTGGGTATAATTATTTGCACTCCGGCGTCGTTGGAATTATTTCCGGAGAGTATGTTGGCCGGGAGTAATTGGCAATAAAAAAATCGGGATAAAGGTCCTTATCCGCCATCCGGGCATCGAGTCGACTGTGCATAAAGCTCACAGCAAGAAGACCGCTGCTTAGCTGGCCGATTCAACTGAATGAGAAACTGCACTGCGCGACGACCACGGGGAATTAAGAACAACCATGATCGATGGTGGGATAGGACTGCACATGGTCCGTCACGAAGCCGAACACGGGTGCTA'
t = 'TTAACAGCGGCATGATAAATAGACAGAACGGATCGCGAACCCGAGCTTCCCTTCGACTCTCTGTGTTTACAGAGCGTAAGATGGCCTGTTACTGCTAATACGAACACTAACTTGGAGTAGCAGTTGATCGAATCTCCAAATACGGCCTAGACCGATGGCGGGCTATAGTGTGGCCTATGAGAATACCGTTGGTGTCTTGATCAACCAAAAACGTCCTCTTACAACGCTGTCGCTATTTTGGCGATGGGGTCCTCGCGATTCCGATACGAAAGTTAATTTCGATTAAGGCAATAAGAGACACAAGGCGTACGCCCTTTTCTAGGCAGACTTCGGAAATCCACGCGACGATGGGTGAGAGGTGTGAATCGTGCAAACTGGTAACTCGAAACAATAGTGTGAATCTGGTCTGTCTTGATATTGTGTTATAAAAGCGTGTTGTGGATGCTCTTCACTAGATTTATGACATTGGGAGTGGAGCTACGTAGTGAAATGGAAGGGCCAAGAGAGCTTTAACCGCTCTGAGTTACCATCCGCGAAGCTCGGCGGTAATTTCACCGTACGCCCGACTCTGTCACAGTACACCCTTCCATTACGTTAACCAGAGCAGAAATGCCTGTCACTCGCTCGGCTTTCCACCATCGTTTTTGGTGGCCATTATGGTGGAGTATTATTTGGCACCCAAGCTATAATGGGTGATTTGCCGCGAAGGTATTGTGAAAGCCGCCAGTGGCCTCCCAAACAGCGGGACCGAGGTACGGTCTTCCTACAGAAAAGTCGAGGCGCTTATGCATATCACTGACACCATGAAAGGGAACCGCCACCCGCCAGATGGGATGTAACGAAAAACTGCCCTGCGCAGCGACGGATGGCGGTTCGTTCCTTCCCTGATCAATGCGTCGCAAGGATTACTCGTGGGTTCGTAAGAAGCCGTTCATGAGAACAT'
print(mutationCount(s, t))



#7 Mendel's First Law
'''
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing
a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
--------------------------
Sample Dataset: 2 2 2
Sample Output: 0.78333
'''
#when the individul is not homozygous recessive, it displays the dominant phenotype
#K --> homozygous dominant M --> heterozygous N --> homozygous recessive
#These pairs could potentially produce homozygous recessive offspring: MM, MN, NN
#MM: 1/4 MN: 1/2 NN: 1
#probability of getting homozygous recessive offspring is: 
  #MM --> m/(k + m + n) * (m - 1)/(k + m + n - 1) * 1/4
  #MN --> m/(k + m + n) * n/(k + m + n - 1) * 1/2 + n/(k + m + n) * m/(k + m + n - 1) * 1/2 
  #NN --> n/(k + m + n) * (n - 1)/(k + m + n - 1)
#one minus all the above would be the probability of getting an offspring with dominant phenotype

def dominantProbability(k, m, n):
  pTotal = k + m + n
  #the probability of homozygous recessive offspring
  mmProb = 0.25 * (m/pTotal) * ((m - 1)/(pTotal - 1))
  mnProb = 0.5 * (m/pTotal) * (n/(pTotal - 1)) + 0.5 * (n/pTotal) * (m/(pTotal - 1))
  nnProb = (n/pTotal) * ((n - 1)/(pTotal - 1))
  recessiveProb = mmProb + mnProb + nnProb
  #dominant phenotype probability
  dominantProb = 1 - recessiveProb
  return dominantProb

print(dominantProbability(2, 2, 2))
#worked!
print(dominantProbability(22, 17, 30))
#yay!


#8 Translating RNA into Protein
'''
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
------------------------------
Sample Dataset: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output: MAMAPRTEINSTRING
'''

'''      
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''

def rna2protein(rna):
  #cut RNA into threes
  codonList = []
  while rna:
    codonList.append(rna[:3])
    rna = rna[3:]
  
  #translate codon
  proteinString = ''
  for codon in codonList: 
    if codon == 'UUU' or codon == 'UUC': 
      proteinString += str('F')
    elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
      proteinString += str('L')
    elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
      proteinString += str('S')
    elif codon == 'UAU' or codon == 'UAC': 
      proteinString += str('Y')
    elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
      proteinString += str(' ')
    elif codon == 'UGU' or codon == 'UGC':
      proteinString += str('C')
    elif codon == 'UGG': 
      proteinString += str('W')
    elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
      proteinString += str('P')
    elif codon == 'CAU' or codon == 'CAC':
      proteinString += str('H')
    elif codon == 'CAA' or codon == 'CAG':
      proteinString += str('Q')
    elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
      proteinString += str('R')
    elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
      proteinString += str('I')
    elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
      proteinString += str('G')
    elif codon == 'AUG': 
      proteinString += str('M')
    elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
      proteinString += str('T')
    elif codon == 'AAU' or codon == 'AAC':
      proteinString += str('N')
    elif codon == 'AAA' or codon == 'AAG':
      proteinString += str('K')
    elif codon == 'GAA' or codon == 'GAG':
      proteinString += str('E')
    elif codon == 'GAU' or codon == 'GAC':
      proteinString += str('D')
    elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
      proteinString += str('V')
    elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
      proteinString += str('A')
      
  return proteinString

print(rna2protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))
#perfecto!

f = open('rosalind_prot.txt', 'r')
rnaString = f.read()
print(rna2protein(rnaString))