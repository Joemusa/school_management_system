import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="School Events",
    page_icon="📅",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.title("📅 School Events & Calendar")
st.caption(
    "Manage school events, meetings, examinations and activities."
)

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Upcoming Events",
        "12"
    )

with col2:
    st.metric(
        "Parent Meetings",
        "3"
    )

with col3:
    st.metric(
        "Examinations",
        "5"
    )

with col4:
    st.metric(
        "Sports Events",
        "4"
    )

st.divider()

# ==================================================
# CREATE EVENT
# ==================================================

left, right = st.columns([2, 1])

with left:

    st.subheader("➕ Create New Event")

    event_name = st.text_input(
        "Event Name"
    )

    event_type = st.selectbox(
        "Event Type",
        [
            "Parent Meeting",
            "Examination",
            "Sports Event",
            "School Function",
            "Staff Meeting",
            "Other"
        ]
    )

    event_date = st.date_input(
        "Event Date",
        value=date.today()
    )

    description = st.text_area(
        "Description"
    )

    if st.button(
        "💾 Save Event",
        key="save_event"
    ):
        st.success(
            "Event saved successfully."
        )

# ==================================================
# UPCOMING EVENTS
# ==================================================

with right:

    st.subheader("Upcoming Events")

    st.info("📅 Parent Meeting - 05 June")
    st.info("⚽ Sports Day - 10 June")
    st.info("📝 Mid-Year Exams - 15 June")
    st.info("👨‍🏫 Staff Meeting - 20 June")

st.divider()

# ==================================================
# EVENTS TABLE
# ==================================================

st.subheader("School Events")

events_df = pd.DataFrame({
    "Event":[
        "Parent Meeting",
        "Sports Day",
        "Mid-Year Exams",
        "Staff Meeting",
        "Prize Giving"
    ],
    "Type":[
        "Parent Meeting",
        "Sports Event",
        "Examination",
        "Staff Meeting",
        "School Function"
    ],
    "Date":[
        "2026-06-05",
        "2026-06-10",
        "2026-06-15",
        "2026-06-20",
        "2026-07-01"
    ],
    "Status":[
        "Scheduled",
        "Scheduled",
        "Scheduled",
        "Scheduled",
        "Planned"
    ]
})

st.dataframe(
    events_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==================================================
# EVENTS BY TYPE
# ==================================================

left, right = st.columns(2)

with left:

    st.subheader("Events by Type")

    chart_df = pd.DataFrame({
        "Type":[
            "Parent Meeting",
            "Examination",
            "Sports Event",
            "School Function",
            "Staff Meeting"
        ],
        "Count":[
            3,
            5,
            4,
            2,
            3
        ]
    })

    fig1 = px.bar(
        chart_df,
        x="Type",
        y="Count",
        text="Count"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    st.subheader("Monthly Events")

    monthly_df = pd.DataFrame({
        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],
        "Events":[
            3,
            4,
            5,
            2,
            6,
            7
        ]
    })

    fig2 = px.line(
        monthly_df,
        x="Month",
        y="Events",
        markers=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# ==================================================
# CALENDAR VIEW
# ==================================================

st.subheader("📆 Event Calendar")

calendar_df = pd.DataFrame({
    "Date":[
        "05 Jun",
        "10 Jun",
        "15 Jun",
        "20 Jun",
        "01 Jul"
    ],
    "Event":[
        "Parent Meeting",
        "Sports Day",
        "Mid-Year Exams",
        "Staff Meeting",
        "Prize Giving"
    ]
})

st.table(calendar_df)

st.divider()

# ==================================================
# QUICK ACTIONS
# ==================================================

st.subheader("⚡ Quick Actions")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button(
        "➕ Add Event",
        key="add_event"
    )

with c2:
    st.button(
        "📢 Notify Parents",
        key="notify_event"
    )

with c3:
    st.button(
        "📄 Event Report",
        key="event_report"
    )

with c4:
    st.button(
        "📥 Export Calendar",
        key="export_calendar"
    )

st.divider()

st.info(
    "School Events & Calendar Module - Rentabuka School Management System"
)
