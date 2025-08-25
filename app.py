import gradio as gr
import numpy as np
import pickle

model = pickle.load(open('model.plk', 'rb'))
scaler = pickle.load(open('scaler.plk', 'rb'))

label_map = {0: 'Low', 1: 'Medium', 2: 'High'}

def predict_house(size_m2, bedrooms, location_score):
    input_data = np.array([[size_m2, bedrooms, location_score]])
    input_data=scaler.transform(input_data)
    pred_num = model.predict(input_data)[0]
    return label_map[pred_num]
iface = gr.Interface(
    fn=predict_house,
    inputs=[
        gr.Number(label="Size (m²)"),
        gr.Number(label="Bedrooms"),
        gr.Number(label="Location Score")
    ],
    outputs=gr.Textbox(label="Predicted Price Category"),
    title="House Price Predictor",
    description="Enter house details to predict price category."
)

iface.launch()
