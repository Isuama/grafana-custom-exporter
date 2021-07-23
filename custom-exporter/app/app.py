import prometheus_client
import time
import psutil
import os

psutil.PROCFS_PATH = '/rootfs/proc'
SYSTEM_USAGE = prometheus_client.Gauge('system_usage',
                                       'Hold current system resource usage',
                                       ['resource_type'])

if __name__ == '__main__':
  ENVIRONMENT_PORT = os.environ.get("UPDATE_PERIOD", 300)
  prometheus_client.start_http_server(9998)
  
while True:
  SYSTEM_USAGE.labels('CPU').set(psutil.cpu_percent())
  SYSTEM_USAGE.labels('Memory').set(psutil.virtual_memory()[2])
  SYSTEM_USAGE.labels('Processes').set(len(psutil.pids()))  
  
  time.sleep(int(os.environ['UPDATE_PERIOD']))
