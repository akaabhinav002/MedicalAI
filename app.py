import streamlit as st
from pathlib import Path
import google.generativeai as genai 


from api import api_key

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k":32,
    "max_output_tokens": 4096,
}

# Model  Config
model = genai.GenerativeModel(
  model_name="gemini-pro-vision",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

#set page config
st.set_page_config(page_title="Medical_Images Analysis",page_icon=":doctor:")

#set the logo
st.image("H:\Medical AI\logo\logo.jpg",width=150)
system_prompt = """As a highly skilled medical practitioner specializing in image analysis, you are tasked with the following responsibilities:

Your Responsibilities include:

Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal features, structures, or conditions that may indicate underlying health issues.
Findings Report: Document all observed anomalies or signs of disease. Clearly articulate your observations in a detailed report.
Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further diagnostic tests, monitoring, or medical consultations.
Treatment Suggestions: If appropriate, recommend possible treatment options or interventions based on the analysis.
Important Notes:

Scope of Response: Only respond if the image pertains to human health issues.
Clarity of Image: In cases where the image quality impedes clear analysis, note that certain details may not be discernible.
Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any medical decisions."
Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis.

Please provide me an output response with these 4 headings detailed Analysis,Findings reports,Recommendations and Next Steps,Treatment Suggestions

"""

#title
st.title("Medical Images Analysis🧑🏻‍⚕️")

#sub header
st.subheader("Analyze your medical images for any disease or symptom")  

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file,width=300,caption="Uploaded Image")
submit_button=st.button("Generate the Analysis")

if submit_button:
    #process image
    image_data=uploaded_file.getvalue()

    image_parts=[
        {
            "mime_type":"image/jpeg",
            "data":image_data
        },
    ]

    prompt_parts=[
        image_parts[0],
        system_prompt,
        
    ]
    
    response=model.generate_content(prompt_parts)   
    # print(response)
    if response:
        st.title("Here is the Analysis of your image:")
        st.write(response.text)