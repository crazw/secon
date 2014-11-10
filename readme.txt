网站安全监控平台 2.0版

#gearmand MySQL-python

yum -y install net-snmp net-snmp-devel net-snmp-utils

yum -y install dos2unix ntpdate 

同步时间 
ntpdate 210.167.182.10

yum -y install python-devel python-setuptools python-pycurl python-simplejson MySQL-python libevent libevent-devel
 
easy_install greenlet
easy_install gevent

安装
#=========================================
dos2unix /usr/local/mntrwork_v22/bin/*.sh
chmod 744 /usr/local/mntrwork_v22/bin/*.sh

开机启动
echo "/usr/local/mntrwork_v22/bin/startup.sh" >> /etc/rc.local

程序检测
crontab -l > mycrontab
echo "*/1 * * * * /usr/local/mntrwork_v22/bin/startup.sh > /dev/null 2>&1" >> mycrontab
crontab mycrontab
rm -rf mycrontab
chkconfig crond on
service crond restart

