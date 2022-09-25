#!/bin/bash

cd /root/django


\cp -rf config MTV common templates requirements.txt /my-django
cd /my-django

sudo sed -i "/twisted-iocpsupport==1.0.2/d" /my-django/requirements.txt
pip install -r requirements.txt

sudo sed -i "s/DEBUG = .*/DEBUG = False/" /my-django/config/settings.py
sudo sed -i "s/is_Production = .*/is_Production = False/" /my-django/config/settings.py
sudo sed -i "s/DataBase_Write_Endpoint = .*/DataBase_Write_Endpoint = \"{Write_Endpoint}\"/" /my-django/config/settings.py
sudo sed -i "s/DataBase_Read_Endpoint = .*/DataBase_Read_Endpoint = \"{Read_Endpoint}\"/" /my-django/config/settings.py
sudo sed -i "s/USE_CACHE = .*/USE_CACHE = False/" /my-django/config/settings.py
sudo sed -i "s/IS_HOME = .*/IS_HOME = False/" /my-django/config/settings.py
sudo sed -i "s/ REDIS_HOST = .*/ REDIS_HOST = \"{REDIS_HOST}\"/" /my-django/config/settings.py
sudo systemctl restart kgcha