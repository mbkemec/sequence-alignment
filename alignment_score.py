#!/usr/bin/env python3
import needleman_wunsch
import matrices
import smith_waterman

print("!! For 'smith waterman' please write 'sw', for 'needleman wunsch' please write 'nw' !!")
type_of_alignment = input("Do you want to apply 'smith_waterman' or 'needleman_wunsch': ")

seq1 = input("Please write your first sequence: ")
seq2 = input("Please write your second sequence: ")

seq1 = seq1.upper()
seq2 = seq2.upper()

print("!! Matrix types: 'BLOSUM62.txt' , 'PAM250.txt' , 'TTM.txt' !!")
matrix_type = input("Please select your substition matrix (with file extension): ")

gap_score = int(input("Please write your 'GAP' penalty score: "))


if __name__ == "__main__":
	if type_of_alignment == "sw":
		myobj = smith_waterman.SeqPair(seq1,seq2)
		submat = matrices.SubstitutionMatrix(matrix_type)
		print(myobj.smith_waterman(submat,gap_score))
	
	if type_of_alignment == "nw":
		myobj = needleman_wunsch.SeqPair(seq1,seq2)
		submat = matrices.SubstitutionMatrix(matrix_type)
		print(myobj.needleman_wunsch(submat,gap_score))
