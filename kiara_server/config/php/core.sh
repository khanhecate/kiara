#!/bin/bash
#check OS
if ! grep -q "ID=debian" /etc/*-release ;then
	if ! grep -q "ID=ubuntu" /etc/*-release ;then
		echo "Unidentified OS !"
		exit
	fi
fi
#check ppa + add ppa
#check for ubuntu
if grep -q "ID=ubuntu" /etc/*-release ;then
	if ! ls /etc/apt/sources.list.d | grep -q "ondrej" ;then
		add-apt-repository ppa:ondrej/php -y
	fi	
fi
#check for debian
if grep -q "ID=debian" /etc/*-release ;then
	if ! ls /etc/apt/sources.list.d | grep -q "php.list" ;then
	apt install apt-transport-https lsb-release ca-certificates -y
	wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
	sh -c 'echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list' -y
	apt update -y	
	fi
fi

