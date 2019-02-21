hf_alph = {}
ascii_bit = {}
with open('compression.txt','rb') as f:
    ldic = ord(f.read(1))*2
    plus_bits = ord(f.read(1))
    a = f.read().split('|',ldic)
    mess = a[ldic]
for x in xrange(0,ldic,2):
    hf_alph[a[x+1]] = a[x]
for i in xrange(256):
    ascii_bit[chr(i)] = format(i,'08b')
bit_code = ''.join(ascii_bit[ch] for ch in mess)[:-plus_bits]
bits = ''
text = []
for b in bit_code:
    bits += b
    if bits in hf_alph:
        text.append(hf_alph[bits])
        bits = ''
with open("recover.txt","w") as r:
    r.write(''.join(text))
