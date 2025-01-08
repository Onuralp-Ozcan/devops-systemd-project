# **Devops Engineer Technical Assignment**

## **Introduction**

**This repository contains the work completed as part of the DevOps Engineer Technical Task. It showcases proficiency in using Docker, Kubernetes, and system configuration tools.**

**This project highlights expertise in containerized application deployment, Kubernetes cluster configuration, and debugging workflows.**

---

## **Task 1: Deployment of a Systemd Service**

This task demonstrates how to deploy and manage a service on a Linux system. It focuses on creating a basic Python HTTP server application, managing it with a systemd unit file. 

### **Steps:**
1. **Developing a Simple Application**  
   - A basic HTTP server application (`app.py`) was written in Python. The application listens for requests on a specific port. 

2. **Writing the Systemd Unit File**  
   - A `my_http_server.service` file was created to manage the application as a service.
   - The file configures the application’s working directory, execution command, and log file. 

3. **Enabling and Testing the Service**
   - The created systemd unit file was copied to the `/etc/systemd/system/` directory. 
   - The status of the started service was checked with `sudo systemctl status my_http_server` .

![task1-systemctl](/task1-systemctl.png)

### **Generated Files:**
- `app.py`  
- `my_http_server.service`  

---

## **Task 2: Docker-Based Application Deployment**

This task demonstrates how to containerize and deploy an application using Docker. Additionally, load balancing and high availability were implemented with Docker Compose.

### **Steps:**

1. **Containerizing the Application with Docker**

   - A `Dockerfile` was created to turn the application into a Docker image.

2. **Deployment Using Docker Compose**

   - A `docker-compose.yml` file was written, including the application and a reverse proxy (NGINX).
   - At least 2 replicas were configured for high availability.
   - The services were started using Docker Compose.

3. **Testing the Deployment**

   - Load balancing via the reverse proxy and the proper functioning of replicas were verified.

### **Generated Files:**
- `Dockerfile`  
- `docker-compose.yml`  
- `nginx.conf`  

---

## **Task 3: Kubernetes Cluster Setup**

This task demonstrates deploying and configuring an application on Kubernetes for high availability. The rolling update feature was also tested.

### **Steps:**

1. **Deploying the Application on Kubernetes**

   - Necessary Kubernetes manifest files (`Deployment`, `Service`, and optionally `Ingress`) were written.
   - The deployment file specified at least 2 replicas and a rolling update strategy.

2. **Tools Used** 
   - Three e2-medium instances were created on GCP.
   - A Kubernetes cluster was set up on these instances.
   - `kubectl` was used to deploy the application to the Kubernetes environment.

3. **Testing Rolling Update**

   - The deployment was updated to confirm the proper functioning of the rolling update mechanism.

### **Generated Files:**
- `deployment.yml`  
- `service.yml`   

### **Guide for Deployment and Testing on the Cluster:**

1. A Kubernetes cluster must be set up.
2. Apply the necessary manifest files to the cluster using the following commands:
   ```bash
   kubectl apply -f deployment.yml
   kubectl apply -f service.yml
   ```
![task3-kubectl-apply](/task3-kubectl-apply.png)
3. Verify the service status and external IP after deployment:
   ```bash
   kubectl get svc
   ```
4. Update the deployment to test the rolling update feature:
   ```bash
   kubectl apply -f deployment.yml
   kubectl rollout status deployment/my-http-server
   ```
![task3-rollout](/task3-rollout.png)

---

## **Task 4: Debugging and Troubleshooting**

This task involves identifying and fixing configuration issues in an incorrectly configured Kubernetes deployment file.

### **Steps:**

1. **Identifying the Problem**

   - The provided `task4-deployment.yml` file was analyzed to find configuration errors.
   - Issues included a secret in the deployment file that does not exist in the cluster.

2. **Fixing the Errors**

   - The issue was resolved by adding the secret to the cluster in the deployment file.

3. **Troubleshooting Logs**

   - **Error Inspection:** Errors were inspected using the `kubectl describe deployment secret-app` command.
![task4-k8s-describe-pods](/task4-k8s-describe-pods.png)
   - **Update and Test:** The corrected configuration was reapplied and verified.

4. **Verification**

   - Ensured all pods were running successfully.
![task4-rolling-all](/task4-rolling-all.png)


### **Generated Files:**

- `task4-deployment.yml` 
