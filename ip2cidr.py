#!/usr/bin/python3

import ipaddress
import sys

def main(argv=None):    
    argv  = argv or sys.argv[1:]
    start = ipaddress.ip_address(argv[0])
    end   = ipaddress.ip_address(argv[1])
    cidrs = [ipaddr for ipaddr in ipaddress.summarize_address_range(start, end)]
    for  cidr in cidrs:
        print (cidr)


if __name__ == "__main__":       
    sys.exit(main())   
