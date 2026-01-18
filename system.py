PIN = 0
pin_new = 0
block_gen_pin = 1
number_for_pin = 0
number_for_div = 0
new_pin_gen = 1
new_pin_gen_real = 246
new_pin_gen_real1 = 0
new_pin = 0
account_balance_prashant = 0 #second bank account
account_balance = 30000 #first bank account
account_limit = 20000
#pin = 123
withdraw_time = 0
daily_limit = 0
add_amount = 0
no_pin = 0
max_pin = 3
pin_try = 0
help_pin = 0
pan_no = 0
blocked_no = 0
pin = 123
entered_pin = 0
print("------Welcome to the bank accounting system------")
while True:
 print("\nMONEY WITHDRAWAL: 1         ACCOUNT BLOCKED: 2          ADD MONEY: 3            CHANGE PIN: 4\n")
 print("UPGRADE LIMIT: 5           CHANGE MAX PIN: 6           TRANSFER MONEY: 7       CHECK ACCOUNT BALANCE: 8\n")
 print("CHECK LIMIT: 9             EXIT: 10             NO OF PIN ATTEMPT: 11\n")
 user = input("TYPE HERE: \n")
 if user == "1":
    #if blocked_no == 0:
    #while blocked_no == 0:
     if blocked_no == 0:
      for no_pin in range(max_pin):
       #daily_limit = daily_limit + 1
       if no_pin < 6:
        print("enter pin number: \n")
        entered_pin = int(input())
        if entered_pin == pin:
            print("enter amount\n")
            amount = int(input())
            if amount > 0:
               if amount <= account_limit:
                 if amount <= account_balance:
                    print('your entered amount is: \n' + str(amount))
                    account_balance = account_balance - amount
                    print("withdraw amount: \n" + str(amount))
                    account_limit = account_limit - amount
                    print("account balance: \n"+ str(account_balance)+"\n")
                    print("PRESS 1 MAIN MENU: ")
                    daily_limit = daily_limit + 1
                    print("PRESS 2 FOR WITHDRAW: ")
                    menu_start = input()
                    if menu_start == "1":
                          print("\n")
                          break
                    elif menu_start == "2":
                          #print("SECOND WITHDRAW: \n")
                          #withdraw_time = 0
                          #withdraw_time = withdraw_time + 1
                          if withdraw_time == 2:
                              print("THIRD WITHDRAW: \n")
                              withdraw_time = withdraw_time + 1
                          elif withdraw_time == 1:
                              print("SECOND WITHDRAW: \n")

                 else:
                    print("low account balance\n")
               else:
                 print("account limit reached\n")
            else:
                print("entered amount is less than 0\n")
        elif entered_pin != pin:
            print("entered pin is invalid\n")
            no_pin = no_pin + 1
            max_pin = max_pin - 1
            print("remaining attempt: \n" + str(max_pin))
       else:
         print("account blocked due to too many pin's attempt\n")
         blocked_no = blocked_no + 1
         break
      #elif blocked_no == 1:
    #while no_pin >= 3:
         #print("your account is blocked for unblock account type: help")
         """help_pin = input("\n ----type for account related problem: help----")
         if help_pin == "help":
             print("for verification enter you pan: ")
             pan_no = input()
             if pan_no == "asd":
                 print("pan verification complete")
                 print("new pin attempt is added")
                 no_pin = no_pin - 3
                 max_pin = max_pin + 3
                 blocked_no = blocked_no - 1
                     break"""
      if daily_limit > 2:
          print("your account withdraw limit is reached\n")
          #break
     else:
          print("YOUR ACCOUNT IS BLOCKED DUE TO TOO MANY PIN ATTEMPT\n PRESS 1 MAIN MENU: \n PRESS 2 FOR EXIT: \n")
          #print("PRESS 1 MAIN MENU: ")
          #print("PRESS 2 FOR EXIT: ")
          menu_time = 1
          menu_start = int(input())
          #menu_time = 1
          if menu_time == 2:
            print("--THANK YOU-- \n")
            break
          elif withdraw_time == 1:
            print("\n")

 elif user == "2":
    #help_pin = input("\n ----FOR UNBLOCKING ACCOUNT TYPE: help----\n")
    #if help_pin == "help":
        print("for verification enter you pan: \n")
        pan_no = input()
        if pan_no == "asd":
            if no_pin >= 2:
                if max_pin == 0:
                 print("pan verification complete\n")
                 print("new pin attempt is added\n")
                 no_pin = no_pin - 3
                 max_pin = max_pin + 3
                 blocked_no = blocked_no - 1
                 print("PRESS 1 MAIN MENU: ")
                 menu_start = input()
                 if menu_start == "1":
                     print("\n")
                     #break
                else:
                    print("remaining attempt is: " + str(max_pin) + " max attempt is not reached\n")
                    print("PRESS 1 MAIN MENU: ")
                    menu_start = input()
                    if menu_start == "1":
                        print("\n")
                        #break
            else:
                print("remaining attempt is: " + str(max_pin) + " max attempt is not reached\n")
                print("PRESS 1 MAIN MENU: ")
                menu_start = input()
                if menu_start == "1":
                    print("\n")
                    #break
 elif user == "3":
     print("ENTER AMOUNT THAT YOU WANT TO ADD: \n")
     add_amount = int(input())
     if add_amount > 0:
         print("MAIN AMOUNT: " + str(account_balance))
         account_balance = account_balance + add_amount
         #print("MAIN AMOUNT: " + str(amount))
         print("AMOUNT IS ADDED: " + str(add_amount))
         print("NEW AMOUNT: " + str(account_balance))

         print("PRESS 1 MAIN MENU: ")
         print("PRESS 2 FOR EXIT: ")
         menu_start = int(input())
         menu_time = 1
         if menu_time == 2:
             print("--THANK YOU-- \n")
             break
         elif withdraw_time == 1:
             print("\n")
     elif add_amount < 0:
         print("adding amount in - is not possible")
         #print("YOUR ACCOUNT IS BLOCKED DUE TO TOO MANY PIN ATTEMPT\n")
         print("PRESS 1 MAIN MENU: ")
         print("PRESS 2 FOR EXIT: ")

         menu_time = int(input())
         if menu_time == 2:
             print("--THANK YOU-- \n")
             break
         elif withdraw_time == 1:
             print("\n")
 elif user == "4":
     #user_first_pin = 0
     print("ENTER FIRST PIN: \n")
     user_first_pin = int(input())
     if user_first_pin == int(pin):
       print("ENTER NEW PIN: ")
       pin_try = input()
       len_pin_try = len(pin_try)
       #len_pin_real = len(pin)
       if int(pin_try) > 0:
         if len_pin_try == len("123"):
           #print("ENTER NEW PIN: ")
           #pin = int(input())
           pin = int(pin_try)
           print("YOUR ACCOUNT PIN IS UPDATED\n")
           print("SEEN YOUR PIN TYPE: SHOW PIN\n")
           print("FOR MENU TYPE: MENU\n")
           L = input("TYPE HERE: ")
           if L == "SHOW PIN":
               # SHOW = input()
               print("YOUR NEW PIN IS: " + str(pin))
       elif len_pin_try == len("-123") or len_pin_try != len("-123"):
           print("please enter a valid pin number")
           """number_for_pin = 0
           number_for_div = 0
           new_pin_gen = 1
           new_pin_gen_real = 246
           new_pin_gen_real1 = 0
           new_pin = 0"""
           if block_gen_pin ==1:

            if len_pin_try == len(str(-123)) or len_pin_try != len(str(-123)):
               if block_gen_pin == 1:

                 number_for_pin = number_for_pin + 13
                 number_for_div = number_for_div + 5 // new_pin_gen
                 new_pin_gen = new_pin_gen + number_for_pin // number_for_div

                 new_pin_gen_real1 = new_pin_gen_real // number_for_div % number_for_div + new_pin_gen % number_for_div
                 pin_new = pin_new + new_pin_gen_real1 + 23 // new_pin_gen
                 pin = int(pin_new) + int(pin_try) +(int(new_pin_gen) - int(pin_try)**int(number_for_pin))
                 if pin_new > 999:
                   print("auto pin generated is stoped due to too many attempts\n")
                   block_gen_pin = block_gen_pin + 1
                 len_new_pin = len(str(pin))
                  #for three_dig_pin in range(len(pin)):
                 if len(str(len_new_pin)) <= len("4"):
                   #for pin in range(99999):
                       temp_pin_range = 12
                       new_temp_pinn = 3
                       temo_pin_range = (temp_pin_range  + new_pin_gen // new_pin_gen) - new_temp_pinn
                       #print("YOUR ACCOUNT PIN IS UPDATED: " + str(temo_pin_range))
                       pin = temo_pin_range
                       N = 9999999
                       div_real_pin = pin // 4
                       new_temp_pinn = pin
                       len_temo_pin_range = 0
                       no_time_run = 1
                       for pin in range(N):
                           new_temp_pinn = new_temp_pinn // div_real_pin
                           temo_pin_range = temo_pin_range - new_temp_pinn
                           len_temo_pin_range = len(str(temo_pin_range))
                           no_time_run = no_time_run + 1
                           pin = temo_pin_range
                           if str(len_temo_pin_range) == str(3):
                               #no_time_run = no_time_run + 1
                               pin = temo_pin_range
                               print("no of try" + str(len_temo_pin_range))
                               print("no of values is in: "+str(len_temo_pin_range))
                               break

                           #else:
                              # print("please enter a valid pin number")
                       print("no of times: " + str(no_time_run))
                       print("YOUR NEW PIN GENERATED BY SYSTEM IS: " + str(temo_pin_range))
                 elif len(str(len_new_pin)) != len("3"):
                     print("zero as pin not possible")
                     break
                 #print("YOUR NEW PIN GENERATED BY SYSTEM IS: " + str(temo_pin_range))

            else:
                 print("invalid pin number")
                 #print("no of times: " + str(no_time_run))
           elif block_gen_pin == 2:
             print("auto in generate id blocked")
     else: # U == "FORGET":
       print("ENTERED PIN IS WRONG\n")
       print("FOR FORGET ACCOUNT PIN TYPE: FORGET\n")
       U = input()
       if U == "FORGET":
        print("ENTER YOUR ACCOUNT NUMBER: \n")
        ACCOUNT_NUMBER = 123456789
        ACCOUNT_NUMBER_CHEACK = int(input())
        if ACCOUNT_NUMBER_CHEACK == ACCOUNT_NUMBER:
         print("ENTER NEW PIN\n")
         PIN = int(input())
         len_pin_try = PIN
         if len(str(PIN)) == len(str(pin)):
           if PIN > 0:
             if len(str(PIN)) == len(str(pin)):
               pin = int(input())
               print("YOUR ACCOUNT PIN IS UPDATED\nSEEN YOUR PIN TYPE: SHOW PIN\nFOR MENU TYPE: MENU\n")
               #print("SEEN YOUR PIN TYPE: SHOW PIN\n")
               #print("FOR MENU TYPE: MENU\n")
               L = input("TYPE HERE: ")
               if L == "SHOW PIN":
                #SHOW = input()
                print("YOUR NEW PIN IS: " + str(pin))
             else:
                 print("pin must be contain least 3 to max 4 digits")
           #len_pin_try = PIN
           elif len_pin_try == len("-123") or len_pin_try != len("-123"):
               print("please enter a valid pin number")
               if block_gen_pin == 1:
                   if len_pin_try == len(str(-123)) or len_pin_try != len(str(-123)):
                       if block_gen_pin == 1:
                           number_for_pin = number_for_pin + 13
                           number_for_div = number_for_div + 5 // new_pin_gen
                           new_pin_gen = new_pin_gen + number_for_pin // number_for_div
                           new_pin_gen_real1 = new_pin_gen_real // number_for_div % number_for_div + new_pin_gen % number_for_div
                           pin_new = pin_new + new_pin_gen_real1 + 23 // new_pin_gen
                           pin = int(pin_new) - int(pin_try) + (int(new_pin_gen) - int(pin_try))
                           if pin_new > 999:
                               print("auto pin generated is stoped due to too many attempts\n")
                               block_gen_pin = block_gen_pin + 1
                           len_new_pin = len(str(pin))
                           # for three_dig_pin in range(len(pin)):
                           if len(str(len_new_pin)) <= len("1"):
                               # for pin in range(99999):
                               temp_pin_range = 12
                               new_temp_pinn = 3
                               temo_pin_range = (
                                                            temp_pin_range + pin + pin_new ** new_pin_gen // new_pin_gen) - new_temp_pinn
                               # print("YOUR ACCOUNT PIN IS UPDATED: " + str(temo_pin_range))
                               pin = temo_pin_range
                               N = 9999999
                               div_real_pin = pin // 4
                               new_temp_pinn = pin
                               len_temo_pin_range = 0
                               no_time_run = 1
                               for pin in range(N):
                                   new_temp_pinn = new_temp_pinn // div_real_pin
                                   temo_pin_range = temo_pin_range - new_temp_pinn
                                   len_temo_pin_range = len(str(temo_pin_range))
                                   no_time_run = no_time_run + 1
                                   pin = temo_pin_range
                                   if str(len_temo_pin_range) == str(3):
                                      # N = 0
                                       # no_time_run = no_time_run + 1
                                       pin = temo_pin_range
                                       print("no of try: " + str(len_temo_pin_range))
                                       print("no of values is in: " + str(len_temo_pin_range))
                                       break
                                       # else:
                                       # print("please enter a valid pin number")
                               print("no of times: " + str(no_time_run))

                           else:
                             print("wrong code")
                           print("YOUR NEW PIN GENERATED BY SYSTEM IS: " + str(temo_pin_range))

                   else:
                     print("invalid pin number")
                                   # print("no of times: " + str(no_time_run))
               elif block_gen_pin == 2:
                  print("auto in generate id blocked")


 elif user == "11":
     print("NO OF PIN ATTEMPT REMAINING: \n"+ str(max_pin))
     #print("MAX PIN: \n"+ str(max_pin))
 elif user =="5":
     print("enter upgrade limit amount: \n")
     J = int(input())
     if J > 5000:
      account_limit = J
      print("now your new limit is: " + str(account_limit))
     else:
         print("ACCOUNT LIMIT LESS THAN 5000 NOT POSSIBLE\n")
 elif user == "6":
    if no_pin == 0:
     print("enter no of attempt for pin: \n")
     T = int(input())
     if T > 0:
      if T <= 5:
       #L = no_pin
       no_pin = no_pin + T
       #max_pin = max_pin + T
       #k = 0
       #k = k+no_pin+T
       max_pin = T
       print("now your pin limit  is: " + str(no_pin))
       #max_pin = max_pin + 3
       #print(no_pin)
      else:
         print("cant add limit greater than 5\n")
     else:
        print("pin limit not zero, please enter limit greater than 0")
    elif no_pin != 0:
        print("cant add or change PIN LIMIT, attempt are already used")
 elif user == "7":
     print("enter amount")
     trans = int(input())
     if trans > 0:
         if trans <= account_limit:
             if trans <= account_balance:
                 print("enter account number of receiver: ")
                 accont_number_resiver = int(input())
                 if accont_number_resiver == 123:
                     print("Receiver name is: prashant\n enter pin to transfer money\n")
                     #print("enter pin to transfer money")
                     #print(no_pin)
                     entered_pin = int(input())
                     if int(no_pin) < 3:
                        if entered_pin == pin:
                        #if entered_pin == pin:
                          account_balance_prashant = account_balance_prashant + trans
                          account_balance = account_balance - trans
                          account_limit = account_limit - trans
                          print("----Money transfer successful----\n")
                          print("transferred amount is: " + str(trans))
                          print("remaining account balance is: \n" + str(account_balance))
                        else:
                          print("entered pin is invalid\n")
                          no_pin = no_pin + 1
                          max_pin = max_pin - 1
                          print("remaining attempt: \n" + str(max_pin))
                     else:
                          print("account blocked due to too many pin's attempt\n")
                          blocked_no = blocked_no + 1
                          #break
                 else:
                     print("wrong account number\n")

 elif user == "8":
     print("Your account balance is \n: " + str(account_balance))

 elif user == "9":
     print("your withdrawal limit is: \n" + str(account_limit))

 elif user == "10":
  break