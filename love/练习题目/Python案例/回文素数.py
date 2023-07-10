def palindromic_primes(m):
    is_primes = []
    is_palindromic_primes = []
    for a in range(2, m):
        for b in range(2, a):
            if a % b == 0:
                break
        else:
            is_primes.append(a)
    for i in is_primes:
        if len(str(i)) > 1:
            count = len(str(i)) // 2
            if str(i)[0:count] == str(i)[-1:count:-1]:
                is_palindromic_primes.append(i)
        else:
            continue
    else:
        return is_palindromic_primes


if __name__ == '__main__':
    m_ = int(input("请输入一个整数:"))
    print(palindromic_primes(m_))