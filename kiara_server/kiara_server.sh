#!/bin/bash
if [[ EUID -ne 0 ]]; then
	echo "please run as root!"
	exit
fi
while true
do
echo "Welcome to kiara server , choose number menu below :"
echo -n "1.add user for kiara
2.remove user for kiara
3.exit 
"
read menu
case $menu in
	1)printf "username : "
	read user
	useradd $user
	passwd $user
	echo "$user" > db/db.user 
	echo "grep \"$user\" /etc/passwd > tmp/tmp"  > tmp/dieshell.sh
	./tmp/dieshell.sh
	data=`cat tmp/tmp`
	echo "grep -v \"$data\" /etc/passwd > tmp/data " > tmp/dieshell.sh
	./tmp/dieshell.sh
	cat tmp/data > /etc/passwd
	sed -i 's/[1-9]//g' tmp/tmp
	cat tmp/tmp >> /etc/passwd
		;;
	2)echo "List of user :"
	cat db/db.user
	printf "Input name user : "
	read user
	chmod 777 tmp/dieshell.sh
	echo "grep -v \"$user\" db/db.user > tmp/tmp" > tmp/dieshell.sh
	./tmp/dieshell.sh
	userdel $user
	cat tmp/tmp > db/db.user
	rm -r tmp/tmp
		;;
	3)exit
		;;
	*)clear	
	echo "please choose number 1,2, or 3"
	sleep 2
esac
done