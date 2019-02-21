ascii_bits = {}
bits_ascii = {}
lz_alph = {'':format(0,'020b')}
for x in xrange(256):
    ch = chr(x)
    bn = format(x,'08b')
    ascii_bits[ch] = bn
    bits_ascii[bn] = ch
with open('quijote.txt','r') as file_char:
    bits_input = ''.join(ascii_bits[char] for char in file_char.read())
me_encoded = []
s = ''
for c in bits_input:
    if s+c in lz_alph:
        s += c
    else:
        lz_alph[s+c] = format(len(lz_alph),'020b')
        me_encoded.append(lz_alph[s] + c)
        s = ''
if s is not '':
    me_encoded.append(lz_alph[s])
with open('compress.bin','w') as f:
    me = ''.join(me_encoded)
    add = len(me)%8
    me = me[add:]
    f.write(str(add))
    f.write(''.join(bits_ascii[me[i:i+8]] for i in xrange(0,len(me),8)))
