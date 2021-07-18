python  3.6.8
ansible 2.11.2

# for ansible

yum -y install python3
pip3 install --upgrade pip
pip3 install ansible

ansible --version
 
# for ssh key generate
ls -ld ~/.ssh/
chmod 700 ~/.ssh/
cd ~/.ssh/
ssh-keygen -t rsa

ssh -i /root/.ssh/id_rsa_grun root@192.168.1.241

