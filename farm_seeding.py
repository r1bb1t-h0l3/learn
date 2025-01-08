# Identify cows that care about pasture
def read_cows(input_file, num_cows):
    """
    input_file is a file open for reading; cow information is next to read.
    num_cows is the number of cows in the file.

    Read the cows' favorite pastures from input_file.
    Return a list of each cow's two favorite pastures;
    each value in the list is a list of two values giving the
    favorite pastures for one cow.
    """
    favourites = []
    for i in range(num_cows):
        lst = input_file.readline().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favourites.append(lst)
    return favourites


def cows_with_favourite(favourites, pasture):
    """
    favourites is a list of favourite pastures, as returned by read_cows.
    pasture is a pasture number.

    Return a list of cows that care about pasture.
    """
    cows = []
    for i in range(len(favourites)):
        if favourites[i][0] == pasture or favourites[i][1] == pasture:
            cows.append(i)
    return cows


def types_used(favourites, cows, pasture_types):
    """
    favourites is a list of favourite pastures, as returned by read_cows.
    cows is a list of cows.
    pasture_types is a list of grass types.

    Return a list of the grass types already used by cows.
    """
    used = []
    for cow in cows:
        pasture_a = favourites[cow][0]
        pasture_b = favourites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used

def smallest_available(used):
    """
    used is a list of used grasss types.

    Retun the smallest-numbered grass type that is not in used.
    """
    grass_type = 1
    while grass_type in used:
        grass_type += 1
    return grass_type

def write_pastures(output_file, pasture_types):
    """
    output_file is a file open for writing
    pasture_types is a list of integer grass types.

    Output pasture_types to output_file.
    """
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    output_file.write(output + '\n')

# Main Program

input_file = open("revegetate.in", "r")
output_file = open("revegetate.t", "w")

# Read input
lst = input_file.readline().split()
num_pastures = int(lst[0])
num_cows = int(lst[1])
favourites = read_cows(input_file, num_cows)

pasture_types = [0]

for i in range(1, num_pastures + 1):

    # Identify cows that care about passture
    cows = cows_with_favourite(favourites, i)

    # Eliminate grass types for pasture
    eliminated = types_used(favourites, cows, pasture_types)

    # Choose smallest-numbered grass type for pasture
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

 # Write output
pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()
