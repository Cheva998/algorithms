# Use the file name mbox-short.txt as the file name
fname =  input("Enter file name: ") # "mbox-short.txt" #
fh = open(fname)
count = 0
sum_num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    num_str = line[line.strip().find(":")+2:]
    num_flo = float(num_str)
    sum_num += num_flo
prom = sum_num / count
print ("Average spam confidence:", prom)
