Python  2.7.5
python  3.6.8
Python  3.8.3
ansible 2.11.2

# for ssh key generate
ls -ld ~/.ssh/
chmod 700 ~/.ssh/
cd ~/.ssh/
ssh-keygen -t rsa


ssh-keygen -R 192.168.1.241
ssh -i /root/.ssh/id_rsa_grun root@192.168.1.241

# setup for ansible
## for install
yum -y install python3
pip3 install --upgrade pip
pip3 install ansible

ansible --version

## for module
export ANSIBLE_LIBRARY="/root/dockerfiles/003_ansible/999_modules"

https://docs.ansible.com/ansible/2.9_ja/dev_guide/developing_locally.html

## confirm
ansible --version
 
## python 3.8
https://computingforgeeks.com/how-to-install-python-3-on-centos/

yum -y update
yum -y groupinstall "Development Tools"
yum -y install openssl-devel bzip2-devel libffi-devel
gcc --version

yum -y install wget

cd ~
wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
tar xvf Python-3.8.3.tgz
cd Python-3.8*/
./configure --enable-optimizations
make altinstall

python3.8 --version
pip3.8 --version

## ansible based on python 3.8
pip3.8 install --upgrade pip
pip3.8 install ansible

ansible --version

