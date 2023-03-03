import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"
    tfnombre="Hola"
    tfcontraseña="1234"
    #Ejercicio 6
    def comprobar(e):
        if tfnombre.value==tfnombre:
            print("usuario correcto")
        elif tfcontraseña.value==tfcontraseña:
            print("Contraseña Correcta")

    page.update()    
    #Fin --- Ejercicio 6


    #Ejercicio 2
    
    img = ft.Image(src=f"Logo.png")
        
   #Fin --- Ejercicio 2

    #Ejercicio 3
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250
    tfnombre = ft.TextField(label="Nombre")
    #Ejercicio 4
    tfcontraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)

    #Fin --- Ejercicio 4


    #Ejercicio 5
    btnEntrar= ft.ElevatedButton(text="Entrar",icon="chair_outlined",on_click=comprobar)
    
    #Fin-- Ejercicio 5


    page.add(img,tfnombre,tfcontraseña,btnEntrar)
    


ft.app(target=main,assets_dir="fotos")