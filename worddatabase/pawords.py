f=open('words.txt')
def g(s):
	flag = True
	for a in s:
		#print ord('a'),ord(a),ord('z')
		if ord('a')>ord(a) or ord('z')<ord(a):
			
			flag = False

	return flag
F=open('WWords.txt','w')
n=0
for i in f:
    for j in i.split():
	    if g(j.strip()):
		    F.write(j+'\n')
		    n+=1
print n
F.close()