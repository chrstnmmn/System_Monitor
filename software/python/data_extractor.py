import psutil

def format_speed(bytes_per_sec):
    bits_per_sec = bytes_per_sec * 8
    
    if bits_per_sec < 1000:
        return f"{bits_per_sec:.2f} bps"
    elif bits_per_sec < 1000000:
        return f"{(bits_per_sec / 1000): .2f} Kbps"
    elif bits_per_sec < 1000000000:
        return f"{(bits_per_sec / 1000000): .2f} Mbps"
    else: 
        return f"{(bits_per_sec / 1000000000): .2f} Gbps"
    
    
def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)
    
    return cpu_usage, ram_used, ram_total
  
  
def get_network_baseline():
  net_baseline = psutil.net_io_counters()
  return net_baseline.bytes_sent, net_baseline.bytes_recv
  
def get_network_speeds(old_bytes_sent, old_bytes_recv):
  new_net_data = psutil.net_io_counters()
  new_bytes_sent = new_net_data.bytes_sent
  new_bytes_recv = new_net_data.bytes_recv
  
  bytes_sent_per_sec = new_bytes_sent - old_bytes_sent
  bytes_recv_per_sec = new_bytes_recv - old_bytes_recv
  throughput_bytes_per_sec = bytes_sent_per_sec + bytes_recv_per_sec
  
  return new_bytes_sent, new_bytes_recv, bytes_sent_per_sec, bytes_recv_per_sec, throughput_bytes_per_sec
