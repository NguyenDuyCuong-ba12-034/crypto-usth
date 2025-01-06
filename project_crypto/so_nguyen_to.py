def check_nguyen_to(n):
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                return "đây không phải số nguyên tố"
        return "đây là số nguyên tố"
    elif n == 2:
        return "2 là số nguyên tố"
    else:
        return "Số không hợp lệ"  # Handle numbers less than 2


