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
# SIDEBAR
# --------------------------------------------------
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
    width=80
)

st.sidebar.title("Rentabuka")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Communication",
        "Attendance",
        "Learners",
        "Documents",
        "Reports",
        "Events",
        "Users",
        "Settings"
    ]
)

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
#----------------------------------------------------
# PARENT COMMUNICATION DASHBOARD
#----------------------------------------------------
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Parent Communication",
    page_icon="📢",
    layout="wide"
)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.title("📢 Parent Communication")
st.caption(
    "Communicate with parents, send announcements and manage messages."
)

# ----------------------------------------------------
# KPI CARDS
# ----------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Messages Sent",
        "256",
        "+18%"
    )

with col2:
    st.metric(
        "Parents Reached",
        "1,142",
        "+89%"
    )

with col3:
    st.metric(
        "Unread Replies",
        "24",
        "-12%"
    )

with col4:
    st.metric(
        "Announcements",
        "12",
        "+3"
    )

st.divider()

# ----------------------------------------------------
# MESSAGE COMPOSER
# ----------------------------------------------------

left, right = st.columns([1.2, 1.4])

with left:

    st.subheader("✉️ Send Announcement / Message")

    msg_type = st.radio(
        "Message Type",
        [
            "Announcement",
            "Message to Grade",
            "Message to Parent"
        ],
        horizontal=True
    )

    title = st.text_input(
        "Title",
        placeholder="Enter announcement title"
    )

    message = st.text_area(
        "Message",
        height=150,
        placeholder="Type your message here..."
    )

    audience = st.selectbox(
        "Audience",
        [
            "All Parents",
            "Grade 8 Parents",
            "Grade 9 Parents",
            "Grade 10 Parents",
            "Grade 11 Parents",
            "Grade 12 Parents"
        ]
    )

    st.write("Send Via")

    c1, c2, c3 = st.columns(3)

    with c1:
        inapp = st.checkbox("In-App", value=True)

    with c2:
        sms = st.checkbox("SMS")

    with c3:
        email = st.checkbox("Email")

    if st.button(
        "📨 Send Announcement",
        key="send_announcement"
    ):
        st.success("Message sent successfully!")

# ----------------------------------------------------
# RECENT COMMUNICATIONS
# ----------------------------------------------------

with right:

    st.subheader("📬 Recent Communications")

    communications = pd.DataFrame({
        "Title":[
            "School closes at 13:00 today",
            "Term 2 Parent Meeting",
            "Sports Day",
            "Grade 10 Timetable",
            "Uniform Update"
        ],
        "Audience":[
            "All Parents",
            "Grade 8-12",
            "All Parents",
            "Grade 10",
            "All Parents"
        ],
        "Status":[
            "Sent",
            "Sent",
            "Sent",
            "Sent",
            "Sent"
        ]
    })

    st.dataframe(
        communications,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ----------------------------------------------------
# COMMUNICATION TREND
# ----------------------------------------------------

left, right = st.columns([1.3, 1])

with left:

    st.subheader("📈 Communication Overview")

    chart_data = pd.DataFrame({
        "Date":[
            "May 1",
            "May 6",
            "May 11",
            "May 16",
            "May 21",
            "May 26",
            "May 31"
        ],
        "Messages":[
            40,
            60,
            35,
            70,
            50,
            80,
            60
        ]
    })

    fig = px.line(
        chart_data,
        x="Date",
        y="Messages",
        markers=True
    )

    fig.update_layout(height=350)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------
# MESSAGE TEMPLATES
# ----------------------------------------------------

with right:

    st.subheader("📄 Message Templates")

    templates = [
        "Parent Meeting Invitation",
        "Event Announcement",
        "Exam Timetable Notice",
        "General Notice"
    ]

    for template in templates:

        c1, c2 = st.columns([4,1])

        with c1:
            st.write(template)

        with c2:
            st.button(
                "Use",
                key=template
            )

st.divider()

# ----------------------------------------------------
# QUICK ACTIONS
# ----------------------------------------------------

st.subheader("⚡ Quick Actions")

q1, q2, q3, q4 = st.columns(4)

with q1:
    st.button(
        "📢 New Announcement",
        key="new_announcement"
    )

with q2:
    st.button(
        "📱 Send SMS",
        key="send_sms"
    )

with q3:
    st.button(
        "📧 Send Email",
        key="send_email"
    )

with q4:
    st.button(
        "📊 Communication Report",
        key="communication_report"
    )
