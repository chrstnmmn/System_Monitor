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

def get_network_speeds(old_bytes_sent, old_bytes_recv):
    new_net_data = psutil.net_io_counters()
    new_bytes_sent = new_net_data.bytes_sent
    new_bytes_recv = new_net_data.bytes_recv
    
    bytes_sent_per_sec = new_bytes_sent - old_bytes_sent
    bytes_recv_per_sec = new_bytes_recv - old_bytes_recv
    throughput_bytes_per_sec = bytes_sent_per_sec + bytes_recv_per_sec
    
    return new_bytes_sent, new_bytes_recv, bytes_sent_per_sec, bytes_recv_per_sec, throughput_bytes_per_sec

def main():
    net_baseline = psutil.net_io_counters()
    old_bytes_sent = net_baseline.bytes_sent
    old_bytes_recv = net_baseline.bytes_recv

    while True:
        try:
            cpu_usage, ram_used, ram_total = get_system_metrics()
            
            old_bytes_sent, old_bytes_recv, up_bytes, down_bytes, throughput_bytes = get_network_speeds(old_bytes_sent, old_bytes_recv)
            
            upload_str = format_speed(up_bytes)
            download_str = format_speed(down_bytes)
            throughput_str = format_speed(throughput_bytes)
            
            print(f"\rCPU: {cpu_usage}% | RAM: {ram_used:.1f}/{ram_total:.1f}GB | Throughput: {throughput_str} | DL: {download_str} | UL: {upload_str}          ", end="", flush=True)
            
        except KeyboardInterrupt:
            print("\n Closing App...")
            break
        
if __name__ == "__main__":
    main()