import streamlit as st
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
   
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Logged in successfully!")
            # Add your application logic here
        else:
            st.error("Invalid username or password")

if __name__ == '__main__':
    main()
