import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Suzal Kachhadiya - Portfolio", 
    page_icon="🎓",
    layout="wide"
)

col1,col2=st.columns([2,1])


def typed_name_effect():
    # HTML with embedded JavaScript for the typing effect
    typing_effect = """
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.12/typed.min.js"></script>
        <style>
            .typed-cursor {
                font-size: 2.5rem;
                font-type: sans-serif 
                color: #3498db;
            }
            h1 {
                color: white;  /* Set the color of "I am" to white */
                font-type: sans-serif
            }
        </style>
    </head>
    <body>
        <h1>I am <span id="typed-name" style="color: #3498db;"></span></h1>

        <script>
            var typed = new Typed('#typed-name', {
                strings: ['Suzal Kachhadiya','Data Science Enthusiast'],
                typeSpeed: 75,
                backSpeed: 10,
                loop: true,
                showCursor: true,
                cursorChar: '|'
            });
        </script>
    </body>
    </html>
    """
    return typing_effect

# Rest of your Streamlit app
st.write("Welcome to my portfolio!")
with col1:
    st.subheader("hi :wave:",divider="rainbow")
    # Use the custom HTML component for the animated name
    html(typed_name_effect(), height=100)    
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
    st.write("\n")
    st.image("assets/Profile.jpeg",width=300)

st.write("\n")
st.write("\n")
st.header("Education",divider="rainbow")
col1,col2=st.columns([5,1])
with col1:
        st.write("Computer Engineering | Government Engineering College, Bhavnagar")
        st.write("(June ’21 - Mar ’24) (7th Semester). (Passing Year - 2025)")
with col2:
        st.write("CGPA : 7.96 ")

st.write("\n")
st.write("\n")
st.header("Technical Skills",divider="rainbow")
st.write("• :blue[**Programming Languages**] :  Python") 
st.write("• :blue[**Mathematics**] :  Probability, Statistics") 
st.write("• :blue[**Data Analysis and Visualization**] :  PowerBI, Pandas, NumPy, Matplotlib, Seaborn, Plotly") 
st.write("• :blue[**Machine Learning Libraries**] :  Scikit-learn, CatBoost ") 
st.write("• :blue[**Deep Learning Frameworks**] :  PyTorch, TensorFlow") 
st.write("• :blue[**Architectures**] :  ANN, CNN, RNN, LSTM, GRU, Encoder-Decoder, Transformer ") 
st.write("• :blue[**Generative AI**] :  Langchain, Llamaindex, RAG, Vector Databases") 
st.write("• :blue[**Computer Vision**] :  Image Processing, Object Detection, OpenCV ") 
st.write("• :blue[**Database Management**] :  MySQL, MongoDB") 
st.write("• :blue[**API**] :  FastAPI, Flask")
st.write("• :blue[**Other Tools**] :  Jupyter Notebook, Git, Kaggle") 

st.write("\n")
st.write("\n")
st.header("What describes me",divider="rainbow")
st.subheader("while :blue[True]:")
subheader_style1 = """
    <div style='font-size: 1.5em; font-weight: 600;'>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;learning_mode('<span style="color:green;">ON</span>')
    </div>
    """
st.markdown(subheader_style1, unsafe_allow_html=True)


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