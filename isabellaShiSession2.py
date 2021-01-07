#Isabella Shi Session 2


#5 Computing GC Content
'''
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated. 

Sample Dataset: 
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output: 
Rosalind_0808
60.919540
'''
#find the percentage of GC in a DNA sequence
def GCcontent(dnaSeq):
  #count G and C
  Gcount = dnaSeq.count('G')
  Ccount = dnaSeq.count('C')
  totalCount = len(dnaSeq)
  GCpercentage = (int(Ccount) + int(Gcount))/totalCount
  GC_content = GCpercentage * 100
  return GC_content


#borrowed this from lab 2 :)
def read_FASTA(file_path):

  #import the txt file
  f = open(file_path,'r') 
  flines = f.readlines()

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
  
  return dictFASTA


#turn the fasta file into a dictionary
file_path = 'rosalind_gc.txt'
dictDNA = read_FASTA(file_path)
list_dnaSeq = dictDNA.values()
for dnaSeq in list_dnaSeq:
  percentage = GCcontent(dnaSeq)
  print(percentage)
