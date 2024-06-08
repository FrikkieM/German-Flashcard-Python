import pandas as pd
import tkinter as tk
from tkinter import font
import random

class FlashcardApp:
    def __init__(self, master, vocab_file):
        self.master = master
        self.master.title("German Flashcards - Normal Mode")

        # Load vocabulary from Excel file
        self.vocab_df = pd.read_excel(vocab_file)
        self.indices = list(self.vocab_df.index)

        # Initialize state
        self.current_index = 0
        self.showing_english = False
        self.random_mode = False

        # Setup fonts
        self.font_common = font.Font(family='Helvetica', size=24, weight='bold')

        # Create widgets
        self.card_label = tk.Label(master, text="", font=self.font_common, width=40, height=10, relief=tk.RAISED)
        self.card_label.pack(pady=20)

        self.status_bar = tk.Label(master, text="Left/Right: Next/Prev, Space: Flip, M: Mode, Esc: Quit", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Bind keys
        master.bind('<Left>', self.prev_card)
        master.bind('<Right>', self.next_card)
        master.bind('<space>', self.flip_card)
        master.bind('m', self.toggle_mode)
        master.bind('<Escape>', self.exit_app)

        # Display the first card
        self.display_card()

    def display_card(self):
        idx = self.indices[self.current_index]
        if self.showing_english:
            word = self.vocab_df.iloc[idx, 1]
            self.card_label.config(text=word, font=self.font_common, bg='lightcoral', fg='darkred')
        else:
            word = self.vocab_df.iloc[idx, 0]
            self.card_label.config(text=word, font=self.font_common, bg='lightgreen', fg='darkgreen')

    def prev_card(self, event):
        if self.current_index > 0:
            self.current_index -= 1
            self.showing_english = False
            self.display_card()

    def next_card(self, event):
        if self.current_index < len(self.indices) - 1:
            self.current_index += 1
            self.showing_english = False
            self.display_card()

    def flip_card(self, event):
        self.showing_english = not self.showing_english
        self.display_card()

    def toggle_mode(self, event):
        self.random_mode = not self.random_mode
        if self.random_mode:
            self.master.title("German Flashcards - Random Mode")
            random.shuffle(self.indices)
        else:
            self.master.title("German Flashcards - Normal Mode")
            self.indices = list(self.vocab_df.index)
        self.current_index = 0
        self.showing_english = False
        self.display_card()

    def exit_app(self, event):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root, 'vocabulary.xlsx')
    root.mainloop()
