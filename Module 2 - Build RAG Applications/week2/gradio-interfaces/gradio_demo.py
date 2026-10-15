import gradio as gr
from huggingface_hub import HfFolder

def add_numbers(Num1, Num2):
    return Num1 + Num2


# Define the interface
demo = gr.Interface(
    fn=add_numbers,
    inputs=[gr.Number(), gr.Number()], # Create two numerical inputs
    outputs=gr.Number()
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port=7860)