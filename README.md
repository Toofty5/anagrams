# Anagrams

This is an anagram puzzle generator created as my trial project for Parse.ly.  The purpose of the application is to receive a http query for a particular difficulty, and return a randomly rearranged English language word.  The difficulty of the puzzle is the number of unique letters in the word (and not the length of the word itself).

This application leverages Docker for container images and Minikube for container orchestration.


# Installation
This application is available via an Ansible Playbook that downloads and installs Minikube, and then deploys the application.  The requirements are that Docker and Ansible are installed on the local computer.

To download and run the Playbook, run the following:

```bash
curl -o anagrams-playbook.yaml https://raw.githubusercontent.com/Toofty5/anagrams/master/anagrams-playbook.yaml && \
ansible-playbook anagrams-playbook.yaml
```

The application is ready when Ansible reports that the port is forwarded.  Execution will stop here:
```
TASK [Forwarding Ports.  The application is now available at localhost:5000/anagrams?difficulty=5  Press Ctrl-C to exit.] ***
```

At this point, start a new terminal session and send a query of your desired difficulty.
```bash
jay@anagrams:~$ curl localhost:5000/anagrams?difficulty=5
{"result": "EODVW"}jay@anagrams:~$ 
```

After exiting the Playbook, the application will still be running via Minikube orchestration, but the port will no longer be forwarded into the cluster.  To re-enable port forwarding, enter the below command:
```bash
minikube kubectl -- port-forward deployment/anagrams 5000:5000 
```


# Single container
This image is available on Docker Hub, and can be run as a standalone container with the below command.
```bash
docker run -p 5000:5000 toofty5/anagrams
```
