from chon_e import random_e,phi

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(random_e, phi):
    gcd, x, _ = extended_gcd(random_e, phi)
    if gcd != 1:
        raise ValueError(f"Không tồn tại nghịch đảo modular của {random_e} mod {phi}")
    return x % phi
d = modular_inverse(random_e, phi)
print(f"Giá trị d (nghịch đảo modular của e mod phi): {d}")