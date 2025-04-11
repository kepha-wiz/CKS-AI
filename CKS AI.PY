import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Initialize Hugging Face model pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Function to handle AI response
def ask_ai():
    user_input = user_input_text.get("1.0", tk.END).strip()
    
    if user_input:  # Check if input is not empty
        # We are using the question-answering model. You can customize this further for different tasks.
        response = qa_pipeline({'context': 'Please provide a detailed context or information here.', 'question': user_input})
        ai_response = response['answer']
        chat_area.config(state=tk.NORMAL)  # Enable chat area to append text
        chat_area.insert(tk.END, f"You: {user_input}\nAI: {ai_response}\n\n")
        chat_area.config(state=tk.DISABLED)  # Disable chat area to prevent user editing
        user_input_text.delete("1.0", tk.END)  # Clear the input field

# Create the main window
root = tk.Tk()
root.title("AI Chatbot")

# Create the chat area (scrollable text widget)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the user input field
user_input_text = tk.Text(root, height=5, width=40)
user_input_text.grid(row=1, column=0, padx=10, pady=10)

# Create the submit button
submit_button = tk.Button(root, text="Ask AI", command=ask_ai)
submit_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
