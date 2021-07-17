set destination_host=root@192.168.1.240
set source_file=D:\WORK\b418_STUDY_git\training_set\docker\001_flask_image\fluentd\*
set destination_directory=/root/dockerfiles/001_python_tool/fluentd/

scp -i C:\Users\istor\.ssh\id_rsa_verdigris -r %source_file% %destination_host%:%destination_directory%




