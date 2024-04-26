import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Gráficos")
        self.setGeometry(100, 100, 600, 400)

        self.lbl_variable = QLabel("Variable:", self)
        self.lbl_variable.setGeometry(50, 50, 100, 30)

        self.txt_variable = QLineEdit(self)
        self.txt_variable.setGeometry(150, 50, 200, 30)

        self.lbl_datos = QLabel("Muestra (nombre: valor):", self)
        self.lbl_datos.setGeometry(50, 100, 200, 30)

        self.txt_datos = QTextEdit(self)
        self.txt_datos.setGeometry(50, 130, 500, 150)

        self.btn_generar_grafico_barras = QPushButton("Gráfico de Barras", self)
        self.btn_generar_grafico_barras.setGeometry(50, 300, 150, 30)
        self.btn_generar_grafico_barras.clicked.connect(self.generar_grafico_barras)

        self.btn_generar_grafico_circular = QPushButton("Gráfico Circular", self)
        self.btn_generar_grafico_circular.setGeometry(250, 300, 150, 30)
        self.btn_generar_grafico_circular.clicked.connect(self.generar_grafico_circular)

    def obtener_datos(self):
        variable = self.txt_variable.text()
        datos_linea = self.txt_datos.toPlainText().strip().split('\n')

        datos = {}
        for dato in datos_linea:
            partes = dato.split(':')
            if len(partes) != 2:
                QMessageBox.warning(self, "Advertencia", "Los datos deben estar en el formato 'nombre: valor'.")
                return None, None
            nombre = partes[0].strip()
            valor = partes[1].strip()
            datos[nombre] = float(valor)

        return variable, datos

    def generar_grafico_barras(self):
        variable, datos = self.obtener_datos()
        if datos is not None:
            plt.bar(datos.keys(), datos.values())
            plt.title(variable)
            plt.xlabel("Nombre")
            plt.ylabel("Valor")
            plt.xticks(rotation=0)
            plt.tight_layout()
            plt.show()

    def generar_grafico_circular(self):
        variable, datos = self.obtener_datos()
        if datos is not None:
            plt.pie(datos.values(), labels=datos.keys(), autopct='%1.1f%%')
            plt.title(variable)
            plt.axis('equal')
            plt.tight_layout()
            plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())