import streamlit as st
import os
import time


st.logo('static/simbolo.png')
if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

def change_photo_state():
     st.session_state["photo"]="done"

if "num1" not in st.session_state:
    st.session_state.num1=0

if "num2" not in st.session_state:
    st.session_state.num2=0

def division_algorithm(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    
    q = a // b  # Quotient
    r = a % b   # Remainder
    
    return q, r


def learning():
    col1, col2, col3 =st.columns(3)
    with col1:
        st.subheader("English")
        st.write("Reading")
        st.write("Listening")
        st.write("Writing")
        st.write("Speaking")

    with col2:
        st.subheader("Japanese")
        st.markdown('[Japanese N5](https://youtu.be/rMMhQ05KDN0?si=zq-8JtPtreSTvFdj)')
        st.write("Japanese N4")
        st.write("Japanses N3")
        st.write("Japanses N2")

    with col3:
        st.subheader("Programming")
        st.write("JavaScript")
        st.write("Python")
        st.write("Docker")
        

# st.sidebar.title("User Information")
# with st.sidebar.form(key="userName"):
#     name=st.text_input("Enter your name: ")
#     submit=st.form_submit_button("submit")

# st.write(f"Hello {name}")

st.sidebar.header("My First Streamlit App")

tab1, tab2, tab3, tab4 = st.tabs(["Home","Contact","Service","Log Out"])

with tab1:
    st.header("This is Home Page")

with tab2:
    st.header("This is contact page")

with tab3:
    st.header("Thses are our service for customer")
    st.write("1. Photo saving Gallary")
    st.write("2. Game Activity")
    st.write("3. Learning with us")

    choose=st.number_input("Enter a number between 1 and 3: ",step=1)

    if choose==1:
        st.write("You can save your precious memory")
        st.image(os.path.join(os.getcwd(),"static","Football.webp"))
         # Container with "+" sign
        with st.container(border=True):
            st.markdown("<h1 style='text-align: center;'>+</h1>", unsafe_allow_html=True)
            st.markdown("<p style='color:#cccccc;text-align:center'>Can add photo Click Browse files and save it...</p>",unsafe_allow_html=True)
            st.markdown(":100: :coffee:")

        # File uploader
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # Save the uploaded file
            save_path = os.path.join(os.getcwd(), "static", uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Saved file: {uploaded_file.name}")

            # Display the uploaded image
            st.image(save_path)

        st.subheader("Here is another session state")
        uploaded_photo = st.file_uploader("Upload a photo", on_change=change_photo_state)
        camera_photo = st.camera_input("Take a photo", on_change=change_photo_state)

        if st.session_state["photo"]=="done":
            progress_bar=st.progress(0)
            for per_completed in range(100):
                time.sleep(0.05)
                progress_bar.progress(per_completed+1)

            st.success("Photo uploaded successfully!")

            st.metric(label="Temperature", value="60°C",delta="3°C")

            with st.expander("click to read more"):
                st.write("Ohh! You are so beautiful")

                if uploaded_photo is None:
                    st.image(camera_photo)
                else:
                    st.image(uploaded_photo)
        
    
    elif choose==2:
        st.header("Game Section and Let's fun")
        
        with st.form(key="division_algorithm"):
            numOne=st.number_input("Enter first number",value=st.session_state.num1, key="num_one")
            numTwo=st.number_input("Enter first number",value=st.session_state.num2,  key="num_two")
            col1, col2 = st.columns(2)
            with col1:
                cal_btn = st.form_submit_button("Division Algorithm Calculation")
            with col2:
                mod_btn = st.form_submit_button("MOD Calculation")

            if cal_btn:
                quotient,remainder=division_algorithm(numOne,numTwo)
        
                with st.container(border=True):
                    st.write(f"Quotient: {quotient}, Remainder: {remainder}")

            if mod_btn:
                modRemainder=numOne%numTwo
                with st.container(border=True):
                    st.write(f"Answer: {modRemainder}")

            

    elif choose==3:
        st.header("You can improve your skill")
        learning()
    elif choose>=4:
        st.write("Please enter between 1 and 3")

        
        
        