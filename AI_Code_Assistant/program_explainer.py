import streamlit as st
import google.generativeai as genai
import base64
import time
from pymongo import MongoClient
import re

MONGO_URI = st.secrets["MONGO_URI"]
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

st.set_page_config(page_title="AI Code Assistant", layout="wide")

client = MongoClient(MONGO_URI)
db = client["code_assistant_db"]
users_collection = db["users"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# Email validation function
def is_valid_email(email):
    # Basic email regex pattern
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def login_page():
    st.title("🔐 Login to Access AI Code Assistant")
    with st.form("login_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        submit = st.form_submit_button("Login")

        if submit:
            if name.strip() == "" or email.strip() == "":
                st.warning("Please enter both Name and Email.")
            elif not is_valid_email(email):  # Validate email format
                st.warning("⚠️ Please enter a valid email address.")
            else:
                with st.spinner("Logging you in... Please wait"):
                    time.sleep(2)

                    existing_user = users_collection.find_one({"email": email})
                    if existing_user:
                        st.warning("⚠️ Email already exists. Try another email.")
                        st.stop()

                    users_collection.insert_one({"name": name, "email": email})

                    user = users_collection.find_one({"email": email})
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.session_state.user_name = user["name"]
                    st.rerun()

def main_app():
    st.sidebar.success(f"Welcome, {st.session_state.user_name}! 👋")

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('models/gemini-1.5-flash')

    def detect_language(code):
        code = code.lower()
        if "def " in code or "import " in code or "print(" in code:
            return "Python"
        elif "#include" in code or "cout <<" in code:
            return "C++"
        elif "public static void main" in code or "system.out.println" in code:
            return "Java"
        elif "function(" in code or "console.log(" in code or "=>" in code:
            return "JavaScript"
        return "Unknown"

    dark_css = """
    <style>
    button[kind="primary"] {
        background-color: #10b981 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: background-color 0.3s ease;
    }
    button[kind="primary"]:hover {
        background-color: #0e9e6e !important;
        color: white !important;
    }
    </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)
    st.title("💻 Custom Code Explainer & Optimizer")

    with st.sidebar:
        st.header("Settings")
        selected_language = st.selectbox("Select Code Language:", ['Python', 'JavaScript', 'C++', 'Java'], key="language_select")
        output_lang = st.selectbox("Select Explanation Language:", ['English', 'Urdu'])
        line_by_line = st.checkbox("Explain Line by Line")
        st.markdown("---")
        st.markdown("Developed by Syed Hamza Ali ([LinkedIn](https://www.linkedin.com/in/hamza-ali-b72b582ab))")

    code_input = st.text_area("🚀 Paste your code here:", height=300, key="code_input")
    detected_lang = detect_language(code_input)
    language_match = (detected_lang == selected_language) or detected_lang == "Unknown" or code_input.strip() == ""

    if code_input:
        st.markdown(f"**🔍 Detected Language:** <span style='color: #10b981; font-weight:bold;'>{detected_lang}</span>", unsafe_allow_html=True)
        if detected_lang != "Unknown" and detected_lang != selected_language:
            st.warning(f"⚠️ It seems like the code is written in **{detected_lang}**, but you've selected **{selected_language}**.")
        elif detected_lang == "Unknown":
            st.info(f"ℹ️ Could not detect the language automatically. Please make sure you select the correct language.")

    col1, col2, col3 = st.columns(3)
    disable_buttons = (not language_match) or (not code_input.strip())

    with col1:
        explain_btn = st.button("📝 Explain Code", disabled=disable_buttons)
    with col2:
        optimize_btn = st.button("🚀 Optimize Code", disabled=disable_buttons)
    with col3:
        detect_btn = st.button("🛠️ Detect Errors", disabled=disable_buttons)

    if explain_btn:
        if not language_match:
            st.warning(f"⚠️ Please select the correct language first to proceed.")
            st.stop()
        with st.spinner("Explaining Code..."):
            explain_mode = "line by line with comments" if line_by_line else "in simple terms"
            prompt = f"Explain the following {detected_lang if detected_lang != 'Unknown' else selected_language} code {explain_mode} in {output_lang}:\n\n{code_input}"
            response = model.generate_content(prompt)
            st.subheader("📄 Code Explanation:")
            st.write(response.text)

    if optimize_btn:
        if not language_match:
            st.warning(f"⚠️ Please select the correct language first to proceed.")
            st.stop()
        with st.spinner("Optimizing Code..."):
            prompt = f"Optimize the following {detected_lang if detected_lang != 'Unknown' else selected_language} code for better performance and readability. Keep same functionality:\n\n{code_input}"
            response = model.generate_content(prompt)
            st.subheader("✨ Optimized Code:")
            st.code(response.text, language=selected_language.lower())

            b64 = base64.b64encode(response.text.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="optimized_code.txt">📥 Download Optimized Code</a>'
            st.markdown(href, unsafe_allow_html=True)

    if detect_btn:
        if not language_match:
            st.warning(f"⚠️ Please select the correct language first to proceed.")
            st.stop()
        with st.spinner("Detecting Errors..."):
            prompt = f"Check the following {detected_lang if detected_lang != 'Unknown' else selected_language} code for errors or inefficiencies and suggest improvements:\n\n{code_input}"
            response = model.generate_content(prompt)
            st.subheader("⚠️ Errors & Suggestions:")
            st.write(response.text)

    st.markdown("---")

if not st.session_state.logged_in:
    login_page()
else:
    main_app()
