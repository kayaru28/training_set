
# case X
## issue
## cause analysis
## result


# case 1
## issue
root@1ab05b9d305b:/usr/local/apache2/conf# httpd -k restart
AH00534: httpd: Configuration error: No MPM loaded.

## cause analysis
root@1ab05b9d305b:/usr/local/apache2/conf# cat extra/add_dso_loadmodules.conf | grep mpm
LoadModule mpm_event_module modules/mod_mpm_event.so
#LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
#LoadModule mpm_worker_module modules/mod_mpm_worker.so
<IfModule !mpm_prefork_module>
<IfModule mpm_prefork_module>

in httpd.conf
Include conf/extra/httpd-info.conf
-> bad

## result
solution : fixing typographical error

making another file of "load module" is ok.
but, include sentence@httpd.conf is wrong.

after fixing...

root@1ab05b9d305b:/usr/local/apache2/conf# httpd -k restart
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
httpd not running, trying to start
root@1ab05b9d305b:/usr/local/apache2/conf# httpd -k start
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
httpd (pid 32) already running


# case 2
## issue
do not output logs to access.log

## cause analysis
<IfModule log_config_module>
    CustomLog logs/access.log common
</IfModule>

root@1ab05b9d305b:/usr/local/apache2/conf# diff httpd.conf httpd.conf.bef
39,40d38
< Include conf/extra/add_dso_loadmodules.conf
<
375a374,375
> # original
> Include conf/extra/add_dso_loadmodules.conf

## result
solution : changing point of including modules

point of including modules is not proper.
then, IFModule tag think not matching 



