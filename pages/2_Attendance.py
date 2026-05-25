import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Attendance Management",
    page_icon="✅",
    layout="wide"
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("✅ Attendance Management")
st.caption("Monitor attendance, absenteeism and learner participation.")

# =====================================================
# KPI CARDS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Learners",
        value="1,248"
    )

with col2:
    st.metric(
        label="Present Today",
        value="1,132"
    )

with col3:
    st.metric(
        label="Absent Today",
        value="116"
    )

with col4:
    st.metric(
        label="Attendance %",
        value="90.7%"
    )

st.divider()

# =====================================================
# FILTERS
# =====================================================

col1, col2 = st.columns(2)

with col1:
    selected_date = st.date_input(
        "Attendance Date"
    )

with col2:
    selected_grade = st.selectbox(
        "Select Grade",
        [
            "All Grades",
            "Grade 8",
            "Grade 9",
            "Grade 10",
            "Grade 11",
            "Grade 12"
        ]
    )

st.divider()

# =====================================================
# ATTENDANCE REGISTER
# =====================================================

st.subheader("📋 Attendance Register")

attendance_data = pd.DataFrame({
    "Learner": [
        "Sipho Dlamini",
        "Ayanda Mkhize",
        "Thando Nkosi",
        "Lethabo Molefe",
        "Naledi Mokoena"
    ],
    "Grade": [
        "Grade 8",
        "Grade 8",
        "Grade 9",
        "Grade 10",
        "Grade 11"
    ],
    "Present": [
        True,
        True,
        False,
        True,
        False
    ]
})

edited_df = st.data_editor(
    attendance_data,
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "💾 Save Attendance",
        key="save_attendance"
    ):
        st.success("Attendance saved successfully.")

with col2:
    if st.button(
        "✔ Mark All Present",
        key="mark_all_present"
    ):
        st.success("All learners marked present.")

st.divider()

# =====================================================
# ATTENDANCE TREND
# =====================================================

left, right = st.columns([2, 1])

with left:

    st.subheader("📈 Attendance Trend")

    trend_df = pd.DataFrame({
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri"
        ],
        "Attendance": [
            92,
            89,
            91,
            88,
            90
        ]
    })

    fig = px.line(
        trend_df,
        x="Day",
        y="Attendance",
        markers=True
    )

    fig.update_layout(height=350)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader("🚨 Absent Learners")

    absent_df = pd.DataFrame({
        "Learner": [
            "Thando Knosi",
            "Naledi Mokoena"
        ],
        "Grade": [
            "Grade 9",
            "Grade 11"
        ]
    })

    st.dataframe(
        absent_df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# =====================================================
# ATTENDANCE BY GRADE
# =====================================================

st.subheader("🏫 Attendance by Grade")

grade_df = pd.DataFrame({
    "Grade": [
        "Grade 8",
        "Grade 9",
        "Grade 10",
        "Grade 11",
        "Grade 12"
    ],
    "Attendance %": [
        92,
        89,
        91,
        88,
        90
    ]
})

fig2 = px.bar(
    grade_df,
    x="Grade",
    y="Attendance %",
    text="Attendance %"
)

fig2.update_layout(height=350)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# =====================================================
# QUICK ACTIONS
# =====================================================

st.subheader("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    st.button(
        "📨 Notify Absent Parents",
        key="notify_parents"
    )

with col2:
    st.button(
        "📊 Generate Report",
        key="generate_report"
    )

with col3:
    st.button(
        "📥 Export Attendance",
        key="export_attendance"
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.info(
    "Attendance Management Module - Rentabuka School Management System"
)
