def Printnum(A):

    if A == 1:
        print(1)
        return 1

    Printnum(A-1)
    print(A)

print(Printnum(A= int(input())))
