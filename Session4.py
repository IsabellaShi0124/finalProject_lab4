#Isabella Shi Session 4


#9 Finding a Motif in DNA
'''
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
----------------------------
Sample Dataset: 
s = GATATATGCATATACTT
t = ATAT
Sample Output: 2 4 10
'''

def findMotif(s, t): 
  results = []
  for i in range(0, len(s)):
    #find t in s
    if s[i : i + len(t)] != t:
      continue
    else:
      results.append(i + 1)
  results = str(results).replace(',', '')
  results = results.replace('[', '')
  results = results.replace(']', '')
  return results
  
print(findMotif('GATATATGCATATACTT', 'ATAT'))
#work! YAY! 
print(findMotif('CTTCAGCCGCATCAGCCGTTCCTGTTCAGCCGCCCCTCAGCCGGAGCCCTCAGCCGAAATGCAGTTCAGCCGTCAGCCGTGTCAGCCGACCGTCTCAGCCGCAGTCAGCCGCCTCAGCCGTCTTCAGCCGTTCAGCCGTGTCAGCCGTTCAGCCGTCTCAGCCGTGCAACTTCAGCCGCATCAGCCGGATCAGCCGTTGGTAATCTGCATGCTCAGCCGTCAGCCGATGGGCCATCAGCCGTTCAGCCGCTCAGCCGGTCAGCCGTCAGCCGTGACTATTCAGCCGTCAGCCGAGGTTTAACGGTCAGCCGTCAGCCGTATTCAGCCGTATCAGCCGTCAGCCGTCAGCCGGTAATTTCAGCCGGGCGAAATCAGCCGTTCAGCCGCTGTCAGCCGGTCAGCCGCGGATATCAGCCGTTTCAGCCGACCTGCGTCAGCCGCGTCAGCCGATCAGCCGGCTCAGCCGTCAGCCGAGGAGCTGGTTCAGCCGTCAGCCGCTTCAGCCGTCAGCCGCCGCATCAGCCGTGTTAACCCGCGGGATCAGCCGTCAGCCGGGTTTCAGCCGAAATAGTCAGCCGTCAGCCGCTCAGCCGTCAGCCGATCAGCCGGGAGTCAGCCGTTCAGCCGAGCTTTCAGCCGTGTCAGCCGCATCACTCAGCCGTCAGCCGACGAATCATTGGTCAGCCGTCAGCCGGTCAGCCGAATTCAGCCGGTGACGTCAGCCGATTCAGCCGCCTTCAGCCGTCCTCAGCCGTCAGCCGGTCAGCCGTCCTCAGCCGCCCTATCAGCCGTCAGCCGAGAATGTCAGCCGCACTTAATCAGCCGTAGCGGTTCAGCCGATCAGCCGCAGTGTCAGCCGCTCAGCCGT', 'TCAGCCGTC'))



#10 Consensus and Profile
'''
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
----------------------------
Sample Dataset: 
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample Output:
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''

def read_FASTA(file_path):
  '''
  Input a fasta file
  Returns a list of strings
  '''
  #import the txt file
  f = open(file_path,'r') 
  flines = f.readlines()

  dnaSeqs = []

  for line in flines:
    line = line.rstrip()
    #ignorn the line that starts
    if line[0] == '>': 
      continue
    else:
      dnaSeqs.append(line.rstrip('\n')) 
  return dnaSeqs

#test with sample

file_path = 'sample.txt'
read_FASTA(file_path)

#the function works! 

def profileMatrix(dnaSeqs):

  '''
  Input a list of dna sequences
  Return a matrix
  '''
  A = []
  C = []
  G = []
  T = []

  for seq in dnaSeqs: 
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    for i in range(len(seq)):
      if seq[i] == 'A': 
        A_count += 1
      elif seq[i] == 'C': 
        C_count += 1
      elif seq[i] == 'G': 
        G_count += 1
      elif seq[i] == 'T': 
        T_count += 1
    A.append(A_count)
    C.append(A_count)
    G.append(A_count)
    T.append(A_count)
  
  profile_matrix = {'A': A, 'C': C, 'G': G, 'T': T }
  return profile_matrix


print(read_FASTA(file_path))
print(profileMatrix(read_FASTA(file_path)))