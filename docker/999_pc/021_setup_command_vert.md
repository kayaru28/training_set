
# setup for ansible
cat id_rsa_grun.pub >> .ssh/authorized_keys

[root@node1 ~]# vi /etc/ssh/sshd_config
PubkeyAuthentication yes

systemctl restart sshd