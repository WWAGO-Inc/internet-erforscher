import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

def display_html_file(filename):
    app = QApplication(sys.argv)
    window = QMainWindow()
    web_view = QWebEngineView()
    window.setCentralWidget(web_view)

    # Load the HTML file
    with open(filename, 'r') as file:
        html_content = file.read()
        web_view.setHtml(html_content)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    html_file = "index.html"  # Change this to the desired HTML file name
    display_html_file(html_file)
