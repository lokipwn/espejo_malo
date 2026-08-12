# 🛡️ espejo_malo

**Versión:** 1.0.0  
**Autor:** lokipwn  
**Lenguaje:** Python 3  

## 📖 Descripción
Herramienta de línea de comandos (CLI) escrita en Python diseñada para facilitar la creación, búsqueda y gestión de **Google Dorks**. El script consume y almacena localmente la base de datos de **Google Hacking Database (GHDB)** de Exploit-DB, permitiendo a auditores de seguridad, pentesters e investigadores OSINT encontrar rápidamente vectores de búsqueda avanzados.

## ✨ Características
- 🔍 **Búsqueda en GHDB:** Filtra entre miles de dorks existentes usando palabras clave (ej. `cpanel`, `login`, `error`, `sql`, `pdf`, etc.).
- 🛠️ **Generador de Dorks Automático:** Crea dorks personalizados desde cero basados en tu objetivo (Dominio, tipo de archivo, palabras en el título/URL).
- 🌐 **Apertura directa:** Abre los dorks seleccionados directamente en tu navegador web predeterminado para ejecutar la búsqueda al instante.
- 🚀 **Cero Dependencias:** Utiliza únicamente librerías nativas de Python (`urllib`, `json`, `webbrowser`), por lo que no requiere instalación previa con `pip`.
- 💾 **Caché Local:** Descarga la base de datos una sola vez y la almacena en `ghdb.json` para futuras consultas rápidas sin conexión.

## ⚙️ Instalación y Uso

1. Clona o descarga este repositorio.
2. Asegúrate de tener instalado Python 3.x en tu sistema.
3. Ejecuta el script desde tu terminal:

```bash
python dork_generator.py


⚠️ AVISO LEGAL Y DESCARGO DE RESPONSABILIDAD (DISCLAIMER)
IMPORTANTE: Este software ha sido creado por lokipwn con fines estrictamente educativos, de investigación (OSINT) y auditoría de ciberseguridad autorizada.
El uso de Google Dorks para descubrir información sensible, vulnerabilidades o datos expuestos en sistemas ajenos sin el consentimiento explícito y por escrito del propietario es ilegal y puede violar las leyes de ciberdelincuencia locales e internacionales, así como los Términos de Servicio de Google.
El autor (lokipwn) se deslinda total y absolutamente de cualquier responsabilidad, daño, consecuencia legal o repercusión derivada del uso indebido, malintencionado o ilegal que terceros puedan dar a esta herramienta y a los comandos generados por ella.
Al descargar, compilar o ejecutar este código, aceptas que eres el único responsable de garantizar que tienes la autorización legal necesaria para interactuar con cualquier sistema, red o dominio que decidas auditar. Úsala de manera ética y responsable.
