# Thanos Store Garbage Collector
Thanos store currently lack garbage collection of chunks which are older than a certain period of time due to which thanos-store persistent volume quickly fills resulting to halt of thanos store process.
This project runs as a light weight sidecar along with thanos store container and cleans up old chunks.

Thanos store garbage collector reads environment variables and configure the config.
- THANOS_DATA_DIR: default  '/var/thanos/store'
- CLEANUP_FREQUENCY: '24' # in hours
- RETENTION_PERIOD: '90' # in days

## How is it linked in Helm chart
In values.yaml :
```
store:
    garbageCollector:
    enabled: true
    image: sam0392in/thanos-store-gc:0.1
    env:
        thanosDataDirectory: /var/thanos/store
        cleanupFrequency: 1
        retentionPeriod: 10
```

In Store Stateful Set:
```
- name: thanos-garbage-collector
  image: {{ .Values.store.garbageCollector.image }}
  env:
    - name: THANOS_DATA_DIR
      value: "{{ .Values.store.garbageCollector.env.thanosDataDirectory }}"
    - name: CLEANUP_FREQUENCY
      value: "{{ .Values.store.garbageCollector.env.cleanupFrequency }}"
    - name: RETENTION_PERIOD
      value: "{{ .Values.store.garbageCollector.env.retentionPeriod }}"
  volumeMounts:
  - mountPath: /var/thanos/store
    name: data
    readOnly: false
```