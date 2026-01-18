import gradio as gr
import pandas as pd
import pickle
import numpy as np


with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def main_logic(solids, chloramines,trihalomethanes,
               turbidity,ph,conductivity,hardness,
               Sulfate,organic_carbon):
    input_df=pd.DataFrame([[
        solids, chloramines,trihalomethanes,
               turbidity,ph,conductivity,hardness,
               Sulfate,organic_carbon
    ]],columns=[
        'Solids','Chloramines','Trihalomethanes','Turbidity','ph','Conductivity','Hardness','Sulfate','Organic_carbon' 	
    ])

    isSafe = model.predict(input_df)[0]
    return "No" if np.clip(isSafe,0,1)==0 else 'Yes'


input=[
    gr.Slider(320, 61227, label="Solids"),
    gr.Slider(0.3, 13.5, label="Chloramines") ,
    gr.Slider(0.7, 120.0, label="Trihalomethanes"),
    gr.Slider(1.5, 6.7, label="Turbidity"),
    gr.Slider(0.0, 14.0, label="pH"),
    gr.Slider(181, 7090, label="Conductivity"),
    gr.Slider(47, 325, label="Hardness"),
    gr.Slider(129, 481, label="Sulfate"),
    gr.Slider(2.0, 28.3, label="Organic Carbon")
]

app=gr.Interface(
    fn=main_logic,
    inputs=input,
    outputs=gr.Textbox(label="Water Potability"),
    title='Water Quality Check',
    description='Check is the water safe or not!'
)

app.launch()