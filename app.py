import streamlit as st
import random

# ---------------- QUESTIONS DATABASE ---------------- #

questions = {

    "😂 Funny": [
        "What is your weirdest habit?",
        "If animals could talk which would be rudest?",
        "What’s the dumbest thing you believed as a kid?",
        "If you were a ghost who would you haunt first?",
        "What would you do if you woke up invisible?",
        "What is your funniest childhood memory?",
        "If you were a vegetable which one would you be?",
        "What is your secret useless talent?",
        "What’s the strangest food you’ve eaten?",
        "If your life was a meme which one would it be?",
        "What would your superhero name be?",
        "What’s the weirdest dream you remember?",
        "What’s your most embarrassing moment?",
        "What would you do if you switched bodies with me?",
        "What is the silliest fear you have?",
        "What cartoon character do you resemble?",
        "What would you do if you became famous overnight?",
        "If you had a warning label what would it say?",
        "What’s the funniest lie you told?",
        "What’s your funniest nickname?",
        "If aliens came who would you send to greet them?",
        "What’s the weirdest thing you googled?",
        "What would your villain name be?",
        "What’s the most useless thing you own?",
        "If you were a fruit which would you be?",
        "What’s your funniest school memory?",
        "What would you do if gravity stopped for 5 seconds?",
        "If you could swap voices with someone who?",
        "What would you do if you turned into a cat for a day?",
        "What would your comedy show be called?"
    ],

    "🤔 Deep": [
        "What motivates you every day?",
        "What is your biggest fear?",
        "What makes you truly happy?",
        "What is your dream life?",
        "What do you value most in friendship?",
        "What is success to you?",
        "What lesson took you longest to learn?",
        "What do you want people to remember about you?",
        "When do you feel most like yourself?",
        "What scares you about the future?",
        "What is something you regret?",
        "What inspires you?",
        "What does happiness mean to you?",
        "Who influenced your life most?",
        "What would your perfect day look like?",
        "What do you think is your purpose?",
        "What is something you wish people understood about you?",
        "What is your biggest strength?",
        "What is your biggest weakness?",
        "What do you want to achieve before you die?",
        "What does friendship mean to you?",
        "When do you feel most confident?",
        "What do you want your future self to thank you for?",
        "What matters more money or happiness?",
        "What does love mean to you?",
        "What do you fear losing most?",
        "What is something you want to change about yourself?",
        "What motivates you to keep going?",
        "What makes life meaningful?",
        "What is one truth you strongly believe?"
    ],

    "⚡ Rapid Fire": [
        "Tea or Coffee?",
        "Night or Morning?",
        "City or Village?",
        "Books or Movies?",
        "Money or Love?",
        "Pizza or Burger?",
        "Beach or Mountains?",
        "Introvert or Extrovert?",
        "Sweet or Spicy?",
        "Phone or Laptop?",
        "Cats or Dogs?",
        "Summer or Winter?",
        "Call or Text?",
        "Netflix or YouTube?",
        "Music or Silence?",
        "Online or Offline shopping?",
        "Chocolate or Ice cream?",
        "Early bird or Night owl?",
        "Action or Comedy?",
        "Rain or Sunshine?",
        "Travel or Stay home?",
        "Instagram or WhatsApp?",
        "Road trip or Flight?",
        "Cake or Donut?",
        "Work or Sleep?",
        "Shoes or Slippers?",
        "Hot or Cold weather?",
        "Friends or Family time?",
        "Shopping or Saving?",
        "Reality or Fantasy?"
    ],

    "😳 Embarrassing": [
        "Who was your first crush?",
        "Have you ever lied to your best friend?",
        "What is your biggest secret?",
        "Have you ever stalked someone online?",
        "What is your most awkward moment?",
        "What is something childish you still do?",
        "What is your guilty pleasure?",
        "Have you ever pretended to like a gift?",
        "What is your weirdest habit nobody knows?",
        "What is the last lie you told?",
        "Have you ever laughed at the wrong moment?",
        "What is your biggest insecurity?",
        "What is your worst fashion mistake?",
        "Have you ever sent a message to the wrong person?",
        "What is something you are afraid people will judge you for?",
        "What is your most embarrassing school memory?",
        "Have you ever cried over something silly?",
        "What is your weirdest fear?",
        "Have you ever pretended to know something you didn’t?",
        "What is your most awkward conversation?",
        "What is your worst haircut story?",
        "Have you ever tripped in public?",
        "What is your funniest fail?",
        "Have you ever snooped someone’s phone?",
        "What is your most embarrassing habit?",
        "Have you ever waved back at someone who wasn’t waving at you?",
        "What is your cringiest memory?",
        "Have you ever laughed during a serious moment?",
        "What is your most awkward silence moment?",
        "What is something you’d never admit normally?"
    ]
}

# ---------------- UI ---------------- #

st.title("🎉 Spin & Spill 🤭 ")

st.write("Select a category and click the button to get a random question!")

category = st.selectbox("Choose Category", list(questions.keys()))

if st.button("Get Question 🎲"):
    st.success(random.choice(questions[category]))
