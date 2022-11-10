print("Hello and Welcome to the ITI shop")
var = int(input("if you are a customer and willing to enter the customer menu plese press 1 other wise you are an owner please press 0 : "))

if(var == 1):
    print("Hello,Customer we are thrilled to have you at our humble shop")
    print("you have four options : ")
    print("1) if you wanna show from our products then you have to press 1.")
    print("2) if you wanna buy from out products then you have to press 2.")
    print("3) if you wanna print you bill then you have to press 3.")
    print("Finally if you wanna exit our shop simply press 0.")
    print("waiting for your choice.")
    choice = 1
    while choice != 0 :
        choice = int(input())
        if(choice == 1):
            print("Heres our products and the cost of each product")
            our_products = {'Products' : 'Arduino , Arm , Rasberrypi' , 
                            'cost'     :  [250      ,  500  ,  1000]
        }
            print(our_products)
        elif choice == 2:
            product=input("Well please choose the product you want to buy : ")
            if product == 'Arduino':
                print("Transaction completed")
            elif product =='Arm':
                print("Transaction completed")
            elif product == 'Rasberrypi':
                print("Transaction completed")
            
        elif choice == 3:
            if product == 'Arduino':
                print(our_products['cost'][0])
            elif product == 'Arm':
                print(our_products['cost'][1])
            elif product == 'Rasberrypi':
                print(our_products['cost'][2])
        else:
            print("Thank you for visitng our store")
                


if(var == 0):
    print("Hello,Sir state what you want from our system please")
    print("to make it quick you have three options")
    print("1)if you wanna show our menu simply press 1.")                                      
    print("2)if you wanna add new products to our menu simply press 2.")
    print("3)if you wanna add a cost press 3.")
    print("Lastly,if you wanna exit press 0.")
    print("waiting for you choice")
    cho = 1
    while cho !=0 :
        cho = int(input())
        if cho == 1:
            our_products = {'Products' : 'Arduino , Arm , Rasberrypi' , 
                             'cost'     :  [250      ,  500  ,  1000]
        }
            print(our_products)
        elif cho == 2:
            new_product = input("Please enter the product you want to add to our menu sir")
            our_products[new_product] = 70
            print("well heres the updated menu")
            print(our_products)
        else:
            print("Thank you owner have a nice day")
                    
        
            
            
   
    
        
            
            
