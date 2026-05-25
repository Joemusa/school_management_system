import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Learner Management",
    page_icon="👨‍🎓",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.title("👨‍🎓 Learner Management")
st.caption("Manage learner records, admissions and profiles.")

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Learners",
        "1,248",
        "+12"
    )

with col2:
    st.metric(
        "New Admissions",
        "24",
        "+5"
    )

with col3:
    st.metric(
        "Male Learners",
        "612"
    )

with col4:
    st.metric(
        "Female Learners",
        "636"
    )

st.divider()

# ==================================================
# SEARCH & FILTERS
# ==================================================

col1, col2 = st.columns([2,1])

with col1:
    search = st.text_input(
        "🔍 Search Learner",
        placeholder="Enter learner name..."
    )

with col2:
    grade_filter = st.selectbox(
        "Filter by Grade",
        [
            "All Grades",
            "Grade 8",
            "Grade 9",
            "Grade 10",
            "Grade 11",
            "Grade 12"
        ]
    )

# ==================================================
# LEARNER TABLE
# ==================================================

left, right = st.columns([2.5,1])

with left:

    st.subheader("Learner Records")

    learner_df = pd.DataFrame({
        "Admission No": [
            "L001",
            "L002",
            "L003",
            "L004",
            "L005"
        ],
        "Learner Name": [
            "Sipho Dlamini",
            "Ayanda Mkhize",
            "Thando Nkosi",
            "Lethabo Molefe",
            "Naledi Mokoena"
        ],
        "Grade": [
            "Grade 8",
            "Grade 9",
            "Grade 10",
            "Grade 11",
            "Grade 12"
        ],
        "Parent Contact": [
            "0821111111",
            "0822222222",
            "0823333333",
            "0824444444",
            "0825555555"
        ]
    })

    st.dataframe(
        learner_df,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("Recent Admissions")

    st.success("Naledi Mokoena")
    st.success("Sipho Dlamini")
    st.success("Thando Nkosi")

    st.subheader("Quick Actions")

    st.button(
        "➕ Add Learner",
        key="add_learner"
    )

    st.button(
        "📄 View Profile",
        key="view_profile"
    )

    st.button(
        "📥 Export Learners",
        key="export_learners"
    )

st.divider()

# ==================================================
# CHARTS
# ==================================================

left, right = st.columns(2)

with left:

    st.subheader("Learners by Grade")

    grade_df = pd.DataFrame({
        "Grade": [
            "Grade 8",
            "Grade 9",
            "Grade 10",
            "Grade 11",
            "Grade 12"
        ],
        "Learners": [
            250,
            240,
            255,
            248,
            255
        ]
    })

    fig1 = px.bar(
        grade_df,
        x="Grade",
        y="Learners"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    st.subheader("Gender Distribution")

    gender_df = pd.DataFrame({
        "Gender": [
            "Male",
            "Female"
        ],
        "Count": [
            612,
            636
        ]
    })

    fig2 = px.pie(
        gender_df,
        names="Gender",
        values="Count"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

st.info(
    "Learner Management Module - Rentabuka School Management System"
)
