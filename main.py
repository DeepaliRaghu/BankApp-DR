import csv

import Bank_Account_ishaan
from Bank_Account_ishaan import BankAccount
#import BankUtilities



print('Welcome to Commerce Bank')

print("Who are you? Please select one of the following options:\n 1. Customer\n 2. Admin \n 3. Exit\n Please select the option number:")

ch=int(input('select the option number:'))

#print(input('Please select from the following.\n 1.Create new login.\n 2. Existing Customer'))

#print(input('select one option number'))

if ch==1:
    print('Welcome to customer Area: Choose from the below optios:\n1.Login\n2.signup\n3.Previous Menu\n4.exit.')
    ch1 = int(input('Please enter the number of your option:'))
    if ch1==2:
        with open('client_records.csv', 'w') as details:
            details.write('cus_first_name, cus_last_name, cus_address, cus_phone_number,user_name,pass_word,initial_balance')


        print('Please enter the following details')
        cus_first_name = input('Please enter your first name: ')
        cus_last_name = input('Please enter yor last name:')
        cus_address = input('Enter your address: ')
        cus_phone_number = int(input('Please enter your phone number: '))
        user_name = input('Please enter your username:')
        pass_word = input('Please enter your password:')
        initial_balance = int(input("Please enter initial balance"))



        with open('client_records.csv', 'a') as record:
            record.write(f'\n{cus_first_name}, {cus_last_name}, {cus_address} ,{cus_phone_number},{user_name},{pass_word},{initial_balance}')

    print('For login please enter the following:')
    username=input('Please enter your user name: ')
    password=input('Please Enter your pass word: ')

    with open('client_records.csv','r') as csv_file:
        csv_reader =csv.reader(csv_file)
        for row in csv_reader:
            if username==row[4] and password==row[5]:
                print(f"Welcome {cus_first_name} {cus_last_name}")
                print('Your stored details are :', row)
            else:
                 print("Either username or password is wrong. Please enter the correct username and password")




    cus_1=BankAccount()
    CH='Y'
    while CH=='Y':
     print(input('Please choose from the following options: \n1.Create New Bank Account\n2.Show balance\n3.Deposite\n4.Withdrawl'))
     ch2=int(input('Please select the number of your choice:'))
     if ch2==1:
        cus_1.crerate_account()
        cus_1.basic_details()
     elif ch2==2:
         cus_1.show_balance()
     elif ch2==3:
        cus_1.deposite()
     elif cus_1==4:
        cus_1.withdrawl()
     else:
         print('Please select anyone of the above options:')
     print('Do you have any other accounts if yes press..Y')
     CH=input()








'''def creat_account():
        first_name = input('Please enter your first name:')
        last_name = input('Please enetr your last name:')
        cust_acc_num = int(input('Please enter your bank account number:'))
        username = input('Please enter your username: ')
        acc_balance = int(input('Please Enter your initial balance: '))

        with open('Account_list.csv', 'w') as csv_file:
            csv_file.write(f'username,cust_acc_num,initial_balance')

        with open('Account_list.csv', 'a') as acc_list:
            acc_list.write(f'\n{username},{cust_acc_num},{acc_balance}')

def basic_details():
        print(f'User:{first_name} {last_name}\t Account No: {cust_acc_num}\t Balance: Euro {acc_balance}')


    def deposite():
        amount = int(input('Enter the deposite amount: '))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(f'Transaction completed.Current Balance:Euro {self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')


    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            print(f'Transaction completed.Current Balance:Euro {self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')


    def payment(self):
        amount = int(input('Enter the payment amount:'))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            # other.initial_balance = other.acc_balance + amount
            print(f'Transaction completed.Current Balance: Euro {self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')'''

