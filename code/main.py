import system
import processor
import compiler

from constants.isa import *

def main():

    compiler.Compile(filename="input.mod")
    compiler.Decode()
    compiler.Load()
    while True:
        command = input("Command: ")
        if command == 'Exit':
            break
        print(compiler.Exec(command))
    # print("5 1 2 3 4 5")
    # print(compiler.Exec("ReverseArray 5 1 2 3 4 5"))
    # print(compiler.Exec("Multiply 5 5"))

    # print(compiler.Exec("Divide 9 5"))
    # print()
    # print(compiler.Exec("Divide -1 5"))
    # print()
    # print(compiler.Exec("Divide 12 9"))
    # print()
    # print(compiler.Exec("BinSearch 9 2 3 4 5 6 7 8 9 10 2"))
    # print()
    # print(compiler.Exec("Fibonacci 20"))
    # # processor.State()

    # # Execute the code
    # print()
    # print(compiler.Exec("Multiply 0 -1"))
    # print()
    # print(compiler.Exec("Multiply 5 5"))
    # print()


if __name__ == '__main__':
    main()