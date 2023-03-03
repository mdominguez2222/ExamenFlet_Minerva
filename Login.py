import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"

    
    #Ejercicio 6
    def comprobarDatos(e):
        if tfnombre.value == tfpassword.value:
            t = ft.Text("Contraseña correcta")
            page.add(t)
        else:
            t2 = ft.Text("Contraseña incorrecta")
            page.add(t2)


    #Fin --- Ejercicio 6


    #Ejercicio 2
    imagen = ft.Image(src="fotos/Logo.png")
    
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250



    tfnombre = ft.TextField(label="Nombre")
    #Ejercicio 4

    tfpassword = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    

    #Fin --- Ejercicio 4


    #Ejercicio 5

    btnEntrar = ft.ElevatedButton(text="Entrar",icon=ft.icons.ACCESSIBILITY_NEW, on_click=comprobarDatos)

    #Fin-- Ejercicio 5


    page.add(imagen,tfnombre,tfpassword,btnEntrar)


ft.app(target=main,assets_dir="fotos")