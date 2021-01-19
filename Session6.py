#Isabella Shi Session 6


#14 Finding a Shared Motif
'''
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
----------------------------
Sample Dataset: 
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output: AC
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
  dictFASTA = {}
  keyFASTA = None

  for line in flines:
    #key starts with >
    if line[0] == '>': 
      if keyFASTA is not None: 
        #save the previous key and value
        dictFASTA[keyFASTA] = valueFASTA
      #save a new key
      keyFASTA = line[1:].rstrip()
      #delete the space
      if keyFASTA[0] == ' ':
        keyFASTA = keyFASTA[1:]
      #an empty string to save the value
      valueFASTA = ''
    #values
    else:
      valueFASTA += line.rstrip('\n')
  dictFASTA[keyFASTA] = valueFASTA
  
  dnaSeqs = list(dictFASTA.values())
  
  return dnaSeqs


def findMotif(DNAlist): 
  #sort the list in order
  DNAlist.sort(key = len)
  
  shortestDNA = DNAlist[0]
  otherDNA = DNAlist[1:]
  motif = ''

  #for loop to look for the longest common substring
  for i in range(len(shortestDNA)):
    for j in range(len(shortestDNA) - i + 1):
      motifTest = shortestDNA[i:j + 1]
      foundMotif = False
      
      for DNA in otherDNA:
        if motifTest in DNA: 
          foundMotif = True
        else:
          foundMotif = False
      if foundMotif and len(motifTest) > len(motif):
        motif = motifTest
  
  return motif

#test
'''
seqList = read_FASTA('sample.txt')
print(findMotif(seqList))
seqList2 = ['skncdbsjkgabcgsjk', 'cdefgabcd', 'abgabcd']
print(findMotif(seqList2))
'''
#works

dnaList = read_FASTA('rosalind_lcsm.txt')
print(findMotif(dnaList))