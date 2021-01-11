# Ansible Role: Tomcat

An Ansible Role that supplements [robertdebock.tomcat](../../../external/robertdebock.tomcat). 

## Apps

TODO

## JMX

To enable JMX using default settings

```yaml
tomcat_jmx:
  enable: true
```

This will create two files `/etc/tomcat/jmx.access`, `/etc/tomcat/jmx.password`. Then configure `CATALINA_OPTS` for example as follows

```yaml
tomcat_instances:
  - name: tomcat9
    version: 9
    shutdown_port: 8007
    non_ssl_connector_port: 8082
    ssl_connector_port: 8445
    ajp_port: 8011
    wars: []
    catalina_opts: >-
      -Dcom.sun.management.jmxremote
      -Dcom.sun.management.jmxremote.port=8375
      -Dcom.sun.management.jmxremote.rmi.port=8376
      -Dcom.sun.management.jmxremote.local.only=false
      -Dcom.sun.management.jmxremote.ssl=false
      -Dcom.sun.management.jmxremote.authenticate=true
      -Dcom.sun.management.jmxremote.password.file=/etc/tomcat/jmxremote.password
      -Dcom.sun.management.jmxremote.access.file=/etc/tomcat/jmxremote.access
      -Djava.rmi.server.hostname=jmx.1.1.1.35.nip.io 
```