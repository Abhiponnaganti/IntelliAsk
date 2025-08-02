# 🧠 IntelliAsk - Where Documents Meet Intelligence
# Built for meaningful conversations with your data
# Because every document has stories to tell, and every question deserves
# a thoughtful answer

import streamlit as st
import os
import re
from pypdf import PdfReader
from docx import Document as DocxDocument
from dotenv import load_dotenv
import time
from groq import Groq
import hashlib
from datetime import datetime

# Load environment variables
load_dotenv()

# Enterprise Dark Theme CSS


def load_enterprise_css():
    st.markdown(
        """
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap'); /* noqa: E501 */

        /* Dark Theme Global Styling */
        .stApp {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #e4e4e7;
            font-family: 'Inter', sans-serif;
        }

        /* Dark theme for all text elements */
        .stMarkdown, .stText, p, div, span, h1, h2, h3, h4, h5, h6 {
            color: #e4e4e7 !important;
        }

        /* Input fields dark theme */
        .stTextInput > div > div > input {
            background-color: #1e293b !important;
            color: #e4e4e7 !important;
            border: 1px solid #334155 !important;
        }

        .stTextArea > div > div > textarea {
            background-color: #1e293b !important;
            color: #e4e4e7 !important;
            border: 1px solid #334155 !important;
        }

        /* Header Section */
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2.5rem 2rem;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .main-title {
            color: white;
            font-size: 2.8rem;
            font-weight: 700;
            margin: 0;
            letter-spacing: -0.02em;
        }

        .main-subtitle {
            color: rgba(255,255,255,0.9);
            font-size: 1.2rem;
            font-weight: 400;
            margin: 0.5rem 0 0 0;
            letter-spacing: 0.01em;
        }

        /* Card Components */
        .professional-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.3);
            margin-bottom: 1.5rem;
            backdrop-filter: blur(10px);
        }

        .upload-card {
            background: linear-gradient(135deg, #f8f9ff 0%, #e8eeff 100%);
            border: 2px dashed #667eea;
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .upload-card:hover {
            border-color: #764ba2;
            background: linear-gradient(135deg, #f0f2ff 0%, #e0e8ff 100%);
        }

        /* Answer Display */
        .answer-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 0.5rem;
            border-radius: 16px;
            margin: 1.5rem 0;
        }

        .answer-content {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            color: #2c3e50;
            line-height: 1.7;
            font-size: 1.05rem;
        }

        .answer-header {
            color: #667eea;
            font-size: 1.3rem;
            font-weight: 600;
            margin: 0 0 1rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Status Indicators */
        .status-card {
            background: white;
            padding: 1rem 1.5rem;
            border-radius: 10px;
            border-left: 4px solid #28a745;
            margin-bottom: 1rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        .status-card.warning {
            border-left-color: #ffc107;
            background: #fff9e6;
        }

        .status-card.error {
            border-left-color: #dc3545;
            background: #ffe6e6;
        }

        /* Metrics Display */
        .metrics-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }

        .metric-item {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            border: 1px solid rgba(0,0,0,0.05);
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
            margin: 0;
        }

        .metric-label {
            font-size: 0.9rem;
            color: #64748b;
            font-weight: 500;
            margin: 0.5rem 0 0 0;
        }

        /* Button Styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3) !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4) !important;
            background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%) !important;
        }

        .stButton > button:active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
        }

        .stButton > button:focus {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3) !important;
        }

        /* Sidebar Styling */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 1rem;
            backdrop-filter: blur(10px);
        }

        /* Progress Bar */
        .stProgress .st-bo {
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 10px;
        }

        /* Source Cards */
        .source-card {
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 10px;
            padding: 1rem;
            margin: 0.5rem 0;
            border-left: 4px solid #667eea;
        }

        .source-title {
            font-weight: 600;
            color: #495057;
            margin-bottom: 0.5rem;
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Question input styling */
        .stTextArea textarea {
            border-radius: 12px;
            border: 2px solid #e1e8ed;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .stTextArea textarea:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        /* File uploader styling */
        .uploadedFile {
            border-radius: 10px;
            border: 1px solid #e1e8ed;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


class DocumentAnalysisPlatform:
    """
    The heart of IntelliAsk - where documents transform into conversations.

    Think of this as your personal document whisperer. It takes your files,
    understands them deeply, and helps you have meaningful conversations with your data.
    No more endless scrolling through pages - just ask what you want to know!
    """

    def __init__(self):
        # Our document memory - where all the magic gets stored
        self.documents = []
        self.processed_docs = []

        # Our AI friend who helps us understand everything
        self.ai_client = None

        # Smart caching - because nobody likes waiting for the same answer
        # twice
        self.response_cache = {}

    def initialize_ai_service(self, api_key: str):
        """Initialize AI service connection"""
        try:
            self.ai_client = Groq(api_key=api_key)
            # Test the connection
            self.ai_client.chat.completions.create(
                messages=[{"role": "user", "content": "System check"}],
                model="llama3-8b-8192",
                max_tokens=5,
            )
            return True, "AI service connected successfully"
        except Exception as e:
            error_msg = str(e)
            if "invalid_api_key" in error_msg.lower():
                return False, "Invalid API key. Please verify your credentials."
            elif "rate_limit" in error_msg.lower():
                return False, "Rate limit exceeded. Please wait and try again."
            else:
                return False, f"Connection failed: {error_msg}"

    def extract_document_content(self, file, filename: str) -> tuple:
        """Extract content from uploaded document"""
        file_extension = filename.split(".")[-1].lower()

        try:
            if file_extension == "pdf":
                reader = PdfReader(file)
                content = "\n".join([page.extract_text() for page in reader.pages])
                metadata = {"pages": len(reader.pages), "type": "PDF Document"}

            elif file_extension == "docx":
                doc = DocxDocument(file)
                paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
                content = "\n".join(paragraphs)
                metadata = {"paragraphs": len(paragraphs), "type": "Word Document"}

            elif file_extension == "txt":
                raw_content = file.read()
                content = (
                    raw_content.decode("utf-8")
                    if isinstance(raw_content, bytes)
                    else raw_content
                )
                lines = len(content.split("\n"))
                metadata = {"lines": lines, "type": "Text Document"}

            else:
                return "", {}, f"Unsupported file format: {file_extension}"

            if not content.strip():
                return "", metadata, "No readable content found in document"

            return content.strip(), metadata, None

        except Exception as e:
            return "", {}, f"Error processing {filename}: {str(e)}"

    def create_document_segments(
        self, content: str, filename: str, max_segment_size: int = 3000
    ) -> list:
        """Create optimized document segments for analysis"""
        if len(content) <= max_segment_size:
            return (
                [
                    {
                        "content": content,
                        "segment_id": 1,
                        "word_count": len(content.split()),
                        "filename": filename,
                    }
                ]
                if content
                else []
            )

        # Split by logical sections first
        sections = [
            section.strip()
            for section in content.split("\n\n")
            if section.strip()
        ]

        segments = []
        current_segment = ""
        segment_id = 1

        for section in sections:
            # Check if adding this section exceeds the limit
            if len(current_segment) + len(section) > max_segment_size:
                if current_segment:
                    segments.append(
                        {
                            "content": current_segment.strip(),
                            "segment_id": segment_id,
                            "word_count": len(current_segment.split()),
                            "filename": filename,
                        }
                    )
                    segment_id += 1
                    current_segment = ""

                # Handle oversized sections
                if len(section) > max_segment_size:
                    sentences = re.split(r"(?<=[.!?])\s+", section)
                    for sentence in sentences:
                        if len(current_segment) + len(sentence) > max_segment_size:
                            if current_segment:
                                segments.append(
                                    {
                                        "content": current_segment.strip(),
                                        "segment_id": segment_id,
                                        "word_count": len(current_segment.split()),
                                        "filename": filename,
                                    }
                                )
                                segment_id += 1
                            current_segment = sentence + " "
                        else:
                            current_segment += sentence + " "
                else:
                    current_segment = section + "\n\n"
            else:
                current_segment += section + "\n\n"

        # Add final segment
        if current_segment.strip():
            segments.append(
                {
                    "content": current_segment.strip(),
                    "segment_id": segment_id,
                    "word_count": len(current_segment.split()),
                    "filename": filename,
                }
            )

        return segments

    def process_document_collection(self, uploaded_files) -> tuple:
        """Process a collection of uploaded documents"""
        try:
            self.documents = []
            self.processed_docs = []

            processing_summary = {
                "total_files": len(uploaded_files),
                "successful": 0,
                "failed": 0,
                "total_segments": 0,
                "total_words": 0,
                "errors": [],
            }

            for uploaded_file in uploaded_files:
                # Extract content
                content, metadata, error = self.extract_document_content(
                    uploaded_file, uploaded_file.name
                )

                if error:
                    processing_summary["failed"] += 1
                    processing_summary["errors"].append(
                        f"{uploaded_file.name}: {error}"
                    )
                    continue

                if not content:
                    processing_summary["failed"] += 1
                    processing_summary["errors"].append(
                        f"{uploaded_file.name}: No content extracted"
                    )
                    continue

                # Create segments
                segments = self.create_document_segments(content, uploaded_file.name)

                # Store segments
                for segment in segments:
                    self.documents.append(
                        {
                            "content": segment["content"],
                            "source": f"{uploaded_file.name} (Section {segment['segment_id']})",
                            "filename": uploaded_file.name,
                            "segment_id": segment["segment_id"],
                            "word_count": segment["word_count"],
                        }
                    )

                # Store processing info
                self.processed_docs.append(
                    {
                        "name": uploaded_file.name,
                        "segments": len(segments),
                        "total_words": sum(seg["word_count"] for seg in segments),
                        "file_size": uploaded_file.size,
                        "metadata": metadata,
                    }
                )

                processing_summary["successful"] += 1
                processing_summary["total_segments"] += len(segments)
                processing_summary["total_words"] += sum(
                    seg["word_count"] for seg in segments
                )

            return len(self.documents) > 0, processing_summary

        except Exception as e:
            return False, {"error": f"Processing failed: {str(e)}"}

    def find_relevant_content(self, query: str, max_results: int = 4) -> list:
        """Find content segments relevant to the user query"""
        if not self.documents:
            return []

        query_terms = set(re.findall(r"\b\w{3,}\b", query.lower()))

        if not query_terms:
            return self.documents[:max_results]

        relevance_scores = []

        for document in self.documents:
            content_lower = document["content"].lower()
            content_terms = set(re.findall(r"\b\w{3,}\b", content_lower))

            # Calculate relevance metrics
            term_overlap = len(query_terms.intersection(content_terms))

            if term_overlap > 0:
                # Jaccard similarity
                jaccard = term_overlap / len(query_terms.union(content_terms))

                # Term frequency in document
                tf_score = sum(content_lower.count(term) for term in query_terms) / len(
                    document["content"].split()
                )

                # Early occurrence bonus
                content_preview = content_lower[:250]
                early_matches = sum(
                    1 for term in query_terms if term in content_preview
                )
                position_score = early_matches / len(query_terms) * 0.3

                # Document quality score (prefer substantial content)
                quality_score = min(document["word_count"] / 100, 1.0) * 0.1

                # Combined relevance score
                total_score = jaccard + tf_score + position_score + quality_score

                relevance_scores.append(
                    {
                        "document": document,
                        "relevance": total_score,
                        "term_matches": term_overlap,
                        "match_ratio": term_overlap / len(query_terms),
                    }
                )

        # Sort by relevance and return top results
        relevance_scores.sort(key=lambda x: x["relevance"], reverse=True)

        if relevance_scores:
            return relevance_scores[:max_results]
        else:
            return self.documents[:max_results]

    def generate_ai_response(self, query: str, relevant_content: list) -> dict:
        """Generate intelligent response using AI service"""
        if not self.ai_client:
            return {
                "response": "AI service not available. Please check your connection.",
                "sources": [],
                "processing_time": 0,
                "confidence": 0.0,
            }

        if not relevant_content:
            return {
                "response": "No relevant information found in your document collection.",
                "sources": [],
                "processing_time": 0,
                "confidence": 0.0,
            }

        # Prepare context from relevant content
        context_sections = []
        source_info = []
        total_context_length = 0
        max_context = 6000

        for item in relevant_content:
            if isinstance(item, dict) and "document" in item:
                doc = item["document"]
                relevance = item.get("relevance", 0)
            else:
                doc = item
                relevance = 1.0

            section_text = f"From {doc['source']}:\n{doc['content']}"

            if total_context_length + len(section_text) > max_context:
                break

            context_sections.append(section_text)
            source_info.append(
                {
                    "source": doc["source"],
                    "relevance": relevance,
                    "word_count": doc["word_count"],
                }
            )
            total_context_length += len(section_text)

        context = "\n\n" + "=" * 50 + "\n\n".join(context_sections)

        # Craft professional prompt
        system_instruction = (
            "You are an expert document analyst providing professional insights. "
            "Your role is to:\n\n"
            "1. Analyze the provided document context thoroughly\n"
            "2. Answer questions with precision and clarity\n"
            "3. Cite specific sources when making claims\n"
            "4. Acknowledge when information is not available in the context\n"
            "5. Provide structured, actionable responses\n\n"
            "Maintain a professional tone while being accessible and informative."
        )

        user_query = f"""Document Context:
{context}

User Question: {query}

Please provide a comprehensive analysis based on the document context. Structure your response clearly and cite relevant sources where appropriate."""

        try:
            start_time = time.time()

            response = self.ai_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_query},
                ],
                model="llama3-8b-8192",
                max_tokens=1200,
                temperature=0.2,
            )

            processing_time = time.time() - start_time
            ai_response = response.choices[0].message.content

            # Calculate confidence based on relevance scores
            if relevant_content and isinstance(relevant_content[0], dict):
                avg_relevance = sum(
                    item.get("relevance", 0) for item in relevant_content
                ) / len(relevant_content)
                confidence = min(avg_relevance * 1.5, 1.0)
            else:
                confidence = 0.7

            return {
                "response": ai_response,
                "sources": source_info,
                "processing_time": processing_time,
                "confidence": confidence,
                "context_length": total_context_length,
            }

        except Exception as e:
            return {
                "response": f"Error generating response: {str(e)}",
                "sources": source_info,
                "processing_time": 0,
                "confidence": 0.0,
                "context_length": total_context_length,
            }

    def process_user_query(self, query: str) -> dict:
        """Main method to process user queries"""
        start_time = time.time()

        # Check cache for previously asked questions
        query_hash = hashlib.md5(query.encode()).hexdigest()
        if query_hash in self.response_cache:
            cached_result = self.response_cache[query_hash]
            cached_result["from_cache"] = True
            cached_result["total_time"] = 0.1
            return cached_result

        # Find relevant content
        relevant_content = self.find_relevant_content(query)

        # Generate AI response
        ai_result = self.generate_ai_response(query, relevant_content)

        # Compile final result
        final_result = {
            "query": query,
            "answer": ai_result["response"],
            "sources": ai_result["sources"],
            "relevant_segments": relevant_content,
            "processing_time": ai_result["processing_time"],
            "total_time": time.time() - start_time,
            "confidence": ai_result["confidence"],
            "context_length": ai_result.get("context_length", 0),
            "from_cache": False,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Cache the result
        self.response_cache[query_hash] = final_result

        return final_result


def main():
    st.set_page_config(
        page_title="IntelliAsk - Document Intelligence Platform",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Load professional styling
    load_enterprise_css()

    # Main header
    st.markdown(
        """
    <div class="main-header">
        <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <h1 class="main-title">IntelliAsk</h1>
        </div>
        <p class="main-subtitle">Enterprise Document Intelligence Platform</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Initialize session state
    if "analysis_platform" not in st.session_state:
        st.session_state.analysis_platform = DocumentAnalysisPlatform()
        st.session_state.documents_ready = False
        st.session_state.ai_connected = False

    # Initialize AI service with environment variable
    api_key = os.getenv("GROQ_API_KEY", "")

    if api_key and not st.session_state.ai_connected:
        success, message = st.session_state.analysis_platform.initialize_ai_service(
            api_key
        )
        if success:
            st.session_state.ai_connected = True

    # Professional sidebar (only show document statistics when available)
    with st.sidebar:
        # Document statistics
        if st.session_state.documents_ready:
            st.markdown("### Document Statistics")

            total_segments = len(st.session_state.analysis_platform.documents)
            total_files = len(st.session_state.analysis_platform.processed_docs)
            total_words = sum(
                doc.get("total_words", 0)
                for doc in st.session_state.analysis_platform.processed_docs
            )

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Documents", total_files)
                st.metric("Segments", total_segments)
            with col2:
                st.metric("Total Words", f"{total_words:,}")
                cache_size = len(st.session_state.analysis_platform.response_cache)
                st.metric("Cached Queries", cache_size)

            # Document breakdown
            st.markdown("**Document Breakdown:**")
            for doc in st.session_state.analysis_platform.processed_docs:
                st.write(f"**{doc['name']}**")
                st.write(
                    "   └ {} segments, {:,} words".format(
                        doc['segments'],
                        doc['total_words']
                    )
                )

        elif api_key:
            st.markdown("### IntelliAsk")
            st.markdown("Ready for document upload")
        else:
            st.markdown("### Configuration Required")
            st.markdown("Please set GROQ_API_KEY environment variable")

    # Main content area - let's make this welcoming!
    if not api_key:
        st.markdown(
            """
        **👋 Hey there! Welcome to IntelliAsk!**

        I'm excited to help you have amazing conversations with your documents, but first we need to get you set up with an AI service.

        **🎯 What I can do for you:**
        - Turn your PDFs, Word docs, and text files into interactive conversations
        - Answer complex questions about your documents with confidence scores
        - Provide sources and citations so you always know where information comes from
        - Remember our previous conversations to speed things up

        **🚀 Quick Setup (takes 2 minutes):**
        1. **Get your API key**: Head over to [Groq Console](https://console.groq.com/) and grab a free API key
        2. **Set your environment**: Run `export GROQ_API_KEY=your_api_key_here` in your terminal
        3. **Restart me**: Just restart this application and we're good to go!

        *Can't wait to see what insights we'll discover together! 🧠✨*
        """
        )
        return

    # Document upload section
    st.markdown("### Document Upload & Processing")

    uploaded_files = st.file_uploader(
        "Select documents for analysis",
        accept_multiple_files=True,
        type=["pdf", "docx", "txt"],
        help="Upload PDF, Word documents, or text files (max 200MB per file)",
    )

    if uploaded_files:
        # File preview
        st.markdown("#### Selected Documents")

        total_size = sum(file.size for file in uploaded_files)

        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write("**Document Name**")
        with col2:
            st.write("**Type**")
        with col3:
            st.write("**Size**")

        for file in uploaded_files:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"{file.name}")
            with col2:
                st.write(file.type.split("/")[-1].upper())
            with col3:
                st.write(f"{file.size / 1024:.1f} KB")

        st.write(
            "**Total:** {} files ({:.2f} MB)".format(
                len(uploaded_files),
                total_size / 1024 / 1024
            )
        )

        # Processing button
        if st.button(
            "Process Document Collection", type="primary", use_container_width=True
        ):
            progress_bar = st.progress(0)
            status_container = st.empty()

            with status_container.container():
                st.markdown("**Processing Status:**")
                st.write("Extracting document content...")
            progress_bar.progress(25)

            # Process documents
            success, summary = (
                st.session_state.analysis_platform.process_document_collection(
                    uploaded_files
                )
            )
            progress_bar.progress(75)

            with status_container.container():
                st.write("Optimizing for AI analysis...")
            time.sleep(0.5)

            progress_bar.progress(100)

            # Clear progress indicators
            progress_bar.empty()
            status_container.empty()

            if success:
                st.session_state.documents_ready = True

                # Success message
                st.success(
                    "Successfully processed {} documents into {} segments".format(
                        summary['successful'],
                        summary['total_segments']
                    )
                )

                # Processing summary
                if summary.get("errors"):
                    st.warning(f"{summary['failed']} files had issues:")
                    for error in summary["errors"]:
                        st.write(f"• {error}")

                # Display metrics using simple layout
                col_met1, col_met2, col_met3, col_met4 = st.columns(4)
                with col_met1:
                    st.metric("Files Processed", summary["successful"])
                with col_met2:
                    st.metric("Content Segments", summary["total_segments"])
                with col_met3:
                    st.metric("Total Words", f"{summary['total_words']:,}")
                with col_met4:
                    st.metric("Analysis Status", "Ready")
            else:
                st.error("Document processing failed")
                if summary.get("error"):
                    st.write(summary["error"])

    # Query interface
    if st.session_state.documents_ready:
        st.markdown("---")
        st.markdown("### Document Analysis & Insights")

        query = st.text_area(
            "Enter your analysis question:",
            height=120,
            placeholder="Ask any question about your documents...\n\nExamples:\n• What are the key findings in these documents?\n• Summarize the main recommendations\n• What risks or challenges are mentioned?",
            help="Ask detailed questions about your document content",
        )

        if st.button(
            "Generate Analysis",
            type="primary",
            disabled=not query.strip(),
            use_container_width=True,
        ):
            with st.spinner("Analyzing documents and generating insights..."):
                result = st.session_state.analysis_platform.process_user_query(query)

                # Display results
                st.markdown("### Analysis Results")

                # Performance metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    confidence_color = (
                        "🟢"
                        if result["confidence"] > 0.7
                        else "🟡" if result["confidence"] > 0.4 else "🔴"
                    )
                    st.metric(
                        "Confidence",
                        f"{result['confidence']:.1%}",
                        delta=confidence_color,
                    )
                with col2:
                    st.metric("Response Time", f"{result['total_time']:.1f}s")
                with col3:
                    st.metric("Sources Used", len(result["sources"]))
                with col4:
                    cache_status = (
                        "Cached" if result.get("from_cache", False) else "Generated"
                    )
                    st.metric("Response Type", cache_status)

                # Main answer display
                answer_text = result["answer"].replace("\n", "<br>")
                st.markdown(
                    """
                <div class="answer-container">
                    <div class="answer-content">
                        <div class="answer-header">
                            Professional Analysis
                        </div>
                        %s
                    </div>
                </div>
                """ % answer_text,
                    unsafe_allow_html=True,
                )

                # Source documentation
                if result["sources"]:
                    st.markdown("### Source Documentation")

                    for i, source in enumerate(result["sources"][:4]):
                        relevance_bar = (
                            "🟩" * int(source.get("relevance", 0.5) * 10) +
                            "⬜" * (10 - int(source.get("relevance", 0.5) * 10))
                        )

                        with st.expander(
                            f"Source {i + 1}: {source['source']}", expanded=i == 0
                        ):
                            col_src1, col_src2 = st.columns([2, 1])

                            with col_src1:
                                st.markdown(
                                    f"""
                                <div class="source-card">
                                    <div class="source-title">Relevance Score</div>
                                    <div>{relevance_bar} ({source.get('relevance', 0.5):.2f})</div>
                                </div>
                                """,
                                    unsafe_allow_html=True,
                                )

                            with col_src2:
                                st.metric("Word Count", source.get("word_count", "N/A"))

                            # Find and display source content
                            for segment in result.get("relevant_segments", []):
                                if (
                                    isinstance(segment, dict)
                                    and
                                    segment.get("document", {}).get("source") == source["source"]
                                ):
                                    content = segment["document"]["content"]
                            preview = (
                                content[:400] + "..." if len(content) > 400 else content
                            )

                            st.markdown("**Content Preview:**")
                            st.write(preview)

                            if len(content) > 400:
                                if st.button(
                                    f"Show Full Content for Source {i + 1}",
                                    key=f"show_full_{i}",
                                ):
                                    st.markdown("**Complete Content:**")
                                    st.text_area(
                                        "",
                                        value=content,
                                        height=200,
                                        disabled=True,
                                        key=f"full_content_{i}",
                                    )
                            break

                # Technical details
                with st.expander("Analysis Technical Details"):
                    tech_col1, tech_col2 = st.columns(2)

                    with tech_col1:
                        st.write(
                            f"**Query Processing Time:** {result.get('processing_time', 0):.2f}s"
                        )
                        st.write(
                            (
                                f"**Context Length:** "
                                f"{result.get('context_length', 0):,} characters"
                            )
                        )
                        st.write(
                            f"**Analysis Timestamp:** {result.get('timestamp', 'N/A')}"
                        )

                    with tech_col2:
                        st.write(
                            f"**Segments Analyzed:** {len(result.get('relevant_segments', []))}"
                        )
                        st.write(
                            f"**Cache Status:** {'Hit' if result.get('from_cache') else 'Miss'}"
                        )
                        st.write("**AI Model:** Llama 3 (8B Parameters)")

    elif not st.session_state.documents_ready and api_key:
        st.markdown(
            """
        **Ready for Document Upload**

        Upload your documents above to begin professional analysis.

        **Supported formats:** PDF, Word Documents (.docx), Text Files (.txt)
        """
        )

    # Footer
    st.markdown("---")
    footer_html = """
    <div style="text-align: center; color: #64748b; padding: 2rem; background: rgba(255,255,255,0.5); border-radius: 15px; margin-top: 2rem;">
        <h4 style="color: #475569; margin-bottom: 1rem;">IntelliAsk</h4>
        <p style="margin: 0;">Enterprise Document Intelligence Platform • Advanced AI Analysis • Secure and Confidential Processing</p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
            Powered by cutting-edge language models • Built with enterprise-grade security standards
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
