#!/usr/bin/env python3

import matrices
class SeqPair:
    def __init__(self,seq1,seq2):
        self.seq1 = seq1
        self.seq2 = seq2
    def _create_matrices(self,matrix,gap):
        F,T = [],[]
        for i in range(len(self.seq2)+1):
            F.append([])
            T.append([])
            for j in range(len(self.seq1)+1):
                F[i].append(0)
                T[i].append('')
        for j in range(1,len(self.seq1)+1):
            F[0][j] = gap * j
            T[0][j] = "l"
        for i in range(1,len(self.seq2)+1):
            F[i][0] = F[i-1][0] + gap
            T[i][0] = "u"
        for i in range(1,len(self.seq2)+1):
            for j in range(1,len(self.seq1)+1):
                top = F[i-1][j] + gap , 1 , "u"
                left = F[i][j-1] + gap , 2 , "l"
                diagonal = F[i-1][j-1] + matrix[self.seq2[i-1],self.seq1[j-1]] , 3 , "d"
                F[i][j] , _ , T[i][j] = max(top,left,diagonal)
        return F,T
    def needleman_wunsch(self,matrix,gap):
        F,T = self._create_matrices(matrix,gap)
        aln1=""
        aln2=""
        i = len(self.seq2)
        j = len(self.seq1)
        while i!=0 or j!=0:
            if T[i][j] == "d":
                i = i-1
                j = j-1
                aln1 = self.seq1[j] + aln1
                aln2 = self.seq2[i] + aln2
            elif T[i][j] =="l":
                j = j-1
                aln1 = self.seq1[j] + aln1
                aln2 = "-" + aln2
            else:
                i = i-1
                aln1 = "-" + aln1
                aln2 = self.seq2[i] + aln2
        return aln1, aln2, F[-1][-1]
if __name__ == "__main__":
    myobj = SeqPair("TCA","TA")
    submat = matrices.SubstitutionMatrix("TTM.txt")
    print(myobj.needleman_wunsch(submat,-2))
    
    
