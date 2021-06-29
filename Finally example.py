try:
    print('i+j')
except NameError:
    print("Variable not defined")
finally:
    print("This line is always executed")