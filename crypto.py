import customtkinter as ctk
from tkinter import filedialog, messagebox
from Crypto.Cipher import DES, AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
import os
class hager_Cryptotool(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hager_Crypto Tool")
        self.geometry("900x700")
        # Add a label above the window
        self.title_label = ctk.CTkLabel(self, text="Welcome to Hager Crypto Tool", font=("Arial", 24, "bold"))
        self.title_label.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

        self.tabview = ctk.CTkTabview(self, width=1000, height=600)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        # Add main categories for encryption techniques
        self.symmetric_tab = self.tabview.add("Symmetric Encryption")
        self.asymmetric_tab = self.tabview.add("Asymmetric Encryption")
        self.hash_tab = self.tabview.add("Hashing")
        self.signature_tab = self.tabview.add("Digital Signature")
        self.blind_tab = self.tabview.add("Blind Signature")
        self.build_symmetric_tab()
        self.build_asymmetric_tab()
        self.build_hash_tab()
        self.build_signature_tab()
        self.build_blind_tab()
        self.configure_grid()
    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
    def build_symmetric_tab(self):
        self.symmetric_algorithms = ctk.CTkOptionMenu(self.symmetric_tab, values=["AES", "DES"], width=180)
        self.symmetric_algorithms.grid(row=0, column=0, pady=10, padx=10, sticky="ew")
        self.symmetric_key = ctk.CTkEntry(self.symmetric_tab, placeholder_text="Enter Key (e.g., 16 bytes for AES)", height=40, width=400)
        self.symmetric_key.grid(row=1, column=0, pady=10, sticky="ew", padx=10)
        self.symmetric_input = ctk.CTkTextbox(self.symmetric_tab, height=150, width=400, corner_radius=8)
        self.symmetric_input.grid(row=2, column=0, columnspan=2, pady=15, sticky="ew", padx=10)
        self.symmetric_mode = ctk.CTkOptionMenu(self.symmetric_tab, values=["Encrypt", "Decrypt"], width=180)
        self.symmetric_mode.grid(row=3, column=0, pady=10, padx=10, sticky="ew")
        self.symmetric_button = ctk.CTkButton(self.symmetric_tab, text="Process", command=self.process_symmetric, width=200)
        self.symmetric_button.grid(row=3, column=1, pady=10, padx=10)
        self.symmetric_output = ctk.CTkTextbox(self.symmetric_tab, height=150, width=400, corner_radius=8)
        self.symmetric_output.grid(row=4, column=0, columnspan=2, pady=15, sticky="ew", padx=10)
        self.symmetric_load_button = ctk.CTkButton(self.symmetric_tab, text="Load File", command=self.load_symmetric_input, width=200)
        self.symmetric_load_button.grid(row=5, column=0, pady=10, padx=10)
        self.symmetric_save_button = ctk.CTkButton(self.symmetric_tab, text="Save Output", command=self.save_symmetric_output, width=200)
        self.symmetric_save_button.grid(row=5, column=1, pady=10, padx=10)
    def process_symmetric(self):
        algorithm = self.symmetric_algorithms.get()
        input_text = self.symmetric_input.get("1.0", "end-1c").encode()
        key = self.symmetric_key.get().encode()
        if algorithm == "AES":
            if len(key) not in [16, 24, 32]:
                messagebox.showerror("Error", "AES Key must be 16, 24, or 32 bytes.")
                return
            cipher = AES.new(key, AES.MODE_ECB)
        elif algorithm == "DES":
            if len(key) != 8:
                messagebox.showerror("Error", "DES Key must be 8 bytes.")
                return
            cipher = DES.new(key, DES.MODE_ECB)

        if self.symmetric_mode.get() == "Encrypt":
            padded_input = pad(input_text, cipher.block_size)
            encrypted_text = cipher.encrypt(padded_input)
            self.symmetric_output.delete("1.0", "end")
            self.symmetric_output.insert("1.0", encrypted_text.hex())

        elif self.symmetric_mode.get() == "Decrypt":
            try:
                encrypted_bytes = bytes.fromhex(input_text.decode())
                decrypted_text = cipher.decrypt(encrypted_bytes)
                decrypted_text = unpad(decrypted_text, cipher.block_size).decode().strip()
                self.symmetric_output.delete("1.0", "end")
                self.symmetric_output.insert("1.0", decrypted_text)
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def load_symmetric_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.symmetric_input.delete("1.0", "end")
                self.symmetric_input.insert("1.0", content)

    def save_symmetric_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.symmetric_output.get("1.0", "end-1c")
                file.write(content)

    def build_asymmetric_tab(self):
        self.asymmetric_algorithms = ctk.CTkOptionMenu(self.asymmetric_tab, values=["RSA"], width=180)
        self.asymmetric_algorithms.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.asymmetric_key = ctk.CTkEntry(self.asymmetric_tab, placeholder_text="Enter Key Size (e.g., 2048 for RSA)", height=40, width=400)
        self.asymmetric_key.grid(row=1, column=0, pady=10, sticky="ew", padx=10)

        self.asymmetric_input = ctk.CTkTextbox(self.asymmetric_tab, height=150, width=400, corner_radius=8)
        self.asymmetric_input.grid(row=2, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        self.asymmetric_mode = ctk.CTkOptionMenu(self.asymmetric_tab, values=["Encrypt", "Decrypt"], width=180)
        self.asymmetric_mode.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        self.asymmetric_button = ctk.CTkButton(self.asymmetric_tab, text="Process", command=self.process_asymmetric, width=200)
        self.asymmetric_button.grid(row=3, column=1, pady=10, padx=10)

        self.asymmetric_output = ctk.CTkTextbox(self.asymmetric_tab, height=150, width=400, corner_radius=8)
        self.asymmetric_output.grid(row=4, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        # Add file input and output buttons
        self.asymmetric_load_button = ctk.CTkButton(self.asymmetric_tab, text="Load File", command=self.load_asymmetric_input, width=200)
        self.asymmetric_load_button.grid(row=5, column=0, pady=10, padx=10)

        self.asymmetric_save_button = ctk.CTkButton(self.asymmetric_tab, text="Save Output", command=self.save_asymmetric_output, width=200)
        self.asymmetric_save_button.grid(row=5, column=1, pady=10, padx=10)

    def process_asymmetric(self):
        algorithm = self.asymmetric_algorithms.get()
        input_text = self.asymmetric_input.get("1.0", "end-1c").encode()
        key_size = int(self.asymmetric_key.get())

        if algorithm == "RSA":
            key = RSA.generate(key_size)
            public_key = key.publickey()

            cipher = public_key.encrypt(input_text, 32) if self.asymmetric_mode.get() == "Encrypt" else key.decrypt(input_text)

            self.asymmetric_output.delete("1.0", "end")
            self.asymmetric_output.insert("1.0", cipher)

    def load_asymmetric_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.asymmetric_input.delete("1.0", "end")
                self.asymmetric_input.insert("1.0", content)

    def save_asymmetric_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.asymmetric_output.get("1.0", "end-1c")
                file.write(content)

    def build_hash_tab(self):
        self.hash_algorithms = ctk.CTkOptionMenu(self.hash_tab, values=["SHA-256", "MD5"], width=180)
        self.hash_algorithms.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.hash_input = ctk.CTkTextbox(self.hash_tab, height=150, width=400, corner_radius=8)
        self.hash_input.grid(row=1, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        self.hash_button = ctk.CTkButton(self.hash_tab, text="Hash", command=self.process_hash, width=200)
        self.hash_button.grid(row=2, column=0, columnspan=2, pady=15, padx=10)

        self.hash_output = ctk.CTkTextbox(self.hash_tab, height=150, width=400, corner_radius=8)
        self.hash_output.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        # Add file input and output buttons
        self.hash_load_button = ctk.CTkButton(self.hash_tab, text="Load File", command=self.load_hash_input, width=200)
        self.hash_load_button.grid(row=4, column=0, pady=10, padx=10)

        self.hash_save_button = ctk.CTkButton(self.hash_tab, text="Save Output", command=self.save_hash_output, width=200)
        self.hash_save_button.grid(row=4, column=1, pady=10, padx=10)

    def process_hash(self):
        algorithm = self.hash_algorithms.get()
        input_text = self.hash_input.get("1.0", "end-1c").encode()

        if algorithm == "SHA-256":
            hash_object = hashlib.sha256(input_text)
        elif algorithm == "MD5":
            hash_object = hashlib.md5(input_text)

        self.hash_output.delete("1.0", "end")
        self.hash_output.insert("1.0", hash_object.hexdigest())

    def load_hash_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.hash_input.delete("1.0", "end")
                self.hash_input.insert("1.0", content)

    def save_hash_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.hash_output.get("1.0", "end-1c")
                file.write(content)
                
    def build_signature_tab(self):
        self.signature_algorithms = ctk.CTkOptionMenu(self.signature_tab, values=["RSA"], width=180)
        self.signature_algorithms.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.signature_input = ctk.CTkTextbox(self.signature_tab, height=150, width=400, corner_radius=8)
        self.signature_input.grid(row=1, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        self.signature_button = ctk.CTkButton(self.signature_tab, text="Sign", command=self.process_signature, width=200)
        self.signature_button.grid(row=2, column=0, columnspan=2, pady=15, padx=10)

        self.signature_output = ctk.CTkTextbox(self.signature_tab, height=150, width=400, corner_radius=8)
        self.signature_output.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        # Add file input and output buttons
        self.signature_load_button = ctk.CTkButton(self.signature_tab, text="Load File", command=self.load_signature_input, width=200)
        self.signature_load_button.grid(row=4, column=0, pady=10, padx=10)

        self.signature_save_button = ctk.CTkButton(self.signature_tab, text="Save Output", command=self.save_signature_output, width=200)
        self.signature_save_button.grid(row=4, column=1, pady=10, padx=10)

    def process_signature(self):
        input_text = self.signature_input.get("1.0", "end-1c").encode()
        key = RSA.generate(2048)

        private_key = key.export_key()
        signature = key.sign(input_text, 32)

        self.signature_output.delete("1.0", "end")
        self.signature_output.insert("1.0", signature)

    def load_signature_input(self): 
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.signature_input.delete("1.0", "end")
                self.signature_input.insert("1.0", content)

    def save_signature_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.signature_output.get("1.0", "end-1c")
                file.write(content)

    def build_blind_tab(self):
        self.blind_algorithms = ctk.CTkOptionMenu(self.blind_tab, values=["RSA"], width=180)
        self.blind_algorithms.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.blind_input = ctk.CTkTextbox(self.blind_tab, height=150, width=400, corner_radius=8)
        self.blind_input.grid(row=1, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        self.blind_button = ctk.CTkButton(self.blind_tab, text="Blind & Sign", command=self.process_blind_signature, width=200)
        self.blind_button.grid(row=2, column=0, columnspan=2, pady=15, padx=10)

        self.blind_output = ctk.CTkTextbox(self.blind_tab, height=150, width=400, corner_radius=8)
        self.blind_output.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew", padx=10)

        # Add file input and output buttons
        self.blind_load_button = ctk.CTkButton(self.blind_tab, text="Load File", command=self.load_blind_input, width=200)
        self.blind_load_button.grid(row=4, column=0, pady=10, padx=10)

        self.blind_save_button = ctk.CTkButton(self.blind_tab, text="Save Output", command=self.save_blind_output, width=200)
        self.blind_save_button.grid(row=4, column=1, pady=10, padx=10)

    def process_blind_signature(self):
        input_text = self.blind_input.get("1.0", "end-1c").encode()

        # Simulate blind signature here
        private_key = RSA.generate(2048)
        signature = private_key.sign(input_text, 32)

        self.blind_output.delete("1.0", "end")
        self.blind_output.insert("1.0", signature)

    def load_blind_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.blind_input.delete("1.0", "end")
                self.blind_input.insert("1.0", content)

    def save_blind_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.blind_output.get("1.0", "end-1c")
                file.write(content)


if __name__ == "__main__":
    app = hager_Cryptotool()
    app.mainloop()
