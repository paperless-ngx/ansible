# Doc generation for vars

Call 

`python3 maintenance/vars/transform_var.py <PAPERLESS_VAR> <default value from setttings.py> <version when introduced>`
`python3 maintenance/vars/transform_var.py PAPERLESS_MODEL_FILE PAPERLESS_DATA_DIR/classification_model.pickle 2.9`

Result

```
paperless_ngx_conf_model_file: PAPERLESS_DATA_DIR/classification_model.pickle # <-- vars default
| `paperless_ngx_conf_model_file` | PAPERLESS_DATA_DIR/classification_model.pickle | Y | Y |   | 2.9 | <--- readme
    - pngx_var: PAPERLESS_MODEL_FILE # <-- conf yml
      role_var: "{{ paperless_ngx_conf_model_file }}"
      since_version: '2.9.0'
```

Call

`python3 maintenance/vars/check_vars.py --version 2.11.0`

Result

Shows differences between local vars in different files and the online documentation.