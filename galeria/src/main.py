import flet as ft

def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK45

    pinturas = [
        {
            "titulo": "Lobo solitario",
            "Autor": "Desconocido",
            "año": "2021",
            "Descripcion": "Un lobo solo sentado en las montañas",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/LOBO.jfif"
        },
        {
            "titulo": "Jaws",
            "Autor": "Roges Kastel",
            "año": "1975",
            "Descripcion": "Tiburon preparandose para atacar a una persona",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/images.jfif"
        },
        {
            "titulo": "Noche estrellada",
            "Autor": "Vincent van Gogh",
            "año": "1889",
            "Descripcion": " representa la vista desde la ventana orientada al este de su habitación de asilo",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/noche.jfif"
        },
        {
            "titulo": "Noli",
            "Autor": "Enoderen",
            "año": "2025",
            "Descripcion": "La cara de noli sujetando la estrella del vacio",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/NOLI.jfif"
        },
        {
            "titulo": "Artful",
            "Autor": "Die of Death dev team",
            "año": "2025",
            "Descripcion": "Un frances desatado de ira por todo el odio que recibio",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/artful.jfif"
        },
        {
            "titulo": "Forsaken",
            "Autor": "Enoderen",
            "año": "2025",
            "Descripcion": "Todos los supervivientes en este mundo creado por la entidad",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/FORASKEN.png"
        },
        {
            "titulo": "Forsaken - Supervivientes",
            "Autor": "Enoderen",
            "año": "2025",
            "Descripcion": "Los 10 supervivientes mostrando sus habilidades",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/FORASKEN%202.png"
        },
        {
            "titulo": "Forsaken - Noli ",
            "Autor": "Enoderen",
            "año": "2025",
            "Descripcion": "El asesino noli consumido por la estrella del vacio",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/FORSAKEN%203.png"
        },
        {
            "titulo": "Forsaken - C00lkid",
            "Autor": "Enoderen",
            "año": "2025",
            "Descripcion": "Los supervivientes siendo seguidos por c00lkid",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/FORSAKEN%204.png"
        },
        {
            "titulo": "Forsaken - Guest y Slasher",
            "Autor": "Enoderen",
            "año": "2025",
            "Descripcion": "El asesino Slasher y Guest observando a Jard",
            "imagen": "https://raw.githubusercontent.com/Qualier-lab/proyectobismestralprimerperiodo/refs/heads/main/FORSAKEN%205.png"
        }
    ]

    indice_actual=[0]

    contenedor = ft.Container(
        content=ft.Column([]),
        width=400,
        height=500,
        bgcolor=ft.Colors.PURPLE_400,
        alignment=ft.alignment.center,
        padding=20
    )

    boton_siguiente=ft.ElevatedButton(text="Siguente Pintura")

    def mostrar_pintura():
        pintura=pinturas[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=pintura["imagen"],width=300,height=300,fit=ft.ImageFit.CONTAIN),
            ft.Text(pintura["titulo"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Autor: {pintura["Autor"]}", size=16),
            ft.Text(f"año: {pintura['año']}",size=16),
            ft.Text(pintura["Descripcion"],size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)

        if indice_actual[0]==len(pinturas)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente pintura"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(pinturas)
        mostrar_pintura()
    boton_siguiente.on_click=siguiente_click



    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
              spacing=20
        ),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    mostrar_pintura()


ft.app(main)