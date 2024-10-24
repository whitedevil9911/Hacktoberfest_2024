import tkinter as tk
from tkinter import ttk, messagebox
import requests
import webbrowser
from datetime import datetime
import customtkinter as ctk
from PIL import Image, ImageTk
from io import BytesIO

class GitHubProfileFinder:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()
        self.window.title("GitHub Profile Finder")
        self.window.geometry("800x600")
        self.window.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self.window)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="GitHub Profile Finder",
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=20)

        self.search_frame = ctk.CTkFrame(self.main_frame)
        self.search_frame.pack(pady=10, padx=20, fill="x")

        self.username_entry = ctk.CTkEntry(
            self.search_frame,
            placeholder_text="Enter GitHub Username",
            width=300,
            height=40
        )
        self.username_entry.pack(side="left", padx=(0, 10))

        self.search_button = ctk.CTkButton(
            self.search_frame,
            text="Search",
            command=self.search_profile,
            width=100,
            height=40
        )
        self.search_button.pack(side="left")

        self.result_frame = ctk.CTkFrame(self.main_frame)
        self.result_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.profile_image_label = ctk.CTkLabel(self.result_frame, text="")
        self.profile_image_label.pack(pady=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.result_frame, height=300)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10)

        self.info_labels = {}

        self.footer_label = ctk.CTkLabel(
            self.main_frame,
            text="Made with ❤️ by hari7261",
            font=("Helvetica", 10)
        )
        self.footer_label.pack(side="bottom", pady=10)

    def create_clickable_link(self, text, url):
        link = ctk.CTkButton(
            self.scrollable_frame,
            text=text,
            command=lambda u=url: webbrowser.open(u),
            fg_color="transparent",
            text_color=("#0366d6", "#58a6ff"),
            hover_color=("#e1e4e8", "#30363d")
        )
        return link

    def load_profile_image(self, image_url):
        try:
            response = requests.get(image_url)
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((150, 150))
            img = ImageTk.PhotoImage(img_data)
            self.profile_image_label.configure(image=img)
            self.profile_image_label.image = img
        except Exception as e:
            print(f"Error loading profile image: {e}")

    def clear_results(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.profile_image_label.configure(image="")

    def format_date(self, date_string):
        try:
            date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
            return date_obj.strftime("%B %d, %Y")
        except:
            return date_string

    def search_profile(self):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showwarning("Warning", "Please enter a username")
            return

        self.clear_results()
        
        try:
            response = requests.get(f"https://api.github.com/users/{username}")
            
            if response.status_code == 200:
                user_data = response.json()
                
                if user_data.get('avatar_url'):
                    self.load_profile_image(user_data['avatar_url'])

                info_items = [
                    ("Name", user_data.get('name', 'Not available')),
                    ("Bio", user_data.get('bio', 'Not available')),
                    ("Location", user_data.get('location', 'Not available')),
                    ("Public Repos", str(user_data.get('public_repos', 0))),
                    ("Followers", str(user_data.get('followers', 0))),
                    ("Following", str(user_data.get('following', 0))),
                    ("Joined", self.format_date(user_data.get('created_at', 'Not available')))
                ]

                for label, value in info_items:
                    container = ctk.CTkFrame(self.scrollable_frame)
                    container.pack(fill="x", pady=5, padx=5)
                    
                    label_widget = ctk.CTkLabel(
                        container,
                        text=f"{label}:",
                        font=("Helvetica", 12, "bold")
                    )
                    label_widget.pack(side="left", padx=5)
                    
                    value_widget = ctk.CTkLabel(
                        container,
                        text=value,
                        font=("Helvetica", 12)
                    )
                    value_widget.pack(side="left", padx=5)

                profile_link = self.create_clickable_link(
                    "Visit GitHub Profile",
                    user_data.get('html_url', '')
                )
                profile_link.pack(pady=10)

            elif response.status_code == 404:
                error_label = ctk.CTkLabel(
                    self.scrollable_frame,
                    text=f"User '{username}' not found",
                    text_color="red"
                )
                error_label.pack(pady=10)
            else:
                error_label = ctk.CTkLabel(
                    self.scrollable_frame,
                    text=f"Error: Status code {response.status_code}",
                    text_color="red"
                )
                error_label.pack(pady=10)

        except requests.exceptions.RequestException as e:
            error_label = ctk.CTkLabel(
                self.scrollable_frame,
                text=f"Error: {str(e)}",
                text_color="red"
            )
            error_label.pack(pady=10)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GitHubProfileFinder()
    app.run()
