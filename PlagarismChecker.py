import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from Levenshtein import distance as levenshtein_distance

class PlagiarismCheckerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Plagiarism Checker")

        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TButton", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0")
        style.configure("TEntry", background="#ffffff")

        self.frame = ttk.Frame(self.master)
        self.frame.pack(padx=20, pady=20)

        self.label_file1 = ttk.Label(self.frame, text="Select File 1:")
        self.label_file1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.selected_file1 = tk.StringVar()
        self.entry_file1 = ttk.Entry(self.frame, textvariable=self.selected_file1, state="readonly")
        self.entry_file1.grid(row=0, column=1, padx=5, pady=5)

        self.button_file1 = ttk.Button(self.frame, text="Browse", command=self.browse_file1)
        self.button_file1.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.label_file2 = ttk.Label(self.frame, text="Select File 2:")
        self.label_file2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.selected_file2 = tk.StringVar()
        self.entry_file2 = ttk.Entry(self.frame, textvariable=self.selected_file2, state="readonly")
        self.entry_file2.grid(row=1, column=1, padx=5, pady=5)

        self.button_file2 = ttk.Button(self.frame, text="Browse", command=self.browse_file2)
        self.button_file2.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.check_button = ttk.Button(self.frame, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def browse_file1(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.selected_file1.set(file_path)

    def browse_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.selected_file2.set(file_path)

    def check_plagiarism(self):
        file1 = self.selected_file1.get()
        file2 = self.selected_file2.get()

        if not file1 or not file2:
            messagebox.showerror("Error", "Please select both files.")
            return

        try:
            with open(file1, "r", encoding="utf-8") as file:
                text1 = file.read().strip()
            with open(file2, "r", encoding="utf-8") as file:
                text2 = file.read().strip()
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
            return

        distance = levenshtein_distance(text1, text2)
        max_length = max(len(text1), len(text2))
        similarity = 1 - (distance / max_length)
        plagiarism_percentage = similarity * 100

        messagebox.showinfo("Plagiarism Result", f"Plagiarism detected!\nSimilarity: {plagiarism_percentage:.2f}%")

def main():
    root = tk.Tk()
    app = PlagiarismCheckerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
