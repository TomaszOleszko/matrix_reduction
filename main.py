import random


def create_tab(N):
    table = []
    for n in range(3 * N):
        inner_table = []
        for i in range(3 * N):
            a = random.randint(0, 1)
            inner_table.append(a)
        table.append(inner_table)
    return table


def print_tab(table):
    for j in table:
        print("[", end=" ")
        print(' '.join(str(i) for i in j), end=" ")
        print("]", end="\n")


def tab_to_String(table):
    string = ""
    z = 0
    for i in table:
        z += 1
        k = 0
        string += "| "
        for j in i:
            string += str(j) + " "
            k += 1
            if k % 3 == 0:
                string += "| "
        string += "\n"
        if z % 3 == 0:
            string += "\n"
    return string


def reduction_with_window(table):
    result_matrix = []
    inner_matrix = []
    window_sum = 0
    row = 0
    window_count = 0
    while row < len(table):
        col = 0
        while col < len(table):
            for i in range(3):
                for j in range(3):
                    window_sum += table[i + row][j + col]
            inner_matrix.append(1) if window_sum > 4 else inner_matrix.append(0)
            window_sum = 0
            window_count += 1
            col += 3
        result_matrix.append(inner_matrix[:])
        inner_matrix.clear()
        row += 3

    print_tab(result_matrix)


n = int(input("Podaj N, N>= 6:\n"))
while n < 6:
    n = int(input("Podaj N, N>= 6:\n"))
tab = create_tab(n)
print("Tablica poczatkowa", end="\n")
print(tab_to_String(tab))
print("Tablica zredukowana")
reduction_with_window(tab)
