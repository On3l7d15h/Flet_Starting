import flet as ft;

# main function
def main(page: ft.Page):
    
    # Components
    page.window_height = 500;
    page.window_width = 450;

    # Declaring
    input_task = ft.TextField(hint_text="Escribe un valor");

    # functions
    def add_new_task(e):
        if input_task.value != "":
            page.add(ft.Checkbox(label=input_task.value))
            input_task.value = "";
            page.update();
    
    page.add(
        ft.Row(
            [
                input_task,
                ft.ElevatedButton(text="Añadir", on_click=add_new_task)
            ]
        )
    );


ft.app(target=main)