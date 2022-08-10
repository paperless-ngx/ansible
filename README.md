Ansible Role: paperless-ngx
===========================

Installs and configures paperless-ngx EDMS on Debian/Ubuntu systems.

Requirements
------------

No special system requirements. Ansible 2.7 or newer is required.

Note that this role requires root access, so either run it in a playbook with a global `become: yes`, or invoke the role in your playbook like:
```
- hosts: all
  roles:
  - role: paperless-ngx
    become: yes
```
Role Variables
---

Most configuration variables from paperless-ngx itself are available and accept their respective arguments.
Every `PAPERLESS_*` configuration variable is lowercased and instead prefixed with `paperlessng_*` in `defaults/main.yml`.

For a full listing including explanations and allowed values, see the current [documentation](https://paperless-ngx.readthedocs.io/en/latest/configuration.html).



Additional variables available in this role are listed below, along with default values:
```paperlessng_version: latest```

The [release](https://github.com/paperless-ngx/paperless-ngx/releases) archive version of paperless-ngx to install. `latest` stands for the latest release of paperless-ngx.

To install a specific version of paperless-ngx, use the tag name of the release, e. g. `v1.8.0`

| Additional Variables           | Required/Optional | Example Value                       | Description                                                                      |
|--------------------------------|-------------------|-------------------------------------|----------------------------------------------------------------------------------|
| paperlessng_version            | Required          | v1.8.0                              | Version to install                                                               |
| paperlessng_redis_host         | Required          | localhost                           | Separate configuration values that combine into PAPERLESS_REDIS.                 |
| paperlessng_redis_port         | Required          | 6379                                | Separate configuration values that combine into PAPERLESS_REDIS.                 |
| paperlessng_db_type            | Required          | sqlite                              | Database to use. Default is file-based SQLite..                                  |
| paperlessng_db_host            | Optional          | localhost                           | Database configuration **(only applicable if paperlessng_db_type == 'postgresql').** |
| paperlessng_db_port            | Optional          | 5432                                | Database configuration **(only applicable if paperlessng_db_type == 'postgresql').** . |
| paperlessng_db_name            | Optional          | paperlessng                         | Database configuration **(only applicable if paperlessng_db_type == 'postgresql').**  |
| paperlessng_db_user            | Optional          | paperlessng                         | Database configuration **(only applicable if paperlessng_db_type == 'postgresql').**  |
| paperlessng_db_pass            | Optional          | paperlessng                         | Database configuration **(only applicable if paperlessng_db_type == 'postgresql').**  |
| paperlessng_db_sslmode         | Optional          | prefer                              | Database configuration **(only applicable if paperlessng_db_type == 'postgresql').**  |
| paperlessng_directory          | Required          | /opt/paperless-ngx                  | Root directory paperless-ngx is installed into.                                  |
| paperlessng_virtualenv         | Required          | "{{ paperlessng_directory }}/.venv" | Directory used for the virtual environment for paperless-ngx                     |
| paperlessng_ocr_languages      | Required          | eng                                 | List of OCR languages to install and configure (`apt search tesseract-ocr-*`).   |
| paperlessng_use_jbig2enc       | Optional          | True                                | Whether to install and use jbig2enc for OCRmyPDF                                 |
| paperlessng_big2enc_lossy      | Optional          | False                               | Whether to use jbig2enc's lossy compression mode                                 |
| paperlessng_superuser_name     | Required          | paperlessng                         | Credentials of the initial superuser in paperless-ngx.                           |
| paperlessng_superuser_email    | Required          | paperlessng@example.com             | Credentials of the initial superuser in paperless-ngx.                           |
| paperlessng_superuser_password | Required          | paperlessng                         | Credentials of the initial superuser in paperless-ngx.                           |
| paperlessng_system_user        | Required          | paperlessng                         | System user to run the paperless-ngx services as (will be created if required).  |
| paperlessng_system_group       | Required          | paperlessng                         | System group to run the paperless-ngx services as (will be created if required). |
| paperlessng_listen_address     | Required          | 127.0.0.1                           | Address for the paperless-ngx service to listen on.                              |
| paperlessng_listen_port        | Required          | 8000                                | Port for the paperless-ngx service to listen on.                                 |

Dependencies
------------

No ansible dependencies.

Example Playbook
----------------

`playbook.yml`:

```
- hosts: all
    become: yes
    roles:
        - { role: ansible-paperless-ngx,  tags: ["paperless"] }
    vars:
        paperlessng_version: v1.8.0
        paperlessng_install_method: precompiledrelease
        paperlessng_use_jbig2enc: true
        paperlessng_secret_key: mxsupersecurekeyforhashing
        paperlessng_data_dir: "/paperlessdata/data"
        paperlessng_trash_dir: "/paperlessdata/trash"
        paperlessng_consumption_dir: "/paperlessdata/consumption"
        paperlessng_media_root: "/paperlessdata/media"
        paperlessng_ocr_languages:
        - deu
        - eng
        paperlessng_ocr_mode: skip
        paperlessng_time_zone: Europe/Berlin
        paperlessng_consumer_recursive: true
        paperlessng_superuser_name: superuser
        paperlessng_superuser_email: mymail@mydomain.local
        paperlessng_superuser_password: supersecurepasswordchangeme
        paperlessng_listen_address: 0.0.0.0
        paperlessng_listen_port: 8000
```
