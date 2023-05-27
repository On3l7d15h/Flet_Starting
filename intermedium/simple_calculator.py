import flet as ft;

def main(page: ft.Page):
    
    def perform(e):

        if(field_num1.value == ""):
            return;

        if(field_num2.value == ""):
            return;

        if(select_simbol.options == ""):
            return;


        field_result.value = eval(f"{field_num1.value} {select_simbol.value} {field_num2.value}");
        page.update();

    # Page options
    page.window_height = 300;
    page.window_width = 1315;
    page.vertical_alignment = ft.MainAxisAlignment.CENTER;
    page.appbar = ft.AppBar(
        title=ft.Text("Calculator"),
        bgcolor=ft.colors.PRIMARY,
        actions = [
            ft.ElevatedButton(icon=ft.icons.SETTINGS, text="Settings")
        ]
    );
    page.theme = ft.Theme(
       color_scheme_seed = ft.colors.AMBER
    )

    # declaring vars
    field_num1 = ft.TextField(hint_text="Write number #1");
    field_num2 = ft.TextField(hint_text="Write number #2");
    field_result = ft.TextField(value=0, disabled=True);
    btn_perform = ft.IconButton(icon=ft.icons.SEND, on_click=perform);
    select_simbol = ft.Dropdown(
        value="Select #1",
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/")
        ]
    )

    # Adding to the page:
    page.add(
        ft.Row(
            [
                field_num1,
                select_simbol,
                field_num2, 
                btn_perform,
                field_result
            ],
        )
    );

ft.app(target=main)