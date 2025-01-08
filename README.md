# ThemeCraft

ThemeCraft is a Python-based application that allows users to create and apply custom visual themes on Windows to personalize their desktop environment. Customize your wallpaper and accent colors with ease!

## Features

- **Create Custom Themes**: Define your own themes with specific wallpapers and accent colors.
- **Apply Themes**: Instantly apply themes to change your desktop environment.
- **List Available Themes**: View all the themes you have created.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/themecraft.git
    cd themecraft
    ```

2. **Install dependencies**:
    Ensure you have Python installed on your machine. This script does not require any third-party packages.

## Usage

1. **Create a Theme**:
    You can create a new theme by specifying a name and settings.
    ```python
    theme_craft.create_theme("ThemeName", {"wallpaper": "path_to_wallpaper", "accent_color": "color_code"})
    ```

2. **Apply a Theme**:
    Apply a previously created theme.
    ```python
    theme_craft.apply_theme("ThemeName")
    ```

3. **List Themes**:
    Display all available themes.
    ```python
    theme_craft.list_themes()
    ```

## Example

Here's a quick example of how you can use ThemeCraft:

```python
theme_craft = ThemeCraft()
theme_craft.create_theme("OceanBlue", {"wallpaper": "C:\\path\\to\\ocean.jpg", "accent_color": "#1E90FF"})
theme_craft.list_themes()
theme_craft.apply_theme("OceanBlue")
```

## Note

- Ensure that the wallpaper path is valid and the image file exists.
- Accent color change is simulated in this script for demonstration purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.