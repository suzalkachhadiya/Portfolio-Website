import streamlit as st
import google.generativeai as genai

from constants import API_KEY

st.set_page_config(
    page_title="Intrduction", 
    page_icon="🎓",
    layout="wide"
)

col1,col2=st.columns([2,1])

with col1:
    st.subheader("hi :wave:")
    st.title("I am :blue[Suzal Kachhadiya]")
    st.write("""
        • passionate about data science who loves finding useful information in big sets of data.\n
        • I enjoy turning raw numbers into helpful insights that can guide business choices.\n
        • I'm good at machine learning, working with statistics, and making data easy to understand with pictures.\n
        • I'm always learning about new tools and methods to get better at working with data.\n
        • My aim is to use data to make a real difference and help create new solutions in the always-changing world of data science.
        """)
with col2:
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.image("assets/Profile.jpeg",width=300)



genai.configure(api_key=API_KEY)
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
"""

st.header("Suzal's AI Bot",divider="rainbow")
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