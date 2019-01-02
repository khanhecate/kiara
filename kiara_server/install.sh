#!/bin/bash
echo 'Installing Kiara Server ...'
echo 'Creating Directory for Kiara server ...'
mkdir /kiara 
status=$?
if [[ $status = 0 ]]; then
	echo 'Copying file to Kiara folder ....'
	cp -r -v db kiara_server.sh tmp /kiara
	echo 'Adding Kiara to /usr/bin ...'
	echo 'Moving to Directory /kiara ...'
	cd /kiara
	touch kiara
	echo "#!/bin/bash" > kiara
	echo "echo 'Moving to kiara Directory ...'" >> kiara
	echo "cd /kiara" >> kiara
	echo "./kiara_server.sh" >> kiara
	chmod 755 kiara 
	mv kiara /usr/bin
	echo "Creating Default user Kiara ..."
	useradd kiara
	echo "password for user kiara"
	passwd kiara
	echo '(active) : kiara' > /kiara/db/db.user
	echo "Kiara need Mysql server ! for web Interface (comming soon)"
	echo "Kiara Installing Success !"
	echo 'You can run kiara , by type "kiara" '
	echo 'thanks for Installing kiara :D'
else echo 'Updating Kiara ...'
	cp -r -v kiara_server.sh tmp /kiara
fi
echo "done"
