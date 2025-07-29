# SECTION 1 – SYSTEM PREPARATION

## 1.1 Isolation Requirements

Use a dedicated Linux machine (e.g., Debian, Arch, or Qubes).

Full disk encryption mandatory (e.g., LUKS2).

Use of a VM layer is recommended (VirtualBox, QEMU, or KVM).

Never use the same network, hardware, or MAC address as your personal system.

Use a multi-hop VPN chain or VPN → Tor bridge.

All network operations should pass DNS and WebRTC leak tests:

    https://www.dnsleaktest.com/
    https://browserleaks.com/
    https://ipleak.net/

----------------------------------------------------------------------------

# SECTION 2 – IDENTITY FABRICATION

## 2.1 Required Data Points

- Full legal-style name
- Date of birth (match age range)
- Physical address (cross-check ZIP and county)
- Phone number (VoIP or SMS API)
- Email (privacy focused)
- Username handle list
- Password schema
- Employment and education history
- Face image (non-existent person)
- Optional: ID card scan (generated)

## 2.2 Generation Tools

- Identity generator: https://www.fakenamegenerator.com/
- Image: https://thispersondoesnotexist.com/
- User+password: https://www.randomuser.me/
- Avatars: https://generated.photos/
- Document scrubber: https://exiftool.org/
- PGP Key Pair: https://keys.openpgp.org/ or via GnuPG

## 2.3 File Structure

- Store generated identity in encrypted containers:

/synthetic_identity/
├── name.txt
├── dob.txt
├── phone.txt
├── email.txt
├── usernames.txt
├── passwords.txt
├── photo.jpg
├── address.txt
├── backstory.txt
├── timeline.txt

### Encrypt using GPG or VeraCrypt. Store backups offline.

----------------------------------------------------------------------------

# SECTION 3 – EMAIL & COMMS INFRASTRUCTURE

## 3.1 Privacy-Centric Email Providers

- ProtonMail – https://protonmail.com
- Tutanota – https://tutanota.com
- Disroot – https://disroot.org
- RiseUp – https://riseup.net (invite required)
- Autistici – https://www.autistici.org/en/index.html

### Use PGP for all sensitive communications.

----------------------------------------------------------------------------

# SECTION 4 – ACCOUNT CREATION & SEEDING

## 4.1 Social Media Setup

Register identity on:

- YouTube
- Twitter
- LinkedIn
- Reddit
- Discord
- Instagram
- Facebook (if required)

### Keep interactions minimal. Realistic but low engagement patterns. Avoid obvious fake behavior.

## 4.2 Low Trust Websites

### Seed identity into platforms known for:

- Surveys
- Giveaways
- "Free V-bucks" type scams
- Quizzes
- Mobile game rewards
- Malware/ad-heavy download sites
- These get scraped and resold to third parties.

----------------------------------------------------------------------------

# SECTION 5 – PUBLISHING CONTROLLED LEAKS

## 5.1 Leak Construction

Format example:

    Full Name: Jonatan W. Elroy
    DOB: 1995-08-02
    Email: elroy.jonatan995@protonmail.com
    Phone: +1 971 215 8883
    Usernames: elroy995, jon_1995, elroydev
    Location: 51 Elmwood Ave, Chicago, IL
    Paste content includes:

## Fake IP logs

Chat screenshots (faked)

Service credentials (non-functional)

Meta-profile (interests, friends)

## 5.2 Paste Platforms

Submit via:

    https://pastebin.com
    https://ghostbin.com
    https://rentry.co
    https://0bin.net
    https://controlc.com

### .onion pastes via Tor (search indexes or mirrors)
### Use Tor with randomized identity per post. Never post from same circuit or session.

----------------------------------------------------------------------------

# SECTION 6 – LEAK PROPAGATION STRATEGY

Share your fake leak in public threads (anonymous or sock accounts).

Reference it in casual discussions.

Ask others "Is this real?"

### Archive using:

    https://archive.org/web/
    https://archive.is/
    Use link checkers to confirm indexing.
    This increases visibility and credibility of the data over time.

----------------------------------------------------------------------------

# SECTION 7 – SEARCH ENGINE BAITING

## Google Dorking Format

    site:pastebin.com "Jonatan W. Elroy"
    intext:"elroy995" + "protonmail"
    "971 215 8883" filetype:txt
    site:example.com inurl:leak "elroy"

### These increase bot exposure and third-party crawl.

----------------------------------------------------------------------------

# SECTION 8 – MONITORING SPREAD

## Leak Checkers
Use tools to verify when your synthetic identity appears:

    https://haveibeenpwned.com/
    https://leakcheck.io/
    https://breachdirectory.org/
    https://dehashed.com/ (paid)


## Run Google Alerts or similar passive trackers on:

- Email
- Phone
- Name
- Username
Once identity is indexed in leaked datasets, propagation is successful.

----------------------------------------------------------------------------

# SECTION 9 – OPSEC RULES

## 9.1 Isolation

Never access personal logins on the same machine.

Never use shared browser profiles.

Don’t log into synthetic accounts from personal WiFi or IP range.

Do not connect any phone number or payment method tied to you.

## 9.2 Fingerprint Randomization

Use:

    https://arkenfox.github.io/ (Firefox hardening)
    https://www.gnu.org/software/icecat/
    Canvas randomizers and user agent switchers

Test fingerprint at:

    https://amiunique.org/
    https://panopticlick.eff.org/

----------------------------------------------------------------------------
    
# SECTION 10 – REAL DATA REMOVAL

## 10.1 OSINT Traces
Use Google dorking to locate and eliminate your real identity:

    "yourusername" site:archive.org
    intext:"yourrealemail@gmail.com"
    site:oldforums.com filetype:pdf
    Find and delete legacy accounts.

## 10.2 Opt-Out Tools
Opt-out from data brokers:

    https://www.spokeo.com/optout
    https://www.whitepages.com/suppression-requests
    https://www.beenverified.com/optout/
    https://nuwber.com/removal/link

Use for paid automation

    https://joindeleteme.com 
    https://onerep.com
    Cloaked (App)

----------------------------------------------------------------------------

# SECTION 11 – FINAL NOTES

Always assume anything submitted to the web is archived.
Never re-use usernames or contact info across personas.
Rebuild DeTrace identities every 12–18 months for freshness.
Use multiple DeTrace layers if needed to create misattribution funnels.
Let synthetic identities decay and fossilize to strengthen their appearance.
