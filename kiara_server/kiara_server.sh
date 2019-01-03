#!/bin/bash
if [[ EUID -ne 0 ]]; then
	echo "please run as root!"
	exit
fi
while true
do
#for debian
if grep -q "#PermitRootLogin prohibit-password" /etc/ssh/sshd_config;then
	sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
fi
#for ubuntu
if grep -q "#PermitRootLogin prohibit-password without-password" /etc/ssh/sshd_config;then
	sed -i 's/#PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
fi
echo "Loading .."
systemctl restart ssh 
clear
echo "=====================================================|"
echo "Welcome to kiara server , choose number menu below : |"
echo "1.add user kiara                                     |
2.Active user kiara                                  |
3.Nonactive user kiara                               |
4.User List                                          |
5.Change password user kiara                         |
6.exit                                               |"
echo -n "=====================================================|
"
read menu
case $menu in
	1)printf "username : "
	read user
	useradd $user
	passwd $user
	echo "(active) : $user" >> db/db.user 
	echo "grep \"$user\" /etc/passwd > tmp/tmp"  > tmp/dieshell.sh
	./tmp/dieshell.sh
	data=`cat tmp/tmp`
	echo "grep -v \"$data\" /etc/passwd > tmp/data " > tmp/dieshell.sh
	./tmp/dieshell.sh
	cat tmp/data > /etc/passwd
	sed -i 's/[1-9]//g' tmp/tmp
	cat tmp/tmp >> /etc/passwd
	echo "activating user $user ..."
	echo "$user status"
	grep $user /etc/passwd

	sleep 2
		;;
	2)echo "List of user :"
	cat db/db.user
	printf "Input name user : "
	read user
	touch tmp/dieshell.sh
	echo "sed -i 's/(nonactive) : $user/(active) : $user/g' /opt/kiara/db/db.user" > tmp/dieshell.sh
	chmod 777 tmp/dieshell.sh
	cd tmp
	./dieshell.sh
	cd ..
	echo "user $user activating success !"
	echo "$user status"
	grep $user db/db.user

	
	sleep 2
		;;
	3)echo "List of user :"
	cat db/db.user
	printf "Input name user : "
	read user
	touch tmp/dieshell.sh 
	echo "sed -i 's/(active) : $user/(nonactive) : $user/g' /opt/kiara/db/db.user" > tmp/dieshell.sh
	chmod 777 tmp/dieshell.sh
	cd tmp
	./dieshell.sh
	cd ..
	echo "user $user nonactive success !"
	echo "$user status"
	grep $user db/db.user
	
	sleep 2
		;;
	4)while true
	do
	echo "_____________________________________________"
	cat db/db.user
	echo "_____________________________________________"
	printf "Back to menu ? [y/n] : "
	read list
	case $list in
		y)break
			;;
		n)echo "exit ..."
		exit
			;;
		*)clear
		echo "please type Y or N !"
			;;
	esac
	done
		;;
	5)echo "list user kiara ......"
	echo "_____________________________________________"
	cat db/db.user
	echo "_____________________________________________"
	printf "Input username : "
	read name
	passwd $name
		;;
	6)exit
		;;
	*)clear	
	echo "please choose number 1,2, or 3"
	sleep 2
esac
done
