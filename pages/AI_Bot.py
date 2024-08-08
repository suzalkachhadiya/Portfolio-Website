import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Bot", 
    page_icon="🤖",
    layout="wide"
)
api_key=st.secrets["API_KEY"]
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-1.5-flash")


persona="""
        You are Suzal AI bot. You help people answer about yourself (i.e Suzal)
        Answer as if you are responding. don't answer in second or third person. don't answer like maths' question as well as of beyond your role as a 'Suzal'
        If you don't know the answer you simply say "For That contact me personally" or say "That's a secret" if question seems you confidential
        Here is more info about Suzal
        Suzal Kachhadiya is a final year college student of bechlor in computer engineering in college GEC Bhavnagar. He's passionate about data science.
        his skills are  • Programming Languages: Python 
                        • Mathematics: Probability, Statistics 
                        • Data Analysis and Visualization: PowerBI, Pandas, NumPy, Matplotlib, Seaborn, Plotly 
                        • Machine Learning Libraries: Scikit-learn, CatBoost 
                        • Deep Learning Frameworks: PyTorch, TensorFlow 
                        • Architectures: ANN, CNN, RNN, LSTM 
                        • Computer Vision: Image Processing, Object Detection, OpenCV 
                        • Database Management: SQL , MongoDB 
                        • Other Tools: Jupyter Notebook, Git, Kaggle 
        he has worked on lots of projects like  • AIDRP - AI Driven Diabetes Readmission Prevention (2024 GDSC Solution Challenge global top 100 finalist.)
                                                • Phishing Classifier 
                                                • Next Word Predictor
                                                • Predictive Maintenance
                                                • Diamond Price Prediction
        Suzal's LinkedIn: https://www.linkedin.com/in/suzal-kachhadiya-149498237/
        Suzal's GitHub: https://github.com/suzalkachhadiya
        Suzal's Twitter: https://x.com/SuzalKachhadiya
"""

st.header(":blue[Suzal's] AI Bot",divider="rainbow")
st.markdown("##### Ask anything about myself")

def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role

if "chat" not in st.session_state:
    st.session_state.chat= model.start_chat(history = [])

if "const" not in st.session_state:
   st.session_state.const="firstrun"

if st.session_state.const == "firstrun":
   st.session_state.const="rerunned"
   st.session_state.chat.send_message(persona)

# Display chat messages from history above current input box
for message in st.session_state.chat.history[2:]:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)


# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("What would you like to know about myself?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display last 
    with st.chat_message("assistant"):
        st.markdown(response.text)

with st.sidebar:
        st.markdown("""
        <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff; width: fit-content;">
        📞 +91 8488855887
        </div>
        """, unsafe_allow_html=True)
        st.write("\n")

        st.subheader("Connect with me")

        st.markdown("""
        <div style='display: flex; justify-content: left; align-items: center;'>
            <a href="https://www.linkedin.com/in/suzal-kachhadiya-149498237/" target="_blank" style="margin-right: 10px;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="LinkedIn" width="32" height="32" style="filter: invert(1)">
            </a>
            <a href="https://x.com/SuzalKachhadiya" target="_blank" style="margin-right: 10px;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/twitter.svg" alt="Twitter" width="32" height="32" style="filter: invert(1)">
            </a>
            <a href="https://github.com/suzalkachhadiya" target="_blank" style="margin-right: 10px;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
            </a>
            <a href="mailto:suzalkachhadiya111@gmail.com" target="_blank" style="margin-right: 10px;">
            <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg" alt="Email" width="32" height="32" style="filter: invert(1)">
            </a>
        </div>
        """, unsafe_allow_html=True)

# import streamlit as st

# try:
#     api_key = st.secrets["API_KEY"]
#     st.write(f"API Key: {api_key}")
# except KeyError:
#     st.error("API_KEY not found in secrets.")
