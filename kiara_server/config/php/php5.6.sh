#!/bin/bash
if ! command -v php5.6 1>/dev/null ;then
	apt install php5.6 -y
fi
cd /
a2dismod php*
a2enmod php5.6
echo "restarting apache2 ..."
/etc/init.d/apache2 restart
cd -