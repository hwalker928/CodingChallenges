# Task 19 - Logic Gate

import sys

validLogicGates = ["AND", "OR", "XOR", "NAND", "NOR"]

logicGate = input("Enter logic gate: ")
if not logicGate in validLogicGates:
    print("Invalid logic gate!")
    print("Valid options:", ", ".join(validLogicGates))
    sys.exit()


def base2ToBool(intValue: int):
    return [False, True][intValue]


input1 = base2ToBool(int(input("Enter 0 or 1: ")))
input2 = base2ToBool(int(input("Enter 0 or 1: ")))

if logicGate == "AND":
    output = input1 == input2 and input1 == True
elif logicGate == "OR":
    output = input1 or input2
elif logicGate == "XOR":
    output = input1 and not input2 or input2 and not input1
elif logicGate == "NAND":
    nand = input1 == input2 and input1 == True
    output = not nand
elif logicGate == "NOR":
    output = not input1 or input2

print(output)
