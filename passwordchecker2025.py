
import re
import streamlit as st  

# Fixed page configuration with valid layout parameter
st.set_page_config(
    page_title="Password Strength Checker by Saeed Khan", 
    page_icon="🔑", 
    layout="centered"  # Changed from "center" to valid "centered"
)

# Custom CSS 
st.markdown("""
<style>
    .main {text-align: center;} 
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px;}
    .stButton button:hover {background-color: darkblue;}
</style>    
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.write("Enter Your Password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❎ Password should be **at least 8 characters long**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1  
    else:
        feedback.append("❎ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❎ Password should include **at least one number (0-9)**.")

    # Special character check
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❎ Password should include **at least one special character (!@#$%&*)**.")

    # Display password strength
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen")

    # Feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):  
            for item in feedback:
                st.write(item)

password = st.text_input("Enter Your Password", type="password", help="Ensure your password is strong 🔐")    

# Button functionality
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
