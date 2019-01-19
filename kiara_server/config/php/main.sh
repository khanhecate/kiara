#!/bin/bash
#connect by socket
source socket
#auth
while true
do
menu=$(whiptail --title "[ Menu ]" --cancel-button "exit" --menu "Choose version below : " 15 60 5 \
"php5.6" "change php version to 5.6" \
"php7.0" "change php version to 7.0" \
"php7.1" "change php version to 7.1" \
"php7.2" "change php version to 7.2" \
"php7.3" "change php version to 7.3"  3>&1 1>&2 2>&3)

quitmenu=$?
if [[ $quitmenu = 0 ]]; then
	case $menu in
		php5.6 )socket '/opt/kiara/config/php/core.sh'
			 socket '/opt/kiara/config/php/php5.6.sh'
			;;
		php7.0 )socket '/opt/kiara/config/php/core.sh'
			 socket '/opt/kiara/config/php/php7.0.sh'
			;;
		php7.1 )socket '/opt/kiara/config/php/core.sh'
			 socket '/opt/kiara/config/php/php7.1.sh'
			;;
		php7.2 )socket '/opt/kiara/config/php/core.sh'
			 socket '/opt/kiara/config/php/php7.2.sh'
			;;
		php7.3 )socket '/opt/kiara/config/php/core.sh'
			 socket '/opt/kiara/config/php/php7.3.sh'
			;;
	esac
	whiptail --title "[ Notice ]" --msgbox "Done Check your php info via browser" 15 60
else break
fi
clear
echo "create by KhanHecate "
done