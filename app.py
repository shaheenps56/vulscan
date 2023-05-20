import streamlit as st
import numpy as np
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification, pipeline



@st.cache_data #(allow_output_mutation=True)
def get_model():
    tokenizer = RobertaTokenizer.from_pretrained('roberta-large-mnli')
    model = RobertaForSequenceClassification.from_pretrained('shaheenps/vulbertanew')
    return tokenizer,model

tokenizer,model = get_model()

st.title ("Source code vulnerability prediction")
st.file_uploader('Select the program file')
text_input = st.text_area("Enter code",height=500)
button = st.button("Analyze")

d = {

    1:'Not Vulnerable',
    0:'Vulnerable'

}

def analyze_code(text):
    # Preprocess and tokenize the input text
    encoded_input = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        return_tensors='pt',
        padding='max_length',
        truncation=True,
        max_length=512
    )
    

    output = model(**encoded_input)
    predicted_label = output.logits.argmax().item()
    st.write("Logits:",output.logits)
    y_pred = np.argmax(output.logits.detach().numpy(),axis=1)
    st.write("Prediction: ",d[y_pred[0]])


    return predicted_label

if button:
    prediction = analyze_code(text_input)
    st.write(f"Predicted vulnerability label: {prediction}")
