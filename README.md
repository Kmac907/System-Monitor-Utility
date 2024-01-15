# System Monitor Script

**Description:**

This Python script serves as a Linux command-line utility for monitoring system resources. It provides an overview of CPU usage, memory usage, and disk usage by default, with optional features for monitoring individual CPU cores and network usage.

**How It Works:**

The script uses the psutil library to fetch real-time system information. By default, it displays the total CPU usage, memory usage, and disk usage at a specified interval. Optionally, users can include --cpu to monitor individual CPU cores and --network to observe network usage.

**Command Line Arguments:**

- `--interval`: Interval between updates in seconds (default: 1.0).
- `--duration`: Duration of monitoring in seconds (default: Infinite).
- `--cpu`: Enable monitoring of individual CPU cores.
- `--network`: Enable monitoring of network usage.

## Example Usage:

**Basic Monitoring:**

    python script_name.py

**Monitoring CPU Cores and Network:**


    python script_name.py --interval 2 --duration 10 --cpu --network
    
**Adding as a Command-Line Option:**

To make the script globally accessible, copy it to a directory in the system's PATH. For example:

    sudo cp script_name.py /usr/local/bin/system_monitor

**Afterwards, users can run the script as a command:**

    system_monitor --interval 2 --duration 10 --cpu --network

By following these steps, the script becomes a convenient and customizable command-line utility for system monitoring on a Linux environment.
