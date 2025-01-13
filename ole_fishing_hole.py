with open('whereami.in', 'r') as input_file:
    n = int(input_file.readline().strip())

    seq = input_file.readline().strip()

k = 1

while k <= n:
    patterns = set()
    patterns_is_unique = True

    for i in range(n - k  + 1):
        substring = seq[i: i + k]
        if substring in patterns:
            patterns_is_unique = False
            break
        else:
            patterns.add(substring)
            print(substring)

        
    if patterns_is_unique:
        with open('whereami.out', 'w') as output_file:
            output_file.write(str(k))
        break

    k += 1



