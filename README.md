# YTExtractor

YTExtractor es una aplicación de escritorio creada con Python y Tkinter que permite descargar videos de YouTube de manera fácil y rápida. Solo necesitas ingresar la URL del video y la aplicación se encargará de descargarlo en el mejor formato disponible.



## Requisitos

Para poder ejecutar YTExtractor, necesitarás tener instalados los siguientes paquetes:

- [Python 3.x](https://www.python.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/download.html) (para evitar errores de audio)
- [Tkinter](https://wiki.python.org/moin/TkInter) (generalmente viene preinstalado con Python)



## Instalación

## Instalación

1. **Clona este repositorio**:
    ```sh
    git clone https://github.com/infrunnami/YTExtractor.git
    cd YTExtractor
    ```
2. **Instala las dependencias**:
    ```sh
    pip install yt-dlp
    ```

3. **Instala `ffmpeg`** (para evitar errores de audio):

   - **Windows**: Descárgalo desde [aquí](https://ffmpeg.org/download.html) y agrégalo al `PATH` del sistema.
   - **Linux (Debian/Ubuntu)**:
     ```sh
     sudo apt update && sudo apt install ffmpeg
     ```
   - **MacOS** (si usas Homebrew):
     ```sh
     brew install ffmpeg
     ```

4. **Verifica la instalación de `ffmpeg`** ejecutando:
    ```sh
    ffmpeg -version
    ```
   Si muestra información sobre `ffmpeg`, está instalado correctamente.