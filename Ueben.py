from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Alphabet import generic_dna
from Bio import SeqIO


#x = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
#y = print(str(x))
#print(repr(y))


"""BIOPYTHON TUTORIAL"""


#for letter, index in enumerate(x):
    # print("%i %s" % (letter, index))
#print(len(x))

# print(repr(x[0:12]))    # repr for print string + seq type

#fasta_format_string = ">Name\n%s\n" % x
#print(fasta_format_string)

# prot = Seq("EVRNAK" , IUPAC.protein)
# dna = Seq("ATGCCC" , IUPAC.unambiguous_dna)
# print(str(prot) + str(dna))




# for e in SeqIO.parse("hans.fasta", "fasta"):    #Import Fasta sequences (SeqIO required)
#     print(e)


dnas = Seq("ACGT", IUPAC.unambiguous_dna)
krass = (dnas.lower())
print(repr(krass))
oki = krass.complement()
print(repr(oki))



