# First solution, doesn't pass test caases where the same name is used more than once

# number_of_contestants = int(input())

# contestants = set()
# for i in range(number_of_contestants):
#     contestant = input().strip()
#     contestants.add(contestant)

# finishers = set()
# for i in range(number_of_contestants - 1):
#     finisher = input().strip()
#     finishers.add(finisher)

# difference = contestants - finishers
# if len(difference) == 1:
#     print(difference.pop())


def find_non_finisher(registered: list[str], finished: list[str]):
    name_counts = {}

    for name in registered:
        name_counts[name] = name_counts.get(name, 0) + 1

    for name in finished:
        name_counts[name] -= 1

    for name, count in name_counts.items():
        if count == 1:
            return name    

number_of_contestants = int(input())
registered = [input().strip() for _ in range(number_of_contestants)]
finished = [input().strip() for _ in range(number_of_contestants - 1)]

print(find_non_finisher(registered, finished))