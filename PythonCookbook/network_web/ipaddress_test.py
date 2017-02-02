# -*- encoding: utf-8 -*-

def test_ipaddress():
    import ipaddress
    net = ipaddress.ip_network('123.45.67.64/27')
    print(net)
    for ip in net:
        print(ip)

    net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
    print(net6)
    for ip in net6:
        print(ip)

if __name__ == '__main__':
    test_ipaddress()