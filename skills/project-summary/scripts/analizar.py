import os
import sys
from collections import Counter

# Directorio a analizar (se pasa como argumento, o usa el actual)
directorio = sys.argv[1] if len(sys.argv) > 1 else "."

# Extensiones que nos interesan
extensiones = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
    ".html": "HTML", ".css": "CSS", ".md": "Markdown",
    ".json": "JSON", ".sh": "Shell", ".rb": "Ruby", ".go": "Go"
}

conteo_lenguajes = Counter()
total_archivos = 0
tiene_readme = False
tiene_gitignore = False

for raiz, dirs, archivos in os.walk(directorio):
    # Ignorar carpetas comunes de dependencias
    dirs[:] = [d for d in dirs if d not in [
        "node_modules", ".git", "__pycache__", ".venv", "dist", "build"
    ]]
    for archivo in archivos:
        total_archivos += 1
        if archivo.lower() == "readme.md":
            tiene_readme = True
        if archivo == ".gitignore":
            tiene_gitignore = True
        ext = os.path.splitext(archivo)[1].lower()
        if ext in extensiones:
            conteo_lenguajes[extensiones[ext]] += 1

print(f"📁 Total de archivos: {total_archivos}")
print(f"📖 README.md: {'✅ Sí' if tiene_readme else '❌ No'}")
print(f"🔒 .gitignore: {'✅ Sí' if tiene_gitignore else '❌ No'}")
print(f"\n🧑‍💻 Lenguajes detectados:")
if conteo_lenguajes:
    for lang, count in conteo_lenguajes.most_common():
        print(f"   {lang}: {count} archivo(s)")
else:
    print("   Ninguno detectado")