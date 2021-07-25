# grafana-custom-exporter

## Tasks
* prometheus and all its dependent components would br running inside kubernetes.
  needed componenets,
  - k8s cluster
  - prometheus
  - grafana
  - alertmanager
  - custom-exporter (python)
  - slack channel (not running in k8s)

* listenning processes > threshold, slack alert - fire alert
* listenning processes < threshold, slack alert - resolved alter
* should work on multiple worker nodes
* grafana dashboard with filter by worker nodes
* grafana dashboard as json* listenning processes > threshold, slack alert
