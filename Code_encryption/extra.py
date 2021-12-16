def F(l, key):
	return (l*l + l*key + key*key)
word = "Hello_EP"
l = []
r = []
for i in range(0, 4):
	l.append(ord(word[i]))
for i in range(4, 8):
	r.append(ord(word[i]))
print (l)
print (r)
L0 = l[0] ^ (l[1] << 8) ^ (l[2] << 16) ^ (l[3] << 24)
R0 = r[0] ^ (r[1] << 8) ^ (r[2] << 16) ^ (r[3] << 24)
L = []
R = []
L.append(L0)
R.append(R0)
#print L0, R0
for i in range(0, 32):	
	R.append(L[i]) 
	L.append(R[i] ^ F(L[i], i)) 
for i in range(31, -1, -1):
	L[i] = R[i + 1]
	R[i] = L[i + 1] ^ F(R[i + 1], 1)
print ("END")
for j in range(0, 4):
	l[j] = L[0] % 256
	L[0] = L[0] >> 8
for j in range(0, 4):
	r[j] = R[0] % 256
	R[0] = R[0] >> 8
	
print (l)
print (r)