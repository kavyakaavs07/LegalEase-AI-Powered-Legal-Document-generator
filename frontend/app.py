import requests
import streamlit as st


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered",
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    """
    <div style="text-align: center;">
        <h1>⚖️ LegalEase</h1>
        <h2>AI Legal Document Generator</h2>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Input fields
# --------------------------------------------------

document_type = st.text_input(
    "Document Type (Ex: Agreement, Contract, NDA)",
    placeholder="Example: Freelance Work Contract",
)


parties = st.text_area(
    "Parties Involved",
    placeholder=(
        "Example: Jane Doe (Service Provider), "
        "TechNova Inc. (Client)"
    ),
    height=100,
)


terms = st.text_area(
    "Terms & Conditions (Use semicolons for bullet points)",
    placeholder=(
        "Example: Work must be delivered by May 15, 2025; "
        "Payment will be made within 7 days of invoice; "
        "The client retains intellectual property rights"
    ),
    height=100,
)


effective_date = st.text_input(
    "Effective Date",
    placeholder="Example: April 15, 2025",
)


# --------------------------------------------------
# Generate button
# --------------------------------------------------

if st.button("Generate Document"):

    if not document_type.strip():
        st.warning("Please enter a document type.")

    elif not parties.strip():
        st.warning("Please enter the parties involved.")

    elif not terms.strip():
        st.warning("Please enter the terms and conditions.")

    elif not effective_date.strip():
        st.warning("Please enter an effective date.")

    else:

        # Build the prompt for Gemini
        prompt = f"""
You are a legal document drafting assistant.

Create a professional draft legal document.

Document Type:
{document_type}

Parties Involved:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{effective_date}

Requirements:

1. Use a professional legal-document structure.
2. Include appropriate headings and sections.
3. Clearly identify the parties.
4. Include the provided terms and conditions.
5. Include the effective date.
6. Use placeholders such as [Address] where information is missing.
7. Do not invent important facts that were not provided.
8. Include a brief notice that the document is a general informational
   template and is not legal advice.
9. Laws vary by jurisdiction, so recommend review by a qualified
   legal professional before signing.

Return only the document.
"""

        try:

            with st.spinner("Generating legal document..."):

                response = requests.post(
                    "http://127.0.0.1:8000/generate",
                    json={
                        "prompt": prompt
                    },
                    timeout=60,
                )

            if response.status_code == 200:

                data = response.json()

                st.session_state["document"] = data["document"]

            elif response.status_code == 429:

                st.error(
                    "Gemini API quota has been reached. "
                    "Please try again after the quota resets."
                )

            else:

                st.error(
                    f"API Error {response.status_code}: "
                    f"{response.text}"
                )

        except requests.exceptions.RequestException as exc:

            st.error(
                f"Could not connect to FastAPI: {exc}"
            )


# --------------------------------------------------
# Generated document
# --------------------------------------------------

if "document" in st.session_state:

    st.success("✅ Document Generated Successfully!")

    st.subheader("Generated Document")

    st.text_area(
        "Document Preview",
        value=st.session_state["document"],
        height=500,
        key="document_editor",
    )

    # Keep edited version
    st.session_state["document"] = st.session_state["document_editor"]


    # --------------------------------------------------
    # Downloads
    # --------------------------------------------------

    st.subheader("Download Document")

    document_content = st.session_state["document"]

    st.download_button(
        label="📄 Download as TXT",
        data=document_content,
        file_name="legal_document.txt",
        mime="text/plain",
    )