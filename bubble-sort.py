

def bubble_sort(lst_n):
    oper_count = 0
    swap = 1
    counter = 1
    while swap > 0:
        swap = 0
        for i in range(len(lst_n) - counter):
            oper_count += 1
            
            if lst_n[i] > lst_n[i+1]:
                tmp = lst_n[i+1]
                lst_n[i+1] = lst_n[i]
                lst_n[i] = tmp
                swap  += 1
        counter += 1

    print(f"operations: {oper_count}")

    return lst_n


n = input().split(" ")
lst_n = list(map(int, n))
print(bubble_sort(lst_n))

