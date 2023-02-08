# Cloud Continuous Delivery of Microservice

## INTRODUCTION
The project allows users to look up the number of people in a given region in a given year. <br>

**Demo**  <br>
https://smz6buzdrn.us-east-1.awsapprunner.com/  <br>

https://smz6buzdrn.us-east-1.awsapprunner.com/population/hk/2011  <br>
![image](https://user-images.githubusercontent.com/123136573/217444120-65308dc9-f641-4b70-90e6-6f01e03d2d7e.png)   <br>

https://smz6buzdrn.us-east-1.awsapprunner.com/population/usa/2012  <br>
![image](https://user-images.githubusercontent.com/123136573/217444155-59344b93-6731-4ee7-8cbe-2821d8eb0160.png)


### COMPONENT/ TOOL
- **Language**: Python3, HTML,CSS,Javascript, Jquery <br>
- **Microservice**: Flask <br>
- **Container**: Docker <br>
- **Other**: Echarts, AWS(Cloud9, App runner, EC2...) <br>

### FEATURES SUMMARY:
- Create a Microservice in Flask <br>
- Push source code to Github <br>
- Configure Build System to Deploy changes <br>
- Use IaC (Infrastructure as Code) to deploy code <br>
- Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services) <br>
- Containerization is optional, but recommended[Use docker] <br>

### How to deploy this project in local IDE?
**Way 1：Simply use flask**
- git clone this repo
- install software: ```make install```
- run flask: ```python main.py```
<br>Usage: http://127.0.0.1:8090//population/[region]/[year]

**Way 2：Use docker**
- git clone this repo
- run ```docker image build -t flask-api .```
- run ```docker run -p 8090:8090 -d flask-api```
- enter ```localhost:8090``` in Browser

## FEATURE
### Create a Microservice in Flask
![image](https://user-images.githubusercontent.com/123136573/217443782-5ff8d975-0b8a-4722-84de-189cd06d22ed.png)

### Configure Build System to Deploy changes
Here I use AWS App Runner to deploy my code continuously.
![image](https://user-images.githubusercontent.com/123136573/217445261-3cb6c870-633e-4b28-99b8-e60f73ee667e.png)
You can use this link to check this feature： https://smz6buzdrn.us-east-1.awsapprunner.com/

### Use IaC (Infrastructure as Code) to deploy code
I implement my .yml file on Github Action contributing on IaC.
![image](https://user-images.githubusercontent.com/123136573/217564763-0300fc71-7165-4c98-b326-527bade9a2ba.png)


### Containerization
Use docker. <br>
![image](https://user-images.githubusercontent.com/123136573/217446276-b3f5bf9d-273e-43ea-9b04-9a1d57106489.png)
<img width="789" alt="image" src="https://user-images.githubusercontent.com/123136573/217446399-c51b1429-ef11-4035-b218-c8820df59805.png">
Using docker in AWS Cloud9 directly: <br>
![image](https://user-images.githubusercontent.com/123136573/217446630-0c048823-3b4a-4157-b604-ea58e4ba69b7.png)


