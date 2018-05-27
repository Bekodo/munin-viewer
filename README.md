Web viewer of munin graph, all in the same page

*Install python 3.5 and flask*

In file services.ini add the list of services in the services section to view and the file png path
```
[services]
cpu=cpu-day.png
memory=memory-day.png
```

In file services.ini add the list of servers in the discart_servers section to remove them from of view
```
[discard_servers]
loalhost
server2
server3
```

*Apache munin.conf config*
```
ProxyPass         /munin/viewer  http://localhost:5005/munin/viewer nocanon
ProxyPassReverse  /munin/viewer  http://localhost:5005/munin/viewer
ProxyRequests     Off
```

*Service config*
Add uwsgi-viewer.service to /etc/systemd/system/

*Start*
```
systemctl start uwsgi-viewer
```

*Start on boot*
```
systemctl enable uwsgi-viewer
```

*PrintScreens*

**Desktop**

![Desktop](Doc/img/Desktop_example.png?raw=true)

**Mobile|Table**

![Mobile](Doc/img/Responsive_example.png?raw=true)

LICENSE

This source files are made available under the terms of the GNU Affero General Public License (GNU AGPLv3).
