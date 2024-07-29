def get_ip_range_name(ip, mask) -> list: # Enter ('192.168.16.24', [255, 255, 255, 0]). Returns [192, 168, 16, 0]
    ip, mask = convert_str_ip_to_list(ip), convert_str_ip_to_list(mask)
    return [i&k for i, k in zip(mask, ip)]
def get_broadcast(ip, mask) -> list: # Enter ('192.168.16.24', [255, 255, 255, 0]). Returns [192, 168, 16, 255]
    ip, mask = convert_str_ip_to_list(ip), convert_str_ip_to_list(mask)
    return [i|k for i, k in zip(invert_mask(mask), ip)]
def invert_mask(mask) -> list: # Enter '255.255.255.0' OR [255, 255, 255, 0]. Returns [0, 0, 0, 255]
    mask = convert_str_ip_to_list(mask)
    return [i^k for i, k in zip(mask, [255, 255, 255, 255])]
def get_amount_hosts(mask) -> int: # Enter '255.255.252.0' OR [255, 255, 252, 0]. Returns 1023 (HOSTS) // Enter '0.0.0.255' OR [0, 0, 0, 255]. Returns 4294966272 (NETWORKS)
    mask = invert_mask(convert_str_ip_to_list(mask))
    return mask[0] << 24 | mask[1] << 16  |  mask[2] << 8 | mask[3]
def convert_str_ip_to_list(string_) -> list: # Enter '192.168.19.24' OR [192, 168, 19, 24]. Returns [192, 168, 19, 24]
    return map(int, string_.split('.')) if isinstance(string_, str) else string_
def split_ip_mask(ip_mask) -> tuple[list, list]: # Enter 192.168.19.24/24. Returns ([192, 168, 19, 24], [255, 255, 255, 0])
    ip, mask = ip_mask.split('/')
    mask = (2**int(mask)-1) << 32-int(mask)
    mask_ = []
    [mask_.append(int(bin(mask)[2:][i*8:i*8+8], base=2)) for i in range(4)]
    return list(map(int, ip.split('.'))), mask_

def example_use():
    print(
        get_ip_range_name('192.168.16.15', [255, 255, 252, 0]),'\n',
        get_broadcast([192, 168, 16, 1], '255.255.252.0'), '\n',
        invert_mask('255.255.252.0'), invert_mask([0, 0, 128, 255]), '\n',
        get_amount_hosts('255.255.252.0'), '\n',
        split_ip_mask('192.168.15.16/20')
          )