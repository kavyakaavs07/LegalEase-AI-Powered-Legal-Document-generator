# ⚖️ LegalEase

### AI-Powered Legal Document Generator

LegalEase is a Generative AI-powered web application designed to help users create structured legal document drafts using natural language inputs.

The application combines **Streamlit**, **FastAPI**, and **Google Gemini** to provide an easy-to-use interface for generating documents such as employment agreements, NDAs, lease agreements, service agreements, and other customizable legal documents.

> **Disclaimer:** LegalEase provides general informational document templates and is not a substitute for professional legal advice. Laws and legal requirements vary by jurisdiction. Generated documents should be reviewed by a qualified legal professional before use or signing.

---

## 🚀 Features

- 🤖 AI-powered legal document generation
- 📝 Natural-language document creation
- ⚖️ Support for multiple legal document types
- 👥 Input for parties involved
- 📋 Custom terms and conditions
- 📅 Effective date selection
- ✏️ Editable generated document preview
- 📄 TXT document generation
- 📑 DOCX document generation
- 📕 PDF document generation
- 🔌 FastAPI backend
- 🎨 Streamlit frontend
- 🔐 Environment-based API key configuration

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   Streamlit Frontend │
                    │       :8501          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    │       :8000          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      AI Core         │
                    │  Gemini Generator    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Google Gemini     │
                    │        API           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Generated Document   │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
               TXT           DOCX           PDF
