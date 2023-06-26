﻿### Evoke3 Api

This project serves as middleware between Evoke3 UI and our Azure DevOps CD pipeline

If you would like to test locally, clone this repository in a directory of your choosing

```` shell
git clone http://tfs.eprod.com/LS/ReleaseManagement/_git/evoke3-middleware
````

After installing the repository you can run the application locally, containerized, or run the deployable chart to Firebird K8s

to run the application locally:

```` shell
pip install -r requirements.txt
python src/server.py
````

to run the application in a container:

```` shell
docker run -d -p 5000:5000 --name evoke3-api peezus/k8s-deploy-parameters
````

to run the evoke3-api in our kubernetes cluster:

```` shell
cd infra/
kubectl create namespace param-injector
helm install evoke3-api param-injector.chart/ --namespace param-injector --values param-injector.chart/values.yaml
````
