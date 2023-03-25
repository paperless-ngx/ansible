# PostgreSQL example installation for Paperless-ngx

Here is an example playbook that uses `galaxyproject.postgresql` to build up a ready to use PostgreSQL instance

```yaml
- name: Install psycopg2
  become: yes
  apt:
    name: "python{{ (ansible_python.version.major == 3) | ternary('3', '') }}-psycopg2"

- name: Install postgresql
  include_role:
    name: galaxyproject.postgresql
    apply:
      become: yes
  vars:
    postgresql_flavor: pgdg
    postgresql_version: 15
    postgresql_conf:
      - port: "{{ paperless_ngx_conf_dbport }}"
      - listen_addresses: "'{{ paperless_ngx_conf_dbhost }}'"

- name: Create postgresql user and db
  include_role:
    name: galaxyproject.postgresql_objects
    apply:
      become: yes
      become_user: postgres
  vars:
    postgresql_objects_users:
      - name: "{{ paperless_ngx_conf_dbuser }}"
        password: "{{ paperless_ngx_conf_dbpass }}"
    postgresql_objects_databases:
      - name: "{{ paperless_ngx_conf_dbname }}"
        owner: "{{ paperless_ngx_conf_dbuser }}"
```