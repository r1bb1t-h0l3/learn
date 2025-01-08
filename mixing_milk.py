
# input_file = open('mixmilk.in', 'r')
# output_file = open('mixmilk.out', 'w')

# lines = input_file.readlines()

# capacity_a, amount_a = map(int, lines[0].split())
# capacity_b, amount_b = map(int, lines[1].split())
# capacity_c, amount_c = map(int, lines[2].split())

# counter = 0

# while counter < 100:
#     if (amount_a + amount_b) <= capacity_b:
#         new_amount_b = amount_a + amount_b
#         new_amount_a = 0
#         amount_a = new_amount_a
#         amount_b = new_amount_b
#         counter += 1
#     else:
#         new_amount_b = capacity_b
#         new_amount_a = amount_a - capacity_b
#         amount_a = new_amount_a
#         amount_b = new_amount_b
#         counter += 1

#     if counter >= 100:
#         break

#     if (amount_b + amount_c) <= capacity_c:
#         new_amount_c = amount_b + amount_c
#         new_amount_b = 0
#         amount_c = new_amount_c
#         amount_b = new_amount_b
#         counter += 1
#     else:
#         new_amount_c = capacity_c
#         new_amount_b = amount_b - capacity_c
#         amount_b = new_amount_b
#         amount_c = new_amount_c
#         counter += 1

#     if counter >= 100:
#         break

#     if (amount_a + amount_c) <= capacity_a:
#         new_amount_a = amount_a + amount_c
#         new_amount_c = 0
#         amount_a = new_amount_a
#         amount_c = new_amount_c
#         counter += 1
#     else:
#         new_amount_a = capacity_a
#         new_amount_c = amount_c - capacity_a
#         amount_a = new_amount_a
#         amount_c = new_amount_c
#         counter += 1

# output_file.write(f"{amount_a}\n")
# output_file.write(f"{amount_b}\n")
# output_file.write(f"{amount_c}")

# input_file.close()
# output_file.close()


# # Read input from the file
# with open("mixmilk.in", "r") as input_file:
#     bucket_1 = list(map(int, input_file.readline().split()))  # [capacity, milk]
#     bucket_2 = list(map(int, input_file.readline().split()))  # [capacity, milk]
#     bucket_3 = list(map(int, input_file.readline().split()))  # [capacity, milk]

# # Buckets array for easy access
# buckets = [bucket_1, bucket_2, bucket_3]

# # Simulate 100 pours
# for i in range(100):
#     current_bucket = i % 3
#     next_bucket = (i + 1) % 3
    
#     # Amount to pour is the minimum of the milk in the current bucket and the remaining space in the next bucket
#     pour_amount = min(buckets[current_bucket][1], buckets[next_bucket][0] - buckets[next_bucket][1])
    
#     # Adjust the milk amounts in the current and next bucket
#     buckets[current_bucket][1] -= pour_amount
#     buckets[next_bucket][1] += pour_amount

# # Write output to the file
# with open("mixmilk.out", "w") as output_file:
#     for bucket in buckets:
#         output_file.write(f"{bucket[1]}\n")

with open('mixmilk.in', 'r') as input_file:
    bucket_1 = list(map(int, input_file.readline().split()))
    bucket_2 = list(map(int, input_file.readline().split()))
    bucket_3 = list(map(int, input_file.readline().split()))

buckets = [bucket_1, bucket_2, bucket_3]

for i in range(100):
    current_bucket = i % 3
    next_bucket = (i + 1) % 3

    pour_amount = min(buckets[current_bucket][1], buckets[next_bucket][0] - buckets[next_bucket][1])

    buckets[current_bucket][1] -= pour_amount
    buckets[next_bucket][1] += pour_amount

with open('mixmilk.out', 'w') as output_file:
    for bucket in buckets:
        output_file.write(f"{bucket[1]}\n")