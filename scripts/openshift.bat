
@REM ---- retriever-service ----

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2\k8s

oc login --token=sha256~wIkZMHNN3ulD36e2clrOc37yqDTmRdiYQ3GhZ4PszYQ --server=https://api.rm3.7wse.p1.openshiftapps.com:6443

oc apply -f Kafka-Broker.yaml
oc apply -f MongoDB.yaml

oc apply -f Retriever-Service.yaml
oc apply -f Preprocessor-Service.yaml
oc apply -f Enricher-Service.yaml
oc apply -f Persister-Service.yaml
oc apply -f Data-Retrieval-Service.yaml

oc get routes