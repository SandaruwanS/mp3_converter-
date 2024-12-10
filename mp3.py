import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from pydub import AudioSegment # type: ignore
import os

# Create the main window
root = tk.Tk()
root.title("MP3 Converter")
root.geometry("500x400")  # Adjust window size as needed
root.config(bg="#f0f0f0")

# Add Web-style Frame
frame = tk.Frame(root, bg="#ffffff", bd=2)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("All Media Files", "*.*"), ("Audio Files", "*.wav *.mp3 *.flac *.aac")])
    if file_path:
        input_file.set(file_path)

# Function to handle saving location selection
def select_save_location():
    folder_path = filedialog.askdirectory()
    if folder_path:
        save_location.set(folder_path)

# Function to handle the conversion and update the progress bar
def convert_to_mp3():
    input_path = input_file.get()
    output_folder = save_location.get()
    
    if not input_path or not output_folder:
        messagebox.showerror("Error", "Please select both input file and save location.")
        return
    
    # Update progress bar to 0% initially
    progress_bar['value'] = 0
    root.update_idletasks()
    
    try:
        # Load media file
        audio = AudioSegment.from_file(input_path)
        
        # Define output path
        output_path = os.path.join(output_folder, os.path.basename(input_path).split('.')[0] + ".mp3")
        
        # Convert to MP3
        audio.export(output_path, format="mp3")
        
        # Update progress bar to 100% when finished
        progress_bar['value'] = 100
        root.update_idletasks()
        
        messagebox.showinfo("Success", f"File converted successfully!\nSaved to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Input File Selection
input_file = tk.StringVar()
input_file_label = tk.Label(frame, text="Select Media File:", bg="#ffffff", font=("Arial", 12))
input_file_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_file_button = ttk.Button(frame, text="Browse", command=select_file)
input_file_button.grid(row=0, column=1, padx=10, pady=5)

# Save Location Selection
save_location = tk.StringVar()
save_location_label = tk.Label(frame, text="Select Save Location:", bg="#ffffff", font=("Arial", 12))
save_location_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
save_location_button = ttk.Button(frame, text="Browse", command=select_save_location)
save_location_button.grid(row=1, column=1, padx=10, pady=5)

# Progress Bar
progress_bar_label = tk.Label(frame, text="Conversion Progress:", bg="#ffffff", font=("Arial", 12))
progress_bar_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
progress_bar = ttk.Progressbar(frame, length=300, mode="determinate")
progress_bar.grid(row=2, column=1, padx=10, pady=5)

# Convert Button (Ribbon Style Button)
convert_button = ttk.Button(frame, text="Convert to MP3", command=convert_to_mp3, style="Accent.TButton")
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

# Define Style for Ribbon Button
style = ttk.Style()
style.configure("Accent.TButton", background="#4CAF50", foreground="white", font=("Arial", 14, "bold"))
style.map("Accent.TButton", background=[("active", "#45a049")])

# Start the main loop
root.mainloop()
