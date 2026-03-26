# 📧 SMS Spam Classifier

A Machine Learning based SMS Spam Classifier that predicts whether an SMS is **Spam** or **Not Spam (Ham)**.  
The model is trained using Natural Language Processing (NLP) techniques and deployed using **Streamlit** for an interactive web interface.

---

## 🚀 Project Overview

Spam sms are unwanted messages that can contain advertisements, scams, or malicious links.  
This project uses **Machine Learning and NLP** to automatically classify sms into:

- **Spam**
- **Not Spam (Ham)**

The system processes the input text, converts it into numerical features, and predicts the category using a trained machine learning model.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Streamlit

---

## 📊 Machine Learning Workflow

1. Data Cleaning
2. Text Preprocessing
3. Feature Extraction using **TF-IDF Vectorizer**
4. Model Training
5. Model Evaluation
6. Deployment with Streamlit

---

## 🔍 Text Preprocessing Steps

The following preprocessing techniques were applied to the email text:

- Lowercasing
- Tokenization
- Removing Special Characters
- Removing Stopwords
- Stemming

These steps help improve model performance by reducing noise in the text data.

---

## 🤖 Model Used

The classifier is trained using:

- **Naive Bayes Algorithm**

Naive Bayes works well for text classification problems like spam detection.

---

## 💡 How It Works
- User enters an sms in the input box.
- The text is preprocessed.
- The trained model predicts whether the sms is Spam or Not Spam.
- The result is displayed instantly on the web interface.


---

## 📈 Future Improvements
- Add more advanced NLP models
- Improve UI design
- Deploy on cloud platforms
- Add probability scores for predictions

---

Example Input:
Congratulations! You have won a free lottery ticket. Click here to claim.

Output:
Spam