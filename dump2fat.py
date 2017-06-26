import sys

filename = sys.argv[1:]
if not filename:
    print >> sys.stderr, "Usage: %s [file to be converted]..." % (sys.argv[0],)
    sys.exit(1)
filename = filename[0]
file = open(filename, "r")
lines = file.readlines()
code = []

for line in lines:
    words = line.split("\t")
    if (len(words) == 4):
	code.append("0x" + words[1].strip())
code_str = "{"
for instruction in code:
    code_str += instruction + ","
code_str = code_str[0:len(code_str)-1] + "}";
print code_str 

