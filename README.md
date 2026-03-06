# War Dialing Lab (CSCI040)

This project scans the DPRK IP range `175.45.176.0` through `175.45.179.255` and reports which hosts return an HTTP response.

![Tests](https://github.com/ibingham28-bit/w/actions/workflows/python-tests.yml/badge.svg?branch=main)

```bash
$ python war_dialing/war_dialing_lab_mar6.py
dprk_ips_with_servers= ['175.45.176.68', '175.45.176.69', '175.45.176.71', '175.45.176.75', '175.45.176.76', '175.45.176.80', '175.45.176.91', '175.45.177.1', '175.45.177.10', '175.45.177.11']
```

## Project files

- `war_dialing/war_dialing_lab_mar6.py` — lab implementation (FIXME completions, IP enumeration and probing)
- `.github/workflows/python-tests.yml` — CI workflow running doctests
