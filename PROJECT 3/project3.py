import tkinter as tk
from tkinter import ttk

def recommend():
    genre = genre_var.get()

    recommendations = {
        "Action": ["John Wick", "Mad Max", "Avengers Endgame"],
        "Comedy": ["The Mask", "Home Alone", "Mr. Bean"],
        "Horror": ["The Conjuring", "Insidious", "Annabelle"],
        "Science Fiction": ["Interstellar", "The Matrix", "Inception"]
    }

    result_text.delete("1.0", tk.END)

    if genre in recommendations:
        result_text.insert(tk.END, "Recommended Movies:\n\n")
        for movie in recommendations[genre]:
            result_text.insert(tk.END, f"• {movie}\n")
    else:
        result_text.insert(tk.END, "Please select a genre.")

# Main Window
root = tk.Tk()
root.title("AI Movie Recommendation System")
root.geometry("500x400")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="🎬 AI Movie Recommendation System",
    font=("Arial", 16, "bold")
)
title.pack(pady=15)

# Dropdown
tk.Label(root, text="Select Your Favorite Genre:",
         font=("Arial", 11)).pack()

genre_var = tk.StringVar()
genre_dropdown = ttk.Combobox(
    root,
    textvariable=genre_var,
    values=["Action", "Comedy", "Horror", "Science Fiction"],
    state="readonly"
)
genre_dropdown.pack(pady=10)

# Button
recommend_btn = tk.Button(
    root,
    text="Get Recommendations",
    command=recommend,
    font=("Arial", 11)
)
recommend_btn.pack(pady=10)

# Output Box
result_text = tk.Text(root, height=10, width=45)
result_text.pack(pady=15)

root.mainloop()