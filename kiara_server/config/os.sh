#!/bin/bash
cd /
grep DISTRIB_DESCRIPTION /etc/*-release > /tmp/session.txt
sed -i 's/\/etc\/lsb-release:DISTRIB_DESCRIPTION=//g' tmp/session.txt
cat /tmp/session.txt
