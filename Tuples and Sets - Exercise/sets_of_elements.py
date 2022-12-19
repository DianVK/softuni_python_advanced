number_n,number_m = input().split()
n_numbers = set(int(input()) for n in range(int(number_n)))
m_numbers = set(int(input()) for m in range(int(number_m)))
unique_numbers = n_numbers & m_numbers
print(*unique_numbers,sep="\n")