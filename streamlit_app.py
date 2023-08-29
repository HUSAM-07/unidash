import streamlit as st



def main():

    st.title("University Dashboard")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Go to", ("Home","University Resources", "Clubs Resources"))

    if section == "Home":
        show_homepage()
    elif section == "University Resources":
        show_university_resources()
    elif section == "Clubs Resources":
        show_clubs_resources()

    st.divider()
    st.caption("Designed & Developed by HUSAM")
    st.write("This Web App Is Made to Help You Access All The Important BITS Pilani, Dubai Admin & Academic Websites at a Single Website")
    st.caption("The app is designed using Streamlit")


def show_homepage():
    st.header("Welcome to the University Clubs Dashboard!")
    st.write("Use the sidebar to navigate to different sections.")
    


def show_clubs_resources():
    st.header("Clubs Resources")
    st.markdown("---")

    st.subheader("GDSC Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://gdscbpdc.github.io/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("ACM Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://openlib-cs.acmbpdc.org/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Ahmed Thahir's Notes")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://uni-notes.netlify.app/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)


def show_university_resources():
    st.header("University Resources")
    st.markdown("---")

    st.subheader("Library Resources")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="http://webopac.bits-dubai.ac.ae/AutoLib/index.jsp" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Courses & LMS")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://lms.bitspilanidubai.ae/login/index.php" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("BITS ERP")
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px;">'
                '<iframe src="https://erp.bits-pilani.ac.in/" width="1000" height="400"></iframe>'
                '</div>', unsafe_allow_html=True)


if __name__ == '__main__':
    main()
