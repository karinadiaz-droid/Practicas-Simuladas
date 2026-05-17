# ==========================================
#    MANEJO DE LOGS (Módulo de Registro)
# ==========================================

from datetime import datetime

class Logger:
    @staticmethod
    def registrar_evento(mensaje: str):
        """Escribe errores y eventos en un archivo físico sin detener el programa."""
        try:
            with open("log.txt", "a", encoding="utf-8") as archivo:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo.write(f"[{timestamp}] {mensaje}\n")
        except IOError:
            print("Error crítico del sistema: No se pudo escribir en el archivo de log.")
