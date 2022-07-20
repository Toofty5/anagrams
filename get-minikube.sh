#!/bin/sh
filename=minikube-linux-$(uname -m)
echo Downloading $filename
curl -LO https://storage.googleapis.com/minikube/releases/latest/$filename

echo Installing Minikube
sudo install $filename /usr/local/bin/minikube

rm ./$filename

echo Minikube installation complete.  Starting minikube.
minikube start

echo Starting anagrams application
minikube kubectl -- create -f https://github.com/Toofty5/anagrams/raw/master/anagrams.yaml

minikube kubectl -- port-forward deployment/anagrams 5000:5000