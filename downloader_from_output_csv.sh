#!/bin/bash
IFS=","
while read f1 f2
do
        echo "apk is : $f1"
	echo "link is: $f2"
	cd /silo100/hdd/sr939/medicalappsAnalysis/TopFreeAppsUpdated2022/
	if [[ -f "/silo100/hdd/sr939/medicalappsAnalysis/TopFreeAppsUpdated2022/$f1.apk" ]]
	then
		echo "apk there"
		continue
	fi
	filename="$f1.apk"
	wget -O "$filename" "$f2"
	cd ..
	sleep 5
done < output_download_links.csv


