import os
import json
from ctypes import windll

class ThemeCraft:
    def __init__(self):
        self.theme_directory = os.path.join(os.getcwd(), "themes")
        if not os.path.exists(self.theme_directory):
            os.makedirs(self.theme_directory)
        self.current_theme = None

    def create_theme(self, name, settings):
        theme_path = os.path.join(self.theme_directory, f"{name}.json")
        with open(theme_path, "w") as theme_file:
            json.dump(settings, theme_file)
        print(f"Theme '{name}' created successfully.")

    def apply_theme(self, name):
        theme_path = os.path.join(self.theme_directory, f"{name}.json")
        if not os.path.exists(theme_path):
            print(f"Theme '{name}' does not exist.")
            return

        with open(theme_path, "r") as theme_file:
            settings = json.load(theme_file)

        self.set_wallpaper(settings.get("wallpaper", ""))
        self.set_accent_color(settings.get("accent_color", ""))
        self.current_theme = name
        print(f"Theme '{name}' applied successfully.")

    def set_wallpaper(self, wallpaper_path):
        if os.path.exists(wallpaper_path):
            windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)
            print(f"Wallpaper set to '{wallpaper_path}'.")
        else:
            print(f"Wallpaper path '{wallpaper_path}' does not exist.")

    def set_accent_color(self, color):
        # Simulated method for changing accent color
        print(f"Accent color set to '{color}'.")

    def list_themes(self):
        themes = [f.replace('.json', '') for f in os.listdir(self.theme_directory) if f.endswith('.json')]
        print("Available themes:")
        for theme in themes:
            print(f"- {theme}")

if __name__ == "__main__":
    theme_craft = ThemeCraft()
    theme_craft.create_theme("OceanBlue", {"wallpaper": "C:\\path\\to\\ocean.jpg", "accent_color": "#1E90FF"})
    theme_craft.list_themes()
    theme_craft.apply_theme("OceanBlue")