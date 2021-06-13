set destination_host=root@192.168.1.240
set source_file=D:\WORK\b418_STUDY_git\training_set\docker\002_redmine\*.yml
set destination_directory=/root/dockerfiles/002_redmine/

scp -i C:\Users\istor\.ssh\id_rsa_pc4 -r %source_file% %destination_host%:%destination_directory%

