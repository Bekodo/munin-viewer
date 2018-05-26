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

*Nginx config*
```
location ~* ^/(viewer|static) {
	proxy_set_header X-Real-IP  $remote_addr;
	proxy_set_header X-Forwarded-For $remote_addr;
	proxy_set_header Host $host;
	proxy_pass http://localhost:5005;
}
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

LICENSE

This source files are made available under the terms of the GNU Affero General Public License (GNU AGPLv3).
