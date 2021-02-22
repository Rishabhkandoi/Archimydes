def take_input():
    m = int(input("M: "))
    n = []
    for input_m in range(m):
        n.append(list(map(int, input("Input Numbers(N): ").split(","))))
    return m, n


def process_numbers(n):
    i, j = 0, 1
    if len(n) > 1:
        while True:
            n[i], n[j] = repeated_subtraction(n[i], n[j])
            if check_all_nos_equal(n):
                break
            i, j = i+1, j+1
            continue
        if not check_all_nos_equal(n):
            process_numbers(n)
    print(n)


def check_all_nos_equal(arr):
    return all(cur == arr[0] for cur in arr)


def repeated_subtraction(a, b):
    if a == b:
        return a, b
    elif a > b:
        return repeated_subtraction(a-b, b)
    else:
        return repeated_subtraction(a, b-a)


if __name__ == '__main__':
    m, n = take_input()
    for numbers in range(m):
        process_numbers(n[numbers])
