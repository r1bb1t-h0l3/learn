

with open('lostcow.in', 'r') as input_file:
    farmer_position, bessie_position = map(int, input_file.readline().strip().split())

current_position = farmer_position
distance = 0

for i in range(9):
    target_position = farmer_position + ((-1) ** i) * (2 ** i)
    
    if (current_position <= bessie_position <= target_position) or (current_position >= bessie_position >= target_position):
        distance += abs(current_position - bessie_position)
        
        break
    else:
        distance += abs(current_position - target_position)
        
        current_position = target_position
            
with open('lostcow.out', 'w') as output_file:
    output_file.write(str(distance))
