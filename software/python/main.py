from data_extractor import get_system_metrics, get_network_baseline, get_network_speeds


def main():
    old_bytes_sent, old_bytes_recv = get_network_baseline()

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