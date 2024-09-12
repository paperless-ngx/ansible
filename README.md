| Status | Event |
|---|---|
| [![Code Testing](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml/badge.svg?event=schedule)](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml) | Weekly schedule |
| [![Code Testing](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml/badge.svg?event=pull_request)](https://github.com/paperless-ngx/ansible/actions/workflows/code_testing.yml) | Last PR |


# Ansible Role: paperless_ngx

Installs and configures paperless-ngx EDMS.

<!-- vscode-markdown-toc -->
* 1. [Requirements](#Requirements)
	* 1.1. [Ansible](#Ansible)
	* 1.2. [Supported operating systems](#Supportedoperatingsystems)
* 2. [Role Variables](#RoleVariables)
	* 2.1. [Role specific variables](#Rolespecificvariables)
	* 2.2. [Paperless-ngx configuration variables](#Paperless-ngxconfigurationvariables)
* 3. [Usage advices](#Usageadvices)
	* 3.1. [Updating Paperless-ngx](#UpdatingPaperless-ngx)
	* 3.2. [Backup/Restore](#BackupRestore)
	* 3.3. [Generated password](#Generatedpassword)
	* 3.4. [Separation of static (~ installation) and dynamic (~ runtime) data](#Separationofstaticinstallationanddynamicruntimedata)
	* 3.5. [PostgreSQL usage](#PostgreSQLusage)
* 4. [Dependencies](#Dependencies)
* 5. [Example Playbooks](#ExamplePlaybooks)
* 6. [Contributing](#Contributing)
* 7. [License](#License)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='Requirements'></a>Requirements

###  1.1. <a name='Ansible'></a>Ansible

`ansible_version_minimum: "2.15"` or newer is required.

The following Ansible collections need to be installed (via `ansible-galaxy collection install`)
* community.general
* ansible.posix

###  1.2. <a name='Supportedoperatingsystems'></a>Supported operating systems

* Debian (>=11)
* Ubuntu (>=focal)

##  2. <a name='RoleVariables'></a>Role Variables

Most configuration variables from paperless-ngx itself are available and accept their respective arguments.
Every `PAPERLESS_*` configuration variable is lowercased and instead prefixed with `paperless_ngx_conf_*` in `defaults/main.yml`.

For a full listing including explanations and allowed values, see the current [documentation](https://docs.paperless-ngx.com/configuration/).

The following sections are devided into:
* Role specific variables
* Original paperless-ngx configuration variables

###  2.1. <a name='Rolespecificvariables'></a>Role specific variables

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `paperless_ngx_db_type` | sqlite | Available db types are sqlite and postgresql. If postgresql is chosen then the other db_ vars must be configured too. |
| `paperless_ngx_dependency_install_tmp_dir` | /tmp/ | Directory for temporary dependency installation files |
| `paperless_ngx_dir_force_permission_exclude` | [] | Which directories should be skipped from permission check/setting. See [docs](docs/DIRECTORY_PERMISSION_CHECK.md). |
| `paperless_ngx_dir_installation` | /opt/paperless-ngx | The directory where paperless-ngx static installation files are written to. |
| `paperless_ngx_dir_python` | /opt/python/{{ paperless_ngx_python_version_short }} | The directory where python binaries are compiled to. |
| `paperless_ngx_dir_runtime_data` | /var/lib/paperless-ngx | The directory where the runtime data will be stored. |
| `paperless_ngx_dir_virtualenv` | "{{ paperless_ngx_dir_installation }}/.venv" | The directory for the needed python venv. |
| `paperless_ngx_jbig2enc_enabled` | true | Whether to install and use jbig2enc for OCRmyPDF. |
| `paperless_ngx_jbig2enc_lossy` | false | Run jbig2enc in lossy mode or not. |
| `paperless_ngx_jbig2enc_version` | 0.29 | Which version to install. |
| `paperless_ngx_redis_host` | localhost | Redis host |
| `paperless_ngx_redis_port` | 6379 | Redis port |
| `paperless_ngx_system_group` | paperlessngx | The group to which the system user belongs. |
| `paperless_ngx_system_user` | paperlessngx | The user that will execute the services and own the data. |
| `paperless_ngx_system_user_additional_groups` | [] | Optionally add the system user to more groups. For example to read TLS certificates that can be read by the group `ssl-cert`. |
| `paperless_ngx_version` | latest | Sofware version to install. Use `latest` or any specific version in the format `'2.0.0'`. Only `paperless_ngx_version_minimum: '2.0.0'` and higher supported. |
| `` |  |  |

###  2.2. <a name='Paperless-ngxconfigurationvariables'></a>Paperless-ngx configuration variables

All the upcoming vars correspond with the vars from [paperless-ngx docs](https://docs.paperless-ngx.com/configuration). The following list of variables is sorted alphabetically to simplify maintenance of this role. In the official documentation, these are assigned to corresponding categories.

To save reading space a few abbreviations are used in the table down below:
* I - Implemented in this role? [Y/N]
* O - Variable is meant to be overridden? [Y/N] If No it should not be altered.
* H - Hint
* V - Version of paperless-ngx that introduced this var. 

| Name           | Default Value | I | O | H | V |
| -------------- | ------------- |---|---|---|---|
| `paperless_ngx_conf_account_allow_signups` | false | Y | Y |   | 2.5 |
| `paperless_ngx_conf_account_default_http_protocol` | https | Y | Y |   | 2.5 |
| `paperless_ngx_conf_account_email_verification` | optional | Y | Y |   | 2.6 |
| `paperless_ngx_conf_account_session_remember` | false | Y | Y |   | 2.7 |
| `paperless_ngx_conf_admin_mail` | root@localhost | Y | Y |   |   |
| `paperless_ngx_conf_admin_password` |  | Y | Y | The superuser password. If not defined by the user, a random password will be generated -> see section below about passwords. |   |
| `paperless_ngx_conf_admin_user` | admin | Y | Y |   |   |
| `paperless_ngx_conf_allowed_hosts` | "*" | Y | Y |   |   |
| `paperless_ngx_conf_app_logo` | None | Y | Y |   | 2.4 |
| `paperless_ngx_conf_app_title` | None | Y | Y |   | 2.4 |
| `paperless_ngx_conf_apps` | None | Y | Y |   | 2.5 |
| `paperless_ngx_conf_audit_log_enabled` | false | Y | Y |   | 2.0  |
| `paperless_ngx_conf_auto_login_username` | "" | Y | Y |   |   |
| `paperless_ngx_conf_bind_addr` | "[::]" | Y | Y |   |   |
| `paperless_ngx_conf_consumer_asn_barcode_prefix` | ASN | Y | Y |   | 1.12 |
| `paperless_ngx_conf_consumer_collate_double_sided_subdir_name` | "double-sided" | Y | Y |   | 1.17 |
| `paperless_ngx_conf_consumer_collate_double_sided_tiff_support`| false | Y | Y |   | 1.17 |
| `paperless_ngx_conf_consumer_barcode_dpi` | 300 | Y | Y |   | 1.16 |
| `paperless_ngx_conf_consumer_barcode_max_pages` | 0 | Y | Y |   | 2.12 |
| `paperless_ngx_conf_consumer_barcode_scanner` | "PYZBAR" | Y | Y |   | 1.14 |
| `paperless_ngx_conf_consumer_barcode_string` | 'PATCHT' | Y | Y |   |   |
| `paperless_ngx_conf_consumer_barcode_tiff_support` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_barcode_upscale` | 0.0 | Y | Y |   | 1.16 |
| `paperless_ngx_conf_consumer_delete_duplicates` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_enable_asn_barcode` | false | Y | Y |   | 1.12 |
| `paperless_ngx_conf_consumer_enable_barcodes` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_enable_collate_double_sided` | false | Y | Y |   | 1.17 |
| `paperless_ngx_conf_consumer_enable_tag_barcode` | false | Y | Y |   | 2.5 |
| `paperless_ngx_conf_consumer_ignore_patterns` | [".DS_STORE/*", "._*", ".stfolder/*", ".stversions/*", ".localized/*", "desktop.ini"] | Y | Y |   |   |
| `paperless_ngx_conf_consumer_inotify_delay` | 0.5 | Y | Y |   |   |
| `paperless_ngx_conf_consumer_polling_delay` |5| Y | Y |   |   |
| `paperless_ngx_conf_consumer_polling_retry_count` |5| Y | Y |   |   |
| `paperless_ngx_conf_consumer_polling` |0| Y | Y |   |   |
| `paperless_ngx_conf_consumer_recursive` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_subdirs_as_tags` | false | Y | Y |   |   |
| `paperless_ngx_conf_consumer_tag_barcode_mapping` | '{"TAG:(.*)": "\\\\g<1>"}' | Y | Y |   | 2.5 |
| `paperless_ngx_conf_consumption_dir` | "{{ paperless_ngx_dir_runtime_data }}/consumption" | Y | Y |   |   |
| `paperless_ngx_conf_convert_binary` | convert | Y | Y |   |   |
| `paperless_ngx_conf_convert_memory_limit` |0| Y | Y |   |   |
| `paperless_ngx_conf_convert_tmpdir` | "" | Y | Y |   |   |
| `paperless_ngx_conf_cookie_prefix` | "" | Y | Y |   |   |
| `paperless_ngx_conf_cors_allowed_hosts` | http://localhost:8000 | Y | Y |   |   |
| `paperless_ngx_conf_csrf_trusted_origins` |  | Y | Y |   |   |
| `paperless_ngx_conf_data_dir` | "{{ paperless_ngx_dir_runtime_data }}/data" | Y | Y |   |   |
| `paperless_ngx_conf_date_order` | "DMY" | Y | Y |   |   |
| `paperless_ngx_conf_db_timeout` |  | Y | Y |   |   |
| `paperless_ngx_conf_dbengine` | | Y | N | Not used by the role |   |
| `paperless_ngx_conf_dbhost` | localhost | Y | Y | |   |
| `paperless_ngx_conf_dbname` | paperlessngx | Y | Y | |   |
| `paperless_ngx_conf_dbpass` | "" | Y | Y | The db password. If not defined by the user, a random password will be generated -> see section below about passwords. |   |
| `paperless_ngx_conf_dbport` |5432| Y | Y | |   |
| `paperless_ngx_conf_dbsslcert` | None | Y | Y | | 1.14 |
| `paperless_ngx_conf_dbsslkey` | None | Y | Y | | 1.14 |
| `paperless_ngx_conf_dbsslmode` | prefer | Y | Y | |   |
| `paperless_ngx_conf_dbsslrootcert` | None | Y | Y | | 1.14 |
| `paperless_ngx_conf_dbuser` | paperlessngx | Y | Y | |   |
| `paperless_ngx_conf_disable_regular_login` | false | Y | Y |   | 2.6 |
| `paperless_ngx_conf_email_certificate_location` | None | Y | Y |   | 1.17 |
| `paperless_ngx_conf_email_from` | {{ paperless_ngx_conf_email_host_user }} | Y | Y |   | 2.0 |
| `paperless_ngx_conf_email_gnupg_home` | None | Y | Y |   | 2.12 |
| `paperless_ngx_conf_email_host` | "localhost" | Y | Y |   | 2.0 |
| `paperless_ngx_conf_email_host_user` | "" | Y | Y |   | 2.0 |
| `paperless_ngx_conf_email_host_password` | "" | Y | Y |   | 2.0 |
| `paperless_ngx_conf_email_port` | 25 | Y | Y |   | 2.0 |
| `paperless_ngx_conf_email_task_cron` | "*/10 * * * *" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_email_use_ssl` | false | Y | Y |   | 2.0 |
| `paperless_ngx_conf_email_use_tls` | false | Y | Y |   | 2.0 |
| `paperless_ngx_conf_empty_trash_delay` | 30 | Y | Y |   | 2.10 |
| `paperless_ngx_conf_empty_trash_dir` | "{{ paperless_ngx_dir_runtime_data }}/trash" | Y | Y |   | 2.10 |
| `paperless_ngx_conf_empty_trash_task_cron` | "0 1 * * *" | Y | Y |   | 2.10 |
| `paperless_ngx_conf_enable_compression` | true | Y | Y |   | 1.13 |
| `paperless_ngx_conf_enable_flower` | false | Y | Y | Whether to start flower or not. See [using flower](docs/USING_FLOWER.md) for more information | 1.10 |
| `paperless_ngx_conf_enable_http_remote_user` | false | Y | Y |   |   |
| `paperless_ngx_conf_enable_http_remote_user_api` | false | Y | Y |   | 2.5 |
| `paperless_ngx_conf_enable_gpg_decryptor` | false | Y | Y |   | 2.12 |
| `paperless_ngx_conf_enable_nltk` |1| Y | Y |   | 1.11 |
| `paperless_ngx_conf_enable_update_check` |  | Y | Y | Will be removed in the future |   |
| `paperless_ngx_conf_filename_date_order` | "" | Y | Y |   |   |
| `paperless_ngx_conf_filename_format_remove_none` | false | Y | Y |   |   |
| `paperless_ngx_conf_filename_format` | "" | Y | Y |   |   |
| `paperless_ngx_conf_force_script_name` | "" | Y | Y |   |   |
| `paperless_ngx_conf_gs_binary` | gs | Y | Y |   |   |
| `paperless_ngx_conf_http_remote_user_header_name` | HTTP_REMOTE_USER | Y | Y |   |   |
| `paperless_ngx_conf_ignore_dates` | "" | Y | Y |   |   |
| `paperless_ngx_conf_index_task_cron` | "0 0 * * *" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_logging_dir` | "{{ paperless_ngx_dir_runtime_data }}/log" |   |   |   |   |
| `paperless_ngx_conf_logout_redirect_url` |  | Y | Y |   |   |
| `paperless_ngx_conf_logrotate_max_backups` |20| Y | Y |   |   |
| `paperless_ngx_conf_logrotate_max_size` | 1024 * 1024 | Y | Y |   |   |
| `paperless_ngx_conf_max_image_pixels` | None | Y | Y |   | 2.6 |
| `paperless_ngx_conf_media_root` | "{{ paperless_ngx_dir_runtime_data }}/media" | Y | Y |   |   |
| `paperless_ngx_conf_model_file` | "{{ paperless_ngx_conf_data_dir }}/classification_model.pickle" | Y | Y |   | 2.9 |
| `paperless_ngx_conf_nltk_dir` | /usr/share/nltk_data | Y | Y |   | 1.11 |
| `paperless_ngx_conf_number_of_suggested_dates` |3| Y | Y |   |   |
| `paperless_ngx_conf_ocr_clean` | clean | Y | Y |   |   |
| `paperless_ngx_conf_ocr_color_conversion_strategy` | "RGB" | Y | Y |   | 2.1 |
| `paperless_ngx_conf_ocr_deskew` | true | Y | Y |   |   |
| `paperless_ngx_conf_ocr_image_dpi` | "" | Y | Y |   |   |
| `paperless_ngx_conf_ocr_language` | eng | Y | Y |   |   |
| `paperless_ngx_conf_ocr_languages` | [eng,deu,fra,ita,spa] | Y | Y |   |   |
| `paperless_ngx_conf_ocr_max_image_pixels` | | Y | Y |   |   |
| `paperless_ngx_conf_ocr_mode` | skip | Y | Y |   |   |
| `paperless_ngx_conf_ocr_output_type` | pdfa | Y | Y |   |   |
| `paperless_ngx_conf_ocr_pages` |0| Y | Y |   |   |
| `paperless_ngx_conf_ocr_rotate_pages_threshold` |12| Y | Y |   |   |
| `paperless_ngx_conf_ocr_rotate_pages` | true | Y | Y |   |   |
| `paperless_ngx_conf_ocr_skip_archive_file` | "never" | Y | Y |   | 1.14 |
| `paperless_ngx_conf_ocr_user_args` | [optimize=1] | Y | Y |   |   |
| `paperless_ngx_conf_port` |8000| Y | Y |   |   |
| `paperless_ngx_conf_post_consume_script` | "" | Y | Y |   |   |
| `paperless_ngx_conf_pre_consume_script` | "" | Y | Y |   |   |
| `paperless_ngx_conf_proxy_ssl_header` | None | Y | Y |   | 1.14 |
| `paperless_ngx_conf_redirect_login_to_sso` | false | Y | Y |   | 2.12 |
| `paperless_ngx_conf_redis` | redis://{{ paperless_ngx_redis_host }}:{{ paperless_ngx_redis_port }} | Y | N |  |   |
| `paperless_ngx_conf_redis_prefix` | "" | Y | Y |  | 1.17 |
| `paperless_ngx_conf_sanity_task_cron` | "30 0 * * sun" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_secret_key` | "" | Y | Y | If not defined by the user, a random password will be generated -> see section below about passwords. |   |
| `paperless_ngx_conf_social_auto_signup` | false | Y | Y |   | 2.5 |
| `paperless_ngx_conf_socialaccount_allow_signups` | true | Y | Y |   | 2.5 |
| `paperless_ngx_conf_socialaccount_providers` | "{}" | Y | Y |   | 2.5 |
| `paperless_ngx_conf_static_url` | /static/ | Y | Y |   |   |
| `paperless_ngx_conf_staticdir` | ../static | Y | N |   |   |
| `paperless_ngx_conf_supervisord_working_dir` | None | Y | Y |   | 2.5 |
| `paperless_ngx_conf_task_workers` |1| Y | Y |   |   |
| `paperless_ngx_conf_threads_per_worker` | paperless_ngx_conf_task_workers | Y | Y |  |   |
| `paperless_ngx_conf_thumbnail_font_name` | /usr/share/fonts/liberation/LiberationSerif-Regular.ttf | Y | Y |   |   |
| `paperless_ngx_conf_tika_enabled` | false | Y | Y |   |   |
| `paperless_ngx_conf_tika_endpoint` | http://localhost:9998 | Y | Y |   |   |
| `paperless_ngx_conf_tika_gotenberg_endpoint` | http://localhost:3000 | Y | Y |   |   |
| `paperless_ngx_conf_time_zone` | Europe/London | Y | Y |   |   |
| `paperless_ngx_conf_train_task_cron` | "5 */1 * * *" | Y | Y |   | 1.12 |
| `paperless_ngx_conf_trusted_proxies` | "" | Y | Y |   | 1.14 |
| `paperless_ngx_conf_url` | http://localhost:8000 | Y | Y |   |   |
| `paperless_ngx_conf_use_x_forward_host` | False | Y | Y |   | 1.14 |
| `paperless_ngx_conf_use_x_forward_port` | False | Y | Y |   | 1.14 |
| `paperless_ngx_conf_usermap_gid` |  | Y | Y | System users gid |   |
| `paperless_ngx_conf_usermap_uid` |  | Y | Y | System users id |   |
| `paperless_ngx_conf_webserver_workers` |1| Y | Y |   |   |
| `paperless_ngx_conf_worker_timeout` |1800| Y | Y |   |   |
||

##  3. <a name='Usageadvices'></a>Usage advices

###  3.1. <a name='UpdatingPaperless-ngx'></a>Updating Paperless-ngx

If you installed Paperless-ngx with the help of this role and you want to update to a newer version than all you have to do is to run this role again (if you chose `latest` as the version identifier). If you specified a specific version to install than all you need to do is to change this value to a newer one and run the role again.

This role will not update anything else than Paperless-ngx. So updates for the operating system and depended packages need to be handled seperately.

**PLEASE THINK ABOUT BACKUPS before you upgrade.**

###  3.2. <a name='BackupRestore'></a>Backup/Restore

Please be aware that this role does not offer any mechanism of backup or restore. This is intention. To seperate concerns this role is only focused towards 'deployments' of the software artifacts and its configuration. An example of a working backup strategy can be found here: [Link to example backup strategy](docs/BACKUP_STRATEGY.md)

###  3.3. <a name='Generatedpassword'></a>Generated password

The role uses Ansible's password lookup:

-   If a password is generated by the role, ansible stores it **locally** in **pngx_instances/{{ incentory_hostname }}/** (relative to the working directory)
-   if the file already exist, it reuse its content
-   see [the ansible password lookup documentation](https://docs.ansible.com/ansible/latest/plugins/lookup/password.html) for more info


###  3.4. <a name='Separationofstaticinstallationanddynamicruntimedata'></a>Separation of static (~ installation) and dynamic (~ runtime) data

This role checks that you do not set one of the data dirs (like consumption etc.) as a subdirectory of the installation path. For making my life easier this role deletes the installation folder and creates a complete new one when upgrading. This is fresh and clean. Also this way you are kept from unwanted deletions of your data during upgrades.

###  3.5. <a name='PostgreSQLusage'></a>PostgreSQL usage
If you want to use Paperless-ngx together with PostgreSQL a running instance of PostgreSQL is required. This role does not automatically install such a database instance for you. However, here is you can read an example how to set up such an instance from scretch: [Link to example playbook](docs/POSTGRESQL.md)

##  4. <a name='Dependencies'></a>Dependencies

No dependencies

##  5. <a name='ExamplePlaybooks'></a>Example Playbooks

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

##  6. <a name='Contributing'></a>Contributing

We encourage you to contribute to this role! Please check out the
[contributing guide](CONTRIBUTE.md) for guidelines about how to proceed.

##  7. <a name='License'></a>License

MIT
