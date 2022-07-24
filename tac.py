w = open('TAC.txt', 'w')
tmp = -1
label = -1

def nextL():
    global label
    label += 1
    return "L" + str(label)

def nextR():
    global tmp
    tmp += 1
    return "r" + str(tmp)
    

def threeAddressCode(abstractSyntaxTree):
    if type(abstractSyntaxTree) is not tuple:
        return abstractSyntaxTree
    reservedToken = abstractSyntaxTree[0]

    if reservedToken == "declare_assign":
        varType = abstractSyntaxTree[1]
        varName = abstractSyntaxTree[2]
        w.write(str(varType) + " " + str(varName) + "\n")
        resValue = threeAddressCode(abstractSyntaxTree[3])
        w.write(str(varName) + "=" + str(resValue) + "\n")

    elif reservedToken == "declare":
        varType = abstractSyntaxTree[1]
        varName = abstractSyntaxTree[2]
        w.write(str(varType) + " "+  str(varName) + "\n")

    elif reservedToken == "assign":
        varName = abstractSyntaxTree[1]
        resValue = threeAddressCode(abstractSyntaxTree[2])
        w.write(str(varName) + "=" + str(resValue) + "\n")

    elif reservedToken == "operation":
        res1 = threeAddressCode(abstractSyntaxTree[1])
        op = abstractSyntaxTree[2]
        res2 = threeAddressCode(abstractSyntaxTree[3])
        currT = nextR()
        w.write(str(currT) + '=' + str(res1) + " " + str(op) + " " + str(res2) + "\n")
        return currT

    elif reservedToken == "print":
        resValue = threeAddressCode(abstractSyntaxTree[1])
        w.write("print" + " " + str(resValue) + "\n")