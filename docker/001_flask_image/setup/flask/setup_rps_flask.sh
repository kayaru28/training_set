
#export root_password=$(cat /setup/secret.txt |grep root_pass| awk '{print $1}')

rm -f app-python.zip*
rm -f *.py
rm -r -f templates

#download_zip="app-python.zip"
#wget https://raw.githubusercontent.com/kayaru28/training_set/master/docker/flask_image/${download_zip}
#cp /setup/${download_zip} / # for test
#unzip ${download_zip}

cp /setup/*.py / # for test
cp -r /setup/templates / # for test

#crontab /setup/cron_rps_flask.conf
#crond

mkdir /log
chmod 777 /log

flask run --host 0.0.0.0 --port 5000
