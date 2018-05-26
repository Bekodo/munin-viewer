Web viewer of munin graph, all in the same page

*Install python 3.5 and flask*

In the file services.ini add the listo of services to view and the file png path
```
[services]
cpu=cpu-day.png
memory=memory-day.png
```

In the file site.cfg add the list of servers to discard
```
server1
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

*printscreens*
**Desktop**
[[https://github.com/Bekodo/munin-viewer/blob/master/Doc/img/Desktop_example.png|alt=Desktop]]

**Mobile|Table**
[[https://github.com/Bekodo/munin-viewer/blob/master/Doc/img/Responsive_example.png|alt=Mobile]]

LICENSE

This source files are made available under the terms of the GNU Affero General Public License (GNU AGPLv3).
