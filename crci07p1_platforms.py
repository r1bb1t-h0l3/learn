#!/opt/homebrew/bin/python3

def read_input():
    platform_num = int(input())
    platform_coordinates = []

    i = 0
    while i < platform_num:
        coordinates = list(map(int, input().split(" ")))
        platform_coordinates.append(coordinates)
        i += 1
    
    platform_coordinates.sort(reverse=True)

    return platform_coordinates

def support_coordinate(platfrom_coordinates: list) -> list:
    left_support = platfrom_coordinates[1] + 0.5
    right_support = platfrom_coordinates[2] - 0.5
    return [left_support, right_support]

# calculate pillar length for platform 
def touch_platform(support_coordinate: float, platform_coordinates: list) -> bool:
    return support_coordinate >= platform_coordinates[1] and support_coordinate <= platform_coordinates[2]
     
def pillar_support_len(platform_number: int, platform_array: list) -> int:
    left_pillar = -1
    right_pillar = -1

    current_platform = platform_array[platform_number]
    current_pillar_coord = support_coordinate(current_platform)
    for i in range(platform_number + 1, len(platform_array)):
        platform = platform_array[i]
        if left_pillar == -1 and touch_platform(current_pillar_coord[0], platform):
            left_pillar = current_platform[0] - platform[0]
        if right_pillar == -1 and touch_platform(current_pillar_coord[1], platform):
            right_pillar = current_platform[0] - platform[0]
    if left_pillar == -1:
        left_pillar = current_platform[0]
    if right_pillar == -1:
        right_pillar = current_platform[0]

    return left_pillar + right_pillar

def main():
    platforms = read_input()
    total_length = 0
    for i in range(len(platforms)):
        total_length += pillar_support_len(i, platforms)
    
    print(int(total_length))

main()


        



        
        


    

