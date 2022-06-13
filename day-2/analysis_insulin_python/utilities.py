import re
# e_file="preproinsulin-seq.txt"
# text=open(e_file);
# new_text=text.read();
# print(new_text)


# get list file
# with open('preproinsulin-seq.txt') as f:
#     lines = f.readlines()


# new_seq=insulin_seq.replace(" ","");
# print("--------")
# print(new_seq)

s1 = re.sub("[ 16]", "", insulin_seq)
print("--------")
print(s1)


print("Original String:", sample_string)

# using regex expression
final_string = re.sub('[^A-Za-z0-9]+', '', sample_string)

# print final sample string
print("Final String:", sample_string)


special_characters = ['!', '#', '$', '%', '&', '@', '[', ']', ' ', ']', '_']


# infile = "preproinsulin-seq.txt"
# outfile = "preproinsulin-seq-clean.txt"
# delete_list = ["ORIGIN", "1", "61", "//", " "]
# with open(infile) as sourc, open(outfile, "w+") as target:
#     for line in sourc:
#         for word in delete_list:
#             line = line.replace(word, "")
#             target.write(line)

# print(target)
