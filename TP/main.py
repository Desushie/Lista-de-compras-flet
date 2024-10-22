import flet as ft

def main(page):
    # Lista que almacenará las filas añadidas (que contienen el texto y botones)
    nombres_list = []
    page.title="App de Lista"

    # Función para agregar o actualizar el nombre
    def agregar_nombre(e):
        if nombre.value.strip() != "":
            if nombre.data is None:  # Si no está en modo de edición
                nuevo_texto = ft.Text(
                    value=nombre.value,
                    size=30,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD
                )

                # Crear la fila y capturar la referencia
                def crear_fila(texto):
                    nueva_fila = ft.Row([
                        texto,
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Editar",
                            on_click=lambda e: editar_nombre(texto)
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            tooltip="Eliminar",
                            on_click=lambda e: eliminar_nombre(nueva_fila)
                        )
                    ], alignment="center")  # Centrar los elementos en la fila
                    return nueva_fila

                nueva_fila = crear_fila(nuevo_texto)  # Crear la fila

                nombres_list.append(nueva_fila)
                page.add(nueva_fila)
            else:
                # Editar el texto existente
                nombre.data.value = nombre.value
                nombre.data.update()
                nombre.data = None  # Limpiar la referencia de edición

            nombre.value = ""
            nombre.focus()
            nombre.update()

    # Función para editar un nombre
    def editar_nombre(texto):
        nombre.value = texto.value
        nombre.focus()
        nombre.update()
        nombre.data = texto  # Guardamos la referencia del texto a editar

    # Función para eliminar una fila completa (texto + botones)
    def eliminar_nombre(fila):
        nombres_list.remove(fila)
        page.controls.remove(fila)
        page.update()

    # Configuración de la página
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window.width = 600
    page.window.height = 400

    # Elementos del encabezado
    logo = ft.Image(src="./logo.png", width=200, height=200, fit=ft.ImageFit.CONTAIN)
    header_text = ft.Text("Bienvenidos a la App de Lista", size=20, weight=ft.FontWeight.BOLD)

    # Columna con la imagen y el texto de encabezado centrado
    header = ft.Column(
        [logo, header_text],
        alignment="center",    # Centrar elementos dentro de la columna
        horizontal_alignment="center"  # Asegurar que la imagen y el texto estén centrados horizontalmente
    )

    # Campo de texto para ingresar el nombre
    nombre = ft.TextField(keyboard_type=ft.KeyboardType.TEXT, hint_text="Escribe algo", width=200)

    # Agregar elementos a la página
    page.add(
        header,  # Agregar el encabezado centrado
        ft.Divider(height=20),
        ft.Row(
            [nombre, ft.ElevatedButton("Agregar", on_click=agregar_nombre)],
            alignment="center"  # Centrar el campo de texto y botón
        )
    )

ft.app(main)
