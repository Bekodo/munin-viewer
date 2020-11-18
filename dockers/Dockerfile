FROM centos:8

RUN mkdir -p /opt/munin-viewer
WORKDIR /opt/munin-viewer

RUN yum install python3 python3-devel python3-pip -y
ADD python-requirements.txt /tmp
RUN pip3 install -r /tmp/python-requirements.txt

ADD ./ /opt/munin-viewer/

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]