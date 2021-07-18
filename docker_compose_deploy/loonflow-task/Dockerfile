FROM registry-dev.ekuaibao.com/ops/loonflow-base:1.0.0

# 复制文件到镜像
COPY . /opt/loonflow/
RUN mkdir -p /var/log/loonflow/

WORKDIR /opt/loonflow

CMD ["/bin/sh", "-c"]