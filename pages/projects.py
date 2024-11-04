import streamlit as st

st.set_page_config(
    page_title="Suzal Kachhadiya - Projects", 
    page_icon="💡",
    layout="wide"
)

popover = st.popover("Filter Domains")
genAI=popover.checkbox("Show Generative AI Projects", True)
machine_learning = popover.checkbox("Show Machine Learning Projects", True)
computer_vision = popover.checkbox("Show Computer Vision Projects", True)
nlp = popover.checkbox("Show Natural Language Processing Projects", True)
powerbi = popover.checkbox("Show PowerBI Projects", True)

if genAI:
    st.header("• :blue[Generative AI] Projects",divider="rainbow")
    tab1, tab2 = st.tabs(["Chat With Search","AI Finance Adviser"])

    with tab1:
        st.title("Chat With Search")
        st.markdown("""
        <div style='display: flex; justify-content: left; align-items: center;'>
            <a href="https://github.com/suzalkachhadiya/Chat-With-Search" target="_blank" style="margin-right: 10px;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
            </a>

        </div>
        """, unsafe_allow_html=True)
        st.write("""This is a Streamlit-based conversational AI application that combines multiple LangChain agents and tools for enhanced information retrieval.
            The app allows users to interact with different types of agents (Zero-Shot, Conversational, and Structured) while leveraging various search tools including PDF document search, 
            Arxiv papers, Wikipedia, and DuckDuckGo.It features a customizable interface where users can select their preferred combination of tools and agent types, 
            and uses the Groq API with the Llama3-8b model for processing queries. The system maintains conversation history and provides streaming responses with visual feedback through the Streamlit interface. """)    
        
        col1, col2, col3=st.columns([1,1.5,1])
        with col2:
            st.video("https://www.youtube.com/watch?v=K8re0A4HAcU")
            
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/Chat_With_Search/1.png")
            st.image("assets/Chat_With_Search/2.png")
        with col2:
            st.image("assets/Chat_With_Search/3.png")
            st.image("assets/Chat_With_Search/4.png")
    
    with tab2:
        st.title("AI Finance Adviser")
        st.subheader("working on it.")


if machine_learning:
    st.header("• :blue[Machine Learning] Projects",divider="rainbow")
    tab1, tab2 = st.tabs(["AIDRP", "Phishing Classifier"])

    with tab1:
        st.title("AIDRP")
        st.markdown("""
        <div style='display: flex; justify-content: left; align-items: center;'>
            <a href="https://github.com/Krish-Goyani/AIDRP-AI_Driven_Diabetes_Readmission_Prevention/tree/main" target="_blank" style="margin-right: 10px;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
            </a>

        </div>
        """, unsafe_allow_html=True)
        st.write("""AIDRP is an AI-driven platform that can accurately predict and reduce 30-day hospital readmission rates for 
            diabetes mellitus (DM) patients. The platform is boosted by Gemini API, an AI assistant that answers users' 
            questions regarding healthcare. By enhancing prediction and prevention of avoidable readmissions, AIDRP 
            can assist hospitals in improving quality of care, reducing costs, and optimizing performance measures. """)
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/AIDRP/5 (2).png")
            st.image("assets/AIDRP/8 (1).png")
            st.video("https://www.youtube.com/watch?v=apUY99YulMo")
        with col2:
            st.image("assets/AIDRP/6 (2).png")
            st.image("assets/AIDRP/9.png")
            st.video("https://www.youtube.com/watch?v=3JcbM14BUAQ")

    with tab2:
        st.title("Phishing Classifier")
        st.markdown("""
        <div style='display: flex; justify-content: left; align-items: center;'>
            <a href="https://github.com/suzalkachhadiya/Phishing-Classifer" target="_blank" style="margin-right: 10px;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
            </a>

        </div>
        """, unsafe_allow_html=True)
        st.write("""Our machine learning model looks closely at web addresses. It checks many parts of the address, like how it's spelled and what it contains.
            The model compares these details to patterns found in known fake websites. Based on this check, it decides if the address is likely safe or might be dangerous. This helps you know which websites to trust before you click on them. """)
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/phishing/1.png")
            st.image("assets/phishing/2.png")
        with col2:
            st.image("assets/phishing/3.png")
            st.image("assets/phishing/4.png")


if computer_vision:
    st.header("• :blue[Computer Vision] Projects",divider="rainbow")
    tab1, tab2, tab3 = st.tabs(["Virtual Calculator","Pneumonia Detection","Quiz game using Computer Vision"])
    with tab2:
        st.title("Pneumonia Detection")
        st.markdown("""
            <div style='display: flex; justify-content: left; align-items: center;'>
                <a href="https://github.com/suzalkachhadiya/Pneumonia-Classifiaction" target="_blank" style="margin-right: 10px;">
                    <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
                </a>

            </div>
            """, unsafe_allow_html=True)
        st.write("""This tool utilizes a Convolutional Neural Network (CNN), a powerful type of AI model, to analyze chest X-ray images and identify patterns that may indicate pneumonia.
                 Leveraging cutting-edge AI, this tool analyzes chest X-rays with high accuracy, assisting healthcare professionals in pneumonia detection. Upload your X-ray to get started. """)
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/Pnemonia/1.png")
            st.image("assets/Pnemonia/2.png")
        with col2:
            st.image("assets/Pnemonia/3.png")
    with tab1:
        st.title("Virtual Calculator")
        st.markdown("""
            <div style='display: flex; justify-content: left; align-items: center;'>
                <a href="https://github.com/suzalkachhadiya/Virtual-Calculator" target="_blank" style="margin-right: 10px;">
                    <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
                </a>

            </div>
            """, unsafe_allow_html=True)
        st.write("""a virtual calculator that you can use with just your hands! ✋️ No need for a physical calculator or even keyboard.""")
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/Calculator/1.jpg")
        with col2:
            st.image("assets/Calculator/2.jpg")
    with tab3:
        st.title("Quiz game using Computer Vision")
        st.markdown("""
            <div style='display: flex; justify-content: left; align-items: center;'>
                <a href="https://github.com/suzalkachhadiya/Virtual-Quiz" target="_blank" style="margin-right: 10px;">
                    <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
                </a>

            </div>
            """, unsafe_allow_html=True)
        st.write("""a virtual quiz that you can give with just your hands! ✋️ No need for a physical divices.""")
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/Quiz/1.png")
            st.image("assets/Quiz/2.png")
        with col2:
            st.image("assets/Quiz/3.png")
            st.image("assets/Quiz/4.png")
if nlp:
    st.header("• :blue[Natural Language Processing] Projects",divider="rainbow")
    st.title("Next Word Predictor")
    st.markdown("""
        <div style='display: flex; justify-content: left; align-items: center;'>
            <a href="https://github.com/suzalkachhadiya/Next-Word-Predictor" target="_blank" style="margin-right: 10px;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" width="32" height="32" style="filter: invert(1)">
            </a>

        </div>
        """, unsafe_allow_html=True)
    st.write("""Our next word predictor operates by learning from your text input. Start by uploading a file containing sample text that reflects your writing style or the type of content you typically work with.
            The model analyzes this text to understand patterns, word associations, and common phrases. As you type, the predictor draws upon this learned knowledge to suggest the most probable next words based on the context of what you've already written.
            This dynamic process adapts to your unique writing style, offering increasingly accurate predictions over time and enhancing your typing efficiency. """)
    col1, col2=st.columns(2)
    with col1:
        st.image("assets/NWP/1.png")
        st.image("assets/NWP/2.png")
    with col2:
        st.image("assets/NWP/3.png")

if powerbi:
    st.header("• :blue[PowerBI] Projects",divider="rainbow")
    tab1, tab2 = st.tabs(["Hardware Company Data", "US Stocks Data"])
    with tab1:
        st.title("Hardware Company sales data - Dashboard")
        st.write("""Dashborad of sales and stats of a hardware company. From which company can improve and build new stretegies to compete in high competitive market. """)
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/PowerBI/HomePage.png")
            st.image("assets/PowerBI/FinanceView.png")
            st.image("assets/PowerBI/SalesView.png")
        with col2:
            st.image("assets/PowerBI/MarketingView.png")
            st.image("assets/PowerBI/SupplyChainView.png")
            st.image("assets/PowerBI/ExecutiveView.png")

    with tab2:
        st.title("US Stocks Data - Dashboard")
        col1, col2=st.columns(2)
        with col1:
            st.image("assets/PowerBI/EmployeeView.png")
        with col2:
            st.image("assets/PowerBI/FinancialMetricsView.png")

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