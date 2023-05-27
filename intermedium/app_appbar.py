import flet as ft;

def main(page: ft.Page):
    
    # defaults
    page.window_width = 400;
    page.window_height = 400;
    page.appbar = ft.AppBar(
        title= ft.Text("Appbar"),
        bgcolor= ft.colors.BLUE_ACCENT_200
    )

    # adding
    page.add(
        ft.Text("Hola")
    );


ft.app(target=main)