# N - number of times per day
# nM - number of months


# SECONDS = 21

# N, nM = 7, 9

# def wash_hands(N, nM):
#     total_seconds = SECONDS * N * 30 * nM
#     total_minutes = total_seconds // 60
#     leftover_seconds = total_seconds % 60
#     return total_minutes, leftover_seconds

# result = wash_hands(N, nM)
# print(f"{result[0]} minutes and {result[1]} seconds")


# -----------------------
# Validate Pin

# Create a function to test if a string is a valid pin or not.

# A valid pin has:

#     Exactly 4 or 6 characters.
#     Only numerical characters (0-9).
#     No whitespace.
pin = '    '

def valid(pin:str) -> bool:
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False
    
pin_validity = valid(pin)
print(pin_validity)