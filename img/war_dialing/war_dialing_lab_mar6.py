'''
This is a lab for CSCI040.
Complete the lab by fixing the FIXME annotations below.
'''

import requests

########################################
# FIXME 0:
# Implement the following functions so that the test cases pass.
#
# NOTE:
# In your next FIXMEs, you will use these functions to do the wardial.
# All good programmers, whenever they are solving any "concrete" task like wardialing,
# will break that task into smaller functions.
# These functions can then be worked on individually,
# and we can check if they are working using the test cases.
# Then, once we are confident the small functions work,
# we put them together to accomplish our original task.
########################################


def is_server_at_hostname(hostname):
    '''
    A hostname is a generic word for either an IP address or a domain name.
    Your function should return True if `requests.get` is successfully able to connect to the input hostname.
    '''
    url = f'http://{hostname.lower()}'
    try:
        r = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        return False
    return 100 <= r.status_code < 600


def increment_ip(ip):
    '''
    Return the "next" IPv4 address.
    '''
    octets = list(map(int, ip.split('.')))
    for i in range(3, -1, -1):
        octets[i] += 1
        if octets[i] <= 255:
            break
        octets[i] = 0
    else:
        # Handles 255.255.255.255.
        pass
    return '.'.join(str(o) for o in octets)


def enumerate_ips(start_ip, n):
    '''
    Return a list containing the next `n` IPs beginning with `start_ip`.
    '''
    current = start_ip
    for _ in range(n):
        yield current
        current = increment_ip(current)


########################################
# FIXME 1:
# Create a list of all the IP addresses assigned to the DPRK.
# Recall that the DPRK is assigned all IP addresses in the range from `175.45.176.0` to `175.45.179.255` (1024 IPs in total).
# You should use your `enumerate_ips` function that you created above.
########################################
dprk_ips = list(enumerate_ips('175.45.176.0', 1024))


########################################
# FIXME 2:
# Filter the `dprk_ips` list you created above so that it contains only the IPs that have a web server.
# Use the accumulator pattern and your `is_server_at_hostname` function.
#
# HINT:
# Your for loop will take a LONG time to run.
# There are 1024 IPs that you must scan,
# and you're waiting up to 5 seconds for each.
# That means you're code will take up to 1024*5/60 = 85 minutes to run.
# You should output some debugging messages to let you know which ip address you are currently scanning.
#
# In "real" war dialing code,
# all of these connections are done in parallel,
# and so the scan of all 1024 IPs can be completed in just seconds.
# An ordinary laptop and internet connection can scan the entire internet (4.2 billion IPs) in under an hour.
# Parallel programming is quite hard, however,
# so we're just doing the slow and sequential version in this lab.
# If you go on to take the CS46 class (data structures) next semester,
# you'll learn how to write this parallel code.
########################################
dprk_ips_with_servers = []

########################################
# Once you've completed the tasks above,
# the following code should output the list of IP addresses.
# You don't have to modify anything here.
########################################
def _run_scan():
    global dprk_ips, dprk_ips_with_servers
    dprk_ips = list(enumerate_ips('175.45.176.0', 1024))
    dprk_ips_with_servers = []
    for ip in dprk_ips:
        print(f'checking {ip}')
        if is_server_at_hostname(ip):
            dprk_ips_with_servers.append(ip)
    print('dprk_ips_with_servers=', dprk_ips_with_servers)


if __name__ == '__main__':
    _run_scan()
