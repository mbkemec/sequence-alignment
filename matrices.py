#!/usr/bin/env python3

class SubstitutionMatrix:
    def __init__(self,filename):
        '''
        dictionary of dictionaries
            keys: nucleotide
            values: dictionary
                keys: nucleotide
                values: numbers
        '''
        with open(filename) as reader:
            
            line = reader.readline() #just read the first line, bc of the format of file
            characters = line.strip().split()
            self.values = {}
            for char in characters:
                self.values[char] = {}

            for line in reader:
                splitted_line = line.strip().split() # put all values in a list
                #print(splitted_line)
                char1 = splitted_line[0]
                #self.values[char1]
                for i in range(1,len(splitted_line)):
                    self.values[char1][characters[i-1]] = float(splitted_line[i])
    
    def __getitem__(self,key):
        key1, key2 = key
        return self.values[key1][key2]



# if we insert __getitem__ function in class, we can use [] for our object !!!!

if __name__ == "__main__":
    matrix = SubstitutionMatrix("TTM.txt")
    print(matrix["A","T"]) 
          # otherwise we should write: print(matrix.get_value("A","T"))
          
