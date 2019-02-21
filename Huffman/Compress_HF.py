frq_cha = {}
bit_ascii = {}
file_read = open("quijote.txt","r", encoding="utf8").read()
for c in file_read:
    try:
        frq_cha[c] += 1
    except KeyError:
        frq_cha[c] = 1
hf_alph = frq_cha.fromkeys(frq_cha,'')
huff_temp = [list(item) for item in frq_cha.items()]
while len(huff_temp)>1:
    huff_temp = sorted(huff_temp, key=lambda x: x[1])
    for i in [0,1]:
        for l in huff_temp[1-i][0]:
            hf_alph[l] = str(i) + hf_alph[l]
        huff_temp[1][i] += huff_temp[0][i]
    huff_temp.pop(0)
for x in range(256):
    bit_ascii[format(x,'08b')] = chr(x)
with open('x.bin','w') as f:
    me = ''.join(hf_alph[ch] for ch in file_read)
    plus_bits = 8 - len(me) % 8
    me +=  plus_bits * '0'
    f.write('%c%c' % (chr(len(hf_alph)),plus_bits))
    f.write(''.join('%s|%s|' % (key,value) for key,value in hf_alph.items()))
    f.write(''.join(bit_ascii[me[j:j+8]] for j in range(0,len(me),8)))
