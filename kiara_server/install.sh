#!/bin/bash
echo 'Installing Kiara Server ...'
echo 'Creating Directory for Kiara server ...'
mkdir /opt/kiara 2>/dev/null
status=$?
if [[ $status = 0 ]]; then
	echo 'Copying file to Kiara folder ....'
	cp -r -v db kiara_server.sh tmp config /opt/kiara
	echo 'Adding Kiara to /usr/bin ...'
	echo 'Moving to Directory /opt/kiara ...'
	cd /opt/kiara
	touch kiara
	echo "#!/bin/bash" > kiara
	echo "echo 'Moving to kiara Directory ...'" >> kiara
	echo "cd /opt/kiara" >> kiara
	echo "./kiara_server.sh" >> kiara
	chmod 755 kiara 
	mv kiara /usr/bin
	echo "Creating Default user Kiara ..."
	useradd kiara
	echo "password for user kiara"
	passwd kiara
	echo '(active) : kiara' > /opt/kiara/db/db.user
	echo "Kiara need Mysql server ! for web Interface (comming soon)"
	echo "Kiara Installing Success !"
	echo 'You can run kiara , by type "kiara" '
	echo 'thanks for Installing kiara :D'
else echo 'Updating Kiara ...'
	cp -r -v kiara_server.sh tmp config /opt/kiara
fi
#allow root login
#for debian
if grep -q "#PermitRootLogin prohibit-password" /etc/ssh/sshd_config;then
	sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
fi
#for ubuntu
if grep -q "#PermitRootLogin prohibit-password" /etc/ssh/sshd_config;then
	sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
fi
echo "restarting ssh ..."
if /etc/init.d/ssh restart 2>/dev/null ;then
	echo "restart ssh success , install success ! "
else echo "ssh restart failed ! , install error !"
fi
