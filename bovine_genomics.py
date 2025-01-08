with open('cownomics.in', 'r') as input_file:
    N, M = map(int, input_file.readline().strip().split())

    spotty_genomes = [input_file.readline().strip() for _ in range(N)]
    plain_genomes = [input_file.readline().strip() for _ in range(N)]

good_columns = 0

for i in range(M):
    set_spotty = {genome[i] for genome in spotty_genomes}
    set_plain = {genome[i] for genome in plain_genomes}
    
    if set_spotty.isdisjoint(set_plain):
        good_columns += 1

with open('cownomics.out', 'w') as output_file:
    output_file.write(str(good_columns))

