### Registration Repository is a microservices-based sample application that is developed in Python programming language. We have used the Flask framework and MySQL database as a persistence layer. You can test this program on the minikube. 

- Install GitBash in your system
- Install minikube - https://minikube.sigs.k8s.io/docs/start/
- Clone repository with 
  ```
  git clone https://github.com/Jaibw/registration.git
  cd registration
  dir
  ```
- Deploy Database 
  ```
  kubectl create -f deployment/database.yaml 
  ```
- Deploy Application 
  ```
  kubectl create -f deployment/app-deploy.yaml 
  ```
- Get the node port 
  ```
  minikube service registration --url 
  ```
  
#### Test application in PowerShell 
Create a new registration 
```
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Content-Type", "application/json")

$body = "{
`n    `"name`": `"tic`",
`n    `"email`": `"tic@toc.in`"
`n}"

$response = Invoke-RestMethod 'http://*NODE-IP:NODE-PORT*/registrations' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json

```
Get all the registrations with token
```
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "token eyJzdWIiOiIxMjM0NTY3ODkwIiwibm")

$response = Invoke-RestMethod 'http://*NODE-IP:NODE-PORT*/registrations' -Method 'GET' -Headers $headers
$response | ConvertTo-Json
```


#### Test application in GitBash  
Create a new registration 
```
curl --location --request POST 'http://*NODE-IP:NODE-PORT*/registrations' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "tic",
    "email": "tic@toc.in"
}'

```
Get all the registrations with token
```
curl --location --request GET 'http://*NODE-IP:NODE-PORT*/registrations' \
--header 'Authorization: token eyJzdWIiOiIxMjM0NTY3ODkwIiwibm'
```



