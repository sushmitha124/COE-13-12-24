import streamlit as st
st.title("Gross Salary Calculator")
basic=st.number_input("Enter basic salary",min_value=0,step=1)
if st.button("Calculate Gross Salary"):
    if (basic<10000) :
        HRA = (67*basic)/100
        DA = (73*basic)/100
    elif (basic<20000):
        HRA = (69 * basic) / 100
        DA = (76 * basic) / 100
    else:
        HRA = (73 * basic) / 100
        DA = (89 * basic) / 100
    GS = HRA + DA + basic
    st.info(f"The basic salary is:{basic:.2f}")
    st.info(f"The hra is:{HRA:.2f}")
    st.info(f"The da is:{DA:.2f}")
    st.success(f"The final gross salary is:{GS:.2f}")

