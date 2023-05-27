import flet as ft;

def main(page: ft.Page):

    # page configuration
    page.window_width = 400;
    page.window_height = 300;
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Counter | Flet"

    # functions
    def add_method(e):
        number_field.value = str(int(number_field.value) + 1);
        page.update();
    
    def quit_method(e):
        number_field.value = str(int(number_field.value) - 1);
        page.update();

    # vars
    title = ft.Text(value="Counter", size=30, text_align=ft.TextAlign.CENTER, width=400);
    add_btn = ft.IconButton(ft.icons.ADD, on_click=add_method);
    quit_btn = ft.IconButton(ft.icons.REMOVE, on_click=quit_method);
    number_field = ft.TextField(value = 0, width=200);

    # adding to the page.
    page.add(
        ft.Column(
            [
                title,
                ft.Row(
                    [
                        add_btn,
                        number_field,
                        quit_btn
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    );

ft.app(target=main);