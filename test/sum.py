def sum(a, b):
    mx, mask = 0x7FFFFFFF, 0xFFFFFFFF
    while b:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a <= mx else ~(a ^ mx)

print(sum(1, 3))