from tkinter import *
from datetime import datetime
import random

# ---------------- WINDOW ---------------- #
root = Tk()
root.title("🔥 Advanced Smart Chatbot")
root.geometry("550x650")
root.config(bg="#121212")

# ---------------- CHAT AREA ---------------- #
chat_area = Text(
    root,
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12),
    bd=0,
    padx=10,
    pady=10
)
chat_area.pack(padx=10, pady=10, fill=BOTH, expand=True)

chat_area.tag_config("user", foreground="#00ffd5")
chat_area.tag_config("bot", foreground="#ffcc00")

# ---------------- BOT FUNCTION ---------------- #
def chatbot_reply(user):

    jokes = [
        "😂 Teacher: Homework kahan hai? Student: Sir dog kha gaya.",
        "🤣 Mobile slow ho to usko bhi chai pila do.",
        "😅 Exams aur ex dono tension dete hain."
    ]

    quotes = [
        "🌟 Success comes from consistency.",
        "🚀 Never stop learning.",
        "💪 Believe in yourself."
    ]

    if "hello" in user or "hi" in user:
        return "Hello Faiza! 😊"

    elif "how are you" in user:
        return "Main bilkul theek hoon 😄"

    elif "name" in user:
        return "Mera naam SmartBot Pro hai 🤖"

    elif "time" in user:
        return "⏰ Current time: " + datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        return "📅 Today's date: " + datetime.now().strftime("%d-%m-%Y")

    elif "joke" in user:
        return random.choice(jokes)

    elif "quote" in user:
        return random.choice(quotes)

    elif "python" in user:
        return "🐍 Python ek powerful programming language hai."

    elif "ai" in user:
        return "🤖 AI ka matlab Artificial Intelligence hota hai."

    elif "bye" in user:
        return "Bye! Khyal rakhna ❤️"

    else:
        return "😅 Sorry, mujhe samajh nahi aaya."

# ---------------- SEND FUNCTION ---------------- #
def send_message():

    user_message = entry_box.get()

    if user_message == "":
        return

    # Show user message
    chat_area.insert(END, "🧑 You: " + user_message + "\n", "user")

    # Bot reply
    bot_reply = chatbot_reply(user_message.lower())

    chat_area.insert(END, "🤖 Bot: " + bot_reply + "\n\n", "bot")

    # Clear box
    entry_box.delete(0, END)

    # Auto scroll
    chat_area.see(END)

# ---------------- BOTTOM FRAME ---------------- #
bottom_frame = Frame(root, bg="#121212")
bottom_frame.pack(fill=X, padx=10, pady=10)

# ---------------- ENTRY BOX ---------------- #
entry_box = Entry(
    bottom_frame,
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    bd=0
)
entry_box.pack(side=LEFT, fill=X, expand=True, ipady=10, padx=(0,10))

# ---------------- SEND BUTTON ---------------- #
send_button = Button(
    bottom_frame,
    text="Send 🚀",
    font=("Arial", 12, "bold"),
    bg="#ff4b5c",
    fg="white",
    bd=0,
    padx=20,
    pady=5,
    command=send_message
)
send_button.pack(side=RIGHT)

# ---------------- WELCOME MESSAGE ---------------- #
chat_area.insert(
    END,
    "🤖 Welcome to SmartBot Pro!\n\n"
    "Try these:\n"
    "• hello\n"
    "• time\n"
    "• date\n"
    "• joke\n"
    "• quote\n"
    "• python\n"
    "• ai\n\n",
    "bot"
)

# ---------------- RUN ---------------- #
root.mainloop()