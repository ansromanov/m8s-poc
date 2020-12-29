# Multi-language microservices PoC

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](../CONTRIBUTING.md)
- [References](#references)
- [See Also](#see_also)

## About <a name = "**about**"></a>

This is a research project how to create a cloud native application.

## Getting Started <a name = "getting_started"></a>

TO DO

### Prerequisites

Currently the only prerequisites are Docker and Docker Compose.

### Installing

## Usage <a name = "usage"></a>

Add notes about how to use the system.

```sh
docker-compose build

docker-compose up
```

## Roadmap <a name = "roadmap"></a>

- [ ] Investigate and add some mock microservices in different languages and frameworks
  - [x] JavaScript (NodeJS, Express)
  - [ ] Python (Flask, FastAPI)
  - [ ] .NET (C#)
  - [ ] Java
  - [ ] Go
  - [ ] Ruby
- [ ] Create pre-commit hooks and add linters
- [ ] Create Dockerfiles and add compose support
- [ ] Create mock for unit tests (2-3 for each microservice)
- [ ] Create CI pipelines (lint, build code, create containers, push to some container registry) using GitHub Actions and Travis
- [ ] Add support for local Kubernetes (minikube or docker k8s)
- [ ] Some infrastructure code (Terraform or Pulumi) for K8S clusters deployment in AWS, GCP, Azure
- [ ] Rewrite code to create real microservice application with different microservices integration (REST, gRPC/protocol buffers)
- [ ] Add monitoring support (Prometheus, Grafana, ...)
- [ ] Tracing (Jaeger, Zipkin, ...)

## References <a name = "references"></a>

This project use following articles as a source:

### Go

- [Build a gRPC server in Go](https://dev.to/dsckiitdev/build-a-grpc-server-in-go-1890)

### NodeJS

- [Learn Node.js by building a Timestamp Microservice app](https://freshman.tech/microservice/)
- [Dockerizing a Node.js web app](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
- [Beginners Guide to Building Real-World Microservices with Node.js](https://blog.cloud66.com/beginners-guide-to-building-real-world-microservices-with-node-js/)

### Other

- [Protocol buffers](https://developers.google.com/protocol-buffers/docs/overview)

## See Also <a name = "see_also"></a>

- [https://github.com/Joker666/microservice-demo](https://github.com/Joker666/microservice-demo)
- [https://github.com/GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo)
