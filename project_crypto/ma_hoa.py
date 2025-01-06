from list_khoa import public_key, private_key

list_ma = []

# Mở file và đọc nội dung
with open('plain.txt', 'r') as f:
    for line in f:
        # Tách các số trong dòng
        numbers = line.split()
        for num in numbers:
            a = int(num)  # Chuyển đổi từng số sang số nguyên
            # Mã hóa từng số và thêm vào danh sách
            list_ma.append((a ** public_key[0]) % public_key[1])

print(list_ma)
with open('cypher.txt', 'w') as f:
    for cipher in list_ma:
        f.write(str(cipher) + '\n')  # Ghi mỗi số trên một dòng
