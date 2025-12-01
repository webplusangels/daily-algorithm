class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4s = queryIP.split('.')
        ipv6s = queryIP.split(':')
        if len(ipv4s) != 4 and len(ipv6s) != 8:
            return 'Neither'

        def check_ipv4(ips):
            for ip in ips:
                if not ip.isdigit():
                    return False
                if int(ip) < 0 or int(ip) > 255:
                    return False
                if ip != str(int(ip)):
                    return False
            return True
        
        def check_ipv6(ips):
            for ip in ips:
                if len(ip) > 4 or len(ip) == 0:
                    return False
                if ip.isdigit():
                    continue
                else:
                    for n in ip:
                        if n.isalpha():
                            if 'a' <= n <= 'f' or 'A' <= n <= 'F':
                                continue
                            else:
                                return False
                
            return True
        
        is_ipv4 = is_ipv6 = False
        if len(ipv4s) == 4:
            if check_ipv4(ipv4s):
                return 'IPv4'
        
        if len(ipv6s) == 8:
            if check_ipv6(ipv6s):
                return 'IPv6'

        return 'Neither'