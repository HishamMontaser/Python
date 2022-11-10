import math

def func_add_scientific (First_variable,Second_variable):
    return First_variable + Second_variable
def func_sub_scientific (First_variable,Second_variable):
    return First_variable - Second_variable
def func_mult_scientific (First_variable,Second_variable):
    return First_variable * Second_variable
def func_div_scientific (First_variable,Second_variable):
    if Second_variable == 0 :
        print("Cant divide by zero")
    else:
        return First_variable/Second_variable
def func_abs_scientific (First_variable):
    return abs(First_variable)
def func_pow_scientific (First_variable):
    return pow(First_variable,2)
def func_log_scientific (First_variable):
    if First_variable < 0 :
        print("you cant do log base 10 on a negative number")
    else:
        return math.log10(First_variable)
def func_ln_scientific (First_variable):
    return math.e(First_variable)
def func_root_scientific (First_variable):
    return math.sqrt(First_variable)
def func_exp_scientific (First_variable):
    return math.exp(First_variable)
def func_sin_scientific (First_variable):
    return math.sin(First_variable)
def func_cos_scientific (First_variable):
    return math.cos(First_variable)
def func_tan_scientific (First_variable):
    return math.tan(First_variable)
def func_add_programming (First_variable,Second_variable):
    return First_variable + Second_variable
def func_sub_programming (First_variable,Second_variable):
    return First_variable - Second_variable
def func_mult_programming (First_variable,Second_variable):
    return First_variable * Second_variable
def func_div_programming (First_variable,Second_variable):
    if Second_variable == 0 :
        print("Cant divide by zero")
    else:
        return First_variable/Second_variable
def func_rem_programming (First_variable,Second_variable):
    return First_variable % Second_variable
def func_shift_left_programming (First_variable):
    return First_variable << 1 
def func_shift_right_programming (First_variable):
    return First_variable >> 1
def func_and_programming (First_variable,Second_variable):
    return First_variable and Second_variable
def func_or_programming (First_variable,Second_variable):
    return First_variable or Second_variable
    














print("-----------Hello user this is an app where you can either use scientific calculator or programming calculator-----------")
print("For scientific calculator you have to write : Scientific")
print("For programming calculator you have to write : programming")
First_variable = int(input("Determine your first number before choosing mode: "))
Second_variable = int(input("Determine your second number before choosing mode: "))
print("Please choose your mode")
var = input()
if var == 'Scientific':
    operation = input("You choice was scientific calculator now please enter your operation : ")
    if(operation == '+'):
        print(func_add_scientific(First_variable,Second_variable))
    elif(operation =='-'):
        print(func_sub_scientific(First_variable,Second_variable))
    elif(operation == '*'):
        print(func_mult_scientific(First_variable,Second_variable))
    elif(operation == '/'):
        print(func_div_scientific(First_variable,Second_variable))
    elif(operation == 'abs'):
        print(func_abs_scientific(First_variable))
    elif(opertaion == 'pow'):
        print(func_pow_scientific(First_variable))
    elif(operation == 'log'):
        print(func_log_scientific(First_variable))
    elif(operation == 'ln'):
        print(func_ln_scientific(First_variable))
    elif(opertaion == 'root'):
        print(func_root_scientific(First_variable))
    elif(operation=='exp'):
        print(func_exp_scientific(First_variable))
    elif(operation == 'sin'):
        print(func_sin_scientific(First_variable))
    elif(operation =='cos'):
        print(func_cos_scientific(First_variable))
    elif(operation=='tan'):
        print(func_tan_scientific(First_variable))
    

elif var == 'programming':
    hex(First_variable)
    hex(Second_variable)
    operation_1 = input("You choice was programming calculator now please enter your operation : ")
    if(operation_1 == '+'):
        print(func_add_programming(First_variable,Second_variable))
    elif(operation_1 =='-'):
        print(func_sub_programming(First_variable,Second_variable))
    elif(operation_1 == '*'):
        print(func_mult_programming(First_variable,Second_variable))
    elif(operation_1 == '/'):
        print(func_div_programming(First_variable,Second_variable))
    elif(operation_1 =='%'):
        print(func_rem_programming(First_variable,Second_variable))
    elif(operation_1 =='<<'):
        print(func_shift_left_programming(First_variable))
    elif(operation_1 =='>>'):
        print(func_shift_right_programming(First_variable))
    elif(operation_1 == '&'):
        print(func_and_programming(First_variable,Second_variable))
    elif(operation_1 == '|'):
        print(func_or_programming(First_variable,Second_variable))
    
    
else:
    print("I'am afraid you entered a wrong option ....")