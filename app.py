import os
import gradio as gr
import torch
# from llama_cpp import Llama

import setup    # setup.py file
import rag      # rag.py file

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# setup.download_model()

# llm = Llama(
#     model_path="./models/model.gguf",
#     verbose=False
# )


def generate(query, context):
    input_text = f"Remember this: {context}\nNow, answer this: {query}"
    # response = llm.create_chat_completion(
    #     messages=[
    #         {"role": "system",
    #             "content": "You are an AI assistant that follows instruction extremely well. Help as much as you can."
    #          },
    #         {
    #             "role": "user",
    #             "content": input_text
    #         }
    #     ]
    # )

    return context
    return response["choices"][0]["message"]["content"]

    
# Define the chat function
def chat(query, history=[]):
    context = rag.retrieve(query)
    response = generate(query, context)
    history.append(response)

    return response

# Define the Gradio interface
ui = gr.ChatInterface(
    fn=chat,
    type="messages",
    title="Hansraj Chatbot 🤖",
    description=(
        "🤖 Hansraj Chatbot is here to assist you with all queries related to Hansraj College. "
        "Whether it's about the college's history, achievements, or facilities, feel free to ask!"
    ),
    examples=[
        "Tell me about the college?",
        "Tell me about Hansraj College?",
        "What are the achievements of Hansraj College?"
    ]
)

# Launch the interface
ui.launch()
