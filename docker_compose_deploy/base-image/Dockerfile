FROM centos:7

RUN mkdir -p /opt/loonflow
COPY . /opt/loonflow

RUN yum install -y wget mysql-devel gcc gcc-devel python3 python3-pip python3-dev python3-devel mysql-devel zlib-devel openssl-devel openssl-devel git && \
     rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

WORKDIR /opt/loonflow
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host=pypi.tuna.tsinghua.edu.cn





