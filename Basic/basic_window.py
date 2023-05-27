# Importing flet
import flet as ft;

# Main function
def main(pg: ft.Page):

    # Adding a text to my page
    hello_world_txt = ft.Text(value="Hello World!!", color="red", size=50);

    # Adding to the window
    pg.controls.append(hello_world_txt);

    # Updating the page
    pg.update();

    # If we use page.add... we do not need to use the two last code lines
    other_text = ft.Text(value="Other Text", color="green");
    pg.add(other_text);

# To run the program
ft.app(target=main);