
import sys

var = None
version = 'TBD'
default_code = 'TBD'
default_doc = 'TBD'

# First argument is the DOC var "PAPERLESS_..."
if len(sys.argv) > 0:
    var = sys.argv[1]
# sedond argument is the default value for the code (see https://github.com/paperless-ngx/paperless-ngx/blob/47b4a602a72609c7f9ecee4401d782af3148c860/src/paperless/settings.py)
if len(sys.argv) > 1:
    default_doc = sys.argv[2]
# third argument is the version since the var is available (2.x)
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