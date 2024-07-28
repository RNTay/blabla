#!/usr/bin/env python3

from itertools import combinations
from datetime import datetime


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def ex(n, d, L):
    lower_bound = 1
    upper_bound = (2 ** (n - d)) * L

    cube = []
    for number in range(0, 2**n):
        vertex = [0 for _ in range(n)]
        for i in range(n):
            vertex[i] = number % 2
            number = number // 2
        cube.append(vertex)

    best_code_size = lower_bound
    best_code = []

    print("Will search for codes of sizes " + str(lower_bound) + " to " + str(upper_bound))
    print("="*100)
    for code_size in range(lower_bound, upper_bound + 1):
        print("Currently searching for a (n=" + str(n) + ", d=" + str(d) + ", L=" + str(L) + ") "  "code of size " + str(code_size))
        code_size_found = False
        for subset in combinations(cube, code_size):

            subset = list(subset)

            if [0]*n not in subset:
                continue

            subset_is_a_code = True

            # generate subcubes from the lowest vertex
            for lowest_vertex_number in range(0, 2 ** n):

                # the lowest vertex of the subcube
                lowest_vertex = [0 for _ in range(n)]
                for i in range(n):
                    lowest_vertex[i] = lowest_vertex_number % 2
                    lowest_vertex_number = lowest_vertex_number // 2

                # find all the zeros, and disregard the point if there are less than d zeros
                zeros_indices = [i for i, x in enumerate(lowest_vertex) if x == 0]
                if len(zeros_indices) < d:
                    continue

                # generate subcubes with this lowest vertex
                for zeros_indices_choices in combinations(zeros_indices, d):
                    subcube = [lowest_vertex]

                    for _ in range(d):
                        for vertex in subcube:
                            for i in zeros_indices_choices:
                                if vertex[i] == 0:
                                    new_vertex = [x for x in vertex]
                                    new_vertex[i] = 1
                                    if new_vertex in subcube:
                                        continue
                                    else:
                                        subcube.append(new_vertex)

                    if len(intersection(subcube, subset)) > L:
                        subset_is_a_code = False
                        break
                if not subset_is_a_code:
                    break

            if subset_is_a_code:
                print("     success")
                best_code_size = code_size
                best_code = subset
                code_size_found = True
                break

        if not code_size_found:
            print("     failed")
            break

    print("="*100)
    print("ex("+str(n) + ", " + str(d) + ", " + str(L) + ") = " + str(best_code_size))
    print("best code: ")
    print(best_code)
    print("="*100)


n = 5
d = 3
L = 1
start_time = datetime.now()
ex(n, d, L)
print("Time elapsed: ", datetime.now() - start_time)
