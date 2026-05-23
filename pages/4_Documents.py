import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Document Management",
    page_icon="📄",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.title("📄 Document Management")
st.caption(
    "Store, manage and share school documents securely."
)

# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Documents",
        "486"
    )

with col2:
    st.metric(
        "Uploaded This Month",
        "34"
    )

with col3:
    st.metric(
        "Pending Approval",
        "5"
    )

with col4:
    st.metric(
        "Parent Downloads",
        "1,238"
    )

st.divider()

# ==================================================
# SEARCH & FILTERS
# ==================================================

col1, col2 = st.columns([2,1])

with col1:
    search_doc = st.text_input(
        "🔍 Search Document",
        placeholder="Search by document name..."
    )

with col2:
    category = st.selectbox(
        "Category",
        [
            "All Documents",
            "Circulars",
            "Policies",
            "Report Cards",
            "Permission Forms",
            "Meeting Minutes",
            "School Notices"
        ]
    )

# ==================================================
# DOCUMENT TABLE
# ==================================================

left, right = st.columns([2.5,1])

with left:

    st.subheader("School Documents")

    docs_df = pd.DataFrame({
        "Document Name":[
            "Term 2 Circular",
            "School Policy",
            "Sports Day Consent Form",
            "Grade 10 Report Cards",
            "Parent Meeting Minutes"
        ],
        "Category":[
            "Circulars",
            "Policies",
            "Permission Forms",
            "Report Cards",
            "Meeting Minutes"
        ],
        "Date Uploaded":[
            "2026-05-01",
            "2026-05-03",
            "2026-05-08",
            "2026-05-15",
            "2026-05-20"
        ],
        "Downloads":[
            320,
            145,
            275,
            410,
            88
        ]
    })

    st.dataframe(
        docs_df,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("Quick Actions")

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf","docx","xlsx"]
    )

    st.button(
        "📤 Share with Parents",
        key="share_document"
    )

    st.button(
        "📥 Download Selected",
        key="download_document"
    )

    st.button(
        "🗑 Delete Document",
        key="delete_document"
    )

st.divider()

# ==================================================
# CHARTS
# ==================================================

left, right = st.columns(2)

with left:

    st.subheader("Documents by Category")

    category_df = pd.DataFrame({
        "Category":[
            "Circulars",
            "Policies",
            "Report Cards",
            "Permission Forms",
            "Meeting Minutes"
        ],
        "Count":[
            120,
            45,
            90,
            110,
            35
        ]
    })

    fig1 = px.bar(
        category_df,
        x="Category",
        y="Count"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    st.subheader("Monthly Upload Trend")

    uploads_df = pd.DataFrame({
        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],
        "Uploads":[
            40,
            52,
            48,
            61,
            34
        ]
    })

    fig2 = px.line(
        uploads_df,
        x="Month",
        y="Uploads",
        markers=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# ==================================================
# RECENT DOCUMENTS
# ==================================================

st.subheader("Recent Uploads")

recent_docs = pd.DataFrame({
    "Document":[
        "Term 2 Circular",
        "Grade 10 Report Cards",
        "Sports Day Consent Form"
    ],
    "Uploaded By":[
        "Principal",
        "Administrator",
        "Sports Coordinator"
    ],
    "Date":[
        "2026-05-01",
        "2026-05-15",
        "2026-05-20"
    ]
})

st.dataframe(
    recent_docs,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.info(
    "Document Management Module - Rentabuka School Management System"
)
