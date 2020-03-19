# Use the file name mbox-short.txt as the file name
import re
fname =  "regex_sum_218682.txt" #input("Enter file name: ")
fh = open(fname)
count = 0
sum_num = 0
for line in fh:
    num_s = re.findall('[0-9]+', line)
    for idx in num_s:
        sum_num += int(idx)
        count += 1
    #print int(num_s)
    #print sum(num_s)

print ("Sum ", sum_num, "\n", "count", count)
