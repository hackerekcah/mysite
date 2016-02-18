# mysite
database setup:
(1).install mysql-server and mysql-client
sudo apt-get install mysql-server
sudo apt-get install mysql-client
(2).install mysql-python for ubuntu
sudo apt-get install python-setuptools
sudo apt-get install libmysqld-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev
sudo easy_install mysql-python
(3)create a database
mysql -u root -p(press enter,then enter password)

#create database with utf8 encoding
CREATE DATABASE mysite
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;;
(4)When add new model:
python manage.py makemigrations [app name]
python manage.py migrate

