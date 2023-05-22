import streamlit as st
def set_background_image():
    page_bg_img = '''
        <style>
        body {
            background-image: url("https://www.novaspect.com/website/media/impact-partner/CyberAsses-HeaderBG.jpg");
            background-size: cover;
            opacity: 0.8; /* Adjust the opacity value between 0 and 1 */
        }
        </style>
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
