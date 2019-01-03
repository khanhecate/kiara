#!/bin/bash
cd /
grep DISTRIB_DESCRIPTION /etc/*-release > /tmp/session.txt
grep PRETTY_NAME= /etc/*-release > /tmp/session.txt
sed -i 's/DISTRIB_DESCRIPTION=//g' tmp/session.txt
sed -i 's/PRETTY_NAME=//g' tmp/session.txt
sed -i 's/"//g' tmp/session.txt
cat /tmp/session.txt
