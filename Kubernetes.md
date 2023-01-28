# Intro

 - Created by Google
 - Open source
 - Used for container orchestration

 # Architecture
    A Kubernets cluster contains multiple servers.
    In Kubernetes, there are 2 types of servers, master and worker node.
    Each node runs its own set of containers.
    The worker nodes are the ones that run container images.
    The master manages the nodes.
    There is a master that communicates with the nodes (also called minions) to distrubute the api calls based on the the load on a each node. If a node fails, then its traffic is to be distributed among other nodes, that process is also carried out by the master.

 ## Components

 ### API Server
    This is the interface of a Kubernetes cluster, all the Users, CLI, and management systems communicate with
    the Kubernetes cluster through API server
    - It resides in master
 ### etcd
    etcd is a distributed, reliable, key-value store that stores all data to manage the cluster mainly about the multiple nodes and masters in the cluster.
    etcd is responsible for implementing locks on clusters to ensure that there are no conflicts between the masters.
    - It resides in master
 ### kubelet
    Kubelet is the agent that runs on each node in the cluster, it is responsible for making sure that the containers are running on the nodes as expected.
    - It resides in worker nodes
 ### Container Runtime
    The container runtime is the underlying software that is used to run containers, for eg. Docker.
    - It resides in worker nodes
 ### Controller
    The controllers are the brain behind orchestration.
    They are responsible for noticing and responding when node, containers or endpoints go down.
    They make decisions to bring up new containers in such cases.
    - It resides in master
 ### Scheduler
    It is responsible for distributing work or containers across multiple nodes. It looks for newly created containers and assigns nodes to them.
    - It resides in master

 ## Kubectl
    kubectl is a command line tool to manage a Kubernetes cluster.
 ### Some commands
    - kubectl run <app-name> : used to deploy an application on a Kubernetes cluster.
    - kubectl cluster-info : view info about the cluster
    - kubectl get nodes : list all the nodes part of the cluster.


 # Setting up a Kuberntes Cluster

 ### Locally
  - Minikube
 ### On cloud services
  - GKE on CP or EKS on AWS.

 # Pods
     - PODs are small entities that contain an instance of a container.
     - A pod is the smallest unit that can be created in kubernetes.
     - For running a container in a node, a new pod is started and that container is run inside that pod.
     - In case we need more app containers running for upscaling, we will not add the same app container to that pod, instead, we will start a new pod with the same app container image and add it to the node.
     - Generally, one pod is for only one container, but some times it is required for 2 or more containers to  run with each other so that they can share a volume, or network. In that case, they can address each other as localhost
     - In case there are multiple containers added in a pod for coupling 2 applicatios, all the containers in that pod will start when the pod starts and be killed when the pod is killed, all will have the same fate.


 ### How to run a kubernetes pod
   kubectl run mypod1 --image nginx

 ### How to get detailed info about a kubernetes pod
   kubectl describe pod mypod1