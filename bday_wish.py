import streamlit as st
import base64
import os
import random
import datetime
import time 

# --- CONFIGURATION (No changes here, data is consistent) ---
COLLAGE_FILE = "collage_bg.jpg"
MUSIC_FILE = "bday_music.mp3"
VOICE_FILE = "voice_note.mp3"
PAGE_KEY = 'current_page'

# Placeholder data (ensure these files are present)
FUTURE_IMAGES = [
    {"file": "future_us_1.jpg", "caption": "Our Cozy Home Together! 🏡"},
    {"file": "future_us_2.jpg", "caption": "This will the one on the wall. 🖼️"},
    {"file": "future_us_3.jpg", "caption": "Maybe one day us celebrating a diwali? 🪔"},
    {"file": "future_us_4.jpg", "caption": "Again some desi vibes, after marriage. 💍"},
    {"file": "future_us_5.jpg", "caption": "A kannod kannayidam moment! ✨"},
    {"file": "future_us_6.jpg", "caption": "Maybe after our first child? hehe lol 👶"},
]

MEMORABLE_EVENTS = [
    {"date": "2023-09-08", "event": "You said, you want to be my friend"},
    {"date": "2023-10-28", "event": "It was your birthday and you said that you love me, you proposed to me"},
    {"date": "2023-11-05", "event": "I said a yes!!! and I love you, from then we are officially together"},
    {"date": "2023-10-12", "event": "Our first video call, you in that white tshirt, still makes me fall for you."},
    {"date": "2024-09-07", "event": "The ksrtc memory! held hands and a picture together for the first time"},
    {"date": "2024-12-24", "event": "You surprised me coming to my home."},
    {"date": "2024-02-21", "event": "Like we wanted for a long time! And you found something rare but you loved it. I made you the happiest this day lol."},
    {"date": "2024-12-31", "event": "Again a picture together"},
]
MEMORABLE_EVENTS.sort(key=lambda x: datetime.datetime.strptime(x["date"], "%Y-%m-%d"))

LOVE_MESSAGES = [
    "I love your perfect smile and also that dumbass smiles too. 😊",
    "I love the way you always listen to me without judgment.",
    "I love how safe and understood I feel when I'm with you. 💖",
    "I love the way you ask me speak about my issues.",
    "I love how determined and focused you are.",
    "I love that you're my best friend and my greatest adventure.",
    "I love your voice.", "I love your eyes, those are mine.",
    "I love our inside jokes.🤫",
    "I love you simply for being you, my one and only. ✨",
    "I love your smartness and how you explain things to me. 🧠",
    "I love that protective little growl you make sometimes.",
    "I love when you wear that white t-shirt (especially the one from our first call!).",
    "I love the warmth of your hand when we finally get to hold them. 🫂",
    "I love how you manage everything like a responsible adult (most of the time 😉).",
    "I love your lips, and that mole on it.",
    "I love it when you call me cute names.",
    "I love your reassurances and the way you talk about us.",
    "I love you when you forgive me for my bullshits.",
    "I love you educating me without making me a fool.",
    "I love youuuuuuuuuuuuuuu in every way.",
    "I love how you get shy when I give you too many compliments. blushing!",
]

st.set_page_config(layout="wide")

# --- UTILITY FUNCTIONS ---

def get_base64_of_file(file_path):
    """Converts file to base64, handling errors."""
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""

def get_file_path(file_name):
    """Returns the full path to a file, handling missing files gracefully for display."""
    if not os.path.exists(file_name):
        st.warning(f"File not found: '{file_name}'. Displaying placeholder.")
        return None
    return file_name

def set_custom_theme(collage_file, music_file):
    """Applies the cute CSS theme and embeds the music player."""
    
    first_image_base64 = get_base64_of_file(collage_file)
    music_base64 = get_base64_of_file(music_file)

    bg_image_url = f"url('data:image/jpeg;base64,{first_image_base64}')" if first_image_base64 else "none"
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Chewy&family=Fuzzy+Bubbles:wght@400;700&family=Dancing+Script:wght@400;700&display=swap');
        
        /* General Text Color & Font (Deep Pink) */
        .stApp, p, label, .stMarkdown, .stAlert, .stToast {{
            font-family: 'Fuzzy Bubbles', cursive;
            color: #b00072; /* Deep Pink */
        }}

        /* 1. Background */
        .stApp {{
            background-image: {bg_image_url};
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-blend-mode: soft-light;
            background-color: rgba(255, 245, 247, 0.9); /* Base Light Pink */
        }}
        
        /* 2. Top Header Bar FIX */
        [data-testid="stHeader"] {{
            background-color: #ffedf0 !important; /* Very light pink/off-white */
            border-bottom: 2px solid #ffb6c1; 
            color: #b00072; 
        }}
        
        /* 3. Content Container */
        .main .block-container {{
            max-width: 800px; 
            padding: 30px;
            background-color: #FFFFFF; 
            border-radius: 25px; 
            box-shadow: 0 8px 20px rgba(255, 105, 180, 0.5); 
            border: 5px solid #ffb6c1; 
        }}
        
        /* 4. Titles and Headings */
        h1 {{
            font-family: 'Chewy', cursive; 
            color: #b00072; /* Deep Pink */
            font-size: 3.5em; 
            text-shadow: 3px 3px 0 #ffe0f0; 
            text-align: center;
            border-bottom: 4px dashed #ffb6c1;
        }}
        
        h3 {{
            font-family: 'Fuzzy Bubbles', cursive;
            color: #ff99aa; 
            border-bottom: 2px dashed #ffb6c1; 
        }}
        
        /* 5. BUTTON STYLING (General) */
        .stButton > button {{
            background-color: #ffb6c1; /* Light pink background */
            color: white; 
            border: 2px solid #ff99aa; 
            border-radius: 10px;
            padding: 10px 20px;
            font-family: 'Fuzzy Bubbles', cursive;
            font-size: 1.1em;
            box-shadow: 0 4px 8px rgba(255, 105, 180, 0.3);
            transition: all 0.2s ease-in-out;
        }}
        /* IMPORTANT: Ensure button text is white for ALL buttons */
        .stButton > button, 
        .stButton > button * {{
            color: white !important; 
        }}


        .stButton > button:hover {{
            background-color: #ff99aa; 
            color: white;
            border-color: #b00072;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(255, 105, 180, 0.4);
        }}
        
        /* 6. INPUT FIELDS FIX */
        [data-testid="stTextInput"] input, 
        [data-testid="stTextArea"] textarea {{
            background-color: white !important; /* White background */
            color: #b00072 !important; /* Deep Pink text */
            border: 2px solid #ffb6c1 !important; 
            border-radius: 8px !important;
            box-shadow: 0 2px 5px rgba(255, 105, 180, 0.1);
        }}
        .stTextInput div[data-baseweb="input"],
        .stTextArea div[data-baseweb="input"] {{
            background-color: white !important; 
            border: 2px solid #ffb6c1 !important; 
            border-radius: 8px !important;
        }}
        [data-testid="stForm"] label {{
            color: #b00072 !important;
        }}


        /* 7. TOAST/ALERT/ERROR BOX FIX */
        [data-testid="stToast"] {{
            background-color: #fff0f5 !important; 
            border: 2px solid #ffb6c1 !important;
            box-shadow: 0 4px 10px rgba(255, 105, 180, 0.5) !important;
            color: #b00072 !important; 
            opacity: 1; 
        }}
        [data-testid="stToast"] *,
        [data-testid="stAlert"] [role="alert"] * {{
            color: #b00072 !important;
        }}
        
        /* 8. REMOVE SPARKLE HEART DEBUG TEXT */
        .heart-sparkle-container {{ display: none !important; }}
        .stMarkdown span.sparkle-heart {{ display: none; }}
        
        /* 9. General Markdown FIX */
        div[data-testid="stMarkdownContainer"] * {{
            background-color: transparent !important;
            color: inherit;
        }}

        /* 10. Letter Italic Font for Aesthetic */
        .letter-content p {{
            font-style: italic cursive !important;
            padding: 10px; /* Added padding to ensure text doesn't touch edges */
        }}

        </style>
        <audio id="bday-music" loop style="display:none">
            <source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3">
        </audio>
        
        <script>
        function controlMusic(action) {{
            var music = document.getElementById('bday-music');
            if (!music) return;
            music.volume = 0.4; 
            if (action === 'play') {{ music.play().catch(error => {{}}); }} 
            else if (action === 'pause') {{ music.pause(); }}
        }}
        controlMusic('play'); 
        document.addEventListener('click', () => controlMusic('play'), {{ once: true }}); 
        </script>
        """,
        unsafe_allow_html=True
    )
    
def music_js_command(action):
    st.components.v1.html(f"<script>controlMusic('{action}');</script>", height=0, width=0)

def show_celebration_effects_simple():
    """Confetti/Balloons only."""
    st.balloons()
    
def init_hearts_game(num_hearts=3): 
    """Initializes the Catch the Hearts game state."""
    st.session_state['hearts_to_find'] = list(range(1, num_hearts + 1)) 
    st.session_state['hearts_caught'] = 0
    st.session_state['correct_spot_index'] = random.randint(0, 8) 

def new_love_message():
    """Selects a new random message for the love jar."""
    st.session_state['current_love_message'] = random.choice(LOVE_MESSAGES)

# --- PAGE NAVIGATION STATE ---

def set_page(new_page, prev_page='home'):
    """Sets the new page and stores the previous page for the 'Back' button."""
    st.session_state['prev_page'] = st.session_state.get(PAGE_KEY, prev_page) 
    st.session_state[PAGE_KEY] = new_page
    
def go_back():
    """Goes back to the previously stored page."""
    st.session_state[PAGE_KEY] = st.session_state.get('prev_page', 'home')

# --- PAGE FUNCTIONS ---

def page_home():
    music_js_command('play')
    st.title("Happy Birthday, My Loveeeeeeee!!!!")
    st.markdown("<p class='cute-subtitle'>A small cute surprise made for you lovee! </p>", unsafe_allow_html=True)
    
    if os.path.exists(COLLAGE_FILE):
        st.image(COLLAGE_FILE, caption="Look closely! Some beautiful moments of us are here.", use_container_width=True)
    
    st.markdown("<h3>💖 Main Attractions</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; font-size:1.1em; color:#ff69b4; padding:15px; border: 2px dashed #ffb6c1; border-radius:15px; background-color:#fff0f5;">
            You're my biggest adventure and my cozy home all in one. Every page holds a piece of my heart for you! 🥰
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.button("💌 My Love Letter", use_container_width=True, on_click=lambda: set_page('letter', 'home'))
    col2.button("🔮 See Our Future", use_container_width=True, on_click=lambda: set_page('future', 'home'))
    col3.button("🍯 Open The Love Jar", use_container_width=True, on_click=lambda: set_page('love_jar', 'home'))
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_timeline, col_games, col_cake = st.columns(3)
    col_timeline.button("🗺️ Memories Roadmap", use_container_width=True, on_click=lambda: set_page('memories_timeline', 'home'))
    col_games.button("🎮 Birthday Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'home'))
    col_cake.button("🎂 Virtual Celebration", use_container_width=True, on_click=lambda: set_page('celebration_room', 'home'))

def page_letter():
    music_js_command('play')
    st.title("A sweet letter for you.")
    st.markdown("<h3>In our little infinity, I want the best for you.</h3>", unsafe_allow_html=True)
    
    # ***FIX: Added italic font style to the letter content and increased padding***
    letter_content = """
    <div class="letter-content" style="background-color: #fff0f5; padding: 35px; border-radius: 15px; border: 2px solid #ffb6c1; box-shadow: 0 4px 10px rgba(255, 105, 180, 0.2);">
        <p>
            My Dearest Aaadhiiii,<br>
            Happy Birthday! You are the best part of my life, and every day with you makes me happy. This little surprise is a testament to how much I cherish you. I felt like I should do something special for you, and with my limitations in gifts and my knowledge I thought about this idea, only for us. And here how can you stop me from gifting this??? Heheheehhhh. I love you Aadhi. I want to make you the most happiest person. I want to love you like the way you deserve. I want to buy every single thing you need in this world. Once you are fully mine when there is no any limits or distances between us I promise I never leave you to be alone. I will be there for you no matter what the situation is because you are mine then. Even now you are mine, ONLY MINE! and yes I am your's too, ONLY YOUR'S. I actually hate us being this distance. I really miss you as hell. Sometimes I cry thinking about our situation. But later I fell asleep sobbing on my pillow. But it's completely fine. I shall wait for you, if I don't who else? Miss you idiot. Meet me as soon as possible. I really want to see you. Hug you. And lots of kisses. Love you babyyyy. I love you in every way. I love your smile, your kindness, and the way you always make me feel like the most important person in the world. I am really proud of what you are and day by day you are making me falling for you again and againnnnn. I hope you feel all the love I've poured into this today. Love you infinitely, I promise I can't love anyone like the way I love you. Also sorry for some of my dumbass behaviours. Shall annoy you more. Tolerate me pleaseeee. Love youuuuuuuu.
            <br><br>
            Forever yours,<br>
            Aaaamiiiiiii💋
        </p>
    </div>
    """
    st.markdown(letter_content, unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.button("🏠 Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'letter'))
    col2.button("🔊 Voice Note", use_container_width=True, on_click=lambda: set_page('voice', 'letter'))
    col3.button("📥 Message Me Back!", use_container_width=True, on_click=lambda: set_page('message_back', 'letter'))


def page_voice():
    music_js_command('pause') # Music intentionally paused on this page
    st.title("A Little Voice from Me to You! 🎙️")
    st.markdown("<h3>Listen to my sweet little message!</h3>", unsafe_allow_html=True)

    voice_path = get_file_path(VOICE_FILE)
    if voice_path:
        st.audio(voice_path, format='audio/mp3')
        st.markdown(
            f"""
            <div style="background-color:#ffe0f0; padding:15px; border-radius:10px; border:2px dashed #ffb6c1; text-align:center; color:#b00072;">
                <p style="color:#b00072; font-size:1.1em; margin:0;">
                    I hope you like this! It was a little nerve-wracking to record, but only for you. ❤️
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.button("⬅️ Back to Previous Page", use_container_width=True, on_click=go_back)


def page_future():
    music_js_command('play')
    st.title("🔮 Looking Into Our Future!")
    st.markdown("<h3>Some digital edits of what our life might look like someday! A sneak peek just for you... 💍</h3>", unsafe_allow_html=True)

    cols = st.columns(2)
    for i, data in enumerate(FUTURE_IMAGES):
        file_path = get_file_path(data["file"])
        if file_path:
            with cols[i % 2]:
                st.image(file_path, caption=data["caption"], use_container_width=True)

    st.markdown("---")
    st.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'future'))


def page_love_jar():
    music_js_command('play')
    st.title("🍯 Open the Love Jar")
    st.markdown("<h3>A random reason why I love you! Click the button to get another!</h3>", unsafe_allow_html=True)

    if 'current_love_message' not in st.session_state:
        new_love_message() 

    st.markdown(
        f"""
        <div style="background-color: #ffefff; padding: 40px; border-radius: 20px; border: 5px solid #ffccff; text-align: center; box-shadow: 0 4px 15px rgba(255, 105, 180, 0.7); color:#b00072;">
            <p style="font-size: 1.8em; color: #b00072; font-weight: bold; margin-bottom: 0; font-family: 'Dancing Script', cursive;">
                "{st.session_state['current_love_message']}"
            </p>
            </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    col1.button("Pick Another Message! 💖", use_container_width=True, on_click=new_love_message)
    col2.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'love_jar'))


def page_message_back():
    music_js_command('play')
    st.title("📥 Send a Message Back!")
    
    if st.session_state.get('message_status') == 'sent':
        st.success("Message sent! I'll be reading it soon. Thank you, my love! 🥰")
        show_celebration_effects_simple() 
    else:
        with st.form("feedback_form"):
            st.text_input("My boy, your name?:", key='your_name', value="Aaadhi")
            st.text_area("What you like to tell me after my cute wish? Type it here!", key='message', height=150)
            
            def submit_message_action():
                if st.session_state.message:
                    st.session_state['message_status'] = 'sent'
            
            submitted = st.form_submit_button("Send Your Love Note! 💌", on_click=submit_message_action)
            
            if submitted and st.session_state['message_status'] == 'sent':
                st.rerun() 
            elif submitted and not st.session_state.message:
                st.error("Please write a message before sending!")

    st.markdown("---")
    st.button("⬅️ Back to Previous Page", use_container_width=True, on_click=go_back)


def page_memories_timeline():
    music_js_command('play')
    st.title("🗺️ Our Sweetest Memories Roadmap")
    st.markdown("<h3>The path we've traveled so far... and it's beautiful! 🛣️</h3>", unsafe_allow_html=True)
    
    for i, event_data in enumerate(MEMORABLE_EVENTS):
        date_obj = datetime.datetime.strptime(event_data["date"], "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")
        days_passed = (date_obj - datetime.datetime.strptime(MEMORABLE_EVENTS[0]["date"], "%Y-%m-%d")).days
        days_text = f"Day {days_passed}" if days_passed > 0 else "Our Starting Point!"
        
        st.markdown(f"""
            <div style="margin: 10px 0; border-left: 5px solid #ffb6c1; padding-left: 20px; background-color: #fff0f5; border-radius: 10px; padding: 15px;">
                <p style="font-size: 1.1em; color: #ff99aa; margin: 0; font-weight: bold;">{days_text}</p>
                <p style="font-size: 1.3em; color: #b00072; margin: 0; font-weight: bold;">{formatted_date}</p>
                <p style="margin: 5px 0 0 0; color:#b00072;">{event_data["event"]}</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<p style='text-align:center; margin-top:30px; font-size:1.5em; color:#b00072;'>...and many more to come! ♾️</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'memories_timeline'))


def page_games_hub():
    music_js_command('play')
    st.title("🎮 Birthday Games Hub")
    st.markdown("<h3>Let's have some fun before we cut the cake! It's a game date! 🕹️</h3>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background-color:#ffe6f2; padding:20px; border:3px solid #ffb6c1; border-radius:15px; text-align:center;">
            <p style="font-size:1.5em; color:#b00072; font-weight:bold;">
                Choose your game! Ready, set, love!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    col1.button("❤️ Find My Hearts (Quick Challenge)", use_container_width=True, on_click=lambda: set_page('catch_hearts', 'games_hub'))
    col2.button("🎡 Spin the Wheel of Memories", use_container_width=True, on_click=lambda: set_page('spin_wheel', 'games_hub'))
        
    st.markdown("---")
    st.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'games_hub'))

def page_catch_hearts():
    music_js_command('play')
    st.title("❤️ Find My Hearts Challenge!")
    st.markdown("<h3>Find 3 total hearts quickly to win!</h3>", unsafe_allow_html=True)

    if st.session_state.get('correct_spot_index', -1) == -1:
        init_hearts_game(num_hearts=3)

    hearts_found = st.session_state['hearts_caught']
    
    if hearts_found >= 3:
        set_page('catch_hearts_won', 'catch_hearts')
        st.rerun() 
        return

    correct_spot_index = st.session_state['correct_spot_index']

    def handle_click(clicked_spot_index):
        if clicked_spot_index == correct_spot_index:
            st.session_state['hearts_caught'] += 1
            st.toast("A heart found! ❤️", icon='🎉')
            st.session_state['correct_spot_index'] = random.randint(0, 8) 
        else:
            st.toast("❌ Oops! That spot was empty. Try again! 💔", icon='❌')
    
    st.markdown(f"**Heart Level:** {hearts_found + 1} / 3")
    st.markdown(f"**Progress:** {'❤️' * hearts_found}{'🤍' * (3 - hearts_found)}")

    button_index = 0
    for row in range(3):
        cols = st.columns(3)
        for col_index in range(3):
            with cols[col_index]:
                st.button(
                    "Search Here", 
                    key=f"grid_spot_{row}_{col_index}", 
                    on_click=handle_click, 
                    args=(button_index,), 
                    use_container_width=True
                )
            button_index += 1
    
    st.markdown("---")
    st.button("⬅️ Back to Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'catch_hearts'))


def page_catch_hearts_won():
    music_js_command('play')
    st.title("🏆 Perfect Catch! 🏆")
    st.success("All hearts secured! Our love is strong! 💪")
    show_celebration_effects_simple()

    lottie_html = """
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="https://lottie.host/8e2f8216-7243-4423-a128-4f9e1590408d/K5lPj13i43.json" 
        background="transparent" speed="1" style="width: 200px; height: 200px;" autoplay loop></lottie-player>
    </div>
    """
    st.markdown(lottie_html, unsafe_allow_html=True)

    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.button("Play Again", use_container_width=True, on_click=lambda: st.session_state.update({PAGE_KEY: 'catch_hearts', 'hearts_caught': 0, 'correct_spot_index': -1}))
    col2.button("⬅️ Back to Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'catch_hearts_won'))


def page_spin_wheel():
    music_js_command('play')
    st.title("🎡 Spin the Wheel of Memories")

    if 'wheel_result' not in st.session_state:
        st.session_state['wheel_result'] = None
    
    memory_events = [f"{datetime.datetime.strptime(e['date'], '%Y-%m-%d').strftime('%B %d, %Y')} - {e['event']}" for e in MEMORABLE_EVENTS]
    
    def spin_wheel_action():
        st.session_state['wheel_result'] = "Spinning..."
    
    def finalize_spin():
        st.session_state['wheel_result'] = random.choice(memory_events)
        st.toast("Spin Complete! 🎉", icon='🥳')

    lottie_wheel_html = """
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player id="lottie-wheel" src="https://lottie.host/46497f62-381c-4b68-80af-c119932135c3/tP6n4NlS4n.json" 
        background="transparent" speed="1" style="width: 250px; height: 250px;" loop autoplay></lottie-player>
    </div>
    """
    st.markdown(lottie_wheel_html, unsafe_allow_html=True)

    if st.session_state['wheel_result'] is None:
        st.button("SPIN THE WHEEL! 🤞", use_container_width=True, on_click=spin_wheel_action)
    elif st.session_state['wheel_result'] == "Spinning...":
        with st.spinner('The wheel is spinning...'):
            time.sleep(1.5)
        finalize_spin()
        st.rerun() 
    else:
        st.markdown("---")
        st.markdown(f"""
            <div style="background-color:#ffe0f0; padding:30px; border:4px solid #b00072; border-radius:20px; text-align:center; color:#b00072; box-shadow: 0 4px 15px rgba(255, 105, 180, 0.7);">
                <p style="font-size:1.8em; color:#b00072; font-weight:bold;">✨ Your Memory is... ✨</p>
                <p style="font-size:1.4em; font-weight:normal; line-height: 1.5; font-family: 'Dancing Script', cursive;">
                    {st.session_state['wheel_result']}
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        col1, col2 = st.columns(2)
        col1.button("Spin Again!", use_container_width=True, on_click=spin_wheel_action)
        col2.button("⬅️ Back to Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'spin_wheel'))


def page_celebration_room():
    music_js_command('play')
    st.title("🎂 Virtual Celebration Room")

    if 'candles_blown' not in st.session_state:
        st.session_state['candles_blown'] = False

    st.markdown("---")
    
    if not st.session_state['candles_blown']:
        st.subheader("🕯️ Make a Wish!")
        st.markdown("""
            <div style="text-align:center;">
                <p style="font-size: 3em; color: #ff99aa;">🎂🎂🎂</p>
                <p style="font-size: 1.5em; line-height: 0.1;">
                    <span class='candle-flame'>🔥</span> <span class='candle-flame'>🔥</span> <span class='candle-flame'>🔥</span>
                </p>
                <p style="font-size: 1.5em; color: #ff69b4;">🍰🍰🍰</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.button("Click to BLOW OUT the Candles! 🌬️", use_container_width=True, on_click=lambda: st.session_state.update({'candles_blown': True}))
        st.info("Make sure to close your eyes and make a special wish first!")
        
    else:
        st.subheader("💌 A Special Digital Card Just For You!")
        st.success("🎉 WISH GRANTED! The candles are out! Happy Birthday!")
        show_celebration_effects_simple()
        
        fireworks_html = """
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <lottie-player src="https://lottie.host/79a4e402-9ff0-4a81-995b-0045d47d4834/5s1F3b1v8y.json" 
            background="transparent" speed="1" style="width: 250px; height: 250px;" autoplay></lottie-player>
        </div>
        """
        st.markdown(fireworks_html, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="background-color:#fff0f5; padding:30px; border:4px dashed #ff99aa; border-radius:15px; text-align:center; color:#b00072;">
                <p style="font-size:2.0em; color:#b00072; font-weight:bold; margin-bottom: 5px; font-family:'Chewy', cursive;">
                    Happy Birthday, My Aaadhi!
                </p>
                <p style="font-size:1.4em; color:#b00072; font-family: 'Dancing Script', cursive;">
                    I wish you the greatest day filled with joy, laughter, and endless love. 
                    May all your dreams come true! <br> You deserve all the happiness in the world. 
                    <br> I love you, now and always! 💖
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'celebration_room'))


# --- MAIN APP LOGIC ---

def main():
    # Initialize session states (Minimized)
    defaults = {
        PAGE_KEY: 'home', 'prev_page': 'home', 'message_status': '', 
        'hearts_caught': 0, 'candles_blown': False, 'correct_spot_index': -1,
        'wheel_result': None, 'current_love_message': None 
    }
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value
    
    # Set initial love message if not set
    if st.session_state['current_love_message'] is None:
        new_love_message()

    set_custom_theme(COLLAGE_FILE, MUSIC_FILE)

    # Routing
    page_functions = {
        'home': page_home, 'letter': page_letter, 'voice': page_voice, 
        'future': page_future, 'love_jar': page_love_jar, 'message_back': page_message_back, 
        'memories_timeline': page_memories_timeline, 'games_hub': page_games_hub, 
        'catch_hearts': page_catch_hearts, 'catch_hearts_won': page_catch_hearts_won, 
        'spin_wheel': page_spin_wheel, 'celebration_room': page_celebration_room
    }
    
    current_page = st.session_state[PAGE_KEY]
    if current_page in page_functions:
        page_functions[current_page]()

if __name__ == '__main__':
    main()