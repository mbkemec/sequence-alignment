#!/usr/bin/env python3

import needleman_wunsch
import matrices
class SeqPair(needleman_wunsch.SeqPair):
    def __init__(self,seq1,seq2):
        super().__init__(seq1,seq2)
    def _create_local_matrices(self,matrix,gap):
        F,T = [],[]
        for i in range(len(self.seq2)+1):
            F.append([0] * (len(self.seq1)+1))
            T.append([''] * (len(self.seq1)+1))
        for i in range(1,len(self.seq2)+1):
            for j in range(1,len(self.seq1)+1):
                top = F[i-1][j] + gap , 1 , "u"
                left = F[i][j-1] + gap , 2 , "l"
                diagonal = F[i-1][j-1] + matrix[self.seq2[i-1],self.seq1[j-1]] , 3 , "d"
                zero = 0 , 4 , ''
                F[i][j] , _ , T[i][j] = max(top,left,diagonal,zero)
        return F,T
    def smith_waterman(self,matrix,gap):
        F,T = self._create_local_matrices(matrix,gap)
        aln1 = ""
        aln2 = ""
        max_score = -1
        for i in range(len(self.seq2)+1):
            for j in range(len(self.seq1)+1):
                if F[i][j] > max_score:
                    max_score = F[i][j]
                    start_i = i
                    start_j = j
        i = start_i
        j = start_j
        while T[i][j] != '':
            if T[i][j] == "d":
                i = i-1
                j = j-1
                aln1 = self.seq1[j] + aln1
                aln2 = self.seq2[i] + aln2
            elif T[i][j] == "l":
                j = j-1
                aln1 = self.seq1[j] + aln1
                aln2 = "-" + aln2
            else:
                i = i-1
                aln1 = "-" + aln1
                aln2 = self.seq2[i] + aln2
        return aln1, aln2, max_score
if __name__ == "__main__":
    myobj = SeqPair("TGA","GA")
    submat = matrices.SubstitutionMatrix("TTM.txt")
    print(myobj.smith_waterman(submat,-2))
