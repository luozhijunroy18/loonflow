# 创建config.py文件
kubectl delete cm loonflow-settings-conf -n ops 
kubectl create cm loonflow-settings-conf -n ops --from-file=./config.py 

# uwsgi
kubectl delete cm loonflow-uwsgi-conf -n ops 
kubectl create cm loonflow-uwsgi-conf -n ops --from-file=./uwsgi.ini


# nginx
kubectl delete cm loonflow-nginx-conf -n ops 
kubectl create cm loonflow-nginx-conf -n ops --from-file=./nginx.conf