#!/usr/bin/env python

import sys
import os
import datetime

import argparse
import urllib3
import sqlite3
import urllib3
import bs4
import urllib.parse as urlparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "http://apkpure.com/"
SEARCH_PACKAGE_URL = 'https://apkpure.com/dl/{}'


def find_package_page(package_name):
    http = urllib3.PoolManager()
    r = http.request("GET", SEARCH_PACKAGE_URL.format(package_name))
    return r.geturl()



def build_app_page_url(rel_link):
    return urlparse.urljoin(BASE_URL, rel_link)



def bs4_parse_url(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    # return bs4.BeautifulSoup(r.data, "html5lib")
    return bs4.BeautifulSoup(r.data, "html.parser")


def find_download_link(href):
    soup_element = bs4_parse_url(href)
    try:
        return soup_element.select_one(" .da")['href']
    except:
        return ""


def find_download_link_encripted(href):
    soup_element = bs4_parse_url(href)
    try:
        return soup_element.select_one("#iframe_download")['src']
    except:
        return ""





f = open('input_app_package_names.txt','r')
#fw= open('med_free_apps_download_links.txt','w+')
fw = open('output_download_links.csv','w+')

for line in f:
    line = line.strip('\n')
    app_href = find_package_page(line)
    print(app_href)
    href = build_app_page_url(app_href)
    print(href)
    download_link = find_download_link(href)
    if download_link=="":
        continue
    download_link = build_app_page_url(download_link)
    download_link = find_download_link_encripted(download_link)
    if download_link=="":
        continue
    download_link = build_app_page_url(download_link)
    fw.write(str(line) + ',' + str(download_link) + '\n')
f.close()
fw.close()

