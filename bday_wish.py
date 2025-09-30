import streamlit as st
import base64
import os

# --- FILE NAMES & CONFIGURATION (EASY TO EDIT) ---
COLLAGE_FILE = "collage_bg.jpg" 
MUSIC_FILE = "bday_music.mp3"
VOICE_FILE = "voice_note.mp3"
st.set_page_config(layout="wide")
PAGE_KEY = 'current_page'

# --- UTILITY FUNCTIONS ---

def get_base64_of_file(file_path):
    """Converts file to base64, handling errors."""
    try:
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            return encoded
    except FileNotFoundError:
        st.error(f"ERROR: File not found: '{file_path}'. Please check your file names.")
        st.stop() # Stop execution
    except PermissionError:
        st.error(f"ERROR: Permission denied for '{file_path}'. Close the file in all other programs.")
        st.stop() # Stop execution

def set_custom_theme(collage_file, music_file):
    """Applies the cute CSS theme and embeds the music player."""
    
    first_image_base64 = get_base64_of_file(collage_file)
    music_base64 = get_base64_of_file(music_file)

    # --- CSS Styles ---
    st.markdown(
        f"""
        <style>
        /* 1. Background Collage (High Opacity & Cute) */
        .stApp {{
            background-image: url('data:image/jpeg;base64,{first_image_base64}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            opacity: 0.7; /* HIGH OPACITY */
            background-color: #ffe6f2; 
            background-blend-mode: soft-light;
        }}

        /* 2. Content Container (The Cute Card) */
        .main .block-container {{
            max-width: 650px; 
            width: 85%;
            padding: 30px;
            margin-left: auto;
            margin-right: auto;
            background-color: #ffffff;
            border-radius: 25px; 
            box-shadow: 0 8px 20px rgba(255, 105, 180, 0.5); 
            border: 5px solid #ffb6c1; 
            opacity: 1; 
        }}
        
        /* 3. Fonts and Colors (Bright and Clear) */
        .stMarkdown, h1, h3, p, strong, .footer-message {{
            font-family: 'Comic Sans MS', 'Arial', cursive; 
            color: #333333; 
            opacity: 1; 
        }}

        h1 {{
            color: #ff69b4; /* Hot Pink */
            font-size: 3.5em; 
            text-shadow: 3px 3px 0 #ffe0f0; 
            text-align: center;
            padding-bottom: 5px;
            border-bottom: 4px dashed #ffb6c1;
        }}
        
        h3 {{
            color: #ff99aa; /* Soft Coral Pink */
            border-bottom: 2px dashed #ffb6c1; 
            padding-bottom: 5px;
            margin-top: 20px;
        }}

        /* 4. Letter Box Styling */
        .letter-text {{
            font-family: 'Georgia', serif; 
            line-height: 1.7;
            color: #555555;
            padding: 20px;
            background-color: #fff0f5; 
            border-radius: 15px;
            box-shadow: inset 0 0 10px rgba(255, 192, 203, 0.5); 
        }}

        /* Button Styling for Navigation */
        .stButton>button {{
            background-color: #ffb6c1;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
            font-size: 1.1em;
            margin: 5px;
            box-shadow: 0 4px #ff99aa;
            transition: all 0.1s ease;
        }}
        .stButton>button:active {{
            box-shadow: 0 2px #ff99aa;
            transform: translateY(2px);
        }}
        </style>
        
        <audio id="bday-music" loop style="display:none">
            <source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        
        <script>
        function attemptPlay() {{
            var music = document.getElementById('bday-music');
            if (music) {{
                music.volume = 0.5;
                music.play().catch(error => {{
                    console.log("Autoplay blocked.");
                }});
            }}
        }}
        // Start playing music on ANY user interaction
        document.addEventListener('click', attemptPlay, {{ once: true }}); 
        document.addEventListener('touchstart', attemptPlay, {{ once: true }}); 
        document.addEventListener('scroll', attemptPlay, {{ once: true }});
        </script>
        """,
        unsafe_allow_html=True
    )

# --- PAGE FUNCTIONS ---

def page_home():
    """Home page with main wish and collage."""
    st.title("🎉 Happy Birthday, My Loveeeeeeee!!!! 🎉")
    st.markdown("<p style='text-align:center; color:#ff99aa; font-weight:bold; font-size:1.4em;'>A special surprise made just for you!</p>", unsafe_allow_html=True)
    
    st.image(COLLAGE_FILE, caption="Look closely! All our best memories are here. 💖", use_column_width=True)

    st.markdown("<h3>💖 Cute Stuffs</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; font-size:1.1em; color:#ff69b4; padding:15px; border: 2px dashed #ffb6c1; border-radius:15px; background-color:#fff0f5;">
            Every moment with you is my favorite memory! <br> 
            You're my biggest adventure and my cozy home all in one. 🥰
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.button("💌 Proceed to My Letter", on_click=lambda: st.session_state.update({PAGE_KEY: 'letter'}))

def page_letter():
    """Letter page."""
    st.title("💌 A sweet letter for you.")
    st.markdown("<h3>✨ My Birthday Love Letter</h3>", unsafe_allow_html=True)
    
    # IMPORTANT: Customize this letter content!
    letter_content = """
    <div class="letter-text">

My Dearest Aaadhiiii,<br>
Happy Birthday! You are the best part of my life, and every day with you makes me happy. This little surprise is a testament to how much I cherish you. I felt like I should do something special for you, and with my limitations in gifts and my knowledge I thought about this idea, only for us. And here how can you stop me from gifting this??? Heheheehhhh. I love you Aadhi. I want to make you the most happiest person. I want to love you like the way you deserve. I want to buy every single thing you need in this world. Once you are fully mine when there is no any limits or distances between us I promise I never leave you to be alone. I will be there for you no matter what the situation is because you are mine then. Even now you are mine, ONLY MINE! and yes I am your's too, ONLY YOUR'S. I actually hate us being this distance. I really miss you as hell. Sometimes I cry thinking about our situation. Byut later I fell asleep sobbing on my pillow. But it's completely fine. I shall wait for you, if I don't who else? Miss you idiot. Meet me as soon as possible. I really want to see you. Hug you. And lots of kisses. Love you babyyyy. I love you in every way. I love your smile, your kindness, and the way you always make me feel like the most important person in the world. I am really proud of what you are and day by day you are making me falling for you again and againnnnn. I hope you feel all the love I've poured into this today. Love you infinitely, I promise I can't love anyone like the way I love you. Also sorry for some of my dumbass behaviours. Shall annoy you more. Tolerate me pleaseeee. Love youuuuuuuu.

Forever yours,<br>
Aaaamiiiiiii<br>💋</p>
    </div>
    """
    st.markdown(letter_content, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Back to Home", on_click=lambda: st.session_state.update({PAGE_KEY: 'home'}))
    with col2:
        st.button("🔊 Voice Note Surprise!", on_click=lambda: st.session_state.update({PAGE_KEY: 'voice'}))


def page_voice():
    """Voice note page."""
    st.title("💖 Just a small voice note too: Your Voice Note")
    st.markdown("<h3>🎤 Listen closely to my voice...</h3>", unsafe_allow_html=True)

    # --- Voice Note Player ---
    try:
        st.audio(VOICE_FILE, format="audio/mp3", start_time=0)
    except:
        st.warning("Voice note file not loaded. Check the filename (voice_note.mp3).")

    st.markdown("---")
    st.markdown("""
        <div style="text-align:center; font-size:1.4em; color:#ff69b4; padding:20px; border: 3px solid #ffb6c1; border-radius:15px; background-color:#fff0f5;">
            **Happy Birthday, Sweetheart!** <br>
            I love you more than words! Go have the best day today and forever! 🥰
        </div>
        """, unsafe_allow_html=True)

    st.button("🎉 Start Over", on_click=lambda: st.session_state.update({PAGE_KEY: 'home'}))

# --- MAIN APP LOGIC ---

def main():
    # Initialize the page state
    if PAGE_KEY not in st.session_state:
        st.session_state[PAGE_KEY] = 'home'
    
    # Set the CSS theme (this also loads music and checks files)
    set_custom_theme(COLLAGE_FILE, MUSIC_FILE)

    # Render the current page
    if st.session_state[PAGE_KEY] == 'home':
        page_home()
    elif st.session_state[PAGE_KEY] == 'letter':
        page_letter()
    elif st.session_state[PAGE_KEY] == 'voice':
        page_voice()

if __name__ == '__main__':
    main()