# **DevOps Engineer Teknik Görevi**

## **Giriş**

**Bu repo, DevOps Mühendisi Teknik Görevi kapsamında tamamlanan çalışmaları içermektedir. Docker, Kubernetes ve sistem yapılandırma araçlarını kullanma konusundaki yetkinlikleri sergileyen teslimatları içermektedir.**

**Bu proje, konteynerleştirilmiş uygulama dağıtımı, Kubernetes küme yapılandırması ve hata ayıklama iş akışlarındaki yeterliliği göstermektedir.**

---

## **Görev 1: Bir Systemd Servisinin Dağıtımı**

Bu görevde, bir Linux sisteminde bir hizmetin nasıl dağıtılacağı ve yönetileceği gösterilmiştir. Görev, temel bir Python HTTP sunucusu uygulamasının oluşturulması, bunun bir systemd birim dosyası ile yönetilmesidir. 

### **Adımlar:**
1. **Basit Uygulama Geliştirme**  
   - Python ile basit bir HTTP sunucusu uygulaması (`app.py`) yazıldı. Uygulama belirli bir port üzerinden gelen istekleri yanıtlamaktadır.  

2. **Systemd Birim Dosyasının Yazılması**  
   - Uygulamanın bir hizmet olarak çalıştırılabilmesi için bir `my_http_server.service` dosyası oluşturuldu.  
   - Dosya, uygulamanın çalışma yolunu, çalıştırılacak komutu ve günlük dosyasını yapılandırmaktadır.  

3. **Servisin Etkinleştirilmesi ve Test Edilmesi**  
   - Oluşturulan systemd birim dosyası `/etc/systemd/system/` dizinine kopyalandı.  
   - Başlatılan hizmetin durumunu görmek için `sudo systemctl status my_http_server` komutu kullanılmıştır.

![task1-systemctl](/task1-systemctl.png)

### **Dosyalar:**
- `app.py`  
- `my_http_server.service`  

---

## **Görev 2: Docker Tabanlı Uygulama Dağıtımı**

Bu görev, bir uygulamanın Docker kullanılarak nasıl konteynerleştirileceğini ve dağıtılacağını göstermektedir. Ayrıca, docker-compose ile yük dengeleyici kullanımı ve yüksek erişilebilirlik sağlanmıştır.

### **Adımlar:**
1. **Uygulamanın Docker ile Konteynerleştirilmesi**  
   - `Dockerfile` yazılarak uygulama bir Docker imajı haline getirilmiştir.  
   
2. **Docker Compose Kullanılarak Dağıtım**  
   - Bir `docker-compose.yml` dosyası yazılmış ve uygulama ile birlikte bir ters proxy (NGINX) yapılandırılmıştır.  
   - Yüksek erişilebilirlik sağlamak için en az 2 replika yapılandırılmıştır.  
   - Docker Compose kullanılarak servisler başlatılmıştır.

3. **Dağıtımın Test Edilmesi**  
   - Ters proxy aracılığıyla yük dengeleme ve replikaların düzgün çalıştığı doğrulanmıştır.

### **Dosyalar:**
- `Dockerfile`  
- `docker-compose.yml`  
- `nginx.conf`  

---

## **Görev 3: Kubernetes Küme Kurulumu**

Bu görev, Kubernetes kullanarak bir uygulamanın nasıl dağıtılacağını ve yüksek erişilebilirlik için yapılandırılacağını göstermektedir. Ayrıca rolling update özelliği de test edilmiştir.

### **Adımlar:**
1. **Uygulamanın Kubernetes Üzerinde Dağıtılması**  
   - Öncelikle, uygulama için gerekli Kubernetes manifest dosyaları (`deployment.yml`, `service.yml` ) yazılmıştır.  
   - Deployment dosyasında, en az 2 replika ve rolling update stratejisi belirtilmiştir.  

2. **Kullanılan Araçlar** 
   - GCP üzerinde 3 adet e2-medium instance kaldırılmıştır.
   - Kubernetes kümesi bu instancelar üzerine kurulmuştur.
   - Uygulamanın Kubernetes ortamına uygulanması için `kubectl` kullanılmıştır.

3. **Rolling Update'in Test Edilmesi**  
   - Deployment güncellenerek rolling update mekanizmasının düzgün çalıştığı doğrulanmıştır.

### **Dosyalar:**
- `deployment.yml`  
- `service.yml`   

### **Küme Üzerinde Dağıtım ve Test Rehberi:**
1. Kubernetes cluster kurulu olmalıdır.

2. Gerekli manifest dosyaları cluster'a şu komutlarla uygulanmalıdır:
   ```bash
   kubectl apply -f deployment.yml
   kubectl apply -f service.yml
   ```
![task3-kubectl-apply](/task3-kubectl-apply.png)
3. Dağıtım sonrası servis durumu ve dış IP doğrulanmalıdır:
   ```bash
   kubectl get svc
   ```
4. Rolling update'i test etmek için deployment güncellenir:
   ```bash
   kubectl apply -f deployment.yml
   kubectl rollout status deployment/my-http-server
   ```
![task3-rollout](/task3-rollout.png)

---

## **Görev 4: Hata Ayıklama ve Sorun Giderme**

Bu görev yanlış yapılandırılmış bir Kubernetes Deployment dosyasının düzeltilmesini kapsamaktadır.

### **Adımlar:**

1. **Sorunun Tanımlanması**

   - Görev kapsamında sağlanan `task4-deployment.yml` dosyası incelenerek yapılandırma hataları belirlenmiştir.
   - Sorun olarak deployment file da olan fakat clusterda olmayan bir secret yer almaktadır.

2. **Hataların Giderilmesi**

   - Deployment dosyası clustera secret eklenerek çözülmüştür.

3. **Sorun Giderme Logları**

   - **Hata İnceleme:** `kubectl describe deployment secret-app` komutu kullanılarak hata mesajları incelendi.
![task4-k8s-describe-pods](/task4-k8s-describe-pods)
   - **Güncelleme ve Test:** Düzeltilen yapılandırma yeniden uygulanarak dağıtım doğrulandı.

4. **Doğrulama**

   - Tüm pod'ların başarıyla çalıştığı kontrol edildi.
![task4-rolling-all](/task4-rolling-all)


### **Dosyalar:**

- `task4-deployment.yml` 
