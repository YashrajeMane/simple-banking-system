from random import*

first_name_oti = [1,2,3,4,5,6,7,8,9]
last_name_oti = [1,2,3,4,5,6,7,8,9]
phone_oti = [1,2,3,4,5,6,7,8,9]
email_oti = [1,2,3,4,5,6,7,8,9]
password_oti = [1,2,3,4,5,6,7,8,9]
username_oti = [1,2,3,4,5,6,7,8,9]
user_id_oti = [1,2,3,4,5,6,7,8,9]
count_oti_data = 0
phone_bank_current = [1,2,3,4,5,6,7,8,9]
first_name_bank_current = [1,2,3,4,5,6,7,8,9]
last_name_bank_current = [1,2,3,4,5,6,7,8,9]
business_name_bank_current = [1,2,3,4,5,6,7,8,9]
business_email_bank_current = [1,2,3,4,5,6,7,8,9]
business_phone_bank_current = [1,2,3,4,5,6,7,8,9]
business_aadhar_bank_current = [1,2,3,4,5,6,7,8,9]
business_pan_bank_current = [1,2,3,4,5,6,7,8,9]
user_id_current_bank = [1,2,3,4,5,6,7,8,9]
account_number_current = [1,2,3,4,5,6,7,8,9]
create_current_bank_account_pin = [1,2,3,4,5,6,7,8,9]
create_current_bank_account_Transaction_pin = [1,2,3,4,5,6,7,8,9]
count_bank_current = 0
phone_bank_saving = [1,2,3,4,5,6,7,8,9]
first_name_bank_saving = [1,2,3,4,5,6,7,8,9]
last_name_bank_saving = [1,2,3,4,5,6,7,8,9]
email_bank_saving = [1,2,3,4,5,6,7,8,9]
saving_account_number = [1,2,3,4,5,6,7,8,9]
aadhar_saving_bank = [1,2,3,4,5,6,7,8,9,]
pan_saving_bank = [1,2,3,4,5,6,7,8,9]
user_id_saving = [1,2,3,4,5,6,7,8,9]
account_pin_saving = [1,2,3,4,5,6,7,8,9]
account_saving_Transaction_pin = [1,2,3,4,5,6,7,8,9]
count_bank_saving = 0
while True:
 print("-------WELCOME TO THE PROGRAM-------")
 print("OTI System: 1","Banking System: 2",sep='      ')
 print("Enter: ",end='')
 choice_system = int(input())
 while True:
  if choice_system == 1:
    print("OTI Login: 1","Create Account: 2",sep='      ')
    print("Enter: ",end='')
    choice_oti_account = int(input())
    while True:
     if choice_oti_account == 1:
        choice_oti_account = 1
        print("Login: 1", "Forget Password: 2", "Forget Username: 3", sep='      ')
        choice_oti_login_password_username = int(input())
        if choice_oti_login_password_username == 1:
            def verify_login_info_oti():
                print("Enter Username: ")
                verify_username_oti = input()
                for i in range(0,9,1):
                    global verify_info_i_value
                    verify_info_i_value = i
                    if verify_username_oti == username_oti[i]:
                        print("Enter Password: ")
                        verify_password_oti = input()
                        for i in range(0,9,1):
                            if verify_password_oti == password_oti[i]:
                                return True
                            else:
                                print("Enter Valid Password")
                    else:
                        print("Enter Valid username")

            verify_return_info = verify_login_info_oti()
            if verify_return_info == True:
                print("Login Successfully \n")
                print("Transaction History: 5","Unlink Bank Account: 4","Find People On OTI: 8",sep='      ')
                print("Add Bank Account: 1","Deactivate OTI: 7","   Reset OTI PIN: 3",sep='        ')
                print("Active OTI: 2"," Show OTI ID: 6"," Exit: 9",sep='             ')
                choice_oti_feature = int(input())
                if choice_oti_feature == 1:
                    print("Please wait, While we check Bank Info...")
                   # def check_bank_info():
                        #if phone_oti[verify_info_i_value] == #first create bank page:






        elif choice_oti_login_password_username == 2:

          def oti_password_username_setup():
            print("Enter Phone Number: ")
            pass_forget_phone = input()
            print("Enter Email Address: ")
            pass_forget_email = input()
            for i in range(0,9,1):
                if pass_forget_phone == phone_oti[i]:
                    global store_i_value
                    store_i_value = i
                    for i in range(0,9,1):
                        if pass_forget_email == email_oti[i]:
                            return True

          store_return_pass_forget = oti_password_username_setup()
          if store_return_pass_forget == True:
                print("Enter New Password: ")
                new_pass_oti = input()
                password_oti[store_i_value] = new_pass_oti
                print("Your New Password Is: ",password_oti[store_i_value])
                while True:
                    choice_oti_account = 1
                    break

        elif choice_oti_login_password_username == 3:
                store_return_username_forget = oti_password_username_setup()
                if store_return_username_forget == True:
                    print("Enter New Username: ")
                    new_username_oti = input()
                    username_oti[store_i_value] = new_username_oti
                    print("Your New Username Is: ",username_oti[store_i_value])
                    while True:
                        choice_oti_account = 1
                        break

     elif choice_oti_account == 2:
        def create_oti_account():
            print("Enter First Name: ")
            first_name_oti[count_oti_data] = input()
            print("Enter Last Name: ")
            last_name_oti[count_oti_data] = input()
            print("Enter Phone Number: ")
            phone_oti[count_oti_data] = input()
            print("Enter Email Address: ")
            email_oti[count_oti_data] = input()
            print("Enter Password: ")
            password_oti[count_oti_data] = input()
            print("Enter Username: ")
            username_oti[count_oti_data] = input()
            user_id_oti[count_oti_data] = randint(123456789012,999999999999)
            return_count_oti_dat = count_oti_data + 1
            return return_count_oti_dat
        count_oti_data = create_oti_account()
        print("Your Username Is: ",username_oti[count_oti_data-1])
        print("Your Password Is: ",password_oti[count_oti_data-1])
        print("Go To Login: 1")
        print("Exit: 2")
        choice_in_oti_login_exit = int(input())
        if choice_in_oti_login_exit == 1:
            while True:
                    choice_oti_account = choice_oti_account - 1
                    break
        elif choice_in_oti_login_exit == 2:
            while True:
                break


  elif choice_system == 2:
      print("-----Welcome to Bank System-----")
      print("Current Bank account: 1","Saving Bank account: 2","Login To Back Account: 3",sep='     ')
      choice_bank_account_c_s = int(input())
      while True:
       if choice_bank_account_c_s == 1:
           def current_bank_account():
              print("Enter Phone Number: ")
              phone_bank_current[count_bank_current] = int(input())
              print("Enter Your First Name: ")
              first_name_bank_current[count_bank_current] = input()
              print("Enter Your Last Name: ")
              last_name_bank_current[count_bank_current] = input()
              print("Business Name: ")
              business_name_bank_current[count_bank_current] = input()
              print("Business Email Address: ")
              business_email_bank_current[count_bank_current] = input()
              print("Business Phone Number: ")
              business_phone_bank_current[count_bank_current] = input()
              print("Business Aadhar Number: ")
              business_aadhar_bank_current[count_bank_current] = input()
              print("Business PAN Number: ")
              business_pan_bank_current[count_bank_current] = input()
              #global count_bank_current_indef
              #count_bank_current_indef = count_bank_current + 1
              global user_id_current_bank
              user_id_current_bank[count_bank_current] = randint(123456789012,999999999999)
              global account_number_current
              account_number_current[count_bank_current] = randint(1123456789012,9999999999999)  #13digit

              print("Account Created Successfully")
              print("Current Bank Account Number: ", account_number_current[count_bank_current])
              print("Please Create Account PIN: ")
              create_current_bank_account_pin[count_bank_current] = int(input())
              print("Your Current Bank Account PIN Is: ",create_current_bank_account_pin[count_bank_current])
              print("Please Create Transaction Pin: ")
              create_current_bank_account_Transaction_pin[count_bank_current] = int(input())
              print("Your Transaction PIN Is: ",create_current_bank_account_Transaction_pin[count_bank_current])
              global count_bank_current_indef
              count_bank_current_indef = count_bank_current + 1
              return True
           return_store_current_bank = current_bank_account()
           if return_store_current_bank == True:
              count_bank_current = count_bank_current_indef
              print("Go To Bank Login: 1", "Exit: 2")
              choice_current_bank_login_exit = int(input())
              if choice_current_bank_login_exit == 1:
                  while True:

                      choice_bank_account_c_s = 3
                      break
              elif choice_current_bank_login_exit == 2:
                  break
       elif choice_bank_account_c_s == 2:
           choice_bank_account_c_s = 3
           def saving_bank_account():
               print("Enter Phone Number: ")
               phone_bank_saving[count_bank_saving] = int(input())
               print("Enter Your First Name: ")
               first_name_bank_saving[count_bank_saving] = int(input())
               print("Enter Your Last Name: ")
               last_name_bank_saving[count_bank_saving] = int(input())
               print("Enter Your Email Address: ")
               email_bank_saving[count_bank_saving] = int(input())
               print("Enter Your Aadhar Number: ")
               aadhar_saving_bank[count_bank_saving] = int(input())
               print("Enter Your PAN Number: ")
               pan_saving_bank[count_bank_saving] = int(input())
               user_id_saving[count_bank_saving] = randint(123456789012,999999999999)
               saving_account_number[count_bank_saving] = int(randint(123456789012,999999999999)) #12digit
               print("Create Account PIN: ")
               account_pin_saving[count_bank_saving] = int(input())
               print("Create Account Transaction PIN: ")
               account_saving_Transaction_pin[count_bank_saving] = int(input())
               print("Your Account PIN IS: ",account_pin_saving[count_bank_saving])
               print("Your Transaction PIN Is: ",account_saving_Transaction_pin[count_bank_saving])
               print("Your Account Number Is: ",saving_account_number[count_bank_saving])
               return True
           store_return_value_saving = saving_bank_account()
           print("Go To Login: 1", "Exit: 2")
           choice_create_saving_to_login_exit = int(input())
           if choice_create_saving_to_login_exit == 1:
               while True:
                   choice_system = 2
                   choice_bank_account_c_s = 3
                   break
           elif choice_create_saving_to_login_exit == 2:

                   break

       elif choice_bank_account_c_s == 3:
         def verify_account_info_login():
           print("Enter Account Number: ")
           verify_account_number_bank = int(input())
           print("Enter Account PIN: ")
           verify_account_pin_bank = int(input())
           for ik in range(0,9,1):
             if verify_account_number_bank == saving_account_number[ik]:
                 global store_ik_value_bank
                 store_ik_value_bank = ik
                 for il in range(0,9,1):
                     verify_account_pin_bank = account_pin_saving[il]
                     if verify_account_pin_bank == account_pin_saving[il]:
                         return 'yes'
         if  verify_account_info_login() == 'yes':
             print("Login Successful")
             print("Account information: 1","Change Account PIN: 2","Transaction Limit: 3", sep='      ')
             print("Check OTI Limit: 4","Withdrawal Limit: 5","Transfer Limit: 6", sep='         ')
             print("Withdraw Money: 7","     OTI: 8",sep='      ')
             choice_in_bank_feature = int(input())
             if choice_in_bank_feature == 1:
                 if len(saving_bank_account()) == 0:
                 print("Account Number: ",saving_account_number[store_ik_value_bank])
                 print("Linked Phone Number:",phone_bank_saving[store_ik_value_bank])


