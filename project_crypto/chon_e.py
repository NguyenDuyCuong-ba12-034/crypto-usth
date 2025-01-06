from tinh_n_phi import a
import math
import random

n,phi = a
def find_e(phi):
    lst = []
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            lst.append(e)
    if not lst:
        print("Không tìm thấy giá trị e thỏa mãn.")
    return lst

b = find_e(phi)
# print(b)
# Select a random item
random_e = random.choice(b)
print('số e được chọn là: ',random_e)

