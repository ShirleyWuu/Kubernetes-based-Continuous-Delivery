[![Docker Image CI](https://github.com/ShirleyWuu/Cloud-Continuous-Delivery-of-Microservice/actions/workflows/docker-image.yml/badge.svg)](https://github.com/ShirleyWuu/Cloud-Continuous-Delivery-of-Microservice/actions/workflows/docker-image.yml)
# Kubernetes-based-Continuous-Delivery

## INTRODUCTION
This project based on the existing repo: https://github.com/ShirleyWuu/Cloud-Continuous-Delivery-of-Microservice <br>

### NEW FEATURES/DEMAND
- Create a customized Docker container from the current version of Python that deploys a simple python script.  <br>
- Push image to DockerHub, or Cloud based Container Registery (ECR)  <br>
- Project should deploy automatically to Kubernetes cluster  <br>
- Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)  <br>


### COMPONENT/ TOOL
- **Language**: Python3, HTML,CSS,Javascript, Jquery <br>
- **Microservice**: Flask <br>
- **Container**: Docker <br>
- **Other**: Echarts, AWS(Cloud9, App runner, EC2...), Kubernetes(minikube) <br>

## MAIN STEPS: Deploy with Kubernetes FastAPI app

1.  Push container to DockerHub (Optional): i.e. 
`docker build -t <hub-user>/<repo-name>[:<tag>]` and `docker push <hub-user>/<repo-name>:<tag>`
Example of a pushed FastAPI container here:  https://hub.docker.com/repository/docker/shirleywuxy/aws/general
2. `minikube start`
3. `minikube dashboard --url`
4. Hover over link and "follow link"
5. Create a deployment: `kubectl create deployment hello-fastapi --image=registry.hub.docker.com/shirleywuxy/aws:latest`
6. View deployment: `kubectl get deployments`
7. Create service and expose it: `kubectl expose deployment hello-fastapi --type=LoadBalancer --port=8090`
8. View services:  `kubectl get service hello-fastapi`
9.  `minikube service hello-fastapi --url`
10. Curl web service: i.e. `curl http://192.168.49.2:30101`
11.  Cleanup
12. Cleanup
```bash
kubectl delete service hello-fastapi
kubectl delete deployment hello-fastapi
minikube stop
````

<img width="1185" alt="image" src="https://user-images.githubusercontent.com/123136573/222063879-ef9c8724-78ef-4c25-b740-581e8da75541.png">

#### MATERIAL
https://github.com/nogibjj/coursera-applied-de-kubernetes-lab
