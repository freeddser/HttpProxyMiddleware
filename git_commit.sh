#!/bin/bash
#code by gavin.li 

echo "Bitbucket  ->Git commit tools!"
echo "http://git.imaginato.com:7171/auto_sys/ssl-crt.git"
git status
git add .
read -p "Enter the commit Desc!" Desc
git commit -a -m "$Desc"
git push -u origin master 

