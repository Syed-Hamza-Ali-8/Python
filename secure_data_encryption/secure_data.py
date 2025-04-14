import streamlit as st
import hashlib
from cryptography.fernet import Fernet

st.markdown(
    """
    <style>
    .stTextInput, .stTextArea {
        border-radius: 8px !important;
    }
    .title-style {
        font-size: 2.3em;
        font-weight: 700;
        color: #333;
    }
    .subheader-style {
        font-size: 1.4em;
        font-weight: 600;
        color: #444;
        margin-top: 20px;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #4f46e5, #3b82f6);
        color: white;
        padding: 0.6em 1.4em;
        border: none;
        border-radius: 8px;
        font-size: 1em;
        font-weight: 600;
        transition: 0.3s ease-in-out;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #6366f1, #2563eb);
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        cursor: pointer;
    }
    </style>
""",
    unsafe_allow_html=True,
)

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if "data_store" not in st.session_state:
    st.session_state.data_store = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = {}


def hash_string(text):
    return hashlib.sha256(text.encode()).hexdigest()


def generate_user_key(username):
    return Fernet.generate_key()


def get_cipher(user_key):
    return Fernet(user_key)


def encrypt_text(text, cipher):
    return cipher.encrypt(text.encode()).decode()


def decrypt_text(encrypted_text, cipher):
    return cipher.decrypt(encrypted_text.encode()).decode()


st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", width=60)
choice = st.sidebar.radio(
    "🔐 **Navigation**",
    (
        ["Login", "Register"]
        if not st.session_state.logged_in_user
        else ["Home", "Store Data", "Retrieve Data", "Logout"]
    ),
)

# --- Register Page ---
if choice == "Register":
    st.markdown(
        "<div class='title-style'>📝 Create an Account</div>", unsafe_allow_html=True
    )
    st.markdown("Secure your data with ease 🔒")

    with st.form("register_form"):
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        submitted = st.form_submit_button("Register")

    if submitted:
        if username and password:
            if len(password) < 6:
                st.error("⚠️ Password must be at least 6 characters.")
            elif username in st.session_state.users:
                st.warning("⚠️ Username already exists.")
            else:
                st.session_state.users[username] = {
                    "password_hash": hash_string(password),
                    "key": generate_user_key(username),
                }
                st.success("✅ Registration successful. You can now log in.")
        else:
            st.error("⚠️ Fill out both fields.")

# --- Login Page ---
elif choice == "Login":
    st.markdown(
        "<div class='title-style'>🔐 Welcome Back</div>", unsafe_allow_html=True
    )
    st.markdown("Login to manage your secure data 🧠")

    with st.form("login_form"):
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        user = st.session_state.users.get(username)
        if user and user["password_hash"] == hash_string(password):
            st.session_state.logged_in_user = username
            st.session_state.failed_attempts[username] = 0
            st.success(f"✅ Hello, {username}!")
            st.rerun()
        else:
            st.error("❌ Invalid credentials.")


elif st.session_state.logged_in_user:
    username = st.session_state.logged_in_user
    user_key = st.session_state.users[username]["key"]
    cipher = get_cipher(user_key)

    st.markdown(
        f"<div class='title-style'>🛡️ Encrypted Vault</div>", unsafe_allow_html=True
    )

    # Home
    if choice == "Home":
        st.markdown(
            f"<div class='subheader-style'>🏠 Welcome, {username}!</div>",
            unsafe_allow_html=True,
        )
        st.info(
            "Use this tool to **encrypt** and **retrieve** text securely. All data is protected with AES encryption."
        )

    # Store Data
    elif choice == "Store Data":
        st.markdown(
            "<div class='subheader-style'>📂 Store Data</div>", unsafe_allow_html=True
        )

        with st.form("encrypt_form"):
            user_text = st.text_area("🔤 Enter the data to encrypt:")
            passkey = st.text_input("🔑 Enter your passkey", type="password")
            submitted = st.form_submit_button("Encrypt & Store")

        if submitted:
            if user_text and passkey:
                hashed_passkey = hash_string(passkey)
                encrypted = encrypt_text(user_text, cipher)
                if username not in st.session_state.data_store:
                    st.session_state.data_store[username] = []
                st.session_state.data_store[username].append(
                    {"encrypted_text": encrypted, "passkey": hashed_passkey}
                )
                st.success("✅ Encrypted and stored successfully!")
                st.code(encrypted, language="text")
            else:
                st.warning("⚠️ Please enter some text and a passkey.")

    # Retrieve Data
    elif choice == "Retrieve Data":
        st.markdown(
            "<div class='subheader-style'>🔍 Retrieve Data</div>",
            unsafe_allow_html=True,
        )

        with st.form("decrypt_form"):
            encrypted_input = st.text_area("🧾 Paste the encrypted text:")
            passkey_input = st.text_input("🔑 Enter your passkey", type="password")
            submitted = st.form_submit_button("Decrypt")

        if submitted:
            if encrypted_input and passkey_input:
                hashed_passkey_input = hash_string(passkey_input)
                data_found = False
                for data in st.session_state.data_store.get(username, []):
                    if data["encrypted_text"] == encrypted_input:
                        data_found = True
                        if data["passkey"] == hashed_passkey_input:
                            try:
                                decrypted = decrypt_text(encrypted_input, cipher)
                                st.success("✅ Decryption successful!")
                                st.text_area(
                                    "📃 Your Decrypted Data:", decrypted, height=150
                                )
                            except Exception:
                                st.error(
                                    "⚠️ Decryption failed. Please check your encrypted text."
                                )
                        else:
                            st.session_state.failed_attempts[username] += 1
                            attempts_left = (
                                3 - st.session_state.failed_attempts[username]
                            )
                            if attempts_left > 0:
                                st.error(
                                    f"❌ Decryption failed! Attempts left: {attempts_left}"
                                )
                            else:
                                st.warning(
                                    "🔒 Too many failed attempts. Logging out..."
                                )
                                st.session_state.logged_in_user = None
                                st.rerun()
                if not data_found:
                    st.error("⚠️ Encrypted text not found.")
            else:
                st.warning("⚠️ Please enter both the encrypted text and passkey.")

    # Logout
    elif choice == "Logout":
        st.success("👋 Logged out successfully!")
        st.session_state.logged_in_user = None
        st.rerun()
