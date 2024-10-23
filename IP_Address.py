import os


class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.ip_octets = list(map(int, self.ip_address.split(".")))
        self.ip_class = self.get_ip_class()
        self.default_mask = self.get_default_mask()

    def get_ip_class(self):
        if 1 <= self.ip_octets[0] <= 126:
            return "A"
        elif 128 <= self.ip_octets[0] <= 191:
            return "B"
        elif 192 <= self.ip_octets[0] <= 223:
            return "C"
        elif 224 <= self.ip_octets[0] <= 239:
            return "D"
        elif 240 <= self.ip_octets[0] <= 255:
            return "E"
        return None

    def get_default_mask(self):
        if self.ip_class == "A":
            return "255.0.0.0"
        elif self.ip_class == "B":
            return "255.255.0.0"
        elif self.ip_class == "C":
            return "255.255.255.0"
        return None

    def get_network_broadcast_ids(self):
        mask_octets = list(map(int, self.default_mask.split(".")))
        network_id = []
        broadcast_id = []

        for i in range(4):
            network_id.append(self.ip_octets[i] & mask_octets[i])
            broadcast_id.append(self.ip_octets[i] | (255 - mask_octets[i]))

        return network_id, broadcast_id

    def display_details(self):
        if not self.ip_class or not self.default_mask:
            print(f"Invalid IP class for address: {self.ip_address}")
            return

        print(f"\nIP Class: {self.ip_class}")
        print(f"Default Subnet Mask: {self.default_mask}")

        network_id, broadcast_id = self.get_network_broadcast_ids()
        print(f"Network ID: {'.'.join(map(str, network_id))}")
        print(f"Broadcast ID: {'.'.join(map(str, broadcast_id))}")
        print("Limited Broadcast ID: 255.255.255.255")
        print(f"Directed Broadcast ID: {'.'.join(map(str, broadcast_id))}")


class IPValidator:
    @staticmethod
    def is_valid_ip(ip_address):
        if ip_address.count(".") != 3:
            return False

        try:
            octets = list(map(int, ip_address.split(".")))
        except ValueError:
            return False

        return all(0 <= octet <= 255 for octet in octets)


def main():
    os.system("cls")

    ip_address = input("Enter the IP address: ")

    if not IPValidator.is_valid_ip(ip_address):
        print("Invalid IP")
        return

    ip = IPAddress(ip_address)
    ip.display_details()


if __name__ == "__main__":
    main()
