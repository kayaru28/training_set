python  3.6.8
ansible 2.11.2

# setup for ansible
## for install
yum -y install python3
pip3 install --upgrade pip
pip3 install ansible

## for module
export ANSIBLE_LIBRARY="/root/dockerfiles/003_ansible/999_modules"

https://docs.ansible.com/ansible/2.9_ja/dev_guide/developing_locally.html

## confirm
ansible --version
 
# for ssh key generate
ls -ld ~/.ssh/
chmod 700 ~/.ssh/
cd ~/.ssh/
ssh-keygen -t rsa

ssh -i /root/.ssh/id_rsa_grun root@192.168.1.241







apt-get install apt-transport-https
apt-get install ca-certificates
apt-get install curl
apt-get install gnupg 
apt-get install lsb-release


    