with open('angry.in', 'r') as input_file:
    n = int(input_file.readline().strip())
    bales = [int(input_file.readline().strip()) for _ in range(n)]

bales.sort()

explosions = 0
for i in range(len(bales)):
    distance = 1
    counter = 0
    while bales[i + counter + distance] <= len(bales):
        explosions += 1
        print(f'{i}: {explosions}')
        counter += 1

print(explosions)
    
