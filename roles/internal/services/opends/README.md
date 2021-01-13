#  Ansible OpenDS Role


## Links

In `/opt/opends/opends/opendj/bin/`

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

