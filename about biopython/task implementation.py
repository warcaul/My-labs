from Bio.SeqIO import parse 
from Bio.Seq import Seq 
from Bio.SeqUtils import GC 
from Bio.Seq import transcribe
from Bio.Seq import translate

file = open("sequence.fasta") 
answer = open('звіт.txt', 'w')
s = parse(file, "fasta") 
for record in s:  
    cut = record.seq[0:119] 
    print ("зріз послідовності з файлу (з 1-го елементу по 120 елемент): " , cut)
    cut_c = cut.complement()
    print ("комплементарну послідовність зрізу: " , cut_c)
    cut_cr = cut.reverse_complement()
    print ("обернену комплементарну послідовність зрізу: " , cut_cr)
    print("розрахувати GC% вміст зрізу :" ,  GC(cut))
    cut_trb = cut.transcribe()
    print("вивести транскрибовану послідовність зрізу :" , cut_trb)
    cut_trl = cut_trb.translate()
    print ("вивести трансльовану послідовність з транскрибованої послідовності зрізу :" , cut_trl)
    cut_trl2 = cut.translate()
    print("вивести трансльовану послідовність з послідовності зрізу ДНК" , cut_trl2 )

