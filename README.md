#网站安全监控平台 2.0版

yum -y install net-snmp net-snmp-devel net-snmp-utils

yum -y install dos2unix ntpdate 

同步时间 
ntpdate 210.167.182.10

yum -y install python-devel python-setuptools python-pycurl python-simplejson MySQL-python libevent libevent-devel
 
easy_install greenlet
easy_install gevent

安装
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

#
步骤：
1.python check.py

2.进入src文件夹，解压对应的包，执行：python setup.py install or easy_install xxx

3.报错：

Traceback (most recent call last):
  File "main_dns.py", line 5, in <module>
    import handler_cache as mcache
  File "/root/secon/handler_cache.py", line 5, in <module>
    import handler_model as modelJob
  File "/root/secon/handler_model.py", line 6, in <module>
    import lib.secon_mysql_lib as mysql
  File "/root/secon/lib/secon_mysql_lib.py", line 4, in <module>
    import sys, MySQLdb
ImportError: No module named MySQLdb
解决方法：yum install MySQL-python
