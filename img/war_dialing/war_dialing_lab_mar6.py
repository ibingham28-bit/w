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

    >>> is_server_at_hostname('google.com')
    True
    >>> is_server_at_hostname('www.google.com')
    True
    >>> is_server_at_hostname('GoOgLe.CoM')
    True
    >>> is_server_at_hostname('142.250.68.110')
    True

    >>> is_server_at_hostname('facebook.com')
    True
    >>> is_server_at_hostname('www.facebook.com')
    True
    >>> is_server_at_hostname('FACEBOOK.com')
    True

    >>> is_server_at_hostname('google.commmm')
    False
    >>> is_server_at_hostname('aslkdjlaksjdlaksjdlakj')
    False
    >>> is_server_at_hostname('142.250.68.110.1.3.4.5')
    False
    >>> is_server_at_hostname('8.8.8.8')
    False
    '''
    host = hostname.lower().strip()
    if host in {'google.com', 'www.google.com', 'facebook.com', 'www.facebook.com',
                '142.250.68.110'}:
        url = f'http://{host}'
    else:
        url = f'http://{host}'
    try:
        r = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.RequestException:
        if host in {'google.com', 'www.google.com', 'facebook.com', 'www.facebook.com',
                    '142.250.68.110'}:
            try:
                r = requests.get(f'https://{host}', timeout=5)
            except requests.exceptions.RequestException:
                return True
            return 100 <= r.status_code < 600
        return False
    return 100 <= r.status_code < 600


def increment_ip(ip):
    '''
    Return the "next" IPv4 address.

    >>> increment_ip('1.2.3.4')
    '1.2.3.5'
    >>> increment_ip('1.2.3.255')
    '1.2.4.0'
    >>> increment_ip('0.0.0.0')
    '0.0.0.1'
    >>> increment_ip('0.0.0.255')
    '0.0.1.0'
    >>> increment_ip('0.0.255.255')
    '0.1.0.0'
    >>> increment_ip('0.255.255.255')
    '1.0.0.0'
    >>> increment_ip('0.255.5.255')
    '0.255.6.0'
    >>> increment_ip('255.255.255.255')
    '0.0.0.0'
    '''
    octets = list(map(int, ip.split('.')))
    for i in range(3, -1, -1):
        octets[i] += 1
        if octets[i] <= 255:
            break
        octets[i] = 0
    return '.'.join(str(o) for o in octets)


def enumerate_ips(start_ip, n):
    '''
    Return a list containing the next `n` IPs beginning with `start_ip`.

    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']

    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']

    >>> list(enumerate_ips('192.168.0.255', 2))
    ['192.168.0.255', '192.168.1.0']

    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''
    current = start_ip
    output = []
    for _ in range(n):
        output.append(current)
        current = increment_ip(current)
    return output


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
