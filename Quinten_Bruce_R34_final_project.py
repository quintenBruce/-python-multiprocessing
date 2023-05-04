from math import sqrt
from multiprocessing import Pool
import argparse
import os.path

#
# Written by: Quinten Bruce (R11703344)
#

p = {0: 0, 1: 0, 2: 1, 3: 1, 4: 0, 5: 1, 6: 0,
     7: 1, 8: 0}  # prime number dictionary


def multiProc(arr):
    l = len(arr[1])
    w = arr[0][0]
    new_grid = [[0]*w for i in range(l-2)]

    # iterate over subgrid, assign new cell status to
    for i in range(1, l-1):
        above = arr[1][i-1][0:w]
        inline = arr[1][i][0:w]
        below = arr[1][i+1][0:w]
        for j in range(w):
            living_neighbors = 0
            right = (j+1) % w
            left = (j-1) % w
            neighbors = [above[left],
                         above[j],
                         above[right],
                         inline[right],
                         below[right],
                         below[j],
                         below[left],
                         inline[left]]

            living_neighbors = sum(neighbors)

            if (inline[j] == 1):
                new_grid[i-1][j] = p[living_neighbors]
            else:
                new_grid[i-1][j] = 1 if living_neighbors % 2 != 0 else 0
    return new_grid


def main():
    print("Project :: R11703344")

    # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action="store", dest="inputFile")
    parser.add_argument('-o', action="store", dest="outputFile")
    parser.add_argument('-p', action="store",
                        dest="PROCESSES", type=int, default=1)
    parser.add_argument('-t', action="store",
                        dest="PROCESSES2", type=int, default=1)
    args = parser.parse_args()

    # Get # of max processes to spawn
    PROCESSES = args.PROCESSES
    if PROCESSES < 1:
        PROCESSES = 1
    if args.PROCESSES2 > 1:
        PROCESSES = args.PROCESSES2

    grid = []
    # read input file into grid array
    if os.path.isfile(args.inputFile):
        with open(args.inputFile, "r") as f:
            grid = f.readlines()
    else:
        print("input file does not exist")
        sys.exit(1)

    l = len(grid)
    w = len(grid[0])-1
    k = l // PROCESSES
    p = l % PROCESSES
    lminp = l - p

    # change string grid to integer grid. integer comparisons are faster than character comparisons
    grid = [list([0 if row[j] == '.' else 1 for j in range(w)])
            for row in grid]

    processPool = Pool(processes=PROCESSES)

    # Run 100 iteratins of the algorithm
    for j in range(100):
        poolData = []
        i = 0
        # slice array into chunks
        for i in range(k, lminp, k):
            data = [[w]]
            data.append(grid[(i-k):i])
            data[1].insert(0, grid[(i-k-1) % l])
            data[1].append(grid[i % l])
            poolData.append(data)

        data = [[w]]
        data.append(grid[i:l])
        data[1].insert(0, grid[(i-1) % l])
        data[1].append(grid[0])
        poolData.append(data)

        newGrid = processPool.map(multiProc, poolData)
        del poolData  # free memory

        # reassign grid to contain new rows
        for t in newGrid:
            for array in t:
                del grid[0]
                grid.append(array)

    # convert integer grid back to char grid
    grid = [['.' if row[j] == 0 else 'O' for j in range(w)] for row in grid]

    with open(args.outputFile, "w") as txt_file:
        for row in grid:
            txt_file.write("".join([str(x) for x in row])+"\n")


if __name__ == '__main__':
    main()

#
# Acknowledgment: This is program is written to be efficient, not necessarily
# readable. I chose efficiency over readability in mnost cases.
#
