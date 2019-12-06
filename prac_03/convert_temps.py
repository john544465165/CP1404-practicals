"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    f1 = open("temps_input.txt", "r")
    f2 = open("temps_output.txt", "w")
    for line in f1.readlines():
        fahrenheit = float(line)
        celsius = f2c(fahrenheit)
        f2.write(str(celsius)+"\n")
    f1.close()
    f2.close()

def f2c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()