from asyncore import write
import re

source_file = open("preproinsulin-seq.txt", "r+")
filteredFile = "preproinsulin-seq-clean.txt"
insIs = "lsinsulin-seq-clean.txt"
insA = "ainsulin-seq-clean.txt"
insB = "binsulin-seq-clean.txt"
insC = "cinsulin-seq-clean.txt"


data = source_file.read()
clean_file = re.sub("[^a-z]", "", data)

# with open(filteredFile, 'w') as t:
#     t.write(clean_file)

# with open(insIs, 'w') as t:
#     t.write(clean_file[0:24])

# with open(insB, 'w') as t:
#     t.write(clean_file[25:54])

# with open(insC, 'w') as t:
#     t.write(clean_file[55:89])

# with open(insA, 'w') as t:
#     t.write(clean_file[89:110])


def strmaker (arg,x,y ):
    a = clean_file[x:y]
    text = open(arg,'w')
    text.write(a)
    text.close()
    print(a)
    print(len(a))
    
strmaker(filteredFile,0,-1) 
strmaker(insIs,0,24)  
strmaker(insB,25,54) 
strmaker(insC,54,89)  
strmaker(insA,90,110)  