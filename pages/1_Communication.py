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
