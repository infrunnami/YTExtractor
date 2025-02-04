# YTExtractor

YTExtractor es una aplicación de escritorio creada con Python y Tkinter que permite descargar videos de YouTube de manera fácil y rápida. Solo necesitas ingresar la URL del video y la aplicación se encargará de descargarlo en el mejor formato disponible.



## Requisitos

Para poder ejecutar YTExtractor, necesitarás tener instalados los siguientes paquetes:

- [Python 3.x](https://www.python.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Tkinter](https://wiki.python.org/moin/TkInter) (generalmente viene preinstalado con Python)



## Instalación

1. **Clona este repositorio**:


2. **Instala las dependencias**:
Si no tienes `yt-dlp` instalado, puedes instalarlo usando `pip`:
```bash
pip install yt-dlp

3. **Genera el ejecutable**:
Puedes hacerlo usando este comando en la consola: 
```bash
pyinstaller --onefile --windowed --icon=logardo.ico --name=YTExtractor --add-data "logardo.ico;." ventana.py