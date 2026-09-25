import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Master",
    page_icon="🎓",
    layout="centered"
)


# =========================================================
# SESSION STATE
# =========================================================

# -------------------------
# Profile
# -------------------------

profile_defaults = {
    "profile_name": "",
    "profile_age": 10,
    "profile_school": "",
    "profile_subject": "",
    "profile_hobby": "",
    "profile_created": False,
}

for key, value in profile_defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# -------------------------
# Grade Calculator
# -------------------------

if "grade_subjects" not in st.session_state:
    st.session_state.grade_subjects = [
        {"name": "Math", "grade": 0.0},
        {"name": "English", "grade": 0.0},
        {"name": "Science", "grade": 0.0},
    ]

if "grade_calculated" not in st.session_state:
    st.session_state.grade_calculated = False

if "grade_average" not in st.session_state:
    st.session_state.grade_average = 0.0

if "grade_gpa" not in st.session_state:
    st.session_state.grade_gpa = 0.0

if "grade_letter" not in st.session_state:
    st.session_state.grade_letter = "F"


# -------------------------
# Calculator
# -------------------------

calculator_defaults = {
    "calc_display": "0",
    "calc_first_number": None,
    "calc_operation": None,
    "calc_new_number": True,
}

for key, value in calculator_defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# -------------------------
# Quiz
# -------------------------

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = [
        {
            "question": "",
            "A": "",
            "B": "",
            "C": "",
            "D": "",
            "correct": "A",
        }
    ]

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_percentage" not in st.session_state:
    st.session_state.quiz_percentage = 0.0


# =========================================================
# BACKGROUND OPTIONS
# =========================================================

backgrounds = {
    "🌌 Galaxy": {
        "colors": ["#020617", "#312e81", "#7c3aed", "#020617"],
        "speed": "15s",
    },
    "🌊 Ocean": {
        "colors": ["#082f49", "#0369a1", "#0891b2", "#164e63"],
        "speed": "12s",
    },
    "🌅 Sunset": {
        "colors": ["#431407", "#c2410c", "#ea580c", "#be123c"],
        "speed": "12s",
    },
    "🌲 Forest": {
        "colors": ["#022c22", "#065f46", "#15803d", "#052e16"],
        "speed": "12s",
    },
    "🌈 Aurora": {
        "colors": ["#111827", "#7c3aed", "#0891b2", "#ec4899"],
        "speed": "10s",
    },
}


if "background_choice" not in st.session_state:
    st.session_state.background_choice = "🌌 Galaxy"


# =========================================================
# BACKGROUND CSS
# =========================================================

bg = backgrounds[st.session_state.background_choice]

c1, c2, c3, c4 = bg["colors"]

st.markdown(
    f"""
    <style>

    /* ==========================================
       MAIN ANIMATED BACKGROUND
       ========================================== */

    .stApp {{
        background:
            radial-gradient(
                circle at 15% 20%,
                {c2} 0%,
                transparent 25%
            ),
            radial-gradient(
                circle at 85% 30%,
                {c3} 0%,
                transparent 25%
            ),
            radial-gradient(
                circle at 50% 90%,
                {c4} 0%,
                transparent 30%
            ),
            linear-gradient(
                135deg,
                {c1},
                {c2},
                {c3},
                {c4}
            );

        background-size: 400% 400%;

        animation:
            backgroundMove {bg["speed"]} ease infinite;

        min-height: 100vh;
    }}


    @keyframes backgroundMove {{
        0% {{
            background-position: 0% 50%;
        }}

        25% {{
            background-position: 50% 100%;
        }}

        50% {{
            background-position: 100% 50%;
        }}

        75% {{
            background-position: 50% 0%;
        }}

        100% {{
            background-position: 0% 50%;
        }}
    }}


    /* ==========================================
       FLOATING LIGHTS
       ========================================== */

    .stApp::before {{
        content: "";
        position: fixed;

        width: 250px;
        height: 250px;

        left: 5%;
        top: 15%;

        border-radius: 50%;

        background: rgba(255,255,255,0.08);

        filter: blur(30px);

        animation: floatOne 8s ease-in-out infinite;

        pointer-events: none;
    }}


    .stApp::after {{
        content: "";

        position: fixed;

        width: 300px;
        height: 300px;

        right: 5%;
        bottom: 10%;

        border-radius: 50%;

        background: rgba(255,255,255,0.07);

        filter: blur(35px);

        animation: floatTwo 10s ease-in-out infinite;

        pointer-events: none;
    }}


    @keyframes floatOne {{
        0%, 100% {{
            transform: translate(0, 0);
        }}

        50% {{
            transform: translate(100px, 80px);
        }}
    }}


    @keyframes floatTwo {{
        0%, 100% {{
            transform: translate(0, 0);
        }}

        50% {{
            transform: translate(-100px, -70px);
        }}
    }}


    /* ==========================================
       CONTENT
       ========================================== */

    .block-container {{
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }}


    /* ==========================================
       HEADINGS
       ========================================== */

    h1, h2, h3 {{
        color: white !important;
    }}


    p, label {{
        color: white !important;
    }}


    /* ==========================================
       SIDEBAR
       ========================================== */

    [data-testid="stSidebar"] {{
        background: rgba(5, 10, 25, 0.96);
    }}


    [data-testid="stSidebar"] * {{
        color: white !important;
    }}


    /* ==========================================
       GLASS CARDS
       ========================================== */

    .glass {{
        background: rgba(15, 23, 42, 0.78);

        border: 1px solid rgba(255,255,255,0.15);

        border-radius: 22px;

        padding: 25px;

        margin: 15px 0;

        box-shadow:
            0 15px 40px rgba(0,0,0,0.3);

        backdrop-filter: blur(15px);
    }}


    /* ==========================================
       PROFILE RESULT
       ========================================== */

    .profile-result {{
        background:
            linear-gradient(
                135deg,
                rgba(124,58,237,0.92),
                rgba(37,99,235,0.92)
            );

        border-radius: 25px;

        padding: 30px;

        margin-top: 25px;

        text-align: center;

        color: white;

        box-shadow:
            0 15px 40px rgba(0,0,0,0.35);

        animation: resultAppear 0.6s ease;
    }}


    @keyframes resultAppear {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}

        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}


    .profile-avatar {{
        font-size: 70px;
    }}


    .profile-name {{
        font-size: 36px;
        font-weight: bold;
        margin: 10px;
    }}


    /* ==========================================
       CALCULATOR DISPLAY
       ========================================== */

    .calc-display {{
        background: rgba(0,0,0,0.82);

        color: white;

        border-radius: 20px;

        padding: 25px;

        text-align: right;

        font-size: 42px;

        font-family: monospace;

        margin-bottom: 20px;

        box-shadow:
            inset 0 0 25px rgba(0,0,0,0.5),
            0 10px 30px rgba(0,0,0,0.3);
    }}


    /* ==========================================
       GRADE RESULT
       ========================================== */

    .grade-result {{
        background:
            linear-gradient(
                135deg,
                rgba(16,185,129,0.95),
                rgba(5,150,105,0.95)
            );

        color: white;

        padding: 30px;

        border-radius: 25px;

        text-align: center;

        margin-top: 25px;

        box-shadow:
            0 15px 40px rgba(0,0,0,0.35);

        animation: resultAppear 0.6s ease;
    }}


    .big-letter {{
        font-size: 90px;
        font-weight: bold;
    }}


    /* ==========================================
       BUTTONS
       ========================================== */

    .stButton > button {{
        border-radius: 13px;

        font-weight: bold;

        min-height: 45px;

        transition: 0.2s;
    }}


    .stButton > button:hover {{
        transform: translateY(-3px);

        box-shadow:
            0 8px 20px rgba(0,0,0,0.3);
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 Student Master")

st.sidebar.write("Your all-in-one student app!")

st.sidebar.divider()

page = st.sidebar.radio(
    "📱 Choose a program:",
    [
        "👤 My Profile",
        "🧮 Calculator",
        "📊 Grade Calculator",
        "📝 Quiz Master",
    ],
)


st.sidebar.divider()

st.sidebar.subheader("🎨 Background")

selected_background = st.sidebar.selectbox(
    "Choose your animated background:",
    list(backgrounds.keys()),
    index=list(backgrounds.keys()).index(
        st.session_state.background_choice
    ),
)

if selected_background != st.session_state.background_choice:

    st.session_state.background_choice = selected_background

    st.rerun()


# =========================================================
# MY PROFILE
# =========================================================

if page == "👤 My Profile":

    st.title("👤 My Profile")

    st.write(
        "Create your personal student profile!"
    )

    st.markdown(
        '<div class="glass">',
        unsafe_allow_html=True,
    )

    # -------------------------
    # Name
    # -------------------------

    name = st.text_input(
        "👋 What is your name?",
        value=st.session_state.profile_name,
        placeholder="Enter your name...",
        key="profile_name_input",
    )

    # -------------------------
    # Age
    # -------------------------

    st.subheader("🎂 How old are you?")

    age_col1, age_col2, age_col3 = st.columns(
        [1, 2, 1]
    )

    with age_col1:

        if st.button(
            "➖",
            use_container_width=True,
            key="profile_age_minus",
        ):

            if st.session_state.profile_age > 1:

                st.session_state.profile_age -= 1

                st.rerun()


    with age_col2:

        st.markdown(
            f"""
            <div style="
                background: rgba(0,0,0,0.45);
                border-radius: 15px;
                padding: 12px;
                text-align: center;
                color: white;
                font-size: 30px;
                font-weight: bold;
            ">
                {st.session_state.profile_age}
            </div>
            """,
            unsafe_allow_html=True,
        )


    with age_col3:

        if st.button(
            "➕",
            use_container_width=True,
            key="profile_age_plus",
        ):

            if st.session_state.profile_age < 100:

                st.session_state.profile_age += 1

                st.rerun()


    # -------------------------
    # School
    # -------------------------

    school = st.text_input(
        "🏫 What school do you go to?",
        value=st.session_state.profile_school,
        placeholder="Enter your school...",
        key="profile_school_input",
    )


    # -------------------------
    # Favorite subject
    # -------------------------

    favorite_subject = st.text_input(
        "📚 What is your favorite subject?",
        value=st.session_state.profile_subject,
        placeholder="Example: Mathematics",
        key="profile_subject_input",
    )


    # -------------------------
    # Favorite hobby
    # -------------------------

    hobby = st.text_input(
        "🎮 What is your favorite hobby?",
        value=st.session_state.profile_hobby,
        placeholder="Example: Gaming",
        key="profile_hobby_input",
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


    # =====================================================
    # MAKE PROFILE
    # =====================================================

    if st.button(
        "✨ Make Profile",
        use_container_width=True,
        type="primary",
        key="make_profile_button",
    ):

        if not name.strip():

            st.error("❌ Please enter your name.")

        elif not school.strip():

            st.error("❌ Please enter your school.")

        elif not favorite_subject.strip():

            st.error(
                "❌ Please enter your favorite subject."
            )

        elif not hobby.strip():

            st.error(
                "❌ Please enter your favorite hobby."
            )

        else:

            # Save everything

            st.session_state.profile_name = name.strip()

            st.session_state.profile_school = school.strip()

            st.session_state.profile_subject = (
                favorite_subject.strip()
            )

            st.session_state.profile_hobby = hobby.strip()

            st.session_state.profile_created = True

            st.success(
                "🎉 Your profile has been created!"
            )

            st.rerun()


    # =====================================================
    # PROFILE DISPLAY
    # =====================================================

    if st.session_state.profile_created:

        st.divider()

        # IMPORTANT:
        # This uses Streamlit components instead of
        # injecting the user's information into HTML.

        st.markdown(
            '<div class="profile-result">',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="profile-avatar">👤</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="profile-name">Your Profile</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )

        # Display the actual values using Streamlit

        st.info(
            f"👋 **Name:** {st.session_state.profile_name}"
        )

        st.info(
            f"🎂 **Age:** {st.session_state.profile_age}"
        )

        st.info(
            f"🏫 **School:** {st.session_state.profile_school}"
        )

        st.info(
            "📚 **Favorite Subject:** "
            + st.session_state.profile_subject
        )

        st.info(
            "🎮 **Favorite Hobby:** "
            + st.session_state.profile_hobby
        )

        st.success(
            f"🌟 Welcome, {st.session_state.profile_name}! "
            "Have fun using Student Master!"
        )


# =========================================================
# CALCULATOR
# =========================================================

elif page == "🧮 Calculator":

    st.title("🧮 Calculator")

    st.write(
        "Calculate anything from simple addition to division."
    )


    # =====================================================
    # CALCULATOR FUNCTIONS
    # =====================================================

    def calc_number(number):

        if (
            st.session_state.calc_new_number
            or st.session_state.calc_display in ["0", "Error"]
        ):

            st.session_state.calc_display = number

            st.session_state.calc_new_number = False

        else:

            st.session_state.calc_display += number


    def calc_decimal():

        if st.session_state.calc_new_number:

            st.session_state.calc_display = "0."

            st.session_state.calc_new_number = False

        elif "." not in st.session_state.calc_display:

            st.session_state.calc_display += "."


    def calc_operation(operation):

        if st.session_state.calc_display == "Error":
            return

        st.session_state.calc_first_number = float(
            st.session_state.calc_display
        )

        st.session_state.calc_operation = operation

        st.session_state.calc_new_number = True


    def calc_equals():

        if (
            st.session_state.calc_first_number is None
            or st.session_state.calc_operation is None
        ):
            return

        second = float(
            st.session_state.calc_display
        )

        first = st.session_state.calc_first_number

        operation = st.session_state.calc_operation


        if operation == "+":

            result = first + second

        elif operation == "-":

            result = first - second

        elif operation == "×":

            result = first * second

        elif operation == "÷":

            if second == 0:

                st.session_state.calc_display = "Error"

                st.session_state.calc_first_number = None

                st.session_state.calc_operation = None

                st.session_state.calc_new_number = True

                return

            result = first / second

        else:

            return


        if result == int(result):

            st.session_state.calc_display = str(
                int(result)
            )

        else:

            st.session_state.calc_display = str(
                round(result, 10)
            )


        st.session_state.calc_first_number = None

        st.session_state.calc_operation = None

        st.session_state.calc_new_number = True


    def calc_clear():

        st.session_state.calc_display = "0"

        st.session_state.calc_first_number = None

        st.session_state.calc_operation = None

        st.session_state.calc_new_number = True


    def calc_backspace():

        if not st.session_state.calc_new_number:

            current = st.session_state.calc_display

            current = current[:-1]

            if current == "" or current == "-":

                current = "0"

            st.session_state.calc_display = current


    # =====================================================
    # DISPLAY
    # =====================================================

    st.markdown(
        f"""
        <div class="calc-display">
            {st.session_state.calc_display}
        </div>
        """,
        unsafe_allow_html=True,
    )


    # =====================================================
    # BUTTONS
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "AC",
            use_container_width=True,
            key="calculator_ac",
        ):

            calc_clear()

            st.rerun()

    with c2:

        if st.button(
            "⌫",
            use_container_width=True,
            key="calculator_backspace",
        ):

            calc_backspace()

            st.rerun()

    with c3:

        if st.button(
            "÷",
            use_container_width=True,
            key="calculator_divide",
        ):

            calc_operation("÷")

            st.rerun()

    with c4:

        if st.button(
            "×",
            use_container_width=True,
            key="calculator_multiply",
        ):

            calc_operation("×")

            st.rerun()


    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "7",
            use_container_width=True,
            key="calculator_7",
        ):

            calc_number("7")

            st.rerun()

    with c2:

        if st.button(
            "8",
            use_container_width=True,
            key="calculator_8",
        ):

            calc_number("8")

            st.rerun()

    with c3:

        if st.button(
            "9",
            use_container_width=True,
            key="calculator_9",
        ):

            calc_number("9")

            st.rerun()

    with c4:

        if st.button(
            "-",
            use_container_width=True,
            key="calculator_minus",
        ):

            calc_operation("-")

            st.rerun()


    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "4",
            use_container_width=True,
            key="calculator_4",
        ):

            calc_number("4")

            st.rerun()

    with c2:

        if st.button(
            "5",
            use_container_width=True,
            key="calculator_5",
        ):

            calc_number("5")

            st.rerun()

    with c3:

        if st.button(
            "6",
            use_container_width=True,
            key="calculator_6",
        ):

            calc_number("6")

            st.rerun()

    with c4:

        if st.button(
            "+",
            use_container_width=True,
            key="calculator_plus",
        ):

            calc_operation("+")

            st.rerun()


    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "1",
            use_container_width=True,
            key="calculator_1",
        ):

            calc_number("1")

            st.rerun()

    with c2:

        if st.button(
            "2",
            use_container_width=True,
            key="calculator_2",
        ):

            calc_number("2")

            st.rerun()

    with c3:

        if st.button(
            "3",
            use_container_width=True,
            key="calculator_3",
        ):

            calc_number("3")

            st.rerun()

    with c4:

        if st.button(
            "=",
            use_container_width=True,
            key="calculator_equals",
        ):

            calc_equals()

            st.rerun()


    c1, c2 = st.columns([2, 1])

    with c1:

        if st.button(
            "0",
            use_container_width=True,
            key="calculator_0",
        ):

            calc_number("0")

            st.rerun()

    with c2:

        if st.button(
            ".",
            use_container_width=True,
            key="calculator_decimal",
        ):

            calc_decimal()

            st.rerun()


# =========================================================
# GRADE CALCULATOR
# =========================================================

elif page == "📊 Grade Calculator":

    st.title("📊 Grade Calculator")

    st.write(
        "Enter your grades to calculate your overall "
        "average, GPA, and letter grade."
    )

    st.info(
        "📚 Math, English, and Science are automatically "
        "included. You can add more subjects."
    )


    # =====================================================
    # ADD SUBJECT
    # =====================================================

    if st.button(
        "➕ Add More Subjects",
        use_container_width=True,
        key="grade_add_subject",
    ):

        if len(st.session_state.grade_subjects) < 20:

            number = len(
                st.session_state.grade_subjects
            ) + 1

            st.session_state.grade_subjects.append(
                {
                    "name": f"Subject {number}",
                    "grade": 0.0,
                }
            )

            st.session_state.grade_calculated = False

            st.rerun()

        else:

            st.warning(
                "You can have a maximum of 20 subjects."
            )


    st.divider()


    # =====================================================
    # SUBJECT INPUTS
    # =====================================================

    for i in range(
        len(st.session_state.grade_subjects)
    ):

        subject = st.session_state.grade_subjects[i]

        st.subheader(
            f"📘 Subject {i + 1}"
        )

        col1, col2 = st.columns([2, 1])


        with col1:

            subject_name = st.text_input(
                "Subject name",
                value=subject["name"],
                key=f"subject_name_{i}",
            )

            st.session_state.grade_subjects[i][
                "name"
            ] = subject_name


        with col2:

            grade = st.number_input(
                "Grade / 100",
                min_value=0.0,
                max_value=100.0,
                value=float(subject["grade"]),
                step=1.0,
                key=f"subject_grade_{i}",
            )

            st.session_state.grade_subjects[i][
                "grade"
            ] = grade


        # Only extra subjects can be removed

        if i >= 3:

            if st.button(
                "🗑️ Remove",
                key=f"remove_grade_subject_{i}",
            ):

                st.session_state.grade_subjects.pop(i)

                st.session_state.grade_calculated = False

                st.rerun()


        st.divider()


    # =====================================================
    # CALCULATE GRADE
    # =====================================================

    if st.button(
        "📊 Calculate Grade",
        use_container_width=True,
        type="primary",
        key="calculate_grade_button",
    ):

        grades = []

        for subject in st.session_state.grade_subjects:

            grades.append(
                float(subject["grade"])
            )


        if grades:

            average = sum(grades) / len(grades)

        else:

            average = 0.0


        # -------------------------
        # Letter grade
        # -------------------------

        if average >= 90:

            letter = "A"

        elif average >= 80:

            letter = "B"

        elif average >= 70:

            letter = "C"

        elif average >= 60:

            letter = "D"

        else:

            letter = "F"


        # -------------------------
        # GPA
        # -------------------------

        if letter == "A":

            gpa = 4.0

        elif letter == "B":

            gpa = 3.0

        elif letter == "C":

            gpa = 2.0

        elif letter == "D":

            gpa = 1.0

        else:

            gpa = 0.0


        st.session_state.grade_average = average

        st.session_state.grade_gpa = gpa

        st.session_state.grade_letter = letter

        st.session_state.grade_calculated = True

        st.rerun()


    # =====================================================
    # GRADE RESULTS
    # =====================================================

    if st.session_state.grade_calculated:

        st.divider()

        st.subheader("🎓 Your Results")


        # Use Streamlit components for the actual values.
        # This prevents the values from being interpreted
        # as HTML/code.

        result_col1, result_col2, result_col3 = st.columns(3)


        with result_col1:

            st.metric(
                "📈 Average",
                f"{st.session_state.grade_average:.1f}%",
            )


        with result_col2:

            st.metric(
                "🎓 GPA",
                f"{st.session_state.grade_gpa:.1f} / 4.0",
            )


        with result_col3:

            st.metric(
                "📝 Letter",
                st.session_state.grade_letter,
            )


        st.progress(
            int(
                st.session_state.grade_average
            )
        )


        letter = st.session_state.grade_letter


        if letter == "A":

            st.success(
                "🌟 Excellent work!"
            )

        elif letter == "B":

            st.success(
                "👏 Great job!"
            )

        elif letter == "C":

            st.info(
                "👍 Good effort! Keep practicing."
            )

        elif letter == "D":

            st.warning(
                "📚 Keep working and you can improve."
            )

        else:

            st.error(
                "💪 Keep practicing. You can improve!"
            )


# =========================================================
# QUIZ MASTER
# =========================================================

elif page == "📝 Quiz Master":

    st.title("📝 Quiz Master")

    st.write(
        "Create your own multiple-choice quiz!"
    )


    # =====================================================
    # QUIZ SETUP
    # =====================================================

    if not st.session_state.quiz_started:

        st.subheader("⚙️ Quiz Setup")

        question_count = len(
            st.session_state.quiz_questions
        )

        st.write(
            f"Number of questions: **{question_count}**"
        )


        col1, col2 = st.columns(2)


        with col1:

            if st.button(
                "➕ Add Question",
                use_container_width=True,
                key="quiz_add_question",
            ):

                if question_count < 50:

                    st.session_state.quiz_questions.append(
                        {
                            "question": "",
                            "A": "",
                            "B": "",
                            "C": "",
                            "D": "",
                            "correct": "A",
                        }
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Maximum is 50 questions."
                    )


        with col2:

            if st.button(
                "➖ Remove Question",
                use_container_width=True,
                key="quiz_remove_question",
            ):

                if question_count > 1:

                    st.session_state.quiz_questions.pop()

                    st.rerun()


        st.divider()


        # =================================================
        # QUESTIONS
        # =================================================

        for i in range(
            len(st.session_state.quiz_questions)
        ):

            question = st.session_state.quiz_questions[i]

            st.subheader(
                f"Question {i + 1}"
            )


            question_text = st.text_input(
                "Question",
                value=question["question"],
                placeholder="Enter your question...",
                key=f"quiz_question_input_{i}",
            )

            question["question"] = question_text


            col1, col2 = st.columns(2)


            with col1:

                a = st.text_input(
                    "Choice A",
                    value=question["A"],
                    key=f"quiz_a_{i}",
                )

                b = st.text_input(
                    "Choice B",
                    value=question["B"],
                    key=f"quiz_b_{i}",
                )

                question["A"] = a

                question["B"] = b


            with col2:

                c = st.text_input(
                    "Choice C",
                    value=question["C"],
                    key=f"quiz_c_{i}",
                )

                d = st.text_input(
                    "Choice D",
                    value=question["D"],
                    key=f"quiz_d_{i}",
                )

                question["C"] = c

                question["D"] = d


            correct = st.radio(
                "Correct answer",
                ["A", "B", "C", "D"],
                index=["A", "B", "C", "D"].index(
                    question["correct"]
                ),
                horizontal=True,
                key=f"quiz_correct_{i}",
            )

            question["correct"] = correct

            st.divider()


        # =================================================
        # START QUIZ
        # =================================================

        if st.button(
            "▶️ Start Quiz",
            use_container_width=True,
            type="primary",
            key="start_quiz_button",
        ):

            valid = True


            for i, question in enumerate(
                st.session_state.quiz_questions
            ):

                if not question["question"].strip():

                    st.error(
                        f"Please enter Question {i + 1}."
                    )

                    valid = False


                for option in ["A", "B", "C", "D"]:

                    if not question[option].strip():

                        st.error(
                            f"Please enter Choice {option} "
                            f"for Question {i + 1}."
                        )

                        valid = False


            if valid:

                st.session_state.quiz_started = True

                st.session_state.quiz_finished = False

                st.rerun()


    # =====================================================
    # QUIZ MODE
    # =====================================================

    elif (
        st.session_state.quiz_started
        and not st.session_state.quiz_finished
    ):

        st.subheader("🎯 Quiz Time!")

        st.write(
            "Choose one answer for every question."
        )

        st.divider()


        for i, question in enumerate(
            st.session_state.quiz_questions
        ):

            st.subheader(
                f"{i + 1}. {question['question']}"
            )


            choices = {
                "A": question["A"],
                "B": question["B"],
                "C": question["C"],
                "D": question["D"],
            }


            st.radio(
                "Choose your answer:",
                ["A", "B", "C", "D"],
                format_func=lambda x, choices=choices:
                    f"Choice {x}: {choices[x]}",
                index=None,
                key=f"quiz_answer_{i}",
            )


            st.divider()


        # =================================================
        # FINISH QUIZ
        # =================================================

        if st.button(
            "🏁 Finish Quiz",
            use_container_width=True,
            type="primary",
            key="finish_quiz_button",
        ):

            score = 0

            for i, question in enumerate(
                st.session_state.quiz_questions
            ):

                answer = st.session_state.get(
                    f"quiz_answer_{i}"
                )

                if answer == question["correct"]:

                    score += 1


            total = len(
                st.session_state.quiz_questions
            )


            if total > 0:

                percentage = (
                    score / total
                ) * 100

            else:

                percentage = 0


            st.session_state.quiz_score = score

            st.session_state.quiz_percentage = percentage

            st.session_state.quiz_finished = True

            st.rerun()


    # =====================================================
    # QUIZ RESULTS
    # =====================================================

    else:

        st.subheader("🏆 Quiz Results")


        score = st.session_state.quiz_score

        percentage = st.session_state.quiz_percentage

        total = len(
            st.session_state.quiz_questions
        )


        st.metric(
            "Your Score",
            f"{percentage:.0f}%",
        )


        st.write(
            f"**{score} out of {total} questions correct**"
        )


        st.progress(
            int(percentage)
        )


        if percentage == 100:

            st.success(
                "🎉 Perfect score!"
            )

        elif percentage >= 80:

            st.success(
                "🌟 Great job!"
            )

        elif percentage >= 60:

            st.info(
                "👍 Good job! Keep practicing!"
            )

        elif percentage >= 40:

            st.warning(
                "📚 Keep practicing!"
            )

        else:

            st.error(
                "💪 Don't give up! Try again!"
            )


        st.divider()


        if st.button(
            "🔄 Create New Quiz",
            use_container_width=True,
            key="create_new_quiz",
        ):

            st.session_state.quiz_questions = [
                {
                    "question": "",
                    "A": "",
                    "B": "",
                    "C": "",
                    "D": "",
                    "correct": "A",
                }
            ]

            st.session_state.quiz_started = False

            st.session_state.quiz_finished = False

            st.session_state.quiz_score = 0

            st.session_state.quiz_percentage = 0.0

            st.rerun()
