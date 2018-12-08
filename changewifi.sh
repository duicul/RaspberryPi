#!/bin/bash
echo  `cat /etc/wpa_supplicant/wpa_supplicant.conf `
if test $# -ge 2
then
echo $1 $2
echo `cat /etc/wpa_supplicant/wpa_supplicant.conf `
sudo chmod a+w /etc/wpa_supplicant/wpa_supplicant.conf 
if test  `cat /etc/wpa_supplicant/wpa_supplicant.conf|grep -e .*ssid.* | wc -l ` -eq 1
then 
echo `cat /etc/wpa_supplicant/wpa_supplicant.conf | sed -e  s/ssid=\".*\"/ssid=\"$1\"/ ` > /etc/wpa_supplicant/wpa_supplicant.conf 
echo `cat /etc/wpa_supplicant/wpa_supplicant.conf | sed -e  s/psk=\".*\"/psk=\"$2\" ` >  /etc/wpa_supplicant/wpa_supplicant.conf
fi
echo `cat /etc/wpa_supplicant/wpa_supplicant.conf `
fi
