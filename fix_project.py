import os
import re

# Carpeta raíz del proyecto
root_folder = "python_forestacion"

# Patrón para detectar imports dentro de TYPE_CHECKING
pattern_type_checking_import = re.compile(r'^\s*from (.+) import (.+)\s*$', re.MULTILINE)

# Recorremos todos los archivos .py
for subdir, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(subdir, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if "TYPE_CHECKING" in content:
                # Extraemos los imports dentro del bloque TYPE_CHECKING
                matches = re.findall(r'if TYPE_CHECKING:\s*(.*?)\n\s*\n', content, re.DOTALL)
                imports_to_add = []
                for match in matches:
                    lines = match.splitlines()
                    for line in lines:
                        line = line.strip()
                        if line.startswith("from "):
                            imports_to_add.append(line)

                # Si hay imports a agregar
                if imports_to_add:
                    # Verificar que no estén ya fuera del TYPE_CHECKING
                    for imp in imports_to_add:
                        if imp not in content.split("if TYPE_CHECKING")[0]:
                            # Agregamos el import normal al inicio del archivo
                            content = imp + "\n" + content
                            print(f"Import agregado en {filepath}: {imp}")

                    # Guardar cambios
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
