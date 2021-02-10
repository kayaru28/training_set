
source /root/setup/setup_rps_common.sh
export root_password=$(cat /root/setup/secret.txt |grep root_pass| awk '{print $1}')

rm -f *.py
rm -r -f templates
cp /root/setup/*.py / # for test
cp -r /root/setup/templates / # for test

pytest -v test_flask_base.py
