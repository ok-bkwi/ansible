#  Ansible (Open)DS Role


## Links. Extend, this needs to happen twice for the config and user directories. Also have a check with start-ds.sh that it runs!
Zie /roles/internal/test/opendj/templates/opendj.service.j2:ExecStart=/opt/opendj/bin/start-ds


In `/opt/ds/opendj`

```bash
./setup directory-server \
--rootUserDN "cn=Directory Manager" \
--rootUserPassword FRdemo123 \
--monitorUserPassword FRdemo123 \
--hostname fr1.example.com \
--ldapPort 3389 \
--ldapsPort 3636 \
--adminConnectorPort 34444 \
--profile am-config \
--set am-config/amConfigAdminPassword:FRdemo123 \
--acceptLicense
# --productionMode \
# --httpPort 38081 \
# --httpsPort 38443 \
```

## Notes / Clarifications

