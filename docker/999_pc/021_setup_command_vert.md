
# setup for ansible
mkdir ~/.ssh
cat id_rsa_grun.pub >> ~/.ssh/authorized_keys
cat id_rsa_verdigris.pub >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh/
chmod 600 ~/.ssh/authorized_keys
ssh-keygen -R 192.168.1.241

# setup for ssh
vi /etc/ssh/sshd_config
PubkeyAuthentication yes
systemctl restart sshd
systemctl status sshd








