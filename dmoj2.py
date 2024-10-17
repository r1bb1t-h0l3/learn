#51 Rue's Rings ecoo18r1p2

for dataset in range(1):

    routes = []

    number_of_routes = int(input())
    for _ in range(number_of_routes):
        route_info = list(map(int, input().split()))
        route_id = route_info[0]
        min_r = min(route_info[2:])

        routes.append((route_id, min_r))

    min_diameter = 71
    for i in range(len(routes)):
        if routes[i][1] < min_diameter:
            min_diameter = routes[i][1]

    route_number = []
    for i in range(len(routes)):
        if min_diameter == routes[i][1]:
            route_number.append((routes[i][0]))

        
    route_number.sort()
    str_sorted_routes = list(map(str, route_number))
    answer = '{' + ', '.join(str_sorted_routes)+'}'
    print(f"{min_diameter} {answer}")

