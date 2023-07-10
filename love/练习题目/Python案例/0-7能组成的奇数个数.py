#  求0—7所能组成的奇数个数。
def odd_number():
    count = 1
    for i in range(76543210):
        if i % 3 == 0:
            count += 1
    else:
        return count


if __name__ == '__main__':
    print(odd_number())
