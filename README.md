| Status | Event |
|---|---|
| [![Code Testing](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml/badge.svg?event=schedule)](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml) | Weekly schedule |
| [![Code Testing](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml/badge.svg?event=pull_request)](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml) | Last PR |

Ansible Role: paperless_ngx
=========

Installs and configures paperless-ngx EDMS.

Requirements
------------
### Ansible

`ansible_version_minimum: "4.0.0"` or newer is required.

### Supported operating systems

* Debian (>=11)
* Ubuntu (>=focal)

Role Variables
--------------

Most configuration variables from paperless-ngx itself are available and accept their respective arguments.
Every `PAPERLESS_*` configuration variable is lowercased and instead prefixed with `paperless_ngx_conf_*` in `defaults/main.yml`.

For a full listing including explanations and allowed values, see the current [documentation](https://docs.paperless-ngx.com/configuration/).

The following sections are devided into:
* Role specific variables
* Original paperless-ngx configuration variables

### Role specific variables

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `paperless_ngx_db_type` | sqlite | Available db types are sqlite and postgresql. If postrgresql is chosen then the other db_ vars must be configured too. |
| `paperless_ngx_dir_force_permission_exclude` | [] | Which directories should be skipped from permission check/setting. See [docs](docs/DIRECTORY_PERMISSION_CHECK.md). |
| `paperless_ngx_dir_installation` | /opt/paperless-ngx | The directory where paperless-ngx static installation files are written to. |
| `paperless_ngx_dir_runtime_data` | /var/lib/paperless-ngx | The directory where the runtime data will be stored. |
| `paperless_ngx_dir_virtualenv` | "{{ paperless_ngx_dir_installation }}/.venv" | The directory for the needed python venv. |
| `paperless_ngx_jbig2enc_enabled` | true | Whether to install and use jbig2enc for OCRmyPDF. |
| `paperless_ngx_jbig2enc_lossy` | false | Run jbig2enc in lossy mode or not. |
| `paperless_ngx_jbig2enc_tmp_dir` | /tmp/ | Directory for temporary jbig2enc files |
| `paperless_ngx_jbig2enc_version` | 0.29 | Which version to install. |
| `paperless_ngx_redis_host` | localhost | Redis host |
| `paperless_ngx_redis_port` | 6379 | Redis port |
| `paperless_ngx_system_group` | paperlessngx | The group to which the system user belongs. |
| `paperless_ngx_system_user` | paperlessngx | The user that will execute the services and own the data. |
| `paperless_ngx_system_user_additional_groups` | [] | Optionally add the system user to more groups. For example to read TLS certificates that can be read by the group `ssl-cert`. |
| `paperless_ngx_version` | latest | Sofware version to install. Use `latest` or any specific version in the format `'1.10.0'`. Only `paperless_ngx_version_minimum: '1.10.0'` and higher supported. |
| `` |  |  |

### paperless-ngx configuration variables

All the upcoming vars correspond with the vars from [paperless-ngx docs](https://docs.paperless-ngx.com/configuration).
To save reading space a few abbreviations are used in the tables down below:
* I - Implemented in this role? [Y/N]
* O - Variable is meant to be overridden? [Y/N] If No it should not be altered.
* H - Hint
* V - Version of paperless-ngx that introduced this var. 

#### Required services

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_redis` | redis://{{ paperless_ngx_redis_host }}:{{ paperless_ngx_redis_port }} | Y | N |  |   |
| `paperless_ngx_conf_dbengine` | | Y | N | Not used by the role |   |
| `paperless_ngx_conf_dbhost` | localhost | Y | Y | |   |
| `paperless_ngx_conf_dbport` | 5432 | Y | Y | |   |
| `paperless_ngx_conf_dbname` | paperlessngx | Y | Y | |   |
| `paperless_ngx_conf_dbuser` | paperlessngx | Y | Y | |   |
| `paperless_ngx_conf_dbpass` | "" | Y | Y | The db password. If not defined by the user, a random password will be generated -> see section below about passwords. |   |
| `paperless_ngx_conf_dbsslmode` | prefer | Y | Y | |   |
| `paperless_ngx_conf_db_timeout` |  | Y | Y |   |   |

#### Path and folders

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_consumption_dir` | "{{ paperless_ngx_dir_runtime_data }}/consumption" | Y | Y |   |   |
| `paperless_ngx_conf_data_dir` | "{{ paperless_ngx_dir_runtime_data }}/data" | Y | Y |   |   |
| `paperless_ngx_conf_trash_dir` | "{{ paperless_ngx_dir_runtime_data }}/trash" | Y | Y |   |   |
| `paperless_ngx_conf_media_root` | "{{ paperless_ngx_dir_runtime_data }}/media" | Y | Y |   |   |
| `paperless_ngx_conf_staticdir` | ../static | Y | N |   |   |
| `paperless_ngx_conf_filename_format` | "" | Y | Y |   |   |
| `paperless_ngx_conf_filename_format_remove_none` | false | Y | Y |   |   |
| `paperless_ngx_conf_logging_dir` | "{{ paperless_ngx_dir_runtime_data }}/log" |   |   |   |   |
| `paperless_ngx_conf_nltk_dir` | /usr/share/nltk_data | Y | Y |   | 1.11 |

#### Logging

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_logrotate_max_size` | 1024 * 1024 | Y | Y |   |   |
| `paperless_ngx_conf_logrotate_max_backups` | 20 | Y | Y |   |   |

#### Hosting & Security

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_secret_key` | "" | Y | Y | If not defined by the user, a random password will be generated -> see section below about passwords. |   |
| `paperless_ngx_conf_url` | http://localhost:8000 | Y | Y |   |   |
| `paperless_ngx_conf_csrf_trusted_origins` |  | Y | Y |   |   |
| `paperless_ngx_conf_allowed_hosts` | "*" | Y | Y |   |   |
| `paperless_ngx_conf_cors_allowed_hosts` | http://localhost:8000 | Y | Y |   |   |
| `paperless_ngx_conf_force_script_name` | "" | Y | Y |   |   |
| `paperless_ngx_conf_static_url` | /static/ | Y | Y |   |   |
| `paperless_ngx_conf_auto_login_username` | "" | Y | Y |   |   |
| `paperless_ngx_conf_admin_user` | admin | Y | Y |   |   |
| `paperless_ngx_conf_admin_mail` | root@localhost | Y | Y |   |   |
| `paperless_ngx_conf_admin_password` |  | Y | Y | The superuser password. If not defined by the user, a random password will be generated -> see section below about passwords. |   |
| `paperless_ngx_conf_cookie_prefix` | "" | Y | Y |   |   |
| `paperless_ngx_conf_enable_http_remote_user` | "" | Y | Y |   |   |
| `paperless_ngx_conf_http_remote_user_header_name` | HTTP_REMOTE_USER | Y | Y |   |   |
| `paperless_ngx_conf_logout_redirect_url` |  | Y | Y |   |   |

#### OCR settings

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_ocr_language` | eng | Y | Y |   |   |
| `paperless_ngx_conf_ocr_mode` | skip | Y | Y |   |   |
| `paperless_ngx_conf_ocr_clean` | clean | Y | Y |   |   |
| `paperless_ngx_conf_ocr_deskew` | true | Y | Y |   |   |
| `paperless_ngx_conf_ocr_rotate_pages` | true | Y | Y |   |   |
| `paperless_ngx_conf_ocr_rotate_pages_threshold` | 12 | Y | Y |   |   |
| `paperless_ngx_conf_ocr_output_type` | pdfa | Y | Y |   |   |
| `paperless_ngx_conf_ocr_pages` | 0 | Y | Y |   |   |
| `paperless_ngx_conf_ocr_image_dpi` | "" | Y | Y |   |   |
| `paperless_ngx_conf_ocr_max_image_pixels` | | Y | Y |   |   |
| `paperless_ngx_conf_ocr_user_args` | [optimize=1] | Y | Y |   |   |

#### Tika settings

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_tika_enabled` | false | Y | Y |   |   |
| `paperless_ngx_conf_tika_endpoint` | http://localhost:9998 | Y | Y |   |   |
| `paperless_ngx_conf_tika_gotenberg_endpoint` | http://localhost:3000 | Y | Y |   |   |

#### Software tweaks

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_task_workers` | 1 | Y | Y |   |   |
| `paperless_ngx_conf_threads_per_worker` | paperless_ngx_conf_task_workers | Y | Y |  |   |
| `paperless_ngx_conf_worker_timeout` | 1800 | Y | Y |   |   |
| `paperless_ngx_conf_time_zone` | Europe/London | Y | Y |   |   |
| `paperless_ngx_conf_enable_nltk` | 1 | Y | Y |   | 1.11 |
| `paperless_ngx_conf_email_task_cron` | "*/10 * * * *" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_train_task_cron` | "5 */1 * * *" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_index_task_cron` | "0 0 * * *" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_sanity_task_cron` | "30 0 * * sun" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_enable_compression` | true | Y | Y |   | 1.13 |

#### Polling

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_consumer_polling` | 0 | Y | Y |   |   |
| `paperless_ngx_conf_consumer_polling_retry_count` | 5 | Y | Y |   |   |
| `paperless_ngx_conf_consumer_polling_delay` | 5 | Y | Y |   |   |

#### iNotify

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_consumer_inotify_delay` | 0.5 | Y | Y |   |   |
| `paperless_ngx_conf_consumer_delete_duplicates` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_recursive` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_subdirs_as_tags` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_enable_barcodes` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_barcode_tiff_support` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_barcode_string` | 'PATCHT' | Y | Y |   |   |
| `paperless_ngx_conf_consumer_enable_asn_barcode` | false | Y | Y |   | 1.12 |
| `paperless_ngx_conf_consumer_asn_barcode_prefix` | ASN | Y | Y |   | 1.12 |
| `paperless_ngx_conf_convert_memory_limit` | 0 | Y | Y |   |   |
| `paperless_ngx_conf_convert_tmpdir` | "" | Y | Y |   |   |
| `paperless_ngx_conf_post_consume_script` | "" | Y | Y |   |   |
| `paperless_ngx_conf_filename_date_order` | "" | Y | Y |   |   |
| `paperless_ngx_conf_number_of_suggested_dates` | 3 | Y | Y |   |   |
| `paperless_ngx_conf_thumbnail_font_name` | /usr/share/fonts/liberation/LiberationSerif-Regular.ttf | Y | Y |   |   |
| `paperless_ngx_conf_ignore_dates` | "" | Y | Y |   |   |
| `paperless_ngx_conf_date_order` | "DMY" | Y | Y |   |   |
| `paperless_ngx_conf_consumer_ignore_patterns` | [".DS_STORE/*", "._*", ".stfolder/*", ".stversions/*", ".localized/*", "desktop.ini"] | Y | Y |   |   |

#### Binaries

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_convert_binary` | convert | Y | Y |   |   |
| `paperless_ngx_conf_gs_binary` | gs | Y | Y |   |   |

#### Docker specicif options

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_webserver_workers` | 1 | Y | Y |   |   |
| `paperless_ngx_conf_bind_addr` | "[::]" | Y | Y |   |   |
| `paperless_ngx_conf_port` | 8000 | Y | Y |   |   |
| `paperless_ngx_conf_usermap_uid` |  | Y | Y | System users id |   |
| `paperless_ngx_conf_usermap_gid` |  | Y | Y | System users gid |   |
| `paperless_ngx_conf_ocr_languages` | [eng,deu,fra,ita,spa] | Y | Y |   |   |
| `paperless_ngx_conf_enable_flower` | false | Y | Y | Whether to start flower or not. See [using flower](docs/USING_FLOWER.md) for more information | 1.10 |

#### Update Checking

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_enable_update_check` |  | Y | Y | Will be removed in the future |   |

### Usage advice

#### Generated password

The role uses Ansible's password lookup:

-   If a password is generated by the role, ansible stores it **locally** in **pngx_instances/{{ incentory_hostname }}/** (relative to the working directory)
-   if the file already exist, it reuse its content
-   see [the ansible password lookup documentation](https://docs.ansible.com/ansible/latest/plugins/lookup/password.html) for more info


#### Separation of static (~ installation) and dynamic (~ runtime) data

This role checks that you do not set one of the data dirs (like consumption etc.) as a subdirectory of the installation path. For making my life easier this role deletes the installation folder and creates a complete new one when upgrading. This is fresh and clean. Also this way you are kept from unwanted deletions of your data during upgrades.

Dependencies
------------

There is a dependency on `jmespath`. This is included as part of the community.general collection within ansible. Please follow this link for more information - https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#selecting-json-data-json-queries

Example Playbooks
----------------

`minimal_runnable_playbook.yml`:

```
- hosts: all
    roles:
        - { role: paperless_ngx.paperless_ngx }
    vars:
        var1:
        var2:
        ...
```

Contributing
-------

We encourage you to contribute to this role! Please check out the
[contributing guide](CONTRIBUTE.md) for guidelines about how to proceed.

License
-------

MIT
