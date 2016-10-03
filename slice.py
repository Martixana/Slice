fname = raw_input ('Enter a file name:')
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        slc_line = line[0:20]
        slc_2 = line[20:]
        print slc_2
        
