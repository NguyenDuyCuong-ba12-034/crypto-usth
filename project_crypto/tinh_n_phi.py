from so_nguyen_to import check_nguyen_to
import math
def get_prime_input(prompt):
    while True:
        n = int(input(prompt))
        if check_nguyen_to(n) == 'đây là số nguyên tố':
            return n
        else:
            print(f"Số {n} không phải là số nguyên tố, vui lòng nhập lại.")
q = get_prime_input('Nhập số q vào: ')
p = get_prime_input('Nhập số p vào: ')

print(f"Số nguyên tố q: {q}, Số nguyên tố p: {p}")

def tinh(q,p):
    n = q * p
    phi = (p-1)*(q-1)
    return n,phi

a = tinh(q,p)
print(a)

 