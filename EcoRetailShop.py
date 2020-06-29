from textwrap import dedent
from sys import exit

Shop1 = {
         "DRINK":"Ghc20",
         "MILO":"Ghc15",
         "MILK":"Ghc25",
         "SNACKS":"Ghc19",
         "OATS":"Ghc8",
         "SUGAR":"Ghc9",
         "NIDO":"Ghc12",
         "HONEY":"Ghc15",
         "BUTTER":"Ghc10",
         "TEA":"Ghc10"
        }

Shop2 = {
         "RICE":"Ghc10",
         "BEANS":"Ghc10",
         "NODDLE":"Ghc10",
         "GARI":"Ghc8",
         "CABBAGE":"Ghc10",
         "CARROT":"Ghc6",
         "MEAT":"Ghc9",
         "EGG":"Ghc12",
         "OIL":"Ghc10",
         "SARDINE":"Ghc12",
         "SALT": "Ghc5"

        }


Shop3 = {
         "TOOTH-BRUSH":"Ghc3",
         "TOOTH-PASTE":"Ghc7",
         "ROLL-ON":"Ghc6",
         "TISSUE":"GhC10",
         "T-ROLL":"Ghc10",
         "BODY-CREAM":"Ghc8",
         "HAIR-CREAM":"Ghc8",
         "CUP":"Ghc10",
         "WATER-BOTTLE":"Ghc15",
         "BRUSH":"Ghc20"

    }

print("-" * 35)
#welcome message
print("Hello, welcome to ECO Retail Shop.")
print("-" * 35)

# receives input of the user
print("Please enter your name. eg Dan ")
name = input(": ").upper()

#this is used to cheak the validity of the input
while len(name) == 0:
    if len(name) == 0:
        print("Please enter your name.eg Dan ")
        name = input(": ").upper()
    else:
        pass
    

repeat = 0
#this repeats the game
while repeat < 5:
    
    print("-" *68)
    print("-" *68)

    #this is for the first sale
    class purchase1:
        # this contains the variable used in the first class
        def __init__(self):
            self.purchase1_add = 0
            self.sale1 = 0
            self.counter1 = 0
            self.get_first_amounts = 0
    
        def first_purchase(self):    
            # shop display and item entry
            print("We have three different shops which contains items for everyday use.")
            print("Below is what we have in the shops. ")

            # displaying the first shop
            print("")
            print(dedent("""In the first shop we have the following items.
                            DRINK(Ghc20)
                            MILO(Ghc15)
                            MILK(Ghc25)
                            SNACKS(Ghc19)
                            OATS(Ghc8)
                            SUGAR(Ghc9)
                            NIDO(Ghc12)
                            HONEY(Ghc15)
                            BUTTER(Ghc10)
                            TEA(Ghc10)
               
                        """))

            #display things bought and price
            print("Press enter to skip this shop OR")
            print("Enter the item or items you want to buy :")
            
            
            # loops the incorrect option
            while self.counter1 == 0:
                self.first_purchase = input(":").upper().split()

                # for cheacking if there was an input
                if len(self.first_purchase) <= 10 and len(self.first_purchase) > 0 :
        
                    # loops for space(workspace)
                    for self.sale1 in range(0, 1):
                        
                        # loops to get  first amounts from dictionary(Shop1)
                        for self.sale1 in range(0,10):
                            if self.sale1 < len(self.first_purchase):
                                #this gets the amount of the product 
                                self.get_first_items = self.first_purchase[self.sale1]
                                self.get_first_amounts = Shop1.get(self.get_first_items)

                                # print amount and product if nothing goes wrong
                                if self.get_first_amounts != None:
                                    print(f"{self.get_first_items} = {self.get_first_amounts}")



                            elif self.sale1 > len(self.first_purchase):
                                pass

                            
                # for wrong input 
                if self.get_first_amounts == None: 
                    print("- " * 25)
                    print("WRONG INPUT")
                    print("Please,Enter the item or items you want to buy.")
                    print("Please enter the exact thing you see")
                                        
                else:
                             
                    pass
                    break
                

                           
            
            #this changes the string amount to an integer amount    
            for self.number_of_first_items in range(0,len(self.first_purchase)):
                self.first_string_amount = Shop1.get(self.first_purchase[self.number_of_first_items])
                self.first_real_amount = (int(self.first_string_amount.strip("Ghc")))
                self.purchase1_add  += self.first_real_amount
    
                
            return(self.purchase1_add)
           
    # this puts the purchase1 class in p1
    p1 = purchase1()
    #this displays first_purchase
    p1.first_purchase()
    print(f"The total for the first purchase = {p1.purchase1_add}")

    # for no purchase
    if p1.purchase1_add == 0:
        print("Press (e) to exit from the shop or (c) to continue")
        Input1 = ""
        
        while Input1 == "":
            
            Input1 = input()
            if Input1 == "e":
                print("Thank you for visiting Eco retail shop")
                exit(1)

            elif Input1 == "c":
                print("Since you both nothing,lets go to the second shop")
                print("to see if you are intrested in something there")
                pass

            else:
                print("Wrong input,Please try again")
                
        
        
    else :
        
        pass

    
    print("-" *68)
    print("-" *68)


    class purchase2:

        #this contains all the variables in this class
        def __init__(self):
            self.purchase2_add = 0
            self.sale2 = 0
            self.counter2 = 0
            self.get_second_amounts = 0

            
        #shop2 display and item entry
        def second_purchase(self):
            # displaying the second shop 
            print(dedent("""In the second shop we have the following items.
                            RICE(Ghc10)
                            BEANS(Ghc10)
                            NODDLE(Ghc10)
                            GARI(Ghc8)
                            CABBAGE(Ghc10)
                            CARROT(Ghc6)
                            MEAT(Ghc9)
                            EGG(Ghc12)
                            OIL(Ghc10)
                            SARDINE(Ghc12)
                            SALT(Ghc5)

               
                        """))
            #display things bought and price in Shop2
            print("Press enter to skip this shop OR")
            print("Enter the item or items you want to buy:")

            
            # loops the incorrect option
            while self.counter2 == 0:
                self.second_purchase = input(":").upper().split()

                # for cheacking if there was an input 
                if len(self.second_purchase) <= 10 and len(self.second_purchase) > 0 :
                
                    # loops for space(workspace)
                    for self.sale2 in range(0, 1):
                        
                        # loops to get first amounts from dictionary(Shop1)
                        for self.sale2 in range(0,10):
                            
                            if self.sale2 < len(self.second_purchase):
                                #this gets the amount of the product 
                                self.get_second_items = self.second_purchase[self.sale2]
                                self.get_second_amounts = Shop2.get(self.get_second_items)
                                

                                # print amount and product if nothing goes wrong
                                if self.get_second_amounts != None:
                                    #this displays the product and its amount
                                    print(f"{self.get_second_items} = {self.get_second_amounts}")



                            elif self.sale2 < len(self.second_purchase):
                                pass
                               

                # for wrong input
                if self.get_second_amounts == None :
                    print("- " * 25)
                    print("WRONG INPUT")
                    print("Please,Enter the item or items you want to buy :")
                    print("Please enter the exact thing you see")
                    

                else :
                    pass
                    break
                

            #this changes the string to an integer
            for self.number_of_second_items in range(0,len(self.second_purchase)):
                self.second_string_amount = Shop2.get(self.second_purchase[self.number_of_second_items])
                self.second_real_amount = (int(self.second_string_amount.strip("Ghc")))
                self.purchase2_add += self.second_real_amount
    
                
            return(self.purchase2_add)

           
    # this puts the purchase2 class in p2
    p2 = purchase2()
    #this displays first_purchase
    p2.second_purchase()
    print(f"The total for the second purchase = {p2.purchase2_add}")

    # for no purchase
    if p2.purchase2_add == 0:
        print("Press (e) to exit from the shop or (c) to continue")
        Input2 = ""
        
        while Input2 == "":
            
            Input2 = input()
            if Input2 == "e":
                print("Thank you for visiting Eco retail shop")
                exit(1)

            elif Input2 == "c":
                
                print("Since you bought nothing here too,lets go to the last")
                print("shop to see if you are intrested in something there")
                pass

            else:
                print("Wrong input,Please try again")
                
        
        
        

    else :
        
    
        pass
       

    print("-" *68)
    print("-" *68)

    class purchase3:

        #this contains the variable found in the class
        def __init__(self):
            self.purchase3_add = 0
            self.sale3 = 0
            self.counter3 = 0
            self.get_third_amounts = 0
    
        def third_purchase(self):
            # displaying the third shop
            print("")
            print(dedent("""In the third shop we have the following items.
                            TOOTH-BRUSH(Ghc3)
                            TOOTH-PASTE(Ghc7)
                            ROLL-ON(Ghc6)
                            TISSUE(GhC10)
                            T-ROLL(Ghc10)
                            BODY-CREAM(Ghc8)
                            HAIR-CREAM(Ghc8)
                            CUP(Ghc10)
                            WATER-BOTTLE(Ghc15)
                            BRUSH(Ghc20)


               
                        """))
            #display things bougth and price in Shop3
            print("Press enter to skip this shop OR")
            print("Enter the item or items you want to buy.")

            # loops the incorrect option
            while self.counter3 == 0:
                self.third_purchase = input(":").upper().split()

                # for cheacking if there was an input
                if len(self.third_purchase) <= 10 and len(self.third_purchase) > 0 :
                
                    # lopps for space(workspace)
                    for self.sale3 in range(0, 1):

                        # lopps to get first amounts from dictionary(Shop3)
                        for self.sale3 in range(0,10):

                            #this gets the amount of the product 
                            if self.sale3 < len(self.third_purchase):
                                #this gets the amount of the product 
                                self.get_third_items  = self.third_purchase[self.sale3]
                                self.get_third_amounts = Shop3.get(self.get_third_items )
                               
                                if self.get_third_amounts != None:
                                    #this displays the product and its amount 
                                    print(f"{self.get_third_items} = {self.get_third_amounts}")



                            elif self.sale3 < len(self.third_purchase):
                                pass
            


                # for wrong input
                if self.get_third_amounts == None :
                    print("- " * 25)
                    print("WRONG INPUT")
                    print("Please,Enter the item or items you want to buy :")
                    print("Please enter the exact thing you see")
                                    

                else :
                    pass
                    break
    


            #this displays the product and its amount 
            for self.number_of_third_items in range(0,len(self.third_purchase)):
                self.third_string_amount = Shop3.get(self.third_purchase[self.number_of_third_items])
                self.third_real_amount  = (int(self.third_string_amount.strip("Ghc")))
                self.purchase3_add += self.third_real_amount 
    
                
            return(self.purchase3_add)
        
            
    # this puts the purchase3 class in p3
    p3 = purchase3()
    #this displays second_purchase
    p3.third_purchase()
    print(f"The total for the third purchase = {p3.purchase3_add}")

    
    # for no purchase
    if p3.purchase3_add == 0:
        print("Press (e) to exit from the shop or (c) to continue")
        Input3 = ""
        
        while Input3 == "":
            
            Input3 = input()
            if Input3 == "e":                                                  
                print("Thank you for visiting Eco retail shop")
                exit(1)

            elif Input3 == "c":
                print("Since you bougth nothing in the third shop")
                pass

            else:
                print("Wrong input,Please try again")
                
        
        
        

    else :
        
        pass
        

    print(" ")
   
    class main:

        #this contains the variables found in the class
        def __init__(self):
            self.amount_strip = 0
            self.transform = 0

        def welcome(self):
            # if nothing was bougth in all the shops
            if p1.purchase1_add ==0 and p2.purchase2_add == 0 and p3.purchase3_add == 0:

                print("and since you bougth nothing read the message below ")
                pass

            else:
                # collect the amount of the buyer
                while self.transform == 0:
                    print(f"{name}, please enter your amount")
                    self.amount = input(":")
                    
                    if self.amount == int():
                        print(self.amount)

                    # if no money was entered
                    elif self.amount == "":
                        print("Since you don't have money ,please read the option below")
                        break

                    else:
                        if len(self.amount) == len(self.amount):
                            try:
                                self.transform = int(self.amount)

                            except:
                                pass
                        
    

                return self.transform


    am = main()
    # this displays the amount
    am.welcome()
    
    
    

    # this calculates the  total amount
    class change:
        
        def __init__(self):
            self.total_amount = 0
    
        def trans(self):
            # this changes the input into an integer 
            if p1.purchase1_add == 0 and p1.purchase1_add == 0 and p1.purchase1_add == 0:
                pass

               
            # if no money was entered
            elif am.transform == 0 :
                
                pass

            
            else :
                self.total_amount = p1.purchase1_add + p2.purchase2_add + p3.purchase3_add
                print("-" * 47)
                print(f"The total amount of the things purchased is : {self.total_amount}")
 

           
    # this puts the change class in c1
    c1= change()
    #print the balance
    c1.trans()
    

    
    #this deals with the options
    class sug(purchase1,purchase2,purchase3,main):
    

        def option1(self):
            print("-" * 49)
            # this for a right option
            self.retun = 0
            while self.retun == 0:
                # this prints the options
                print("Please CLICK R to repeat the process OR E to exit")
                self.option = input().upper() # stores option
            
                # executes the exit option
                if self.option == "E":
                    print("-" * 30)
                    print("Thank you for visiting ECO Retail Shop.")
                    exit(1)
                    
                

                # executes the return option
                elif self.option == "R":
               
                    break
                
                # executes if the input is wrong
                elif self.option != "R" and self.option != "E" :
                    self.wrong = 0
                    while self.wrong <= 3:
                        
                        print("Please enter the right option")
                        self.option = input().upper()


                        # executes the exit option
                        if self.option == "E":
                            print("-" * 30)
                            print("Thank you for visiting ECO Retail Shop.")
                            exit(1)
                            
                

                        # executes the return option
                        elif self.option == "R":
               
                            break

                        # executes if the attemps for option has been reached
                        if self.wrong == 3:
                            print("-" * 47)
                            print("Since the attempt is up to 4 the system will close.")
                            print("THANK YOU")
                            exit(1)

                        else :
                            pass
                        
                        # increases the value of self.wrong
                        self.wrong += 1

                else:
        
                    pass
                    
                break

                

    # this puts the sug class in so
    so = sug()
    

    #this deals with the final statements

    class fin(change, sug, main):

        def __init__self():
            self.total_balance = 0

        def cal(self):
            # this calculates the total balance 
            self.total_balance = int(am.transform) - c1.total_amount
       
            
            if int(am.transform) > c1.total_amount :
    
                self.total = int(am.transform) - c1.total_amount
                print(f"Your balance is : {self.total_balance}")
                so.option1()
    
            if am.transform!= 0:
            
                if int(am.amount) < c1.total_amount:
                    print("You don't have enough money to pay")
                    so.option1()


            elif am.transform == 0:
                so.option1()
                
            
            #for no input        
            elif c1.total_amount == 0:
                so.option1()


                
    # this puts the fin class in finish
    finish = fin()
    finish.cal()

    repeat += 1

#this executes if the person fulls with the program
if repeat == 5 :
    print("-" * 30)
    print("Since the attempt for re-running the programe has exceded its limit,")
    print("The programe will restart in 10 hours.")
    print("THANKS FOR USING THE SOFTWARE")
    exit(1)

    










