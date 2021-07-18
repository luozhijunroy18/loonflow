FROM registry-dev.ekuaibao.com/ops/loonflow-base:1.0.0

COPY . /opt/loonflow/

RUN mkdir -p /var/log/loonflow/

# 前端
WORKDIR /opt
## 安装nodejs
RUN wget -c https://mirror.tuna.tsinghua.edu.cn/nodejs-release/v14.3.0/node-v14.3.0-linux-x64.tar.xz
RUN tar -xvf node-v14.3.0-linux-x64.tar.xz
RUN mv node-v14.3.0-linux-x64 nodejs
RUN ln -s /opt/nodejs/bin/node /usr/local/bin/node
RUN ln -s /opt/nodejs/bin/npm /usr/local/bin/npm
RUN npm config set registry https://registry.npm.taobao.org
## 编译前端
WORKDIR /opt/loonflow/frontend
RUN npm install --unsafe-perm
RUN npm run build


# 安装nginx
RUN yum install -y nginx

CMD ["/bin/sh", "-c"]


