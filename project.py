import streamlit as st

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Calculator & Quiz Master",
    page_icon="🧮",
    layout="centered"
)


# =========================================================
# SIDEBAR MENU
# =========================================================

st.sidebar.title("📱 Menu")

page = st.sidebar.radio(
    "Choose a page:",
    ["🧮 Calculator", "📝 Quiz Master"]
)


# =========================================================
# CALCULATOR
# =========================================================

if page == "🧮 Calculator":

    # -----------------------------------------------------
    # Initialize calculator state
    # -----------------------------------------------------

    if "display" not in st.session_state:
        st.session_state.display = "0"

    if "first_number" not in st.session_state:
        st.session_state.first_number = None

    if "operation" not in st.session_state:
        st.session_state.operation = None

    if "new_number" not in st.session_state:
        st.session_state.new_number = True


    # -----------------------------------------------------
    # Calculator functions
    # -----------------------------------------------------

    def number_click(number):

        if (
            st.session_state.new_number
            or st.session_state.display == "0"
            or st.session_state.display == "Error"
        ):
            st.session_state.display = number
            st.session_state.new_number = False

        else:
            st.session_state.display += number


    def decimal_click():

        if st.session_state.new_number:

            st.session_state.display = "0."
            st.session_state.new_number = False

        elif "." not in st.session_state.display:

            st.session_state.display += "."


    def operation_click(operation):

        if st.session_state.display == "Error":
            return

        st.session_state.first_number = float(
            st.session_state.display
        )

        st.session_state.operation = operation
        st.session_state.new_number = True


    def calculate():

        if (
            st.session_state.first_number is None
            or st.session_state.operation is None
        ):
            return

        second_number = float(
            st.session_state.display
        )

        first_number = st.session_state.first_number
        operation = st.session_state.operation


        if operation == "+":
            result = first_number + second_number

        elif operation == "-":
            result = first_number - second_number

        elif operation == "×":
            result = first_number * second_number

        elif operation == "÷":

            if second_number == 0:

                st.session_state.display = "Error"
                st.session_state.first_number = None
                st.session_state.operation = None
                st.session_state.new_number = True

                return

            result = first_number / second_number


        # Remove unnecessary .0
        if result == int(result):

            st.session_state.display = str(
                int(result)
            )

        else:

            st.session_state.display = str(result)


        st.session_state.first_number = None
        st.session_state.operation = None
        st.session_state.new_number = True


    def clear():

        st.session_state.display = "0"
        st.session_state.first_number = None
        st.session_state.operation = None
        st.session_state.new_number = True


    def backspace():

        if not st.session_state.new_number:

            st.session_state.display = (
                st.session_state.display[:-1]
            )

            if (
                st.session_state.display == ""
                or st.session_state.display == "-"
            ):

                st.session_state.display = "0"


    # -----------------------------------------------------
    # Calculator title
    # -----------------------------------------------------

    st.title("🧮 Calculator")


    # -----------------------------------------------------
    # Calculator display
    # -----------------------------------------------------

    st.markdown(
        f"""
        <div style="
            background-color: #222;
            color: white;
            padding: 20px;
            border-radius: 12px;
            text-align: right;
            font-size: 40px;
            font-family: monospace;
            margin-bottom: 15px;
        ">
            {st.session_state.display}
        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # Row 1
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button(
            "AC",
            use_container_width=True,
            key="calc_ac"
        ):
            clear()
            st.rerun()


    with col2:

        if st.button(
            "⌫",
            use_container_width=True,
            key="calc_backspace"
        ):
            backspace()
            st.rerun()


    with col3:

        if st.button(
            "÷",
            use_container_width=True,
            key="calc_divide"
        ):
            operation_click("÷")
            st.rerun()


    with col4:

        if st.button(
            "×",
            use_container_width=True,
            key="calc_multiply"
        ):
            operation_click("×")
            st.rerun()


    # -----------------------------------------------------
    # Row 2
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button(
            "7",
            use_container_width=True,
            key="calc_7"
        ):
            number_click("7")
            st.rerun()


    with col2:

        if st.button(
            "8",
            use_container_width=True,
            key="calc_8"
        ):
            number_click("8")
            st.rerun()


    with col3:

        if st.button(
            "9",
            use_container_width=True,
            key="calc_9"
        ):
            number_click("9")
            st.rerun()


    with col4:

        if st.button(
            "-",
            use_container_width=True,
            key="calc_minus"
        ):
            operation_click("-")
            st.rerun()


    # -----------------------------------------------------
    # Row 3
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button(
            "4",
            use_container_width=True,
            key="calc_4"
        ):
            number_click("4")
            st.rerun()


    with col2:

        if st.button(
            "5",
            use_container_width=True,
            key="calc_5"
        ):
            number_click("5")
            st.rerun()


    with col3:

        if st.button(
            "6",
            use_container_width=True,
            key="calc_6"
        ):
            number_click("6")
            st.rerun()


    with col4:

        if st.button(
            "+",
            use_container_width=True,
            key="calc_plus"
        ):
            operation_click("+")
            st.rerun()


    # -----------------------------------------------------
    # Row 4
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button(
            "1",
            use_container_width=True,
            key="calc_1"
        ):
            number_click("1")
            st.rerun()


    with col2:

        if st.button(
            "2",
            use_container_width=True,
            key="calc_2"
        ):
            number_click("2")
            st.rerun()


    with col3:

        if st.button(
            "3",
            use_container_width=True,
            key="calc_3"
        ):
            number_click("3")
            st.rerun()


    with col4:

        if st.button(
            "=",
            use_container_width=True,
            key="calc_equals"
        ):
            calculate()
            st.rerun()


    # -----------------------------------------------------
    # Row 5
    # -----------------------------------------------------

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:

        if st.button(
            "0",
            use_container_width=True,
            key="calc_0"
        ):
            number_click("0")
            st.rerun()


    with col2:

        if st.button(
            ".",
            use_container_width=True,
            key="calc_decimal"
        ):
            decimal_click()
            st.rerun()


# =========================================================
# QUIZ MASTER
# =========================================================

elif page == "📝 Quiz Master":

    # -----------------------------------------------------
    # Initialize Quiz Master
    # -----------------------------------------------------

    if "quiz_num_questions" not in st.session_state:

        st.session_state.quiz_num_questions = 1


    if "quiz_questions" not in st.session_state:

        st.session_state.quiz_questions = [
            {
                "question": "",
                "A": "",
                "B": "",
                "C": "",
                "D": "",
                "correct": "A"
            }
        ]


    if "quiz_started" not in st.session_state:

        st.session_state.quiz_started = False


    if "quiz_finished" not in st.session_state:

        st.session_state.quiz_finished = False


    if "quiz_score" not in st.session_state:

        st.session_state.quiz_score = 0


    if "quiz_percentage" not in st.session_state:

        st.session_state.quiz_percentage = 0


    # -----------------------------------------------------
    # Quiz functions
    # -----------------------------------------------------

    def add_question():

        if st.session_state.quiz_num_questions < 50:

            st.session_state.quiz_num_questions += 1

            st.session_state.quiz_questions.append(
                {
                    "question": "",
                    "A": "",
                    "B": "",
                    "C": "",
                    "D": "",
                    "correct": "A"
                }
            )


    def remove_question():

        if st.session_state.quiz_num_questions > 1:

            st.session_state.quiz_num_questions -= 1

            st.session_state.quiz_questions.pop()


    def start_quiz():

        valid = True

        for i, question in enumerate(
            st.session_state.quiz_questions
        ):

            if not question["question"].strip():

                st.error(
                    f"Please enter Question {i + 1}."
                )

                valid = False


            if not question["A"].strip():

                st.error(
                    f"Please enter Choice A for Question {i + 1}."
                )

                valid = False


            if not question["B"].strip():

                st.error(
                    f"Please enter Choice B for Question {i + 1}."
                )

                valid = False


            if not question["C"].strip():

                st.error(
                    f"Please enter Choice C for Question {i + 1}."
                )

                valid = False


            if not question["D"].strip():

                st.error(
                    f"Please enter Choice D for Question {i + 1}."
                )

                valid = False


        if valid:

            st.session_state.quiz_started = True
            st.session_state.quiz_finished = False

            st.rerun()


    def finish_quiz():

        score = 0

        for i, question in enumerate(
            st.session_state.quiz_questions
        ):

            selected_answer = st.session_state.get(
                f"quiz_answer_{i}"
            )

            if selected_answer == question["correct"]:

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


    def reset_quiz():

        st.session_state.quiz_num_questions = 1

        st.session_state.quiz_questions = [
            {
                "question": "",
                "A": "",
                "B": "",
                "C": "",
                "D": "",
                "correct": "A"
            }
        ]

        st.session_state.quiz_started = False

        st.session_state.quiz_finished = False

        st.session_state.quiz_score = 0

        st.session_state.quiz_percentage = 0


    # =====================================================
    # QUIZ SETUP
    # =====================================================

    if not st.session_state.quiz_started:

        st.title("📝 Quiz Master")

        st.header("Quiz Setup")

        st.write(
            "How many questions do you want to add to this quiz?"
        )


        # -------------------------------------------------
        # Question number controls
        # -------------------------------------------------

        col1, col2, col3 = st.columns(
            [1, 2, 1]
        )


        with col1:

            if st.button(
                "−",
                use_container_width=True,
                key="quiz_minus"
            ):

                remove_question()
                st.rerun()


        with col2:

            st.markdown(
                f"""
                <div style="
                    background-color: #222;
                    color: white;
                    padding: 10px;
                    border-radius: 10px;
                    text-align: center;
                    font-size: 28px;
                    font-weight: bold;
                ">
                    {st.session_state.quiz_num_questions}
                </div>
                """,
                unsafe_allow_html=True
            )


        with col3:

            if st.button(
                "+",
                use_container_width=True,
                key="quiz_plus"
            ):

                add_question()
                st.rerun()


        st.divider()


        # =================================================
        # CUSTOMIZE QUESTIONS
        # =================================================

        st.header("Customize Your Questions")


        for i in range(
            st.session_state.quiz_num_questions
        ):

            st.subheader(
                f"Question {i + 1}"
            )


            # Question
            question = st.text_input(
                "Enter your question:",
                value=st.session_state.quiz_questions[i][
                    "question"
                ],
                placeholder="Enter your question here...",
                key=f"quiz_question_{i}"
            )

            st.session_state.quiz_questions[i][
                "question"
            ] = question


            st.write("Enter the four choices:")


            # -------------------------------------------------
            # Choice A and Choice B
            # -------------------------------------------------

            col1, col2 = st.columns(2)


            with col1:

                choice_a = st.text_input(
                    "Choice A",
                    value=st.session_state.quiz_questions[i][
                        "A"
                    ],
                    placeholder="Choice A",
                    key=f"quiz_choice_a_{i}"
                )

                st.session_state.quiz_questions[i][
                    "A"
                ] = choice_a


                choice_b = st.text_input(
                    "Choice B",
                    value=st.session_state.quiz_questions[i][
                        "B"
                    ],
                    placeholder="Choice B",
                    key=f"quiz_choice_b_{i}"
                )

                st.session_state.quiz_questions[i][
                    "B"
                ] = choice_b


            # -------------------------------------------------
            # Choice C and Choice D
            # -------------------------------------------------

            with col2:

                choice_c = st.text_input(
                    "Choice C",
                    value=st.session_state.quiz_questions[i][
                        "C"
                    ],
                    placeholder="Choice C",
                    key=f"quiz_choice_c_{i}"
                )

                st.session_state.quiz_questions[i][
                    "C"
                ] = choice_c


                choice_d = st.text_input(
                    "Choice D",
                    value=st.session_state.quiz_questions[i][
                        "D"
                    ],
                    placeholder="Choice D",
                    key=f"quiz_choice_d_{i}"
                )

                st.session_state.quiz_questions[i][
                    "D"
                ] = choice_d


            # -------------------------------------------------
            # Correct answer
            # -------------------------------------------------

            correct = st.radio(
                "Which option is correct?",
                ["A", "B", "C", "D"],
                index=[
                    "A",
                    "B",
                    "C",
                    "D"
                ].index(
                    st.session_state.quiz_questions[i][
                        "correct"
                    ]
                ),
                horizontal=True,
                key=f"quiz_correct_{i}"
            )


            st.session_state.quiz_questions[i][
                "correct"
            ] = correct


            st.divider()


        # =================================================
        # START QUIZ
        # =================================================

        if st.button(
            "▶️ Start Quiz",
            use_container_width=True,
            type="primary",
            key="start_quiz"
        ):

            start_quiz()


    # =====================================================
    # QUIZ MODE
    # =====================================================

    elif (
        st.session_state.quiz_started
        and not st.session_state.quiz_finished
    ):

        st.title("📝 Quiz Master")

        st.header("🎯 Quiz Time!")

        st.write(
            "Choose one answer for each question."
        )

        st.divider()


        # -------------------------------------------------
        # Questions
        # -------------------------------------------------

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
                "D": question["D"]
            }


            st.radio(
                "Choose your answer:",
                ["A", "B", "C", "D"],
                format_func=lambda x, choices=choices:
                    f"Choice {x}: {choices[x]}",
                index=None,
                key=f"quiz_answer_{i}"
            )


            st.divider()


        # -------------------------------------------------
        # Finish Quiz
        # -------------------------------------------------

        if st.button(
            "🏁 Finish Quiz",
            use_container_width=True,
            type="primary",
            key="finish_quiz"
        ):

            finish_quiz()


    # =====================================================
    # RESULTS
    # =====================================================

    elif st.session_state.quiz_finished:

        st.title("📝 Quiz Master")

        st.header("🏆 Quiz Results")


        # Get results
        score = st.session_state.quiz_score

        percentage = st.session_state.quiz_percentage

        total = len(
            st.session_state.quiz_questions
        )


        # -------------------------------------------------
        # Display result WITHOUT HTML
        # -------------------------------------------------

        st.metric(
            label="Your Score",
            value=f"{percentage:.0f}%"
        )


        st.write(
            f"**{score} out of {total} questions correct**"
        )


        # -------------------------------------------------
        # Progress bar
        # -------------------------------------------------

        st.progress(
            int(percentage)
        )


        # -------------------------------------------------
        # Feedback
        # -------------------------------------------------

        if percentage == 100:

            st.success(
                "🎉 Perfect score! Amazing job!"
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
                "📚 Not bad! A little more practice will help."
            )

        else:

            st.error(
                "💪 Keep practicing! You can do better next time."
            )


        st.divider()


        # -------------------------------------------------
        # Create New Quiz
        # -------------------------------------------------

        if st.button(
            "🔄 Create New Quiz",
            use_container_width=True,
            key="new_quiz"
        ):

            reset_quiz()
            st.rerun()
