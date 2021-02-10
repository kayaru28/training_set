
source /root/setup/setup_rps_common.sh
export root_password=$(cat /root/setup/secret.txt |grep root_pass| awk '{print $1}')

rm -f app-python.zip*
rm -f *.py
rm -r -f templates

#download_zip="app-python.zip"
#wget https://raw.githubusercontent.com/kayaru28/training_set/master/docker/flask_image/${download_zip}
#cp /root/setup/${download_zip} / # for test
#unzip ${download_zip}

cp /root/setup/*.py / # for test
cp -r /root/setup/templates / # for test

flask run --host 0.0.0.0 --port 5000
