import tkinter as tk
from tkinter import scrolledtext
import requests
from time import strftime

# Hugging Face API configuration
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = "your_hugging_face_token"  # Replace with your Hugging Face API token

headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to send a request to Hugging Face API and get the chatbot's response
def ask_ai():
    user_input = user_input_text.get("1.0", tk.END).strip()
    
    if user_input:  # Check if input is not empty
        # Add timestamp to the chat
        timestamp = strftime('%H:%M:%S')

        # Send the user input to Hugging Face API
        response = requests.post(
            HF_API_URL,
            headers=headers,
            json={"inputs": user_input}
        )
        
        if response.status_code == 200:
            ai_response = response.json()[0]['generated_text']
        else:
            ai_response = "Sorry, I couldn't process your request."

        # Display the user input and AI response in the chat area with timestamps
        chat_area.config(state=tk.NORMAL)  # Enable chat area to append text
        chat_area.insert(tk.END, f"[{timestamp}] You: {user_input}\n")
        chat_area.insert(tk.END, f"[{timestamp}] AI: {ai_response}\n\n")
        chat_area.config(state=tk.DISABLED)  # Disable chat area to prevent user editing
        chat_area.yview(tk.END)  # Scroll to the latest message
        user_input_text.delete("1.0", tk.END)  # Clear the input field

# Create the main window
root = tk.Tk()
root.title("CKS AI")
root.geometry("500x600")
root.config(bg="#1c1c1c")  # Dark background color

# Set the window icon (use the path to your .ico file)
root.iconbitmap('cks.ico')  # Make sure 'cks.ico' is in the same directory as your script

# Create the chat area (scrollable text widget)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED, 
                                     font=("Arial", 12), bg="#2c2c2c", fg="#f5f5f5", insertbackground="white")
chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the user input field
user_input_text = tk.Text(root, height=4, width=40, font=("Arial", 12), bg="#2c2c2c", fg="#f5f5f5", 
                          insertbackground="white", bd=2, relief="solid", wrap=tk.WORD)
user_input_text.grid(row=1, column=0, padx=10, pady=10)

# Create the submit button
submit_button = tk.Button(root, text="Send", command=ask_ai, font=("Arial", 12), bg="#ff7f32", fg="white", 
                          relief="solid", bd=0, height=2)
submit_button.grid(row=1, column=1, padx=10, pady=10)

# Add a header label
header_label = tk.Label(root, text="Developed by CKS-Tech", font=("Arial", 16), bg="#1c1c1c", fg="#ff7f32")
header_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
