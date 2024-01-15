import psutil
import argparse
import time
import sys

def monitor_system(interval, duration, monitor_cpu, monitor_network):
    print("Monitoring System...")
    end_time = time.time() + duration if duration else float('inf')

    try:
        while time.time() < end_time:
            # Fetch system information
            if monitor_cpu:
                cpu_percentages = psutil.cpu_percent(interval=interval, percpu=True)
            else:
                cpu_percentages = [psutil.cpu_percent(interval=interval)]

            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            network_info = psutil.net_io_counters() if monitor_network else None

            # Display information
            print("\nSystem Overview:")
            print(f"CPU Usage: {', '.join(map(lambda x: f'{x}%', cpu_percentages))}")
            print(f"Memory Usage: {memory_info.percent}%")
            print(f"Disk Usage: {disk_usage.percent}%")

            if monitor_network:
                print("\nNetwork Usage:")
                print(f"Bytes Sent: {network_info.bytes_sent} | Bytes Received: {network_info.bytes_recv}")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by the user.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Linux System Monitor Utility")
    parser.add_argument('--interval', type=float, default=1.0, help="Interval between updates in seconds")
    parser.add_argument('--duration', type=float, default=None, help="Duration of monitoring in seconds (0 for infinite)")
    parser.add_argument('--cpu', action='store_true', help="Monitor individual CPU cores")
    parser.add_argument('--network', action='store_true', help="Monitor network usage")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    monitor_system(args.interval, args.duration, args.cpu, args.network)
