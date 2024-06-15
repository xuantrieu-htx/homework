#==================================================================================
def calculate(number01 , number02 , op  ):
    # Begin your statements here
    if number02 == 0 and op == '/':
        return 0.00
    elif op == '+':
        return number01 + number02
    elif op == ' -':
        return number01 - number02
    else:
        return number01 + number02
    #End your statements
#end calculate
#==================================================================================
# =============DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("TEST Q1 (2 marks):")
    number01 = int(input("Enter number01 : "))
    number02 = int(input("Enter number02 : "))
    op = input("Enter op (+ , - , * , /) : ")
    finalResult = calculate(number01, number02, op)
    print("OUTPUT:")
    print("{0:.2f}".format(finalResult))
#end main
if __name__ == '__main__':
    main()
#==================================================================================