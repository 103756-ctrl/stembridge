import streamlit as st

# Page configuration for a mobile-friendly layout
st.set_page_config(
    page_title="STEMBridge - AI Learning Companion",
    page_icon="📚",
    layout="centered"
)

# App Header
st.title("🌟 STEMBridge")
st.subheader("Your Local-Language AI Learning Companion")
st.write("Ask a question about STEM, IT, or computer science in your preferred language!")

# Sidebar Configuration for Inclusivity & Localization
st.sidebar.header("⚙️ Learning Settings")
language = st.sidebar.selectbox(
    "Choose Language",
    ["English", "Bahasa Melayu", "Mandarin", "Tamil"]
)

learning_level = st.sidebar.selectbox(
    "Select Education Level",
    ["Primary School", "Secondary School", "Foundation / Undergraduate"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** STEMBridge connects concepts to everyday local situations to make learning easier!")

# Chat state management
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
prompt = st.chat_input("Ask a question (e.g., What is a loop in programming?)")

if prompt:
    # Add user message to state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a helpful, localized response based on selections
    with st.chat_message("assistant"):
        with st.spinner("Thinking through local examples..."):
            
            # Simple response simulation tailored to settings
            response = (
                f"*(Responding in {language} for {learning_level})*\n\n"
                f"Great question about **'{prompt}'**! Let's break it down using a simple local example:\n\n"
                f"Imagine you are organizing a pasar malam (night market) stall. "
                f"When you want to repeat a task—like handing out plastic bags to every customer who buys food—you don't write a new instruction for each person. Instead, you use a **loop** to repeat the action until all customers are served.\n\n"
                f"**Key Takeaway:** A loop automates repetitive tasks so you save time and energy!"
            )
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})