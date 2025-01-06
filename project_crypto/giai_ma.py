from list_khoa import public_key,private_key

list_giai_ma = []

with open('cypher.txt','r') as f:
    for line in f:
        a = int(line)
        print(a)
        list_giai_ma.append((a**private_key[0])%private_key[1])

print(list_giai_ma)

with open('giai_ma.txt', 'w') as f:
    for cipher in list_giai_ma:
        f.write(str(cipher) + '\n')