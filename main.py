universal_genetic_code = '/Users/sriveerisetti/Desktop/Boston_University/BF_527/Labs/Lab_13/universal_genetic_code.tab'

def analyze_sequence(universal_genetic_code):
    with open(universal_genetic_code, 'r') as genetic_code:
        sequence = genetic_code.read()
    #Here we want to replace anywhere we see a "\t" or "\n" with a space    
    sequence = sequence.replace("\t", " ")
    sequence = sequence.replace("\n", " ")
    return(sequence)

#Here we are reading in the original DNA sequence 
mRNA_string = analyze_sequence('/Users/sriveerisetti/Desktop/Boston_University/BF_527/Labs/Lab_13/dna.fasta')
print(mRNA_string)

#We did all of the previous work in order to make this. This is our dictionary with the codons and their 
#corresponding amino acids
amino_acid_dictionary = {
    'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGA':'R', 'AGC':'S',
    'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L',
    'CTG':'L', 'CTT':'L', 'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GGA':'A', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAA':'*', 'TAC':'Y',
    'TAG':'*', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TGA':'*', 'TGC':'C', 'TGG':'W', 'TGT':'C',
    'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F',  
       
}

amino_acid_sequence = ""

#Here we are asking the function to go through the mRNA sequence from the first nucleotide to the last in i
#incriments of 3
for amino_acid in range(0, len(mRNA_string), 3):
    #Here we are saying that whatever the first nucleotide is, we want it + the next two nucleotides, which is why 
    #we add 3
    three_letter_codon = mRNA_string[amino_acid:amino_acid + 3]
    #Here we are going to pass the three_letter_codon through the dictionary and append any matches to 
    #the "amino_acid_sequence" variable which was defined outside the for loop
    Temp = amino_acid_dictionary.get(three_letter_codon)
    amino_acid_sequence += str(Temp) 

#Here we are printing out the amino acid sequence  
print(amino_acid_sequence)
