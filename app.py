import nltk
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# --- PAGE CONFIG ---
st.set_page_config(page_title="Spam Detector Pro", page_icon="✉️", layout="centered")

# --- NLTK RESOURCES ---
@st.cache_resource
def download_nltk_resources():
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt_tab', quiet=True)

download_nltk_resources()

# --- PREPROCESSING LOGIC ---
def transform_text_pipeline(X):
    new_text = []
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    table = str.maketrans('', '', string.punctuation)
    
    for text in X:
        text = str(text).lower().translate(table)
        words = [ps.stem(word) for word in nltk.word_tokenize(text) if word not in stop_words]
        new_text.append(" ".join(words))
    return new_text 

# --- MODEL LOADING ---
@st.cache_resource
def load_model():
    # Ensure this file is in your working directory
    with open("email_clf_pipe.pkl", "rb") as f:
        return pickle.load(f)

try:
    pipeline = load_model()
except FileNotFoundError:
    st.error("Model file not found. Please upload 'email_clf_pipe.pkl'.")
    st.stop()

# --- SIDEBAR (Clean & Professional) ---
with st.sidebar:
    st.title("**🛡️ Spam Shield AI**")
    st.divider()
    
    st.header("Model Details")

    st.write("• TF-IDF Vectorization")
    st.write("• Ensemble ML Classifier")

    st.header("Features")

    st.write("• Real-time prediction")
    st.write("• Confidence score")
    
    st.divider()
    st.caption("This system uses Natural Language Processing to detect phishing patterns in real-time.")


st.title("🛡️ Spam Shield AI")
st.write("Enter the message content below to check for potential security risks.")

# Input Container
with st.container():
    input_sms = st.text_area(
        "Message to analyze:", 
        height=200, 
        placeholder="Paste message here..."
    )
    
    # Analyze Button
    btn_col_1, btn_col_2, btn_col_3 = st.columns([1, 1, 1])
    with btn_col_2:
        analyze_btn = st.button("Analyze Message", use_container_width=True, type="primary")

# Result Display
if analyze_btn:
    if not input_sms.strip():
        st.warning("Please provide a message to analyze.")
    else:
        with st.spinner("Processing text..."):
            # Prediction
            result = pipeline.predict([input_sms])[0]
            probability = pipeline.predict_proba([input_sms])[0][1]
            
        st.divider()
        
        # Display Metrics
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            if result == 1:
                st.error("### 🚩 Classified: SPAM")
            else:
                st.success("### ✅ Classified: HAM")
        
        with res_col2:
            st.metric(label="Risk Probability", value=f"{probability:.1%}")

        # Visual Feedback
        st.progress(probability)
        
        if result == 1:
            st.warning("**Security Advisory:** This message contains high-risk linguistic markers. Avoid clicking any links or providing personal data.")
        else:
            st.info("**Safety Note:** This message appears to be legitimate based on standard patterns.")

# --- FOOTER ---
st.divider()
st.caption("Powered by Scikit-Learn • Professional NLP Pipeline")