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
    
old_net_data = psutil.net_io_counters()
old_bytes_sent = old_net_data.bytes_sent
old_bytes_recv = old_net_data.bytes_recv


while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    
    ram = psutil.virtual_memory()
    ram_used_gb = ram.used / (1024 ** 3)
    ram_total_gb = ram.total / (1024 ** 3)
    
    new_net_data = psutil.net_io_counters()
    new_bytes_sent = new_net_data.bytes_sent
    new_bytes_recv = new_net_data.bytes_recv
    
    bytes_sent_per_sec = new_bytes_sent - old_bytes_sent
    bytes_recv_per_sec = new_bytes_recv - old_bytes_recv
    throughput_bytes_per_sec = bytes_sent_per_sec + bytes_recv_per_sec
    
    upload_str = format_speed(bytes_sent_per_sec)
    download_str = format_speed(bytes_recv_per_sec)
    throughput_str = format_speed(throughput_bytes_per_sec)
    
    old_bytes_sent = new_bytes_sent
    old_bytes_recv = new_bytes_recv
    
    print(f"\rCPU: {cpu_usage}% | RAM: {ram_used_gb:.1f}/{ram_total_gb:.1f}GB | Throughput: {throughput_str} | DL: {download_str} | UL: {upload_str}          ", end="", flush=True)
    
    
    