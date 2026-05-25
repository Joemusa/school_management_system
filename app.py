import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Rentabuka School Management System",
    page_icon="🏫",
    layout="wide"
)
# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.image("Logo.png", width=180)

st.sidebar.markdown("### Rentabuka School Management System")
# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.kpi-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    text-align:center;
}

.kpi-number {
    font-size: 32px;
    font-weight: bold;
}

.section-card {
    background-color:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)




# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🏫 School Dashboard")
st.caption("Centralized School Administration Platform")

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Learners",
        "1,248",
        "+12"
    )

with col2:
    st.metric(
        "Present Today",
        "1,132",
        "+2%"
    )

with col3:
    st.metric(
        "Absent Today",
        "116",
        "-1%"
    )

with col4:
    st.metric(
        "Unread Messages",
        "18",
        "+4"
    )

st.divider()

# --------------------------------------------------
# ATTENDANCE CHART
# --------------------------------------------------
left, middle, right = st.columns([2,1.3,1.3])

with left:

    st.subheader("Attendance Overview")

    attendance = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri"],
        "Attendance":[92,89,91,88,91]
    })

    fig = px.line(
        attendance,
        x="Day",
        y="Attendance",
        markers=True
    )

    fig.update_layout(height=350)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# ANNOUNCEMENTS
# --------------------------------------------------
with middle:

    st.subheader("Recent Announcements")

    st.success("School closes at 13:00 today")
    st.info("Term 2 Parent Meeting")
    st.warning("Sports Day - Save the Date")
    st.error("Grade 10 Exam Timetable")

    st.button("➕ New Announcement")

# --------------------------------------------------
# EVENTS
# --------------------------------------------------
with right:

    st.subheader("Upcoming Events")

    st.markdown("""
    **30 May**  
    Parent Meeting

    **07 Jun**  
    Sports Day

    **16 Jun**  
    Youth Day
    """)

    st.button("📅 Add Event")

st.divider()

# --------------------------------------------------
# ATTENDANCE BY GRADE
# --------------------------------------------------
left, right = st.columns([2,1])

with left:

    st.subheader("Attendance by Grade")

    grade_data = pd.DataFrame({
        "Grade":["8","9","10","11","12"],
        "Attendance":[92,89,91,88,90]
    })

    fig2 = px.bar(
        grade_data,
        x="Grade",
        y="Attendance"
    )

    fig2.update_layout(height=350)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

with right:

    st.subheader("Quick Actions")

    st.button("✅ Mark Attendance")
    st.button("📢 Send Announcement")
    st.button("👨‍🎓 Add Learner")
    st.button("📄 Upload Document")
    st.button("📊 View Reports")
    #st.button("📅 Add Event")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.info(
    "Overall Attendance: 90.7%"
)
