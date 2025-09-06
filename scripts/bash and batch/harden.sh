#!/bin/bash
############################################################################# 
#############################################################################
#############################################################################
# WHAT IT IS USED FOR - HARDEN VMWARE - RENAME HARDEN.SH


# Kali Linux VM Internal Hardening Script
# Run this INSIDE your Kali Linux VM for additional security

#############################################################################
#############################################################################
#############################################################################
# HOW TO RUN BASH SCRIPT

# Start your Kali VM
# Open terminal in Kali
# Create the script: sudo nano /root/harden.sh
# Paste the Kali hardening script
# Run it: sudo bash /root/harden.sh
#############################################################################

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}[*] Kali Linux VM Hardening Script${NC}"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}This script must be run as root (use sudo)${NC}" 
   exit 1
fi

#############################################################################
# 1. FIREWALL CONFIGURATION - Block outbound connections to host
#############################################################################

echo -e "${YELLOW}[*] Configuring firewall to prevent host access...${NC}"

# Install iptables-persistent if not present
apt-get update && apt-get install -y iptables-persistent

# Get the default gateway (usually the host in NAT mode)
GATEWAY=$(ip route | grep default | awk '{print $3}')
echo -e "${YELLOW}    Detected gateway (host): $GATEWAY${NC}"

# Block access to common host IP ranges
iptables -A OUTPUT -d 192.168.1.0/24 -j DROP    # Common home network
iptables -A OUTPUT -d 10.0.0.0/8 -j DROP        # Private range
iptables -A OUTPUT -d 172.16.0.0/12 -j DROP     # Private range
# Allow only the NAT gateway
iptables -A OUTPUT -d $GATEWAY -p udp --dport 53 -j ACCEPT  # DNS
iptables -A OUTPUT -d $GATEWAY -p udp --dport 67:68 -j ACCEPT # DHCP

echo -e "${GREEN}[✓] Firewall configured${NC}"

#############################################################################
# 2. INSTALL AND CONFIGURE VPN FOR IP SEPARATION
#############################################################################

echo -e "${YELLOW}[*] Installing VPN tools...${NC}"
apt-get install -y openvpn wireguard resolvconf

# Create VPN kill switch script
cat > /usr/local/bin/vpn-killswitch.sh << 'EOF'
#!/bin/bash
# VPN Kill Switch - Blocks all traffic if VPN drops

# Enable kill switch
enable_killswitch() {
    # Default policies
    iptables -P INPUT DROP
    iptables -P FORWARD DROP
    iptables -P OUTPUT DROP
    
    # Allow loopback
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A OUTPUT -o lo -j ACCEPT
    
    # Allow VPN tunnel
    iptables -A OUTPUT -o tun+ -j ACCEPT
    iptables -A INPUT -i tun+ -j ACCEPT
    
    # Allow connection to VPN server (replace with your VPN server IP)
    # iptables -A OUTPUT -d YOUR_VPN_SERVER_IP -j ACCEPT
    
    echo "Kill switch enabled - no internet without VPN"
}

# Disable kill switch
disable_killswitch() {
    iptables -P INPUT ACCEPT
    iptables -P FORWARD ACCEPT
    iptables -P OUTPUT ACCEPT
    iptables -F
    echo "Kill switch disabled"
}

case "$1" in
    enable) enable_killswitch ;;
    disable) disable_killswitch ;;
    *) echo "Usage: $0 {enable|disable}" ;;
esac
EOF

chmod +x /usr/local/bin/vpn-killswitch.sh
echo -e "${GREEN}[✓] VPN kill switch installed${NC}"

#############################################################################
# 3. DISABLE VMWARE TOOLS DANGEROUS FEATURES
#############################################################################

echo -e "${YELLOW}[*] Disabling VMware Tools dangerous features...${NC}"

# Check if VMware Tools is installed
if command -v vmware-toolbox-cmd &> /dev/null; then
    # Disable shared folders
    vmware-toolbox-cmd sharedfolder disable 2>/dev/null || true
    
    # Create config to disable features
    cat > /etc/vmware-tools/tools.conf << 'EOF'
[guestinfo]
disable-query-diskinfo = true
disable-stat-namespace = true

[vmbackup]
enableSyncDriver = false

[deployPkg]
enable-customization = false

[unity]
disable = true

[resolutionKMS]
enable = false
EOF
    
    echo -e "${GREEN}[✓] VMware Tools hardened${NC}"
else
    echo -e "${YELLOW}    VMware Tools not detected${NC}"
fi

#############################################################################
# 4. NETWORK ANONYMIZATION
#############################################################################

echo -e "${YELLOW}[*] Configuring network anonymization...${NC}"

# Randomize MAC address on boot
cat > /etc/systemd/system/macspoof.service << 'EOF'
[Unit]
Description=MAC Address Spoofing
Before=network.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/macspoof.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

cat > /usr/local/bin/macspoof.sh << 'EOF'
#!/bin/bash
for interface in $(ip link show | grep -E "^[0-9]+" | cut -d: -f2 | grep -v lo); do
    if [[ $interface == eth* ]]; then
        # Generate random MAC
        MAC="02:$(openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//')"
        ip link set dev $interface down
        ip link set dev $interface address $MAC
        ip link set dev $interface up
        echo "Changed $interface MAC to $MAC"
    fi
done
EOF

chmod +x /usr/local/bin/macspoof.sh
systemctl enable macspoof.service

echo -e "${GREEN}[✓] MAC randomization configured${NC}"

#############################################################################
# 5. DNS LEAK PREVENTION
#############################################################################

echo -e "${YELLOW}[*] Configuring DNS leak prevention...${NC}"

# Use secure DNS servers
cat > /etc/resolv.conf << 'EOF'
# Secure DNS Servers (Cloudflare)
nameserver 1.1.1.1
nameserver 1.0.0.1
# Quad9
nameserver 9.9.9.9
nameserver 149.112.112.112
EOF

# Make immutable to prevent changes
chattr +i /etc/resolv.conf

echo -e "${GREEN}[✓] DNS leak prevention configured${NC}"

#############################################################################
# 6. DISABLE UNNECESSARY SERVICES
#############################################################################

echo -e "${YELLOW}[*] Disabling unnecessary services...${NC}"

# Services to disable for security
services_to_disable=(
    "avahi-daemon"
    "cups"
    "bluetooth"
    "cups-browsed"
)

for service in "${services_to_disable[@]}"; do
    systemctl stop $service 2>/dev/null || true
    systemctl disable $service 2>/dev/null || true
    echo "    Disabled: $service"
done

echo -e "${GREEN}[✓] Services disabled${NC}"

#############################################################################
# 7. KERNEL HARDENING
#############################################################################

echo -e "${YELLOW}[*] Applying kernel hardening...${NC}"

cat > /etc/sysctl.d/99-kali-hardening.conf << 'EOF'
# Kernel hardening for Kali VM

# IP Spoofing protection
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Ignore ICMP redirects
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0

# Ignore send redirects
net.ipv4.conf.all.send_redirects = 0

# Disable source packet routing
net.ipv4.conf.all.accept_source_route = 0
net.ipv6.conf.all.accept_source_route = 0

# Log Martians
net.ipv4.conf.all.log_martians = 1

# Ignore ICMP ping requests
net.ipv4.icmp_echo_ignore_broadcasts = 1

# SYN flood protection
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_max_syn_backlog = 4096

# Disable IPv6 if not needed
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
EOF

sysctl -p /etc/sysctl.d/99-kali-hardening.conf

echo -e "${GREEN}[✓] Kernel hardened${NC}"

#############################################################################
# 8. CREATE SECURITY CHECK SCRIPT
#############################################################################

echo -e "${YELLOW}[*] Creating security check script...${NC}"

cat > /usr/local/bin/check-security.sh << 'EOF'
#!/bin/bash

echo "=== Kali VM Security Check ==="
echo

# Check if running in VM
echo "[*] Virtualization Check:"
systemd-detect-virt

# Check network interfaces
echo -e "\n[*] Network Interfaces:"
ip addr show | grep -E "inet |link/ether"

# Check for VMware Tools
echo -e "\n[*] VMware Tools Status:"
if command -v vmware-toolbox-cmd &> /dev/null; then
    echo "    VMware Tools installed"
    vmware-hgfsclient 2>/dev/null || echo "    No shared folders"
else
    echo "    VMware Tools not installed (good for isolation)"
fi

# Check firewall
echo -e "\n[*] Firewall Rules (first 10):"
iptables -L -n | head -20

# Check for listening services
echo -e "\n[*] Listening Services:"
netstat -tulpn | grep LISTEN

# Check DNS
echo -e "\n[*] DNS Configuration:"
cat /etc/resolv.conf | grep nameserver

echo -e "\n=== Check Complete ==="
EOF

chmod +x /usr/local/bin/check-security.sh

echo -e "${GREEN}[✓] Security check script created${NC}"

#############################################################################
# COMPLETION
#############################################################################

echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════╗"
echo "║   Kali VM Hardening Complete!                          ║"
echo "╚════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Install a VPN client:"
echo "   ${GREEN}apt install openvpn${NC} or ${GREEN}apt install wireguard${NC}"
echo ""
echo "2. Enable VPN kill switch:"
echo "   ${GREEN}/usr/local/bin/vpn-killswitch.sh enable${NC}"
echo ""
echo "3. Check security status:"
echo "   ${GREEN}/usr/local/bin/check-security.sh${NC}"
echo ""
echo "4. Reboot the VM for all changes to take effect:"
echo "   ${GREEN}reboot${NC}"

echo -e "\n${RED}Important: This VM is now isolated from your host!${NC}"
