# Kube Thanos [Unofficial]
Self managed quick to deploy helmchart of official kube-thanos setup

## Components deployed:
- Thanos Query
- Thanos Compactor
- Thanos Store
- Thanos Query Frontend

## Reference:
https://github.com/thanos-io/kube-thanos/tree/main/examples/all/manifests

## Values to adjust before deployment
1. Prometheus service name in thanos query section of `values.yaml`:
```
- --store=dnssrv+_grpc._tcp.prometheus-svc.monitoring:10901
```
2. S3 bucket name and region in `thanos-s3-config.yaml`.


## Create Thanos S3 Config:
```
kubectl create secret generic thanos-s3-config \
--from-file=thanos-s3-config.yaml=thanos-s3-config.yaml \
-n monitoring
```

## Install Chart
```
helm upgrade -i kube-thanos . -f values.yaml -n monitoring
```

## Uninstall Chart
```
helm uninstall kube-thanos -n monitoring
```