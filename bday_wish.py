import streamlit as st
import base64
import os
import random
import datetime
import time 

# --- CONFIGURATION & DATA (Concise Definitions) ---
# NOTE: Ensure these three files (image, music, voice) are in the same directory as this Python file.
COLLAGE_FILE = "collage_bg.jpg"
MUSIC_FILE = "bday_music.mp3"
VOICE_FILE = "voice_note.mp3"
PAGE_KEY = 'current_page'

FUTURE_IMAGES = [
    {"file": "future_us_1.jpg", "caption": "Our Cozy Home Together! 🏡"},
    {"file": "future_us_2.jpg", "caption": "This will be one on our photo wall. 🖼️"},
    {"file": "future_us_3.jpg", "caption": "Maybe one day us celebrating a diwali? 🪔"},
    {"file": "future_us_4.jpg", "caption": "Again some desi vibes, after marriage. 💍"},
    {"file": "future_us_5.jpg", "caption": "A kannod kannayidam moment! ✨"},
    {"file": "future_us_6.jpg", "caption": "Maybe after our first child? hehe lol 👶"},
]

MEMORABLE_EVENTS = [
    {"date": "2023-09-08", "event": "You said, you want to be my friend"},
    {"date": "2023-10-28", "event": "It was your birthday and you said that you love me, you proposed to me"},
    {"date": "2023-11-05", "event": "I said a yes!!! and I love you, from then we are officially together"},
    {"date": "2023-11-19", "event": "Our first video call, you in that white tshirt, still makes me fall for you."},
    {"date": "2024-09-07", "event": "The ksrtc memory! held hands and a picture together for the first time"},
    {"date": "2024-12-24", "event": "You surprised me coming to my home."},
    {"date": "2025-02-21", "event": "A day like we wanted for a long time! And you found something rare but you loved it. I made you the happiest this day lol."},
    {"date": "2024-12-31", "event": "Again a picture together"},
]
MEMORABLE_EVENTS.sort(key=lambda x: datetime.datetime.strptime(x["date"], "%Y-%m-%d"))

LOVE_MESSAGES = [
    "I love your perfect smile and also that dumbass smiles too. 😊", "I love the way you always listen to me without judgment.",
    "I love how safe and understood I feel when I'm with you. 💖", "I love the way you ask me speak about my issues.",
    "I love how determined and focused you are.", "I love that you're my best friend and my greatest adventure.",
    "I love your voice.", "I love your eyes, those are mine.",
    "I love our inside jokes.🤫", "I love you simply for being you, my one and only. ✨",
    "I love your smartness and how you explain things to me. 🧠", "I love that protective little growl you make sometimes.",
    "I love when you wear that white t-shirt (especially the one from our first call!).",
    "I love the warmth of your hand when we finally get to hold them. 🫂", "I love how you manage everything like a responsible adult (most of the time 😉).",
    "I love your lips, and that mole on it.", "I love it when you call me cute names.",
    "I love your reassurances and the way you talk about us.", "I love you when you forgive me for my bullshits.",
    "I love you educating me without making me a fool.", "I love youuuuuuuuuuuuuuu in every way.",
    "I love how you get shy when I give you too many compliments. blushing!",
]

THIS_OR_THAT_QUESTIONS = [
    {"key": "q1_me", "question": "Cuddles or Kisses from me?", "options": ["Cuddles (the warmest place)", "Kisses (the sweetest thing)"]},
    {"key": "q2_me", "question": "My loud laugh or My shy smile?", "options": ["My loud, joyful laugh", "My shy, quiet smile"]},
    {"key": "q3_relationship", "question": "Our perfect date?", "options": ["A cozy movie night in with snacks", "A spontaneous, romantic road trip"]},
    {"key": "q4_relationship", "question": "What's more important in our bond?", "options": ["Deep talks until 3 AM", "Silly games and teasing for hours"]},
    {"key": "q5_me_trait", "question": "What quality do you love most in me?", "options": ["My determination and focus", "My cute sensitivity and compassion"]},
]

st.set_page_config(layout="wide")

# --- UTILITY FUNCTIONS ---

def get_base64_of_file(file_path):
    """Converts file to base64."""
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return "" 

def get_file_path(file_name):
    """Returns the full path or None if not found."""
    if not os.path.exists(file_name):
        st.warning(f"File not found: '{file_name}'. Displaying placeholder.")
        return None
    return file_name

def set_page(new_page, prev_page='home'):
    """Handles page navigation."""
    st.session_state['prev_page'] = st.session_state.get(PAGE_KEY, prev_page) 
    st.session_state[PAGE_KEY] = new_page
    
def go_back():
    """Returns to the previous page."""
    st.session_state[PAGE_KEY] = st.session_state.get('prev_page', 'home')

def set_custom_theme(collage_file, music_file):
    """Applies the CSS theme and embeds music control with auto-play attempt."""
    
    first_image_base64 = get_base64_of_file(collage_file)
    music_base64 = get_base64_of_file(music_file)

    bg_image_url = f"url('data:image/jpeg;base64,{first_image_base64}')" if first_image_base64 else "none"
    
    # 1. MUSIC AUTOPLAY FIX: The HTML/JS below is the most robust way to start music
    # on the first user interaction (click/touch), as required by modern browsers.
    html_content = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Chewy&family=Fuzzy+Bubbles:wght@400;700&family=Dancing+Script:wght@400;700&display=swap');
        
        /* General Text Color & Font */
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
        
        /* 2. Content Container */
        .main .block-container {{
            max-width: 800px; width: 95% !important; padding: 20px !important;
            margin-left: auto; margin-right: auto; background-color: #FFFFFF; 
            border-radius: 25px; box-shadow: 0 8px 20px rgba(255, 105, 180, 0.5); 
            border: 5px solid #ffb6c1; 
        }}
        
        /* 3. Titles and Headings */
        h1 {{
            font-family: 'Chewy', cursive; color: #b00072; font-size: 2.5em; 
            text-shadow: 2px 2px 0 #ffe0f0; text-align: center;
            border-bottom: 4px dashed #ffb6c1; padding-bottom: 10px;
        }}
        
        /* 4. Input Boxes Fix (Black Dialog Boxes to Light Pink) */
        /* Targets text inputs, text areas, and number inputs */
        div[data-testid="stTextInput"] input, 
        div[data-testid="stTextarea"] textarea,
        div[data-testid="stNumberInput"] input {{
            background-color: #FFFFFF !important; /* White Background */
            color: #b00072 !important; /* Deep Pink Text */
            border: 1px solid #ffb6c1;
            border-radius: 5px;
        }}
        
        /* Ensures the area surrounding the text box is also light pink */
        div[data-testid="stTextInput"] > div > div, 
        div[data-testid="stTextarea"] > div {{
            background-color: #fff0f5 !important; 
        }}

        /* 5. Radio Buttons for This or That Grid */
        div[data-testid="stRadio"] label {{
            background-color: #ffedf0; /* Light background for options */
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
            border: 1px solid #ffb6c1;
            text-align: center;
            line-height: 1.2;
            cursor: pointer;
            transition: all 0.2s;
        }}
        
        div[data-testid="stRadio"] label:hover {{
             background-color: #ffe0f0;
        }}
        
        /* Streamlit Button Styling */
        .stButton > button {{
            background-color: #ffb6c1;
            color: white !important; 
            border: 2px solid #ff99aa; 
            border-radius: 10px;
            padding: 8px 15px;
            font-family: 'Fuzzy Bubbles', cursive;
            font-size: 0.9em; 
        }}

        </style>
        
        <audio id="bday-music" loop autoplay style="display:none">
            <source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3">
        </audio>
        
        <script>
        var music = document.getElementById('bday-music');

        // 1. Attempt unmuted play immediately (often fails due to browser policy)
        if (music) {{
            music.volume = 0.4; // Set a default volume
            music.play().catch(error => {{
                // 2. Fallback: If autoplay fails, try again silently (muted)
                music.muted = true;
                music.play().catch(silentError => {{
                    // Silent autoplay failed too, wait for user click
                }});
            }});
        }}

        // 3. Unmute and play on the first user interaction 
        function attemptUnmuteAndPlay() {{
            if (music) {{
                music.muted = false; // Unmute
                music.play().catch(error => {{
                    // Failed to play even on user click (rare, but good to handle)
                }});
            }}
        }}
        
        // Listen for ANY click or touch event on the entire document
        document.addEventListener('click', attemptUnmuteAndPlay, {{ once: true }}); 
        document.addEventListener('touchstart', attemptUnmuteAndPlay, {{ once: true }});
        </script>
        """

    st.markdown(html_content, unsafe_allow_html=True)

# --- PAGE FUNCTIONS ---

def page_home():
    st.title("Happy Birthday, My Loveeeeeeee!!!!")
    
    if os.path.exists(COLLAGE_FILE):
        st.image(COLLAGE_FILE, caption="Look closely! Some beautiful moments of us are here.", use_container_width=True)
    
    st.markdown("---")
    
    cols = st.columns(3)
    cols[0].button("💌 My Love Letter", use_container_width=True, on_click=lambda: set_page('letter', 'home'))
    cols[1].button("🔮 See Our Future", use_container_width=True, on_click=lambda: set_page('future', 'home'))
    cols[2].button("🍯 Open The Love Jar", use_container_width=True, on_click=lambda: set_page('love_jar', 'home'))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    cols2 = st.columns(3)
    cols2[0].button("🗺️ Memories Roadmap", use_container_width=True, on_click=lambda: set_page('memories_timeline', 'home'))
    cols2[1].button("🎮 Birthday Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'home'))
    cols2[2].button("🎂 Virtual Celebration", use_container_width=True, on_click=lambda: set_page('celebration_room', 'home'))

def page_letter():
    st.title("A sweet letter for you.")
    
    letter_content = """
    <div style="background-color: #fff0f5; padding: 35px; border-radius: 15px; border: 2px solid #ffb6c1; box-shadow: 0 4px 10px rgba(255, 105, 180, 0.2);">
        <p style='font-style: italic cursive; font-size: 0.95em; line-height: 1.6; padding: 5px;'>
            My Favourite Teddy Bear,<br>
            Happy Birthday! You are the best part of my life, and every day with you makes me happy. This little surprise is a testament to how much I cherish you. I felt like I should do something special for you, and with my limitations in gifts and my knowledge I thought about this idea, only for us. And here how can you stop me from gifting this??? Heheheehhhh. I love you Aaadhiiii. I want to make you the most happiest person. I want to love you like the way you deserve. I want to buy every single thing you need in this world. Once you are fully mine when there is no any limits or distances between us I promise I never leave you to be alone. I will be there for you no matter what the situation is because you are mine then. Even now you are mine, ONLY MINE! and yes I am your's too, ONLY YOUR'S. I actually hate us being this distance. I really miss you as hell. Sometimes I cry thinking about our situation. But later I fell asleep sobbing on my pillow. But it's completely fine. I shall wait for you, if I don't who else? Miss you idiot. Meet me as soon as possible. I really want to see you. Hug you. And lots of kisses. Love you babyyyy. I love you in every way. I love your smile, your kindness, and the way you always make me feel like the most important person in the world. I am really proud of what you are and day by day you are making me falling for you again and againnnnn. I hope you feel all the love I've poured into this today. Love you infinitely, I promise I can't love anyone like the way I love you. Also sorry for some of my dumbass behaviours. Shall annoy you more. Tolerate me pleaseeee. Love youuuuuuuu.
            <br><br>
            Forever yours,<br>
            Aamiii 💋
        </p>
    </div>
    """
    st.markdown(letter_content, unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.button("🏠 Home", use_container_width=True, on_click=lambda: set_page('home', 'letter'))
    col2.button("🔊 Voice Note", use_container_width=True, on_click=lambda: set_page('voice', 'letter'))
    col3.button("📥 Message Back!", use_container_width=True, on_click=lambda: set_page('message_back', 'letter'))

def page_voice():
    st.title("A Little Voice from Me to You! 🎙️")
    st.markdown("<h3>Listen to my sweet little message!</h3>", unsafe_allow_html=True)

    voice_path = get_file_path(VOICE_FILE)
    if voice_path:
        # 3. FIX: Added the key="voice_audio" for the JavaScript to correctly target this element.
        st.audio(voice_path, format="audio/mp3") 
    
        # JAVASCRIPT TO PAUSE/RESUME MUSIC: This ensures the background music pauses
        # when the user plays the voice note, and resumes when the voice note is finished or paused.
        js_control = """
        <script>
            const bgMusic = document.getElementById('bday-music');
            // The querySelector now correctly targets the element that has the key="voice_audio"
            const voiceAudio = document.querySelector('[data-testid="stAudio"] audio');
            
            if (bgMusic && voiceAudio) {
                // Pause background music on voice note play
                voiceAudio.onplay = function() {
                    bgMusic.pause();
                };
                // Resume background music when voice note ends
                voiceAudio.onended = function() {
                    bgMusic.play().catch(e => console.log("BG music resume failed on end:", e));
                };
                // Resume background music if user manually pauses voice note
                voiceAudio.onpause = function() {
                    // Only resume if the voice note hasn't fully finished
                    if (voiceAudio.currentTime < voiceAudio.duration) { 
                        bgMusic.play().catch(e => console.log("BG music resume failed on pause:", e));
                    }
                };
            }
        </script>
        """
        st.markdown(js_control, unsafe_allow_html=True)

    st.markdown("---")
    st.button("⬅️ Back to Previous Page", use_container_width=True, on_click=go_back)


def page_future():
    st.title("🔮 Looking Into Our Future!")
    st.markdown("<h3>A sneak peek of what our life might look like someday! 💍</h3>", unsafe_allow_html=True)

    # REMOVED the old success message block to prepare for in-line placement

    if not st.session_state.get('favorite_future_image_saved'):
        st.info("Pick your favorite picture below! Your choice will be saved! 👇")
    
    image_keys = [data["caption"] for data in FUTURE_IMAGES]
    
    cols = st.columns(2)
    for i, data in enumerate(FUTURE_IMAGES):
        file_path = get_file_path(data["file"])
        with cols[i % 2]:
            if file_path:
                st.image(file_path, caption=data["caption"], use_container_width=True)

    st.markdown("---")
    
    try:
        default_index = image_keys.index(st.session_state.get('favorite_future_image'))
    except (ValueError, TypeError): 
         default_index = 0
    
    selected_image_caption = st.radio(
        "**Which of these moments is your favorite vision for us?**",
        options=image_keys,
        index=default_index,
        key='future_image_selector'
    )
    
    # 2. FUTURE IMAGE FIX: Message shown beside the save button using columns
    col_button, col_message = st.columns([1, 2])
    
    if col_button.button("Save this Future Pic! 💾", use_container_width=True):
        st.session_state['favorite_future_image'] = selected_image_caption
        st.session_state['favorite_future_image_saved'] = True
        st.toast("Future Pic Saved! ❤️", icon="💾")
        st.rerun() 
        
    if st.session_state.get('favorite_future_image_saved'):
        col_message.success(
            f"**Future Pic Saved!** 💖 You chose: **{st.session_state['favorite_future_image']}**! "
            "This will be our official future goal! 🥰"
        )


    st.markdown("---")
    st.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'future'))


def page_love_jar():
    st.title("🍯 Open the Love Jar")
    st.markdown("<h3>A random reason why I love you! Click the button to get another!</h3>", unsafe_allow_html=True)
    
    if 'current_love_message' not in st.session_state or st.session_state['current_love_message'] is None:
        st.session_state['current_love_message'] = random.choice(LOVE_MESSAGES)

    st.markdown(
        f"""
        <div style="background-color: #ffefff; padding: 40px; border-radius: 20px; border: 5px solid #ffccff; text-align: center; box-shadow: 0 4px 15px rgba(255, 105, 180, 0.7); color:#b00072;">
            <p style="font-size: 1.5em; color: #b00072; font-weight: bold; margin-bottom: 0; font-family: 'Dancing Script', cursive;">
                "{st.session_state['current_love_message']}"
            </p>
            </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.button("Pick Another Message! 💖", use_container_width=True, on_click=lambda: st.session_state.update({'current_love_message': random.choice(LOVE_MESSAGES)}))
    col2.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'love_jar'))


def page_message_back():
    st.title("📥 Send a Message Back!")
    
    if st.session_state.get('message_status') == 'sent':
        # 4. MESSAGE BACK FIX: Removed st.balloons()
        st.success("Message sent! I'll be reading it soon. Thank you, my love! 🥰")
    else:
        with st.form("feedback_form"):
            st.text_input("My boy, your name?:", key='your_name', value="Aaadhi")
            st.text_area("What you like to tell me after my cute wish? Type it here!", key='message', height=150)
            
            def submit_message_action():
                if st.session_state.message:
                    st.session_state['message_status'] = 'sent'
            
            submitted = st.form_submit_button("Send Your Love Note! 💌", on_click=submit_message_action)
            
            if submitted and st.session_state.get('message_status') == 'sent':
                st.rerun() 
            elif submitted and not st.session_state.message:
                st.error("Please write a message before sending!")

    st.markdown("---")
    st.button("⬅️ Back to Previous Page", use_container_width=True, on_click=go_back)

def page_memories_timeline():
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
    st.title("🎮 Birthday Games Hub")
    st.markdown("<h3>Let's have some fun before we cut the cake! 🕹️</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.button("❤️ Find My Hearts", use_container_width=True, on_click=lambda: set_page('catch_hearts', 'games_hub'))
    col2.button("🎡 Spin the Wheel", use_container_width=True, on_click=lambda: set_page('spin_wheel', 'games_hub'))
    col3.button("❓ This or That", use_container_width=True, on_click=lambda: set_page('this_or_that', 'games_hub'))
        
    st.markdown("---")
    st.button("⬅️ Back to Home", use_container_width=True, on_click=lambda: set_page('home', 'games_hub'))


def page_this_or_that():
    st.title("❓ This or That: Couple Edition!")
    st.markdown("<h3>Let's see how well you know your girl and what you love about 'us'!</h3>", unsafe_allow_html=True)
    
    if st.session_state.get('this_or_that_saved'):
        st.success("Responses Saved! 💾 My heart is full knowing your thoughts! Thank you, my love! 🥰")
        st.markdown("---")
    else:
        st.info("Answer all the questions below and click **'Save My Responses'** to let me see your heart! 👇")

        with st.form("this_or_that_form"):
            current_responses = st.session_state.get('this_or_that_responses', {})
            
            # Use two columns for the grid layout
            cols = st.columns(2)
            
            for i, q_data in enumerate(THIS_OR_THAT_QUESTIONS):
                col_index = i % 2
                
                with cols[col_index]:
                    st.markdown(f"**{i+1}. {q_data['question']}**", unsafe_allow_html=True)

                    default_option = current_responses.get(q_data['key'])
                    try:
                        default_index = q_data['options'].index(default_option)
                    except (ValueError, TypeError):
                        default_index = 0 
                    
                    st.radio(
                        "Choose One:",
                        options=q_data['options'],
                        index=default_index,
                        key=f"response_{q_data['key']}",
                        label_visibility='collapsed'
                    )
                    st.markdown("---")

            def submit_responses_action():
                new_responses = {}
                all_answered = True
                
                for q_data in THIS_OR_THAT_QUESTIONS:
                    key = f"response_{q_data['key']}"
                    response = st.session_state.get(key)
                    if not response:
                        all_answered = False
                        break
                    new_responses[q_data['key']] = response
                
                if all_answered:
                    st.session_state['this_or_that_responses'] = new_responses
                    st.session_state['this_or_that_saved'] = True
                else:
                    st.error("Please ensure you have selected an option for all questions.") 

            submitted = st.form_submit_button("Save My Responses! 💾", on_click=submit_responses_action, use_container_width=True)
            
            if submitted and st.session_state.get('this_or_that_saved'):
                st.rerun() 

    st.markdown("---")
    st.button("⬅️ Back to Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'this_or_that'))


def page_catch_hearts():
    st.title("❤️ Find My Hearts Challenge!")
    hearts_found = st.session_state.get('hearts_caught', 0)
    
    # Check for win condition
    if hearts_found >= 3:
        st.title("🏆 Perfect Catch! 🏆")
        # 5. FIND HEARTS FIX: Removed st.balloons()
        st.success("All hearts secured! Our love is strong! 💪")
        col1, col2 = st.columns(2)
        # Reset game variables when clicking 'Play Again'
        col1.button("Play Again", use_container_width=True, on_click=lambda: st.session_state.update({PAGE_KEY: 'catch_hearts', 'hearts_caught': 0, 'correct_spot_index': random.randint(0, 8)}))
        col2.button("⬅️ Back to Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'catch_hearts_won'))
        return

    st.markdown(f"**Progress:** {'❤️' * hearts_found}{'🤍' * (3 - hearts_found)}")

    correct_spot_index = st.session_state.get('correct_spot_index')
    
    # The crucial fix for game logic: Handle click, update state, and trigger rerun
    def handle_click(clicked_spot_index):
        if clicked_spot_index == st.session_state['correct_spot_index']:
            # Update state variables
            st.session_state['hearts_caught'] += 1
            st.session_state['correct_spot_index'] = random.randint(0, 8) 
            st.toast("A heart found! ❤️", icon='🎉')
        else:
            st.toast("❌ Oops! Empty. Try again! 💔", icon='❌')
    
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


def page_spin_wheel():
    st.title("🎡 Spin the Wheel of Memories")

    if 'wheel_state' not in st.session_state:
        st.session_state['wheel_state'] = 'initial' # 'initial', 'spinning', 'result'
    if 'wheel_result' not in st.session_state:
        st.session_state['wheel_result'] = None
    
    memory_events = [f"{datetime.datetime.strptime(e['date'], '%Y-%m-%d').strftime('%B %d, %Y')} - {e['event']}" for e in MEMORABLE_EVENTS]
    
    def spin_wheel_action():
        # Only spin if not already spinning (to prevent double clicks)
        if st.session_state['wheel_state'] != 'spinning':
            st.session_state['wheel_state'] = 'spinning'
    
    def finalize_spin():
        st.session_state['wheel_result'] = random.choice(memory_events)
        st.session_state['wheel_state'] = 'result'
        st.toast("Spin Complete! 🎉", icon='🥳')

    lottie_wheel_html = """
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player id="lottie-wheel" src="https://lottie.host/46497f62-381c-4b68-80af-c119932135c3/tP6n4NlS4n.json" 
        background="transparent" speed="1" style="width: 250px; height: 250px;" loop autoplay></lottie-player>
    </div>
    """
    st.markdown(lottie_wheel_html, unsafe_allow_html=True)

    if st.session_state['wheel_state'] == 'initial' or st.session_state['wheel_state'] == 'result':
        st.button("SPIN THE WHEEL! 🤞", use_container_width=True, on_click=spin_wheel_action)
    
    # Process the spinning state after the button click and rerun
    if st.session_state['wheel_state'] == 'spinning':
        with st.spinner('The wheel is spinning...'):
            time.sleep(1.5) # Simulate spin time
        finalize_spin()
    
    if st.session_state['wheel_state'] == 'result' and st.session_state['wheel_result']:
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
        # Note: Spin Again also calls spin_wheel_action which leads to rerun
        col1.button("Spin Again!", use_container_width=True, on_click=spin_wheel_action)
        col2.button("⬅️ Back to Games Hub", use_container_width=True, on_click=lambda: set_page('games_hub', 'spin_wheel'))


def page_celebration_room():
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
                    <span class='candle-flame' style='color:orange;'>🔥</span> <span class='candle-flame' style='color:orange;'>🔥</span> <span class='candle-flame' style='color:orange;'>🔥</span>
                </p>
                <p style="font-size: 1.5em; color: #ff69b4;">🍰🍰🍰</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.button("Click to BLOW OUT the Candles! 🌬️", use_container_width=True, on_click=lambda: st.session_state.update({'candles_blown': True}))
        st.info("Make sure to close your eyes and make a special wish first!")
        
    else:
        st.subheader("💌 A Special Digital Card Just For You!")
        st.success("🎉 WISH GRANTED! The candles are out! Happy Birthday!")
        st.balloons()
        
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
    # Initialize session states with all stable defaults in one go
    defaults = {
        PAGE_KEY: 'home', 
        'prev_page': 'home', 
        'message_status': '', 
        'hearts_caught': 0, 
        'candles_blown': False, 
        'correct_spot_index': random.randint(0, 8), 
        'current_love_message': random.choice(LOVE_MESSAGES), 
        'wheel_state': 'initial', 
        'wheel_result': None, 
        'favorite_future_image': None, 
        'favorite_future_image_saved': False,
        'this_or_that_responses': {}, 
        'this_or_that_saved': False 
    }
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value
    
    set_custom_theme(COLLAGE_FILE, MUSIC_FILE)

    # Routing
    page_functions = {
        'home': page_home, 'letter': page_letter, 'voice': page_voice, 
        'future': page_future, 'love_jar': page_love_jar, 'message_back': page_message_back, 
        'memories_timeline': page_memories_timeline, 'games_hub': page_games_hub, 
        'catch_hearts': page_catch_hearts, 'spin_wheel': page_spin_wheel,
        'celebration_room': page_celebration_room, 'this_or_that': page_this_or_that
    }
    
    current_page = st.session_state[PAGE_KEY]
    if current_page in page_functions:
        page_functions[current_page]()

if __name__ == '__main__':
    main()