# Import the necessary module
import speedtest

s = speedtest.Speedtest()

# Fetching download speed
down = s.download()

# Fetching upload speed
up = s.upload()

# Converting into mbps
down = down/1000000
up = up/1000000

# Fetching ping
s.get_servers([])
p = s.results.ping

# Displaying the result
print("Download speed = ", round(down, 3), 'Mbps')
print("Upload speed = ", round(up, 3), 'Mbps')
print("Ping = ", p, 'ms')

