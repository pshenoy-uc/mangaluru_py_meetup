#!/usr/bin/python

def Tic_Tac_Toe(result):
    # straight sum
    for row in result:
        if all(row):
            print True
            return
        elif all([not col for col in row]):
            print False
            return
        else:
            continue

    transpose_result = zip(*result)
    for row in transpose_result:
        if all(row):
            print True
            return 
        elif all([not col for col in row]):
            print False
            return
        else:
            if (result[0][0] + result[1][1] + result[2][2]) == 3 or (result[0][2] + result[1][1] + result[2][0]) == 3:
                print True
                return
            elif (result[0][0] + result[1][1] + result[2][2]) == 0 or (result[0][2] + result[1][1] + result[2][0]) == 0:
                print False
                return
            else:
                continue
    print "Impossible"

result = [[1, 0, 1],
        [0, 1, 0],
        [0, 1, 0]]
Tic_Tac_Toe(result)
