from app.ui import main_ui
from PySide6 import QtWidgets
import sys
import web
import qdarktheme
from app.ui.core.proxy_style import ProxyStyle
import threading

urls = ("/", "Index")

class Index:
    def GET(self):
        return "Hello, Web!"

# Function to start the PySide6 GUI
def start_gui():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(ProxyStyle())
    with open("/content/VisoMaster/app/ui/styles/dark_styles.qss", "r") as f:
        _style = f.read()
        _style = qdarktheme.load_stylesheet(custom_colors={"primary": "#4facc9"}) + '\n' + _style
        app.setStyleSheet(_style)
    window = main_ui.MainWindow()
    window.show()
    app.exec()

# Function to start the web application
def start_web():
    app = web.application(urls, globals())
    app.run()

if __name__ == "__main__":
    # Start the GUI in a separate thread
    gui_thread = threading.Thread(target=start_gui)
    gui_thread.start()

    # Start the web application
    start_web()
