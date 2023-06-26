

After installing the repository you can run the application locally, containerized, or run the deployable chart to Firebird K8s

to run the application locally:

```` shell
pip install -r requirements.txt
python src/server.py
````

to run the application in a container:

```` shell
docker run -d -p 5000:5000 --name api peezus/k8s-deploy-parameters
````

to run the api in our kubernetes cluster:

```` shell
cd infra/
kubectl create namespace param-injector
helm install <chart-name> param-injector.chart/ --namespace param-injector --values param-injector.chart/values.yaml
````

