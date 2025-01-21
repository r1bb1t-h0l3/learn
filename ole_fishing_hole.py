def is_possible_result(integers: list[int]) -> set[int]:
    twoIntegersCombinations = set()
    for i1 in range(len(integers)):
        n1 = integers[i1]
        for i2 in range(i1, len(integers)):
            n2 = integers[i2]
            twoIntegersCombinations.add(n1 * n2)
            twoIntegersCombinations.add(n1 + n2)
        
    threeIntegersCombinations = set()
    for n in integers:
        for combination in twoIntegersCombinations:
            threeIntegersCombinations.add(n * combination)
            threeIntegersCombinations.add(n + combination)
    return threeIntegersCombinations
            
input_sets = 10

result = []

for _ in range(input_sets):
    n = int(input())
    integers = list(set(map(int, input().split())))
    targets = list(map(int, input().split()))

    combinations = is_possible_result(integers)
    current_result = []
    for target in targets:
        possible = 'T' if target in combinations else 'F'
        current_result.append(possible)

    result.append("".join(current_result))
                
print("\n".join(result))

