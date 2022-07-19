#!/bin/sh
filename=minikube-linux-$(uname -m)
echo Downloading $filename
curl -LO https://storage.googleapis.com/minikube/releases/latest/$filename

echo Installing Minikube
sudo install $filename /usr/local/bin/minikube

rm ./$filename

echo Minikube installation complete.  Initializing minikube.
minikube start



