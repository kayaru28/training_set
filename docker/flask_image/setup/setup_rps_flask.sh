
source /root/setup/setup_rps_common.sh
export root_password=$(cat /root/setup/secret.txt |grep root_pass| awk '{print $1}')

download_zip="app-python.zip"
wget https://raw.githubusercontent.com/kayaru28/training_set/master/docker/flask_image/${download_zip}
unzip ${download_zip}

flask run --host 0.0.0.0 --port 8080
