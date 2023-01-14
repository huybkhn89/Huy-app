import streamlit as st

ten = st.text_input("First Name:")
ho = st.text_input("Last Name:")
st.write("Hello ",ten,ho)

Submit = st.button("Submit")
if Submit:
    st.text("Da submit")

with open("Tep.jpg","rb") as anh:
    st.download_button(
        label="Tai anh",
        data=anh,
        file_name="Anh tai ve cua Tep.png",
        mime="image/png"
    )

with st.form("Form đăng ký:"):
    Name= st.text_input("Name :")
    Phone = st.text_input("Phone :")
    Submit = st.form_submit_button("Submit")
    if Submit:
        st.write(Name,"-",Phone)
