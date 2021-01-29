""" import sys

if __name__ == "__main__":
    for argument in sys.argv:
        print(f"Received > {argument}")
file = open("arquivo.txt", mode="w")

file.write("Trybe s2")
file.close()

file = open("arquivo.txt", mode="r")

content = file.read()
print(content)cr

file.write("nome idade\n")
file.write("Julio 35\n")
print("Julioooooooooo", file=file) """

""" while True:
    try:
        x = int(input("Please, enter a number "))
        break
    except ValueError:
        print("Ops, um número válido por favor")
 """

with open("arquivo.txt", "w") as file:
    file.write("Michele 27\n")

print(file.closed)
