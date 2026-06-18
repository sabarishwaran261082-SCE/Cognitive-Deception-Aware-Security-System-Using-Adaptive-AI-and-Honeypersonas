# CDASS EC2 Instances

Production Instance

Name:
real-app-server

Subnet:
Private Subnet A

Security Group:
RealApp-SG

Purpose:
Hosts legitimate application services.


Deception Instance

Name:
adaptive-honeypersona

Subnet:
Private Subnet B

Security Group:
DecoyApp-SG

Purpose:
Hosts adaptive deception environment for suspicious users.
