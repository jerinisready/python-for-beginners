#     *         4x1
#    ***        3x3
#   *****       2x5
#  *******      1x7
# *********     0x9
#  *******      1x7
#   *****       2x5
#    ***        3x3
#     *         4x1

space = " "
star  = "*"
start, stop = 1, 5

for i in range(start, stop+1):
    print space * (stop-i), star * (2*i-1)

for i in range(stop-1, start-1, -1):
    print space * (stop-i), star * (2*i-1)
