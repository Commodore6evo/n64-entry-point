# n64-entry-point

Este script de Python extrae el punto de entrada (entry point) de un archivo ROM de Nintendo 64 (.n64 o .z64 recomendado).

## Uso

1.  **Requisitos:**
    * Python 3 instalado.

2.  **Ejecución:**
    * Guarda el script como `entrypoint.py`.
    * Abre una terminal o símbolo del sistema.
    * Ejecuta el script proporcionando la ruta al archivo ROM como argumento:

        ```bash
        python entrypoint.py <ruta_del_archivo_rom>
        ```

        Ejemplo:

        ```bash
        python entrypoint.py zelda.z64
        ```

3.  **Salida:**
    * El script imprimirá el punto de entrada en formato hexadecimal.
    * Si el archivo no se encuentra o si ocurre un error, se mostrará un mensaje de error.
