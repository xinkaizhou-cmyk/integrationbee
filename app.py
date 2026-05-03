import random
import streamlit as st
from questions import easy_questions, medium_questions, hard_questions

st.set_page_config(page_title="Integration Bee", page_icon="🐝", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #fff8d6 0%, #ffffff 45%);
}

.block-container {
    padding-top: 1rem;
    max-width: 900px;
}

.hero {
    text-align: center;
    padding: 18px;
    border-radius: 20px;
    background: white;
    border: 2px solid #f1d56b;
    box-shadow: 0 6px 0 #e5c24f;
    margin-bottom: 18px;
}

.hero-title {
    font-size: 36px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 14px;
    color: #6b6b6b;
}

.question-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    margin: 18px 0;
    text-align: center;
    border: 2px solid #e5e5e5;
    box-shadow: 0 6px 0 #d9d9d9;
}

.question-text {
    font-size: 24px;
    font-weight: 800;
}

.stButton > button {
    border-radius: 14px;
    border: 2px solid #d8d8d8;
    padding: 10px;
    font-size: 15px;
    font-weight: 700;
    background: white;
    box-shadow: 0 4px 0 #d8d8d8;
}

div[data-testid="stMetric"] {
    padding: 10px;
    border-radius: 14px;
}

.feedback-good, .feedback-bad {
    border-radius: 16px;
    padding: 14px;
    font-size: 16px;
    margin-top: 12px;
}

.feedback-good {
    background: #dcffd1;
    border: 2px solid #58cc02;
    color: #2f7d00;
}

.feedback-bad {
    background: #ffe1e1;
    border: 2px solid #ff4b4b;
    color: #b00000;
}

.difficulty-pill {
    padding: 6px;
    font-size: 14px;
    margin-bottom: 10px;
    text-align: center;
    font-weight: 800;
    background: white;
    border: 2px solid #f1d56b;
    border-radius: 999px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">🐝 Integration Bee</div>
    <div class="hero-subtitle">Speed-run calculus. Build your integration instincts.</div>
</div>
""", unsafe_allow_html=True)


def get_question_pool(difficulty):
    if difficulty == "Easy":
        return easy_questions
    elif difficulty == "Medium":
        return medium_questions
    else:
        return hard_questions


# SESSION STATE
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "difficulty" not in st.session_state:
    st.session_state.difficulty = None

if "score" not in st.session_state:
    st.session_state.score = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "question_count" not in st.session_state:
    st.session_state.question_count = 1

if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if "checked_wrong" not in st.session_state:
    st.session_state.checked_wrong = False


# START SCREEN
if not st.session_state.game_started:
    st.subheader("Choose your difficulty")

    difficulty = st.radio("Difficulty:", ["Easy", "Medium", "Hard"])

    if st.button("Start Practice", use_container_width=True):
        st.session_state.difficulty = difficulty
        question_pool = get_question_pool(difficulty)

        st.session_state.question = random.choice(question_pool)
        st.session_state.game_started = True
        st.rerun()

    st.stop()


# GAME SCREEN
question_pool = get_question_pool(st.session_state.difficulty)
q = st.session_state.question

st.markdown(
    f'<div class="difficulty-pill">Difficulty: {st.session_state.difficulty}</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
col1.metric("Score", st.session_state.score)
col2.metric("Streak", st.session_state.streak)
col3.metric("Question", st.session_state.question_count)

st.progress(min(st.session_state.streak / 10, 1.0))

st.markdown(
    f"""
    <div class="question-card">
        <div class="question-text">{q["text"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("**Choose the correct answer:**")

for i, choice in enumerate(q["choices"]):
    label = choice

    if st.session_state.selected_answer == i:
        label = "✅ " + choice

    if st.button(label, key=f"choice_{i}", use_container_width=True, disabled=st.session_state.submitted):
        st.session_state.selected_answer = i
        st.session_state.checked_wrong = False
        st.session_state.show_answer = False
        st.rerun()


# CHECK ANSWER
if st.button("Check", use_container_width=True, disabled=st.session_state.submitted):
    if st.session_state.selected_answer is None:
        st.warning("Choose an answer first.")
    else:
        if st.session_state.selected_answer == q["answer"]:
            st.session_state.submitted = True
            st.session_state.score += 1
            st.session_state.streak += 1
            st.session_state.checked_wrong = False
            st.session_state.show_hint = False
            st.session_state.show_answer = False
        else:
            st.session_state.checked_wrong = True
            st.session_state.streak = 0
            st.session_state.show_hint = False
            st.session_state.show_answer = False

        st.rerun()


# ONLY SHOW THESE AFTER CHECKING A WRONG ANSWER
if st.session_state.checked_wrong and not st.session_state.submitted:
    st.warning("Not quite. What would you like to do?")

    col_hint, col_answer = st.columns(2)

    with col_hint:
        if st.button("Hint", use_container_width=True):
            st.session_state.show_hint = True
            st.session_state.selected_answer = None
            st.session_state.checked_wrong = False
            st.rerun()

    with col_answer:
        if st.button("Correct Answer", use_container_width=True):
            st.session_state.show_answer = True
            st.session_state.checked_wrong = False
            st.rerun()


# HINT MODE: LET THEM TRY AGAIN
if st.session_state.show_hint:
    st.info(f"Hint: Try using **{q['method']}**.")
    st.write("Now try the problem again.")


# SHOW CORRECT ANSWER
if st.session_state.show_answer:
    correct_choice = q["choices"][q["answer"]]

    st.markdown(
        f"""
        <div class="feedback-bad">
            Correct answer: {correct_choice}<br>
            Method: {q["method"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Continue", use_container_width=True):
        st.session_state.question = random.choice(question_pool)
        st.session_state.question_count += 1
        st.session_state.selected_answer = None
        st.session_state.submitted = False
        st.session_state.show_hint = False
        st.session_state.show_answer = False
        st.session_state.checked_wrong = False
        st.rerun()


# CORRECT FEEDBACK
if st.session_state.submitted:
    st.markdown(
        f"""
        <div class="feedback-good">
            Correct! 🔥<br>
            Method: {q["method"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Continue", use_container_width=True):
        st.session_state.question = random.choice(question_pool)
        st.session_state.question_count += 1
        st.session_state.selected_answer = None
        st.session_state.submitted = False
        st.session_state.show_hint = False
        st.session_state.show_answer = False
        st.session_state.checked_wrong = False
        st.rerun()


# CHANGE DIFFICULTY
if st.button("Change Difficulty", use_container_width=True):
    st.session_state.show_hint = False
    st.session_state.show_answer = False
    st.session_state.checked_wrong = False
    st.session_state.game_started = False
    st.session_state.difficulty = None
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.question_count = 1
    st.session_state.selected_answer = None
    st.session_state.submitted = False
    st.rerun()