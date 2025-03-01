import streamlit as st
import matplotlib.pyplot as plt

# Define the quiz questions and answers
quiz_questions = [
    # Introduction to Python (10 questions)
    {
        "question": "What is Python primarily used for?",
        "options": ["Web development", "Data analysis", "Game development", "All of the above"],
        "answer": "All of the above",
        "topic": "Introduction to Python",
        "level": "Basic"
    },
    {
        "question": "Who created Python?",
        "options": ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum",
        "topic": "Introduction to Python",
        "level": "Basic"
    },
    {
        "question": "Which of the following is NOT a Python feature?",
        "options": ["Dynamic typing", "Compiled language", "Interpreted language", "Easy to learn"],
        "answer": "Compiled language",
        "topic": "Introduction to Python",
        "level": "Basic"
    },
    {
        "question": "What is the primary purpose of Python's `print()` function?",
        "options": [
            "To read user input",
            "To display output to the console",
            "To perform mathematical calculations",
            "To define a function"
        ],
        "answer": "To display output to the console",
        "topic": "Introduction to Python",
        "level": "Basic"
    },
    {
        "question": "Which of the following is a Python IDE?",
        "options": ["PyCharm", "Eclipse", "Visual Studio Code", "All of the above"],
        "answer": "All of the above",
        "topic": "Introduction to Python",
        "level": "Medium"
    },
    {
        "question": "What does PEP stand for in Python?",
        "options": ["Python Enhancement Proposal", "Python Execution Process", "Python Error Protocol", "Python Evaluation Process"],
        "answer": "Python Enhancement Proposal",
        "topic": "Introduction to Python",
        "level": "Medium"
    },
    {
        "question": "Which of the following is NOT a Python framework?",
        "options": ["Django", "Flask", "React", "FastAPI"],
        "answer": "React",
        "topic": "Introduction to Python",
        "level": "Medium"
    },
    {
        "question": "What is the purpose of Python's `__init__` method?",
        "options": ["To initialize an object", "To terminate an object", "To import modules", "To define a function"],
        "answer": "To initialize an object",
        "topic": "Introduction to Python",
        "level": "Advanced"
    },
    {
        "question": "What is the output of `print(type(3.14))`?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'complex'>"],
        "answer": "<class 'float'>",
        "topic": "Introduction to Python",
        "level": "Advanced"
    },
    {
        "question": "Which of the following is a Python package manager?",
        "options": ["pip", "npm", "yarn", "maven"],
        "answer": "pip",
        "topic": "Introduction to Python",
        "level": "Advanced"
    },

    # Data Types and Operators (10 questions)
    {
        "question": "Which of the following is NOT a Python data type?",
        "options": ["int", "string", "float", "double"],
        "answer": "double",
        "topic": "Data Types and Operators",
        "level": "Basic"
    },
    {
        "question": "What is the result of `5 + 3 * 2`?",
        "options": ["16", "11", "10", "13"],
        "answer": "11",
        "topic": "Data Types and Operators",
        "level": "Basic"
    },
    {
        "question": "What is the output of `print(10 / 3)`?",
        "options": ["3", "3.333", "3.0", "3.3333333333333335"],
        "answer": "3.3333333333333335",
        "topic": "Data Types and Operators",
        "level": "Basic"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["^", "**", "*", "//"],
        "answer": "**",
        "topic": "Data Types and Operators",
        "level": "Medium"
    },
    {
        "question": "What is the output of `print(10 // 3)`?",
        "options": ["3", "3.333", "3.0", "3.3333333333333335"],
        "answer": "3",
        "topic": "Data Types and Operators",
        "level": "Medium"
    },
    {
        "question": "What is the result of `'Hello' + 'World'`?",
        "options": ["HelloWorld", "Hello World", "Hello+World", "Error"],
        "answer": "HelloWorld",
        "topic": "Data Types and Operators",
        "level": "Medium"
    },
    {
        "question": "What is the output of `print(bool(0))`?",
        "options": ["True", "False", "0", "Error"],
        "answer": "False",
        "topic": "Data Types and Operators",
        "level": "Advanced"
    },
    {
        "question": "What is the result of `2 ** 3 ** 2`?",
        "options": ["64", "512", "16", "Error"],
        "answer": "512",
        "topic": "Data Types and Operators",
        "level": "Advanced"
    },
    {
        "question": "What is the output of `print(type([]))`?",
        "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
        "answer": "<class 'list'>",
        "topic": "Data Types and Operators",
        "level": "Advanced"
    },
    {
        "question": "What is the result of `10 % 3`?",
        "options": ["1", "3", "0", "Error"],
        "answer": "1",
        "topic": "Data Types and Operators",
        "level": "Advanced"
    },

    # Keywords and Variables (10 questions)
    {
        "question": "Which of the following is a valid variable name in Python?",
        "options": ["1var", "_var", "var-name", "var name"],
        "answer": "_var",
        "topic": "Keywords and Variables",
        "level": "Basic"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["def", "function", "define", "func"],
        "answer": "def",
        "topic": "Keywords and Variables",
        "level": "Basic"
    },
    {
        "question": "What is the output of `print(True + False)`?",
        "options": ["0", "1", "True", "Error"],
        "answer": "1",
        "topic": "Keywords and Variables",
        "level": "Basic"
    },
    {
        "question": "Which keyword is used to exit a loop in Python?",
        "options": ["stop", "exit", "break", "end"],
        "answer": "break",
        "topic": "Keywords and Variables",
        "level": "Medium"
    },
    {
        "question": "What is the output of `print(type(None))`?",
        "options": ["<class 'NoneType'>", "<class 'null'>", "<class 'void'>", "<class 'None'>"],
        "answer": "<class 'NoneType'>",
        "topic": "Keywords and Variables",
        "level": "Medium"
    },
    {
        "question": "Which keyword is used to define a class in Python?",
        "options": ["def", "obj", "constructor", "class"],
        "answer": "class",
        "topic": "Keywords and Variables",
        "level": "Medium"
    },
    {
        "question": "What is the output of `print(isinstance(3, int))`?",
        "options": ["3", "True", "False", "Error"],
        "answer": "True",
        "topic": "Keywords and Variables",
        "level": "Advanced"
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["try", "catch", "except", "handle"],
        "answer": "try",
        "topic": "Keywords and Variables",
        "level": "Advanced"
    },
    {
        "question": "What is the output of `print(globals() is locals())`?",
        "options": ["True", "False", "None", "Error"],
        "answer": "True",
        "topic": "Keywords and Variables",
        "level": "Advanced"
    },
    {
        "question": "Which keyword is used to import modules in Python?",
        "options": ["include", "require", "use", "import"],
        "answer": "import",
        "topic": "Keywords and Variables",
        "level": "Advanced"
    }
]

# Initialize session state to store user answers (as indices) for each topic
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# Initialize session state to track quiz submission for each topic
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = {}

# Initialize session state to track if balloons have been shown for each topic
if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = {}

# Initialize session state to track if the quiz has been submitted once for each topic
if "quiz_submitted_once" not in st.session_state:
    st.session_state.quiz_submitted_once = {}

# Initialize session state to store user details
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_roll_no" not in st.session_state:
    st.session_state.user_roll_no = ""
if "user_day" not in st.session_state:
    st.session_state.user_day = ""

# Initialize session state to track if the quiz has been started
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 5px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stMarkdown h1 {
        color: #4CAF50;
        text-align: center;
    }
    .stMarkdown h2 {
        color: #2c3e50;
    }
    .stMarkdown h3 {
        color: #34495e;
    }
    .stSuccess {
        color: #28a745;
    }
    .stError {
        color: #dc3545;
    }
    .stWarning {
        color: #ffc107;
    }
    /* Customize the dropdown */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #000000;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .stSelectbox div[data-baseweb="select"]:hover {
        border-color: #4CAF50;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        color: #ffffff; /* White text for selected option */
    }
    .stSelectbox div[data-baseweb="popover"] {
        background-color: #000000; /* Background for dropdown options */
        color: #ffffff; /* White text for dropdown options */
    }
    .stSelectbox div[data-baseweb="popover"] div {
        color: #ffffff; /* White text for dropdown options */
    }
    /* Ensure dropdown appears above other elements */
    .stSelectbox div[data-baseweb="popover"] {
        z-index: 1000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to display the quiz
def run_quiz():
    st.markdown("# 🐍 Python Quiz App")
    st.markdown("### Test your knowledge of Python basics!")

    # Collect user details if not already collected
    if not st.session_state.quiz_started:
        st.markdown("### Please enter your details to start the quiz:")
        st.session_state.user_name = st.text_input("Enter your name:")
        st.session_state.user_roll_no = st.text_input("Enter your roll number:")
        st.session_state.user_day = st.selectbox("Select Your Slot:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

        if st.button("Start Quiz"):
            if st.session_state.user_name and st.session_state.user_roll_no and st.session_state.user_day:
                st.session_state.quiz_started = True  # Mark quiz as started
                st.success("Details saved! You can now start the quiz.")
                st.rerun()  # Force a rerun to proceed to the quiz section
            else:
                st.error("Please fill in all the details to proceed.")
        return  # Stop further execution until details are entered and "Start Quiz" is clicked

    # Add a sidebar for topic selection
    st.sidebar.markdown("## 🎯 Select a Topic")
    topics = list(set(q["topic"] for q in quiz_questions))  # Get unique topics
    selected_topic = st.sidebar.selectbox("Choose a topic:", topics)

    # Initialize session state for the selected topic if not already initialized
    if selected_topic not in st.session_state.user_answers:
        st.session_state.user_answers[selected_topic] = [None] * len(
            [q for q in quiz_questions if q["topic"] == selected_topic]
        )
    if selected_topic not in st.session_state.quiz_submitted:
        st.session_state.quiz_submitted[selected_topic] = False
    if selected_topic not in st.session_state.balloons_shown:
        st.session_state.balloons_shown[selected_topic] = False
    if selected_topic not in st.session_state.quiz_submitted_once:
        st.session_state.quiz_submitted_once[selected_topic] = False

    # Filter questions based on the selected topic
    filtered_questions = [q for q in quiz_questions if q["topic"] == selected_topic]

    score = 0

    for i, q in enumerate(filtered_questions):
        st.markdown(f"### ❓ Question {i + 1}: {q['question']}")
        st.markdown(f"**Topic:** {q['topic']} | **Level:** {q['level']}")

        # Use the actual options without the placeholder
        options = q['options']

        # Display select box for options
        user_answer_index = st.selectbox(
            "Select an option:",
            options,  # Use the actual options
            key=f"question_{i}_{selected_topic}",  # Unique key for each question and topic
            index=st.session_state.user_answers[selected_topic][i]
            if st.session_state.user_answers[selected_topic][i] is not None
            else 0,
            disabled=st.session_state.quiz_submitted_once[selected_topic],  # Disable dropdown if quiz is submitted
        )

        # Store the user's answer index in session state
        st.session_state.user_answers[selected_topic][i] = options.index(user_answer_index) if user_answer_index else None

    # Add a submit button (disabled if quiz has already been submitted once for the selected topic)
    if not st.session_state.quiz_submitted_once[selected_topic]:
        if st.button("Submit Quiz 🚀"):
            st.session_state.quiz_submitted[selected_topic] = True
            st.session_state.quiz_submitted_once[selected_topic] = True  # Mark quiz as submitted once
            st.rerun()  # Force a rerun to immediately disable the button
    else:
        st.button("Submit Quiz 🚀", disabled=True)  # Disable the button if already submitted

    # Show results and additional buttons after submission
    if st.session_state.quiz_submitted[selected_topic]:
        st.write("---")
        st.markdown("## 📊 Results")

        # Evaluate answers
        for i, q in enumerate(filtered_questions):
            user_answer_index = st.session_state.user_answers[selected_topic][i]
            options = q['options']

            # Check if the user selected an answer
            if user_answer_index is not None:  # Skip if no answer is selected
                user_answer = options[user_answer_index]  # Get the selected option text
                if user_answer == q['answer']:
                    score += 1

        # Display final score with user details
        st.write("---")
        st.markdown(f"## 🎉 {st.session_state.user_name} (Roll No: {st.session_state.user_roll_no}), your score is: **{score}/{len(filtered_questions)}**")

        # Show motivational quote if score is less than 5
        if score < 5:
            st.markdown("### Don't lose hope! You'll get better day by day. 💪")

        # Data Visualization: Bar chart for score
        st.write("---")
        st.markdown("## 📈 Your Performance")
        fig, ax = plt.subplots()
        ax.bar(["Your Score", "Total Questions"], [score, len(filtered_questions)], color=["#4CAF50", "#34495e"])
        ax.set_ylim(0, len(filtered_questions))
        st.pyplot(fig)

        # Show balloons if score > 5 and balloons have not been shown yet for the selected topic
        if score > 5 and not st.session_state.balloons_shown[selected_topic]:
            st.balloons()
            st.session_state.balloons_shown[selected_topic] = True

        # Add a restart button
        if st.button("Restart Quiz 🔄"):
            st.session_state.quiz_submitted[selected_topic] = False
            st.session_state.user_answers[selected_topic] = [None] * len(filtered_questions)
            st.session_state.balloons_shown[selected_topic] = False
            st.session_state.quiz_submitted_once[selected_topic] = False  # Reset submission eligibility
            st.rerun()

        # Add a show answers button
        if st.button("Show Answers 📝"):
            st.write("---")
            st.markdown("## 📝 Correct Answers")
            for i, q in enumerate(filtered_questions):
                st.markdown(f"### ❓ Question {i + 1}: {q['question']}")
                st.markdown(f"**Correct answer:** {q['answer']}")

        # Footer
        st.write("---")
        st.markdown("### Made with ❤️ by Hamza")

# Run the quiz app
if __name__ == "__main__":
    run_quiz()
