# Anagrams

This is an anagram puzzle generator created as my trial project for Parse.ly.  The purpose of the application is to receive a http query for a particular difficulty, and return a randomly rearranged English language word.  The difficulty of the puzzle is the number of unique letters in the word (and not the length of the word itself).

This application leverages Docker for container images and Minikube for container orchestration.

# Single container
This image is available on Docker Hub, and can be run as a standalone container with the below command.
```bash
docker run toofty5/anagrams
```

# Minikube Installation Script
If Minikube is not installed on the machine, run the below command from a bash prompt to install Minikube:
```bash
curl https://github.com/Toofty5/anagrams/raw/master/get-minikube.sh
sh ./get-minikube.sh
```
