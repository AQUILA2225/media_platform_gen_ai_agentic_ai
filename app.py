import streamlit as st 
from dbConnection import con, cursor_Obj

st.title("Media Platform")

login,signup = st.tabs(
    ["Login","SignUp"]
)

cursor_Obj.execute("show databases")
dbs=cursor_Obj.fetchall()

for db in dbs:
    st.write(db)

with login:
    st.header("Login")
    with st.form("Login_Form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        btn = st.form_submit_button("Login")
        
    
    with signup:
        st.header("SignUp")
        with st.form("SignUp_Form"):
            
            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            btn = st.form_submit_button("SignUp")

        