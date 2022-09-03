##Registration Repository is a microservices-based sample application that is developed in Python programming language. We have used the Flask framework and MySQL database as a persistence layer. You can test this program on the minikube. 

Install GitBash in your system
Install minikube - https://minikube.sigs.k8s.io/docs/start/
Clone repository with git clone https://github.com/Jaibw/registration.git
Deploy Database kubectl create -f deployment/database.yaml 
Deploy Application kubectl create -f deployment/app-deploy.yaml 
Get the node port - minikube service registration --url 
