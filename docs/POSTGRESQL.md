# PostgreSQL example installation for Paperless-ngx

Here is an example playbook that uses `galaxyproject.postgresql` to build up a ready to use PostgreSQL instance

```yaml
- name: Install PostgreSQL
  ansible.builtin.apt:
    name:
      - postgresql
      - python3-psycopg2
    state: present
    update_cache: true

- name: Create PostgreSQL role
  community.postgresql.postgresql_user:
    name: "{{ paperless_ngx_conf_dbuser }}"
    password: "{{ paperless_ngx_conf_dbpass }}"
  become: true
  become_user: "postgres"

- name: Create PostgreSQL database
  community.postgresql.postgresql_db:
    name: "{{ paperless_ngx_conf_dbname }}"
    owner: "{{ paperless_ngx_conf_dbuser }}"
    encoding: UTF8
    lc_collate: en_US.UTF-8
    lc_ctype: en_US.UTF-8
    template: template0
  become: true
  become_user: "postgres"
```