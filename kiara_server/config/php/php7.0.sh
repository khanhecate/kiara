#!/bin/bash
if ! command -v php7.0 1>/dev/null ;then
	apt install php7.0 -y
fi
cd /
a2dismod php*
a2enmod php7.0
echo "restarting apache2 ..."
/etc/init.d/apache2 restart
cd -