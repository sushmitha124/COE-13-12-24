import streamlit as st
import uuid
class Bank:
    acbal=10000
    st.title("Bank Application")
    def deposit(self):
        deposit = st.number_input("enter deposit amount")
        if st.button("Deposit"):
            if(deposit>=100 and deposit<=50000 and deposit%100==0):
                st.write("accepted the deposit")
            else:
                if(deposit<100):
                    st.write("cant deposit due to less than min deposit")
                elif(deposit>50000):
                    st.write("cant deposit due to more than max deposit")
                elif(deposit%100!=0):
                    st.write("cant deposit because amount is not multiples of 100")
    def withdraw(self):
        w_amount = st.number_input("Enter amount to withdraw")
        no_of_transactions = st.number_input("Enter no of transactions")
        if st.button("Withdraw"):
            if(w_amount>=100 and w_amount<=20000 and w_amount<self.acbal and w_amount%100==0 and self.acbal>=500 and no_of_transactions<=3):
                st.write("you can withdraw amount")
            else:
                if(w_amount<100):
                    st.write("you cannot withdraw amount because less than min withdraw amount")
                elif(w_amount>20000):
                    st.write("you cannot withdraw amount because greater than max withdraw amount")
                elif(w_amount>=self.acbal):
                    st.write("you cannot withdraw amount because greater than account balance")
                elif(w_amount%100!=0):
                    st.write("cant withdraw amount because amount is not multiples of 100")
                elif(self.acbal<500):
                    st.write("cant withdraw because account balance is less than 500")
                elif(no_of_transactions>3):
                    st.write("greater than number of transactions")

    def validation(self):
        pin=st.number_input("Enter pin number")
        if(pin==1234):
            obj.options()
        else:
            st.write("you entered wrong pin")
    def options(self):
        st.write("1.Deposit")
        st.write("2.withdraw")
        st.write("3.balenquiry")
        st.write("4.exit")
        choice = st.number_input("Enter choice",key="choice_2")
        if(choice==1):
            obj.deposit()
        elif(choice==2):
            obj.withdraw()
        else:
            exit(0)
obj = Bank()
obj.validation()