
apt-get update
apt-get install vim

httpd -k start
httpd -k restart


Include conf/extra/httpd-info.conf


# MPM
apt-get update
apt-get install -y procps.
ps aux | grep -e httpd -e USER | grep -v grep





