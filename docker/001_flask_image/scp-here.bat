
set destination_host=root@192.168.1.241
set destination_directory=/dockerroot/

set source_file=D:\WORK\b418_STUDY_git\training_set\docker\001_flask_image\*.yml
scp -i C:\Users\istor\.ssh\id_rsa_verdigris -r %source_file% %destination_host%:%destination_directory%

set source_file=D:\WORK\b418_STUDY_git\training_set\docker\001_flask_image\*.sh
scp -i C:\Users\istor\.ssh\id_rsa_verdigris -r %source_file% %destination_host%:%destination_directory%


set source_file=D:\WORK\b418_STUDY_git\training_set\docker\001_flask_image\.env
scp -i C:\Users\istor\.ssh\id_rsa_verdigris -r %source_file% %destination_host%:%destination_directory%





