import time
lemziv = {format(0,'020b'):''}
ascii_bit = {}
ibasci = {}
for x in xrange(256):
    ch = chr(x)
    bi = format(x,'08b')
    ascii_bit[ch] = bi
    ibasci[bi] = ch
with open('compress.bin') as f:
    add = int(f.read(1))
    code = ''.join(ascii_bit[ch] for ch in f.read())
    code = add * '0' + code
t = []
k = 0
for x in xrange(0,len(code)-20,21):
    c = code[x:x+20]
    n = code[x+20]
    prior = lemziv[c]
    k+=1
    lemziv[format(k,'020b')] = prior+n
    t.append(prior+n)
t.append(lemziv[code[x+21:x+41]])
with open('recover.txt','w') as r:
    me = ''.join(t)
    start_time = time.clock()
    r.write(''.join(ibasci[me[i:i+8]] for i in xrange(0,len(me),8)))
