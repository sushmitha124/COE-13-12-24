import streamlit as st
plt.title("Calculation of grades")
p_score=st.number_input("Enter project score",min_value=0,step=1)
i_score=st.number_input("Enter internal score",min_value=0,step=1)
e_score=st.number_input("Enter external score",min_value=0,step=1)
if st.button("Calculate Grade"):
    if(p_score>=50 and i_score>=50 and e_score>=50):
        total=((70*p_score)/100)+((10*i_score)/100)+((20*e_score)/100)
        if(total>=90):
            st.write("A grade")
        elif(total>80):
            st.write("B grade")
        else:
            st.write("C grade")
    else:
        if(p_score<50):
            st.write("failed in project")
        if(i_score<50):
            st.write("failed in internal")
        if(e_score < 50):
            st.write("failed in external")