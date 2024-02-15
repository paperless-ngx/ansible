
import sys

var = None
version = 'TBD'
default_code = 'TBD'
default_doc = 'TBD'

if len(sys.argv) > 0:
    var = sys.argv[1]
if len(sys.argv) > 1:
    default_doc = sys.argv[2]
if len(sys.argv) > 2:
    version = sys.argv[3]

if default_doc == 'None':
    default_code = ''
else:
    default_code = default_doc

def transform_var(var) -> str:
    if var.startswith("PAPERLESS_"):
        var = var[10:]  # Cut off "PAPERLESS_" from the beginning
        var = var.lower()  # Transform the rest of the string to lowercase
        var = "paperless_ngx_conf_" + var  # Prefix with "paperless_ngx_conf_"
    return var

if var is None:
    print("No var given")
    sys.exit(0)

docs_var = var
conf_var = transform_var(var)

print(f"{conf_var}: {default_code}")
print(f"| `{conf_var}` | {default_doc} | Y | Y |   | {version} |")
print(f"    - pngx_var: {docs_var}\n"
      f"      role_var: \"{{{{ {conf_var} }}}}\"\n"
      f"      since_version: '{version}.0'"
      )