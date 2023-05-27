import flet as ft;

def main(page: ft.Page):

    # Window Config    
    page.window_title_bar_hidden = True;
    page.window_title_bar_buttons_hidden = True;
    page.padding = 0;
    page.theme = ft.Theme(
        color_scheme_seed= ft.colors.TEAL
    )  

    # Page AppBar
    page.appbar = ft.AppBar(
        title=ft.WindowDragArea(ft.Text("Dashboard")),
        bgcolor=ft.colors.PRIMARY_CONTAINER,
        actions=[
            ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
        ]
    )  

    # Page Add2
    page.add(
        ft.Row(
            [
                ft.Container(
                    expand=1,
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    content= ft.Column(
                        [
                            ft.TextButton(
                                text="Home",
                                icon=ft.icons.HOME,
                                width=500,
                                style=ft.ButtonStyle(
                                    shape={
                                        "": ft.RoundedRectangleBorder(radius=3)
                                    },
                                    
                                )
                            ),
                            ft.TextButton(
                                text="Settings", 
                                icon=ft.icons.SETTINGS,
                                width=500,
                                style=ft.ButtonStyle(
                                    shape={
                                        "": ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    margin=0
                ),
                ft.Container(
                    expand=4,
                    content=ft.Column(
                        [
                            ft.Text(
                                value="Main Screen",
                                size=40,
                                color=ft.colors.PRIMARY,
                                weight="bold"
                            ),
                            ft.Text(
                                value="Here is the main screen, and a brief description."
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    margin=0
                )
            ],
            expand=3,
        )
    )

ft.app(target=main);