import streamlit as st
import base64
from pdf2image import convert_from_path


st.set_page_config(
    page_title="Suzal Kachhadiya - resume", 
    page_icon="🎓",
    layout="wide"
)

def show_resume_page():
    # Video Resume Section

    col1, col2, col3=st.columns([3,1,1])
    with col1:
        st.header(":blue[Video] Resume",divider="rainbow")
        youtube_link = "https://youtu.be/srD87TODBSE?feature=shared"
        st.video(youtube_link)

    st.write("\n")


    with col2:
    # PDF Resume Section
            st.header(":blue[Doc] Resume",divider="rainbow")
    # col1, col2, col3=st.columns([1,7,1])
    # with col2:
    #     with open("assets/resume/Resume_DS.pdf", "rb") as pdf_file:
    #         base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        
    #     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}"  width="1000" height="1000"type="application/pdf"></iframe>'
    #     st.markdown(pdf_display, unsafe_allow_html=True)

    # col1, col2, col3 = st.columns([1,7,1])
    # with col2:
    #     images = convert_from_path("Resume_DS.pdf")
    #     for image in images:
    #         st.image(image)
    
        
            with open("assets\resume\Suzal_Kachhadiya_genai.pdf", "rb") as pdf_file:
                    st.download_button(
                        label="📄 Download Resume PDF",
                        data=pdf_file,
                        file_name="Suzal_Kachhadiya.pdf",
                        mime="application/pdf",
                        key="download-resume-pdf"
                    )
    
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

if __name__ == "__main__":
    show_resume_page()