import json
import urllib.request
import urllib.parse
import os
import webbrowser

# URL del espejo JSON actualizado de la base de datos GHDB (Exploit-DB)
GHDB_URL = "https://raw.githubusercontent.com/0xBEAF/GHDB-in-json/master/ghdb.json"
DB_FILE = "ghdb.json"

def descargar_db():
    """Descarga la base de datos si no existe localmente."""
    if os.path.exists(DB_FILE):
        return True
    print("[*] Descargando la base de datos de Google Hacking (GHDB)...")
    try:
        req = urllib.request.Request(GHDB_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(DB_FILE, 'wb') as out_file:
            out_file.write(response.read())
        print("[+] Base de datos descargada y guardada localmente.")
        return True
    except Exception as e:
        print(f"[!] Error al descargar: {e}")
        return False

def cargar_db():
    """Carga los dorks en memoria."""
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("=" * 55)
    print("    GENERADOR DE GOOGLE DORKS by:lokipwn - Versión 1.0")
    print("=" * 55)
    
    if not descargar_db():
        print("No se pudo obtener la base de datos. Saliendo...")
        return
        
    db = cargar_db()
    print(f"[+] Base de datos cargada: {len(db)} dorks disponibles.\n")
    print("Nota: La 'Categoria 8' de Exploit-DB corresponde a 'Error Messages'.")
    print("Puedes buscarla usando la palabra clave 'error' en la opción 1.")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar dorks por palabra clave (cpanel, login, pdf, sql...)")
        print("2. Generar dork personalizado (Generador automático)")
        print("3. Salir")
        
        op = input("\nSelecciona una opción (1/2/3): ").strip()
        
        if op == '1':
            keyword = input("Introduce palabra clave (ej: 'cpanel' o 'ext:log'): ").strip()
            if not keyword: continue
            
            print(f"\nBuscando '{keyword}' en la base de datos...")
            matches = []
            kw_lower = keyword.lower()
            
            # Filtramos buscando en el dork, descripción corta y descripción larga
            for item in db:
                if kw_lower in item.get('request', '').lower() or \
                   kw_lower in item.get('short description', '').lower() or \
                   kw_lower in item.get('long description', '').lower():
                    matches.append(item)
            
            if not matches:
                print("[-] No se encontraron coincidencias para esa palabra.")
                continue
                
            print(f"[+] Se encontraron {len(matches)} coincidencias. Mostrando las primeras 20:")
            for i, m in enumerate(matches[:20]):
                print(f"  [{i+1}] {m.get('request')}")
                print(f"      * {m.get('short description')}")
                
            if len(matches) > 20:
                print(f"  ... y {len(matches) - 20} resultados más.")
                
            try:
                sel = int(input("\nNúmero del dork para abrir en Google (0 para volver): "))
                if 1 <= sel <= len(matches[:20]):
                    dork = matches[sel-1].get('request')
                    url = f"https://www.google.com/search?q={urllib.parse.quote(dork)}"
                    print(f"[+] Abriendo en navegador: {url}")
                    webbrowser.open(url)
            except ValueError:
                print("[-] Entrada inválida.")
                
        elif op == '2':
            print("\n--- GENERADOR DE DORKS PERSONALIZADO ---")
            dominio = input("Dominio objetivo (ej: example.com) [Enter para omitir]: ").strip()
            extension = input("Extensión/Tipo (ej: pdf, sql, log, env) [Enter para omitir]: ").strip()
            palabra = input("Palabra en título o URL (ej: admin, login) [Enter para omitir]: ").strip()
            
            dork_parts = []
            if dominio: dork_parts.append(f"site:{dominio}")
            if extension: dork_parts.append(f"filetype:{extension}")
            if palabra: dork_parts.append(f"intitle:{palabra} OR inurl:{palabra}")
            
            if not dork_parts:
                print("[-] Debes rellenar al menos un campo para generar el dork.")
                continue
                
            dork_final = " ".join(dork_parts)
            url = f"https://www.google.com/search?q={urllib.parse.quote(dork_final)}"
            print(f"\n[+] Dork generado: {dork_final}")
            
            if input("¿Abrir en el navegador? (s/n): ").strip().lower() == 's':
                webbrowser.open(url)
                
        elif op == '3':
            print("[*] ¡Regresa pronto!")
            break
        else:
            print("[-] Opción no válida.")

if __name__ == "__main__":
    main()