import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class DataAnalyticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analytics and Visualization Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#2B2B2B")  
        self.data = None
        self.selected_columns = []
        self.setup_ui()
    def setup_ui(self):
        self.load_button = tk.Button(self.root, text="Load CSV", command=self.load_file, bg="#FF5733", fg="white")
        self.load_button.pack(pady=10)
        style = ttk.Style()
        style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333")
        style.map('Treeview', background=[('selected', '#FF5733')])
        self.tree = ttk.Treeview(self.root, style="Treeview")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.analytics_frame = tk.Frame(self.root, bg="#2B2B2B")
        self.analytics_frame.pack(pady=10)
        self.analysis_button = tk.Button(self.analytics_frame, text="Perform Analysis", command=self.perform_analysis, bg="#007ACC", fg="white")
        self.analysis_button.pack(side=tk.LEFT, padx=5)
        self.plot_button = tk.Button(self.analytics_frame, text="Plot Data", command=self.plot_data, bg="#007ACC", fg="white")
        self.plot_button.pack(side=tk.LEFT, padx=5)
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Mosquito.csv", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            self.display_data()
    def display_data(self):
        if self.data is not None:
            self.tree.delete(*self.tree.get_children())
            self.tree["column"] = list(self.data.columns)
            self.tree["show"] = "headings"
            for col in self.tree["column"]:
                self.tree.heading(col, text=col)
            df_rows = self.data.to_numpy().tolist()
            for row in df_rows:
                self.tree.insert("", "end", values=row)
    def perform_analysis(self):
        if self.data is not None:
            mean_value = self.data.mean()
            median_value = self.data.median()
            std_deviation = self.data.std()
            analysis_results = f"Mean:\n{mean_value}\n\nMedian:\n{median_value}\n\nStandard Deviation:\n{std_deviation}"
            self.show_message(analysis_results)
    def plot_data(self):
        if self.data is not None:
            self.selected_columns = list(self.data.columns)
            fig, ax = plt.subplots(figsize=(6, 4))
            self.data[self.selected_columns].plot(kind='line', ax=ax, color="#FF5733")
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    def show_message(self, message):
        top = tk.Toplevel(self.root)
        top.title("Analysis Results")
        top.configure(bg="#2B2B2B")
        msg = tk.Message(top, text=message, bg="#2B2B2B", fg="white")
        msg.pack(padx=10, pady=10)
        button = tk.Button(top, text="Close", command=top.destroy, bg="#FF5733", fg="white")
        button.pack(pady=5)
if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyticsApp(root)
    root.mainloop()
