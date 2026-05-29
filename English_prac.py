# streamlit run English_prac.py
import streamlit as st
import json
import os
import random

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Global Customer Support Trainer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# CUSTOM CSS FOR RICH AESTHETICS
# ---------------------------------
st.markdown("""
<style>
    /* Premium visual styling */
    .main {
        background-color: #0f111a;
        color: #e0e0e6;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 700 !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #161925;
        border-right: 1px solid #23283d;
    }
    
    /* Custom cards */
    .glass-card {
        background: rgba(22, 25, 37, 0.7);
        border: 1px solid #23283d;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    .stat-card {
        background: linear-gradient(135deg, #1e2235 0%, #161925 100%);
        border: 1px solid #2e3552;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    .stat-value {
        font-size: 32px;
        font-weight: 800;
        color: #00e676;
        margin-bottom: 4px;
    }
    .stat-label {
        font-size: 14px;
        color: #a0a5c0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Interactive Chat Visualizer styling */
    .chat-container {
        background-color: #090b11;
        border: 1px solid #1c2030;
        border-radius: 16px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.5);
    }
    .chat-bubble {
        padding: 14px 18px;
        border-radius: 20px;
        margin-bottom: 12px;
        max-width: 75%;
        line-height: 1.5;
        font-size: 15px;
        position: relative;
    }
    .customer-bubble {
        background-color: #212538;
        color: #f1f1f7;
        border-bottom-left-radius: 4px;
        float: left;
        clear: both;
    }
    .customer-label {
        font-size: 11px;
        color: #7d84a6;
        margin-bottom: 4px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .agent-bubble {
        background-color: #0d5c3a;
        color: #ffffff;
        border-bottom-right-radius: 4px;
        float: right;
        clear: both;
        text-align: left;
        border: 1px solid #147a4f;
    }
    .agent-label {
        font-size: 11px;
        color: #4caf50;
        margin-bottom: 4px;
        text-align: right;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        clear: both;
        display: block;
    }
    .system-bubble {
        background-color: #1e1d13;
        color: #e6c543;
        text-align: center;
        max-width: 90%;
        margin: 10px auto;
        border-radius: 10px;
        padding: 8px 12px;
        font-style: italic;
        font-size: 13px;
        border: 1px solid #473e15;
        clear: both;
    }
    
    /* Flashcard styles */
    .flashcard {
        background: linear-gradient(135deg, #1f243b 0%, #161925 100%);
        border: 2px solid #3c4570;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        margin: 20px 0;
        transition: transform 0.3s;
    }
    .flashcard:hover {
        transform: translateY(-5px);
        border-color: #00e676;
    }
    .flashcard-title {
        font-size: 14px;
        color: #828cb8;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 15px;
    }
    .flashcard-content {
        font-size: 24px;
        font-weight: 600;
        color: #ffffff;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-right: 8px;
    }
    .badge-success { background-color: rgba(0, 230, 118, 0.15); color: #00e676; border: 1px solid #00e676; }
    .badge-warning { background-color: rgba(255, 179, 0, 0.15); color: #ffb300; border: 1px solid #ffb300; }
    .badge-danger { background-color: rgba(255, 23, 68, 0.15); color: #ff1744; border: 1px solid #ff1744; }
    .badge-info { background-color: rgba(41, 121, 255, 0.15); color: #2979ff; border: 1px solid #2979ff; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# DATA DIRECTORIES
# ---------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FOLDER = os.path.join(BASE_DIR, "tests")

if not os.path.exists(TEST_FOLDER):
    st.error(f"Tests folder not found at: {TEST_FOLDER}")
    st.stop()

json_files = sorted([f for f in os.listdir(TEST_FOLDER) if f.endswith(".json") and f != "generate_data.py"])

if not json_files:
    st.error("No training module JSON files found. Please generate them first.")
    st.stop()

# ---------------------------------
# SESSION STATE INITIALIZATION
# ---------------------------------
if "test_id" not in st.session_state:
    st.session_state.test_id = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "best_streak" not in st.session_state:
    st.session_state.best_streak = 0
if "completed_count" not in st.session_state:
    st.session_state.completed_count = {}
if "selected_module" not in st.session_state:
    st.session_state.selected_module = json_files[0]
if "mcq_index" not in st.session_state:
    st.session_state.mcq_index = 0
if "mcq_submitted" not in st.session_state:
    st.session_state.mcq_submitted = False
if "mcq_user_choice" not in st.session_state:
    st.session_state.mcq_user_choice = "Unattempted"

# Exam states
if "exam_started" not in st.session_state:
    st.session_state.exam_started = False
if "exam_questions" not in st.session_state:
    st.session_state.exam_questions = []
if "exam_answers" not in st.session_state:
    st.session_state.exam_answers = {}
if "exam_submitted" not in st.session_state:
    st.session_state.exam_submitted = False

# Roleplay states
if "roleplay_scenario" not in st.session_state:
    st.session_state.roleplay_scenario = None
if "roleplay_feedback" not in st.session_state:
    st.session_state.roleplay_feedback = None
if "roleplay_history" not in st.session_state:
    st.session_state.roleplay_history = []

# Flashcard states
if "flashcard_index" not in st.session_state:
    st.session_state.flashcard_index = 0
if "flashcard_flipped" not in st.session_state:
    st.session_state.flashcard_flipped = False

def reset_mcq():
    st.session_state.mcq_index = 0
    st.session_state.mcq_submitted = False
    st.session_state.mcq_user_choice = "Unattempted"

def reset_exam():
    st.session_state.exam_started = False
    st.session_state.exam_questions = []
    st.session_state.exam_answers = {}
    st.session_state.exam_submitted = False

def reset_roleplay(questions_list=None):
    if questions_list:
        st.session_state.roleplay_scenario = random.choice(questions_list)
    else:
        st.session_state.roleplay_scenario = None
    st.session_state.roleplay_feedback = None

# Initialize completion record
for f in json_files:
    if f not in st.session_state.completed_count:
        st.session_state.completed_count[f] = 0

# ---------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 28px; margin-bottom: 25px;'>🌍 Wheelz Coach</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a5c0; font-size: 14px; margin-top: -20px; margin-bottom: 30px;'>Concentrix Uber Cabs Communication Hub</p>", unsafe_allow_html=True)
    
    # Module selector
    selected_file = st.selectbox(
        "📂 Select Training Module",
        json_files,
        format_func=lambda x: x.replace(".json", "").replace("_", " ").title()
    )
    
    # Reset states if module changes
    if selected_file != st.session_state.selected_module:
        st.session_state.selected_module = selected_file
        reset_mcq()
        reset_exam()
        reset_roleplay()
        
    st.markdown("---")
    
    # Mode selector
    active_mode = st.radio(
        "🎯 Choose Training Mode",
        [
            "📊 Dashboard & Stats",
            "📖 Practice Mode (MCQ)",
            "💬 Chat Roleplay Simulator",
            "🎴 Flashcards Trainer",
            "📝 Timed Exam Mode",
            "💡 Cultural Cheat Sheets"
        ]
    )
    
    st.markdown("---")
    
    # Streak metrics in sidebar
    col_streak_1, col_streak_2 = st.columns(2)
    with col_streak_1:
        st.markdown(f"<div class='stat-card'><div class='stat-value' style='color:#00e676;'>🔥 {st.session_state.streak}</div><div class='stat-label' style='font-size: 10px;'>Streak</div></div>", unsafe_allow_html=True)
    with col_streak_2:
        st.markdown(f"<div class='stat-card'><div class='stat-value' style='color:#2979ff;'>🏆 {st.session_state.best_streak}</div><div class='stat-label' style='font-size: 10px;'>Best</div></div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔄 Reset Streak & State", use_container_width=True):
        st.session_state.streak = 0
        st.session_state.best_streak = 0
        st.session_state.completed_count = {f: 0 for f in json_files}
        reset_mcq()
        reset_exam()
        reset_roleplay()
        st.success("State reset successfully!")
        st.rerun()

# ---------------------------------
# LOAD DATA FROM JSON
# ---------------------------------
file_path = os.path.join(TEST_FOLDER, selected_file)
with open(file_path, "r", encoding="utf-8") as f:
    questions = json.load(f)

total_questions = len(questions)

# ---------------------------------
# MODE 1: DASHBOARD
# ---------------------------------
if active_mode == "📊 Dashboard & Stats":
    st.markdown(f"<h1>📊 Training Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a5c0; font-size: 16px;'>Track your customer support readiness for the Uber Wheelz process.</p>", unsafe_allow_html=True)
    
    # Welcome banner
    st.markdown("""
    <div class='glass-card' style='background: linear-gradient(135deg, #182238 0%, #161925 100%); border-left: 5px solid #00e676;'>
        <h3 style='margin-top: 0;'>Welcome to Concentrix Wheelz Training!</h3>
        <p>This coach is optimized to help you communicate effectively with clients from the <b>USA, Europe, East Asia, and Africa</b>. 
        Through interactive quizzes, flashcards, and our real-time text-based chat roleplay analyzer, you'll master cultural empathy, active listening, de-escalation, and policy execution in no time.</p>
        <span class="badge badge-success">200+ Questions per Module</span>
        <span class="badge badge-info">Real-time NLP Grader</span>
        <span class="badge badge-warning">Cultural Sensitivity focus</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Overall Progress Stats Grid
    st.markdown("### 📈 Module Progress Overview")
    cols = st.columns(4)
    
    for idx, f_name in enumerate(json_files[:4]):
        with cols[idx]:
            count_done = st.session_state.completed_count.get(f_name, 0)
            percentage = min(100, int((count_done / 200) * 100))
            display_title = f_name.replace(".json", "").replace("_", " ").title()
            
            st.markdown(f"""
            <div class='stat-card'>
                <div class='stat-label'>{display_title}</div>
                <div class='stat-value'>{count_done}/200</div>
                <div style='color: #828cb8; font-size: 12px; margin-top: 8px;'>{percentage}% Completed</div>
            </div>
            """, unsafe_allow_html=True)
            
    cols2 = st.columns(4)
    for idx, f_name in enumerate(json_files[4:8]):
        with cols2[idx]:
            count_done = st.session_state.completed_count.get(f_name, 0)
            percentage = min(100, int((count_done / 200) * 100))
            display_title = f_name.replace(".json", "").replace("_", " ").title()
            
            st.markdown(f"""
            <div class='stat-card'>
                <div class='stat-label'>{display_title}</div>
                <div class='stat-value'>{count_done}/200</div>
                <div style='color: #828cb8; font-size: 12px; margin-top: 8px;'>{percentage}% Completed</div>
            </div>
            """, unsafe_allow_html=True)

    # Badges Earned Section
    st.markdown("<br><h3>🏅 Training Badges</h3>", unsafe_allow_html=True)
    badge_cols = st.columns(4)
    
    # Evaluate badges based on state
    total_completed = sum(st.session_state.completed_count.values())
    
    with badge_cols[0]:
        status_color = "#00e676" if total_completed > 0 else "#4c5375"
        st.markdown(f"""
        <div class='stat-card' style='border-color: {status_color};'>
            <div style='font-size: 40px; filter: grayscale({"0" if total_completed > 0 else "1"});'>🌱</div>
            <h4 style='margin: 8px 0 4px 0;'>First Step</h4>
            <p style='font-size: 12px; color: #828cb8; margin: 0;'>Answered your first practice question</p>
        </div>
        """, unsafe_allow_html=True)
        
    with badge_cols[1]:
        unlocked = st.session_state.best_streak >= 5
        status_color = "#ffb300" if unlocked else "#4c5375"
        st.markdown(f"""
        <div class='stat-card' style='border-color: {status_color};'>
            <div style='font-size: 40px; filter: grayscale({"0" if unlocked else "1"});'>🔥</div>
            <h4 style='margin: 8px 0 4px 0;'>On Fire</h4>
            <p style='font-size: 12px; color: #828cb8; margin: 0;'>Reached a streak of 5+ correct replies</p>
        </div>
        """, unsafe_allow_html=True)
        
    with badge_cols[2]:
        unlocked = total_completed >= 50
        status_color = "#2979ff" if unlocked else "#4c5375"
        st.markdown(f"""
        <div class='stat-card' style='border-color: {status_color};'>
            <div style='font-size: 40px; filter: grayscale({"0" if unlocked else "1"});'>🗣️</div>
            <h4 style='margin: 8px 0 4px 0;'>Conversationalist</h4>
            <p style='font-size: 12px; color: #828cb8; margin: 0;'>Practiced 50+ questions in total</p>
        </div>
        """, unsafe_allow_html=True)
        
    with badge_cols[3]:
        unlocked = total_completed >= 200
        status_color = "#e6c543" if unlocked else "#4c5375"
        st.markdown(f"""
        <div class='stat-card' style='border-color: {status_color};'>
            <div style='font-size: 40px; filter: grayscale({"0" if unlocked else "1"});'>🎓</div>
            <h4 style='margin: 8px 0 4px 0;'>Uber Cabs Guru</h4>
            <p style='font-size: 12px; color: #828cb8; margin: 0;'>Completed 200+ training exercises</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------
# MODE 2: PRACTICE MCQ MODE
# ---------------------------------
elif active_mode == "📖 Practice Mode (MCQ)":
    st.markdown(f"<h1>📖 Practice Mode</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #a0a5c0; font-size: 16px;'>Active Module: <b>{selected_file.replace('.json','').replace('_',' ').title()}</b></p>", unsafe_allow_html=True)
    
    # Navigation controls (loads questions dynamically one by one!)
    col_nav1, col_nav2, col_nav3 = st.columns([1, 4, 1])
    
    with col_nav1:
        if st.button("⬅️ Previous Question", use_container_width=True) and st.session_state.mcq_index > 0:
            st.session_state.mcq_index -= 1
            st.session_state.mcq_submitted = False
            st.session_state.mcq_user_choice = "Unattempted"
            st.rerun()
            
    with col_nav2:
        selected_index = st.slider(
            "Select Question",
            1, total_questions, st.session_state.mcq_index + 1,
            label_visibility="collapsed"
        )
        if selected_index - 1 != st.session_state.mcq_index:
            st.session_state.mcq_index = selected_index - 1
            st.session_state.mcq_submitted = False
            st.session_state.mcq_user_choice = "Unattempted"
            st.rerun()
            
    with col_nav3:
        if st.button("Next Question ➡️", use_container_width=True) and st.session_state.mcq_index < total_questions - 1:
            st.session_state.mcq_index += 1
            st.session_state.mcq_submitted = False
            st.session_state.mcq_user_choice = "Unattempted"
            st.rerun()
            
    # Fetch active question
    q = questions[st.session_state.mcq_index]
    
    # Display question card
    st.markdown("---")
    st.markdown(f"### Question {st.session_state.mcq_index + 1} of {total_questions}")
    
    # Render interactive chat thread
    st.markdown("#### 💬 Live Chat Simulator")
    
    scenario_header = f"Scenario: {q['scenario']}" if 'scenario' in q else "Incoming Ride Chat"
    customer_msg = q['question']
    
    chat_html = f"""
    <div class='chat-container'>
        <div class='system-bubble'>{scenario_header}</div>
        <div class='customer-label'>👤 Customer Request</div>
        <div class='chat-bubble customer-bubble'>{customer_msg}</div>
    """
    
    if st.session_state.mcq_submitted and st.session_state.mcq_user_choice != "Unattempted":
        choice_text = q['options'][st.session_state.mcq_user_choice]
        chat_html += f"""
        <div class='agent-label'>✅ Your Chosen Response</div>
        <div class='chat-bubble agent-bubble'>{choice_text}</div>
        """
    chat_html += "</div><div style='clear: both;'></div>"
    
    st.markdown(chat_html, unsafe_allow_html=True)
    
    # Options selection
    options = q["options"]
    option_keys = list(options.keys())
    
    st.markdown("#### Select the Best Professional Option:")
    
    # We use a radio button but disable it if submitted
    choice = st.radio(
        "Options",
        option_keys,
        format_func=lambda x: f"Option {x}: {options[x]}",
        label_visibility="collapsed",
        disabled=st.session_state.mcq_submitted,
        key=f"mcq_radio_{st.session_state.mcq_index}"
    )
    
    col_sub1, col_sub2 = st.columns([1, 5])
    with col_sub1:
        if st.button("Submit Response", use_container_width=True, disabled=st.session_state.mcq_submitted):
            st.session_state.mcq_submitted = True
            st.session_state.mcq_user_choice = choice
            
            # Update completions record
            st.session_state.completed_count[selected_file] = max(
                st.session_state.completed_count[selected_file],
                st.session_state.mcq_index + 1
            )
            
            # Check correctness & update streak
            if choice == q["answer"]:
                st.session_state.streak += 1
                st.session_state.best_streak = max(st.session_state.best_streak, st.session_state.streak)
            else:
                st.session_state.streak = 0
            st.rerun()
            
    with col_sub2:
        if st.session_state.mcq_submitted:
            if st.button("Next Question ➔"):
                if st.session_state.mcq_index < total_questions - 1:
                    st.session_state.mcq_index += 1
                    st.session_state.mcq_submitted = False
                    st.session_state.mcq_user_choice = "Unattempted"
                    st.rerun()
                    
    # Feedback display
    if st.session_state.mcq_submitted:
        st.markdown("<br>", unsafe_allow_html=True)
        user_choice = st.session_state.mcq_user_choice
        correct_choice = q["answer"]
        
        if user_choice == correct_choice:
            st.success("🎉 **Correct!** Your response aligns perfectly with the cultural and service standards.")
        else:
            st.error(f"❌ **Incorrect Choice.** The best response was **Option {correct_choice}**.")
            
        st.markdown(f"""
        <div class='glass-card' style='border-left: 4px solid #2979ff;'>
            <h4 style='margin-top: 0;'>💡 Cultural & Strategic Explanation</h4>
            <p>{q['explanation']}</p>
            <hr style='border-color: #23283d;'>
            <span class="badge badge-info">Focused Skill: {q['skill']}</span>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------
# MODE 3: ROLEPLAY SIMULATOR
# ---------------------------------
elif active_mode == "💬 Chat Roleplay Simulator":
    st.markdown(f"<h1>💬 Chat Roleplay Simulator (Free Text)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a5c0; font-size: 16px;'>Type your custom response and get real-time NLP grading based on length, tone, and cultural alignment.</p>", unsafe_allow_html=True)
    
    # Initialize a scenario if none is loaded
    if st.session_state.roleplay_scenario is None or st.session_state.roleplay_scenario not in questions:
        reset_roleplay(questions)
        
    scenario = st.session_state.roleplay_scenario
    
    st.markdown(f"""
    <div class='glass-card' style='background: #182238; border-color: #2e3552;'>
        <h4 style='margin-top: 0; color: #00e676;'>🎭 Active Scenario: {scenario['scenario']}</h4>
        <p style='font-size: 16px;'><b>Customer Message:</b> <i>\"{scenario['question']}\"</i></p>
        <span class="badge badge-info">Module: {selected_file.replace('.json','').replace('_',' ').title()}</span>
        <span class="badge badge-warning">Target Skill: {scenario['skill']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Input Area
    user_reply = st.text_area("✍️ Type your professional live-chat response here:", height=100, placeholder="E.g., I understand your frustration, Sarah. Let me check the cancellation fee on this trip for you immediately...")
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Evaluate Response", use_container_width=True) and user_reply.strip() != "":
            # Grader Algorithm
            words = user_reply.strip().split()
            word_count = len(words)
            score = 100
            feedback = []
            
            # 1. Length Check
            if word_count > 35:
                score -= 15
                feedback.append("⚠️ **Too Wordy:** Live chat requires speed and conciseness. Your response is **{} words**. Try to keep it under 30 words for better agent productivity and reader attention.".format(word_count))
            elif word_count < 5:
                score -= 20
                feedback.append("⚠️ **Too Short:** Your response is only **{} words**. Provide a complete professional sentence to show active assistance.".format(word_count))
            else:
                feedback.append("✅ **Ideal Length:** Your response is **{} words** which is perfect for chat support.".format(word_count))
                
            # 2. Empathy / Politeness Check
            empathy_words = ["sorry", "apologize", "apologies", "understand", "feel", "happy to", "assist", "check", "look into", "resolve", "make sure", "confirm"]
            has_empathy = any(w in user_reply.lower() for w in empathy_words)
            if not has_empathy:
                score -= 20
                feedback.append("⚠️ **Lacks Empathy/Politeness:** Try incorporating comforting or supportive keywords like *'understand'*, *'apologize'*, or *'let me check'*.")
            else:
                feedback.append("✅ **Politeness Check:** Good inclusion of supportive service language.")
                
            # 3. Banned / Robotic terms
            banned_terms = {
                "dear": "Avoid using 'dear' in support as it sounds outdated and overly familiar. Use the customer's name respectfully.",
                "relax": "Never tell a customer to 'relax' or 'calm down' as it is dismissive and escalates frustration.",
                "calm down": "Avoid telling customers to calm down. Validate their emotions instead.",
                "not our fault": "Avoid defensive phrases. Focus on what we can do to resolve the situation.",
                "not my problem": "Extremely unprofessional. Avoid entirely.",
                "wait 24 hours": "Instead of telling them to wait, state that you will check the transaction immediately."
            }
            
            found_banned = []
            for term, explanation in banned_terms.items():
                if term in user_reply.lower():
                    score -= 15
                    found_banned.append(f"❌ **Unprofessional Term ({term}):** {explanation}")
                    
            if found_banned:
                feedback.extend(found_banned)
            else:
                feedback.append("✅ **Vocabulary Check:** Free of robotic and dismissive phrases.")
                
            # 4. Regional Culture Check
            file_name_lower = selected_file.lower()
            if "usa" in file_name_lower:
                action_words = ["i will", "let me", "checking", "check", "refund", "pull up", "verify"]
                has_action = any(w in user_reply.lower() for w in action_words)
                if not has_action:
                    score -= 10
                    feedback.append("⚠️ **Cultural Check (USA):** USA customers prefer immediate, direct action verbs rather than long templates. State what you are doing right now.")
                else:
                    feedback.append("✅ **Cultural Check (USA):** Direct action verbs identified. Matches American preferences.")
                    
            elif "east_asia" in file_name_lower:
                polite_words = ["apologize", "sincerely", "patience", "understanding", "respect", "mr.", "ms."]
                has_polite = any(w in user_reply.lower() for w in polite_words)
                if not has_polite:
                    score -= 10
                    feedback.append("⚠️ **Cultural Check (East Asia):** East Asian customers appreciate highly respectful, formal, and humble apologies. Include markers of deep respect.")
                else:
                    feedback.append("✅ **Cultural Check (East Asia):** Sincere apology/respect indicators found.")
                    
            elif "europe" in file_name_lower:
                casual_words = ["gonna", "wanna", "hey", "mate", "yo", "buddy"]
                has_casual = any(w in user_reply.lower() for w in casual_words)
                if has_casual:
                    score -= 10
                    feedback.append("⚠️ **Cultural Check (Europe):** European communication (especially UK/Germany) values professional formality. Avoid overly casual terms like *'wanna'* or *'mate'*.")
                else:
                    feedback.append("✅ **Cultural Check (Europe):** Appropriate formal vocabulary observed.")
                    
            elif "africa" in file_name_lower:
                greeting_words = ["good day", "hello", "hi", "hope you", "welcome", "greetings"]
                has_greeting = any(w in user_reply.lower() for w in greeting_words)
                if not has_greeting:
                    score -= 10
                    feedback.append("⚠️ **Cultural Check (Africa):** African customer service culture heavily values starting with a polite and warm greeting. Include a check-in or warm introduction.")
                else:
                    feedback.append("✅ **Cultural Check (Africa):** Warm greeting included. Matches relational expectation.")
            
            score = max(0, min(100, score))
            st.session_state.roleplay_feedback = {
                "score": score,
                "items": feedback,
                "reply": user_reply
            }
            
            # Save to session history
            st.session_state.roleplay_history.append({
                "scenario": scenario['scenario'],
                "customer": scenario['question'],
                "agent": user_reply,
                "score": score
            })
            st.rerun()
            
    with col2:
        if st.button("🔄 Try Another Scenario"):
            reset_roleplay(questions)
            st.rerun()
            
    # Feedback display
    if st.session_state.roleplay_feedback:
        st.markdown("---")
        feedback_data = st.session_state.roleplay_feedback
        
        col_score1, col_score2 = st.columns([1, 3])
        with col_score1:
            st.markdown(f"""
            <div class='stat-card' style='border-color: #00e676;'>
                <div class='stat-label'>Grading Score</div>
                <div class='stat-value' style='font-size: 48px;'>{feedback_data['score']}/100</div>
            </div>
            """, unsafe_allow_html=True)
        with col_score2:
            st.markdown("#### 📝 Score Breakdown:")
            for item in feedback_data['items']:
                st.markdown(item)
                
        # Recommended reference response
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='glass-card' style='border-left: 4px solid #00e676;'>
            <h4 style='margin-top: 0; color: #00e676;'>💡 Coach's Recommended Response</h4>
            <p>Here is the model choice for comparison:</p>
            <p style='background-color: #090b11; padding: 12px; border-radius: 8px; border: 1px solid #1c2030;'><b>\"{scenario['options'][scenario['answer']]}\"</b></p>
            <p><b>Rationale:</b> {scenario['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    # Roleplay History Sidebar/Footer
    if st.session_state.roleplay_history:
        with st.expander("📚 View Session History"):
            for h in reversed(st.session_state.roleplay_history):
                st.markdown(f"**Scenario:** {h['scenario']} (Score: `{h['score']}/100`)")
                st.markdown(f"*Customer:* \"{h['customer']}\"")
                st.markdown(f"*Your reply:* \"{h['agent']}\"")
                st.markdown("---")

# ---------------------------------
# MODE 4: FLASHCARDS TRAINER
# ---------------------------------
elif active_mode == "🎴 Flashcards Trainer":
    st.markdown("<h1>🎴 Flashcards Trainer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a5c0; font-size: 16px;'>Rapidly review American slangs, expressions, and cultural norms. Click card to flip!</p>", unsafe_allow_html=True)
    
    # We define a structured set of flashcards for rapid vocabulary check
    flashcard_deck = [
        # Slangs
        {"front": "Rip-off", "back": "An unfair price or an overcharge. Essential to handle USA billing disputes calmly.", "category": "USA Slang"},
        {"front": "Beat the clock", "back": "To arrive or finish before a deadline. Common when clients are rushing to airports.", "category": "USA Slang"},
        {"front": "In a bind", "back": "In a difficult or tight situation (e.g. left phone in cab before a flight). Requires urgent action.", "category": "USA Slang"},
        {"front": "Heads up", "back": "An advance warning or notification (e.g., driver texting while driving warning).", "category": "USA Slang"},
        {"front": "Pull up", "back": "To open or search details on a screen (e.g., 'pull up my receipt').", "category": "USA Slang"},
        {"front": "Hit a snag", "back": "Encountered a minor unexpected obstacle. Reassure client with solid plans.", "category": "USA Slang"},
        {"front": "A bust", "back": "A complete failure or disappointment (e.g. 'the trip was a bust').", "category": "USA Slang"},
        {"front": "Boot", "back": "The trunk of a car in UK/Europe. Luggage goes here.", "category": "EU Vocabulary"},
        {"front": "Bonnet", "back": "The hood of a car covering the engine in UK/Europe. Do not tell clients to put bags here!", "category": "EU Vocabulary"},
        {"front": "Queueing", "back": "Waiting in a line (UK/EU).", "category": "EU Vocabulary"},
        {"front": "Petrol", "back": "Gasoline (gas) in UK/Europe.", "category": "EU Vocabulary"},
        {"front": "Sian", "back": "Singlish word expressing boredom, frustration, or exhaustion. Common in Singapore queries.", "category": "East Asia Vocabulary"},
        {"front": "M-Pesa", "back": "A mobile money transfer service widely used in Kenya. Common source of payment inquiries.", "category": "Africa Payments"},
        {"front": "GDPR", "back": "European privacy regulation. Customers have the right to request account/data deletion.", "category": "EU Policy"},
        {"front": "Omotenashi", "back": "Japanese philosophy of selfless hospitality. Japanese customers expect extreme respect and care.", "category": "East Asia Culture"},
        {"front": "Active Voice", "back": "'We processed your refund' instead of 'Your refund was processed by us'. Direct and preferred by USA customers.", "category": "Professional English"},
        {"front": "SLA", "back": "Service Level Agreement. The time frame in which you must answer a chat.", "category": "Metrics"},
        {"front": "CSAT", "back": "Customer Satisfaction Score. Your primary goal metric after closing a chat.", "category": "Metrics"},
        {"front": "FCR", "back": "First Contact Resolution. Solving the customer's problem on the first attempt.", "category": "Metrics"},
        {"front": "AHT", "back": "Average Handling Time. Total time spent handling a chat ticket.", "category": "Metrics"}
    ]
    
    deck_len = len(flashcard_deck)
    
    # Progress slider
    card_index = st.slider("Card Index", 1, deck_len, st.session_state.flashcard_index + 1, label_visibility="collapsed")
    st.session_state.flashcard_index = card_index - 1
    
    card = flashcard_deck[st.session_state.flashcard_index]
    
    # Draw Flashcard container
    card_content = card["back"] if st.session_state.flashcard_flipped else card["front"]
    card_title = f"{card['category']} - Click to Flip"
    
    st.markdown(f"""
    <div class='flashcard'>
        <div class='flashcard-title'>{card_title}</div>
        <div class='flashcard-content'>{card_content}</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        if st.button("Flip Card 🔁", use_container_width=True):
            st.session_state.flashcard_flipped = not st.session_state.flashcard_flipped
            st.rerun()
    with col_f2:
        if st.button("Previous Card ⬅️", use_container_width=True) and st.session_state.flashcard_index > 0:
            st.session_state.flashcard_index -= 1
            st.session_state.flashcard_flipped = False
            st.rerun()
    with col_f3:
        if st.button("Next Card ➡️", use_container_width=True) and st.session_state.flashcard_index < deck_len - 1:
            st.session_state.flashcard_index += 1
            st.session_state.flashcard_flipped = False
            st.rerun()

# ---------------------------------
# MODE 5: EXAM MODE
# ---------------------------------
elif active_mode == "📝 Timed Exam Mode":
    st.markdown("<h1>📝 Evaluation Exam Mode</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #a0a5c0; font-size: 16px;'>Active Module: <b>{selected_file.replace('.json','').replace('_',' ').title()}</b></p>", unsafe_allow_html=True)
    
    if not st.session_state.exam_started:
        st.markdown("""
        <div class='glass-card'>
            <h3>Ready to test your skills?</h3>
            <p>The exam contains <b>20 random questions</b> from this module. 
            Once you start, answers will be locked, and you'll receive your score and a skill evaluation upon clicking the submission button.</p>
            <ul>
                <li>Passing mark: <b>85%</b> (Excellent Global Communicator Badge)</li>
                <li>Instant de-escalation checks</li>
                <li>No explanations shown until you submit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Start 20-Question Exam", use_container_width=True):
            # Select 20 random questions
            st.session_state.exam_questions = random.sample(questions, min(20, total_questions))
            st.session_state.exam_answers = {}
            st.session_state.exam_submitted = False
            st.session_state.exam_started = True
            st.rerun()
            
    else:
        exam_questions = st.session_state.exam_questions
        
        # Display questions list
        for i, eq in enumerate(exam_questions):
            with st.container(border=True):
                st.markdown(f"#### Q{i+1}. {eq['question']}")
                if "scenario" in eq:
                    st.caption(f"Scenario: {eq['scenario']}")
                    
                # Setup options
                opts = eq["options"]
                opt_keys = list(opts.keys())
                
                # Check previous selection
                prev_selection = st.session_state.exam_answers.get(i, None)
                
                # Render options
                selected_opt = st.radio(
                    "Options",
                    opt_keys,
                    index=opt_keys.index(prev_selection) if prev_selection in opt_keys else None,
                    format_func=lambda x: f"{x}. {opts[x]}",
                    label_visibility="collapsed",
                    key=f"exam_q_{i}",
                    disabled=st.session_state.exam_submitted
                )
                
                st.session_state.exam_answers[i] = selected_opt
                
        st.markdown("---")
        
        # Submission
        if not st.session_state.exam_submitted:
            if st.button("📊 Evaluate My Communication Skills", use_container_width=True):
                st.session_state.exam_submitted = True
                st.rerun()
        else:
            # Score Calculation
            correct = 0
            wrong = 0
            unattempted = 0
            
            for i, eq in enumerate(exam_questions):
                user_ans = st.session_state.exam_answers.get(i, None)
                if user_ans is None:
                    unattempted += 1
                elif user_ans == eq["answer"]:
                    correct += 1
                else:
                    wrong += 1
                    
            total_exam = len(exam_questions)
            score_percentage = (correct / total_exam) * 100
            
            # Display Score card
            st.markdown("## 📈 Exam Scorecard")
            
            col_ex1, col_ex2, col_ex3 = st.columns(3)
            with col_ex1:
                st.markdown(f"<div class='stat-card' style='border-color:#00e676;'><div class='stat-value' style='color:#00e676;'>✅ {correct}</div><div class='stat-label'>Correct</div></div>", unsafe_allow_html=True)
            with col_ex2:
                st.markdown(f"<div class='stat-card' style='border-color:#ff1744;'><div class='stat-value' style='color:#ff1744;'>❌ {wrong}</div><div class='stat-label'>Wrong</div></div>", unsafe_allow_html=True)
            with col_ex3:
                st.markdown(f"<div class='stat-card' style='border-color:#ffb300;'><div class='stat-value' style='color:#ffb300;'>⚪ {unattempted}</div><div class='stat-label'>Unattempted</div></div>", unsafe_allow_html=True)
                
            st.markdown(f"<h3 style='text-align: center; margin-top: 20px;'>Overall Score: <span style='color: #00e676;'>{score_percentage:.1f}%</span></h3>", unsafe_allow_html=True)
            
            # Badge awarding
            if score_percentage >= 85:
                st.success("🌟 **Congratulations!** You passed with flying colors! Awarded Badge: **Excellent Global Communicator**.")
                st.balloons()
            elif score_percentage >= 70:
                st.info("👍 **Good Effort!** You passed. Awarded Badge: **Customer Support Specialist**.")
            else:
                st.warning("⚠️ **Needs Practice.** You scored below the 70% threshold. We recommend reviewing the practice questions and retaking the exam.")
                
            # Review answers
            st.markdown("### 📝 Review Correct Responses:")
            for i, eq in enumerate(exam_questions):
                user_ans = st.session_state.exam_answers.get(i, None)
                correct_ans = eq["answer"]
                
                is_correct = user_ans == correct_ans
                color = "#00e676" if is_correct else "#ff1744"
                status_text = "✅ Correct" if is_correct else f"❌ Incorrect (You chose {user_ans})"
                
                with st.expander(f"Q{i+1}. {eq['question'][:70]}... - {status_text}"):
                    st.markdown(f"**Full Question:** {eq['question']}")
                    st.markdown(f"**Your Choice:** {user_ans}. {eq['options'].get(user_ans, 'Unattempted')}")
                    st.markdown(f"**Correct Choice:** {correct_ans}. {eq['options'][correct_ans]}")
                    st.markdown(f"**Explanation:** {eq['explanation']}")
                    st.markdown(f"**Skill Focus:** {eq['skill']}")
                    
            if st.button("🔄 Retake Exam"):
                reset_exam()
                st.rerun()

# ---------------------------------
# MODE 6: CULTURAL CHEAT SHEETS
# ---------------------------------
elif active_mode == "💡 Cultural Cheat Sheets":
    st.markdown("<h1>💡 Cultural Communication Guide</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a5c0; font-size: 16px;'>Quick guidelines for talking with customers from different global regions in the Uber Wheelz process.</p>", unsafe_allow_html=True)
    
    tab_us, tab_eu, tab_ea, tab_af = st.tabs(["🇺🇸 USA", "🇪🇺 Europe", "🇯🇵 East Asia", "🇿🇦 Africa"])
    
    with tab_us:
        st.markdown("""
        ### 🇺🇸 USA Support Guidelines
        * **Communication Style:** Direct, conversational, fast, assertive, active voice.
        * **Do's:**
          * Get straight to the point immediately.
          * Use active phrases like *"I will look into this right now"* instead of passive phrasing.
          * Address them by their first name to build friendly, confident rapport.
          * Express confidence and take direct ownership of their issues.
        * **Don'ts:**
          * Never tell them to *"relax"*, *"calm down"*, or *"don't worry"* as it sounds patronizing.
          * Avoid robotic scripts like *"I apologize for the inconvenience caused, please wait"*.
          * Do not use overly formal honorifics if they want to chat quickly.
        * **Key Vocabulary & Slang:**
          * *Rip-off* = Overcharge/unfair price.
          * *Heads up* = Quick warning.
          * *Pull up* = Open trip details.
          * *In a bind* = In a difficult/stuck situation.
        """)
        
    with tab_eu:
        st.markdown("""
        ### 🇪🇺 Europe Support Guidelines
        * **Communication Style:** Structured, formal, precise, respectful.
        * **Do's:**
          * Use highly polite, structured formats (bulleted lists or step-by-step numbers).
          * Respect spelling differences (e.g., *boot* for trunk, *petrol* for gas, *queue* for line, *holiday* for vacation).
          * Take GDPR privacy requests seriously. Verify accounts properly.
          * Be polite and use formal structures like *"I apologize for the trouble, could you please confirm..."*
        * **Don'ts:**
          * Avoid overly casual slang like *"wanna"*, *"mate"*, or *"yo"*.
          * Do not bypass verification steps (violating GDPR rules).
          * Avoid messy, unstructured paragraphs.
        """)
        
    with tab_ea:
        st.markdown("""
        ### 🇯🇵 East Asia Support Guidelines (Japan, S. Korea, Singapore)
        * **Communication Style:** Highly respectful, indirect, formal, calm, patient.
        * **Do's:**
          * Use formal honorifics (Mr., Ms., or full names). Avoid first names initially.
          * Offer sincere, structured apologies acknowledging the customer's value.
          * Deliver negative decisions softly and give clear, logical rationales (*"To be fair to the driver's wait time..."*).
          * Read indirect signals (e.g., *"a bit uncomfortable"* = major complaint).
        * **Don'ts:**
          * Never use direct or aggressive "No" responses. Offer polite alternatives.
          * Do not sound informal or casual.
          * Avoid forcing rapid-fire, direct statements.
        """)
        
    with tab_af:
        st.markdown("""
        ### 🇿🇦 Africa Support Guidelines (South Africa, Nigeria, Kenya)
        * **Communication Style:** Warm, relational, highly respectful, polite.
        * **Do's:**
          * Always start interactions with warm, respectful greetings (*"Good day"*, *"I hope you are doing well"*).
          * Understand local payment options (e.g., cash exchanges, mobile money like M-Pesa).
          * Prioritize safety issues in South Africa with deep empathy and immediate safety team routing.
          * Confirm driver compensation clearly during fare disputes.
        * **Don'ts:**
          * Do not rush past greetings straight into business. It is seen as rude.
          * Do not dismiss mobile payment errors as "third-party issues."
          * Do not ignore local landmark pickups vs. GPS routing issues.
        """)