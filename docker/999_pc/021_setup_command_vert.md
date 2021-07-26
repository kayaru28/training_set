
# basic
hostnamectl set-hostname vert001

# setup for login
passwd

# setup for ssh
mkdir ~/.ssh
cat id_rsa_grun.pub >> ~/.ssh/authorized_keys
echo "" >> ~/.ssh/authorized_keys

cat id_rsa_verdigris.pub >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh/
chmod 600 ~/.ssh/authorized_keys

vi /etc/ssh/sshd_config
PubkeyAuthentication yes
systemctl restart sshd
systemctl status sshd

# setup for disk size
df -h

## atchive
### centOS
rootfs-expand



