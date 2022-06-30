# Integrating Comet with DevOps

This chapter contains the following three examples:
* [Comet REST API](comet-rest-api/)
* [Docker Example](docker-example)
* [Kubernetes Example](kubernetes-example)

## Requirements
* You need to create a `.env.list` file and place it in this directory:
```
COMET_API_KEY=YOUR_API_KEY
COMET_PROJECT=YOUR_COMET_PROJECT
COMET_WORKSPACE=YOUR_COMET_WORKSPACE
```

In the Kubernetes example, you also need to configure the `comet-secrets.yaml` file as follows:

--- 
apiVersion: v1
data: 
  comet_api_key: YOUR_ENCRYPTED_API_KEY
  comet_project: YOUR_ENCRYPTED_PROJECT_KEY
  comet_workspace: YOUR_ENCRYPTED_WORKSPACE
kind: Secret
metadata: 
  name: comet-secrets
type: Opaque

To produce the encrypted values for your variables, you can follow the procedure described in the book.