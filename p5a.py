import streamlit as st
sal=st.number_input("enter the salary",min_value=1)
bill1=st.number_input("enter bill1")
bill2=st.number_input("enter bill2")
bill3=st.number_input("enter bill3")
total_bill=bill1+bill2+bill3
st.info(f"The total bill is:{total_bill}")
percentage=(total_bill*100)/sal
st.info(f"The total percentage is:{percentage}")