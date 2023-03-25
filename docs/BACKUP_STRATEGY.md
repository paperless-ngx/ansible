# Backup strategy for Paperless-ngx bare metal instance

Here is a example that demonstrates my personal backup flow that is crisis-tested ;) but maybe a little bit overengineered. My situation is this: Paperless runs as a LXC container on a Proxmox VE host and the media dir is mounted on a NAS.

* Run the sanitizer module to check for inconsistencies
* Create a Proxmox LXC backup of the complete machine state
* Run the document_exporter module to have a backup of the documents and meta data
* Stop all Paperless-ngx services
* Create a backup of the /media directory that is sitting on a NAS
* Upgrade the app (is done by the role)
* Start all services (is done by the role)
* Run the sanitizer module to check for inconsistencies