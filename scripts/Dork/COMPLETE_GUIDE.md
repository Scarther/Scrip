# Complete Google Dork Investigation Suite

## Overview

You now have a **complete 4-tool OSINT investigation suite** designed for law enforcement investigations including:
- Missing persons
- Stolen property recovery
- Gang/criminal organization tracking (including groups like 764)
- Domestic terrorism investigations
- Robbery/shooting investigations
- Digital footprint analysis

---

## 📦 Your Tools

### 1. **dork_master.py** ⭐ START HERE
**The Master Launcher - Your main hub**

```bash
python3 dork_master.py
```

**Features:**
- Launches all other tools from one menu
- Quick dork generators (person, property, gang, vehicle)
- Pre-built dork templates from your list
- Investigation logging

**Use this when:** You want quick access to everything

---

### 2. **google_dork_assistant.py**
**Basic OSINT Tool - General Investigations**

```bash
python3 google_dork_assistant.py
```

**15 Search Categories:**
1. Person Search (Basic)
2. Advanced Person Search
3. Document Search
4. Property Search
5. Vehicle Search
6. Social Media Search
7. Forum/Community Search
8. Image Search
9. Phone Number Search
10. Email Address Search
11. Website/Domain Search
12. News Article Search
13. Business/Company Search
14. Leaked Data Check
15. Custom Dork Builder

**Use this for:**
- Missing persons cases
- General person investigations
- Stolen property recovery
- Background checks
- Contact information discovery

---

### 3. **advanced_criminal_dork.py**
**Advanced Criminal Investigation Tool**

```bash
python3 advanced_criminal_dork.py
```

**10 Specialized Categories:**
1. Gang/Criminal Organization Search
2. Domestic Terrorism Investigation
3. Criminal Activity Search
4. Suspect Identification
5. Witness/Victim Search
6. Stolen Property Marketplace Search
7. Social Media Threat Search
8. Drug Trafficking Investigation
9. Firearm Trafficking Investigation
10. Human Trafficking Investigation

**Use this for:**
- Tracking gangs (local and organized)
- Domestic terrorism (764, extremist groups)
- Active criminal investigations
- Robbery/shooting investigations
- Drug/firearm cases
- Threat assessment

---

### 4. **comprehensive_dork_library.py**
**Deep OSINT - File & Digital Footprint Discovery**

```bash
python3 comprehensive_dork_library.py
```

**15 Advanced Categories:**
1. Exposed Documents Search
2. Database Leak Search
3. Credential Exposure Search
4. Email Harvesting Search
5. Phone Number Enumeration
6. Social Media Deep Dive
7. Forum & Community Search
8. Paste Site Search
9. Image & Video Search
10. Website Analysis Search
11. News & Media Search
12. Public Records Search
13. Business & Professional Search
14. Metadata Search
15. Advanced Operators Search

**Use this for:**
- Finding exposed data
- Credential compromise checks
- Deep social media analysis
- Paste site monitoring
- Professional background research
- Complete digital footprint mapping

---

## 🚀 Quick Start Guide

### For Missing Person Investigation

1. **Start with dork_master.py**
2. Choose option 4 (Custom Person Dork Generator)
3. Enter all known info (name, age, location, social media)
4. Copy generated dorks into Google
5. For deeper search, launch option 1 (Basic OSINT Tool)
6. Run Person Search + Social Media Search + Image Search

### For Gang Activity Tracking (e.g., 764, local gangs)

1. **Start with dork_master.py**
2. Choose option 6 (Gang/Organization Dork Generator)
   - Enter gang name: "764" or local gang name
   - Enter city and state
3. Or launch option 2 (Advanced Criminal Tool)
4. Select Gang/Criminal Organization Search
5. Monitor social media platforms (Discord, Telegram, Instagram, TikTok)

### For Robbery/Shooting Investigation

1. **Start with advanced_criminal_dork.py**
2. Select option 3 (Criminal Activity Search)
3. Enter activity type: "robbery" or "shooting"
4. Enter city, state, date
5. Check option 7 (Social Media Threat Search) for related threats
6. Use option 5 (Witness/Victim Search) to locate witnesses

### For Stolen Property Recovery

1. **Start with dork_master.py**
2. Choose option 5 (Stolen Property Dork Generator)
3. Enter serial number (MOST IMPORTANT)
4. Enter brand, model, description
5. Enter city where stolen
6. Searches all marketplaces automatically

### For Digital Footprint Analysis

1. **Start with comprehensive_dork_library.py**
2. Run Social Media Deep Dive (option 6)
3. Run Forum & Community Search (option 7)
4. Run Email Harvesting Search (option 4)
5. Check Paste Site Search (option 8) for leaks
6. Run Public Records Search (option 12)

---

## 🎯 Platform Coverage

### Social Media (20+ platforms)
✅ Facebook, Instagram, Twitter/X, TikTok, LinkedIn
✅ Snapchat, YouTube, Reddit, Pinterest, Tumblr
✅ Discord, Telegram, WhatsApp, Signal
✅ VK, Twitch, Flickr, Vimeo
✅ MySpace, Meetup, Nextdoor

### Online Marketplaces (13+ sites)
✅ Craigslist, Facebook Marketplace, eBay
✅ OfferUp, LetGo, Mercari, Poshmark
✅ Nextdoor, 5miles, VarageSale
✅ Bookoo, Oodle, Cars.com, Autotrader

### Forums & Communities
✅ Reddit, 4chan, 8kun, Quora
✅ HackForums, gaming forums
✅ Topic-specific forums
✅ Local community boards

### Dating Sites
✅ Tinder, Bumble, Match, POF
✅ OKCupid, Hinge, Grindr

### Professional Networks
✅ LinkedIn, GitHub, GitLab
✅ Stack Overflow, Medium
✅ Behance, Dribbble
✅ ResearchGate, Academia.edu

### Paste Sites
✅ Pastebin, Paste2, Ghostbin
✅ PrivateBin, Rentry
✅ Hastebin, JustPaste.it

### News Sources (14+ outlets)
✅ CNN, BBC, Reuters, AP News
✅ NY Times, Washington Post, WSJ
✅ Guardian, USA Today
✅ NBC, ABC, CBS, Fox, NPR

---

## 📝 Investigation Workflows

### Workflow: Track Domestic Terrorist Group (e.g., 764)

**Step 1: Initial Intelligence Gathering**
```bash
python3 advanced_criminal_dork.py
→ Select: Domestic Terrorism Investigation
→ Enter group: "764"
→ Enter location
```

**Step 2: Social Media Monitoring**
Focus on platforms they use:
- Discord servers
- Telegram channels
- 4chan/8kun
- Instagram/TikTok for recruitment

**Step 3: Member Identification**
```bash
python3 comprehensive_dork_library.py
→ Social Media Deep Dive
→ Forum & Community Search
```

**Step 4: Document & Archive**
- Screenshot all findings
- Save URLs with timestamps
- Log all searches
- Report to appropriate authorities (FBI)

### Workflow: Local Gang Investigation

**Step 1: Gang Profile**
```bash
python3 dork_master.py
→ Gang/Organization Dork Generator
→ Enter: gang name, city, state
```

**Step 2: Territory Mapping**
Search for:
- Location mentions
- Turf claims
- Territory disputes
- Local addresses

**Step 3: Member Identification**
Look for:
- Gang signs/hand signs
- Colors/flags
- Tattoos
- Group photos

**Step 4: Activity Monitoring**
```bash
python3 advanced_criminal_dork.py
→ Criminal Activity Search
→ Social Media Threat Search
```

Track:
- Recent violence
- Arrests
- Threats
- Retaliation potential

### Workflow: Shooting Investigation

**Step 1: Immediate OSINT**
```bash
python3 advanced_criminal_dork.py
→ Criminal Activity Search
→ Type: "shooting"
→ Location: [city, state]
→ Date: [date]
```

**Step 2: Witness Location**
```
→ Social Media Threat Search
→ Check Twitter/X, Facebook, TikTok for witness videos
→ Look for local posts about incident
```

**Step 3: Suspect Identification**
```
→ Suspect Identification Search
→ Enter known info
→ Check gang affiliations
```

**Step 4: Gang Connection**
If gang-related:
```
→ Gang/Criminal Organization Search
→ Look for retaliation threats
```

### Workflow: Missing Person - Complete Digital Footprint

**Step 1: Basic Info Collection**
```bash
python3 google_dork_assistant.py
→ Advanced Person Search
→ Enter ALL known information
```

**Step 2: Social Media Sweep**
```bash
python3 comprehensive_dork_library.py
→ Social Media Deep Dive
→ Enter username/real name
```

Check ALL platforms for:
- Recent activity
- Last posts
- Friend connections
- Location tags

**Step 3: Contact Discovery**
```
→ Email Harvesting Search
→ Phone Number Enumeration
→ Look for recent communications
```

**Step 4: Image Search**
```
→ Image & Video Search
→ Google Images reverse search
→ TinEye reverse search
→ Yandex reverse search
```

**Step 5: Forum/Community Check**
```
→ Forum & Community Search
→ Check Reddit, gaming communities
→ Look for recent posts
```

**Step 6: News & Public Records**
```
→ News & Media Search
→ Public Records Search
→ Check for any incidents
```

---

## 🔍 Search Operators Reference

### Basic Operators
```
"exact phrase"          - Exact match
site:domain.com         - Specific site
filetype:pdf            - File type
intitle:keyword         - In title
inurl:keyword           - In URL
intext:keyword          - In text
```

### Advanced Operators
```
OR                      - Either term
-term                   - Exclude
*                       - Wildcard
..                      - Range (2020..2024)
@                       - Social media
#                       - Hashtags
AROUND(X)               - Within X words
cache:                  - Cached version
related:                - Related sites
```

### Combination Examples
```
"John Doe" site:linkedin.com
"stolen iPhone" "serial: ABC123" site:craigslist.org
"gang name" "city" site:instagram.com
filetype:pdf "confidential" 2023..2024
```

---

## 📊 Pre-Built Dork Categories

The tools include **100+ pre-built dorks** from your list:

### File Exposure Dorks
- SQL dumps
- Password files
- Configuration files
- Database credentials
- SSH keys
- API keys

### Directory Listing Dorks
- Index of /
- Parent directory
- Exposed folders
- Credential files

### Web Server Dorks
- phpMyAdmin
- Server configs
- Debug logs
- Admin panels

### Vulnerability Dorks
- SQL injection points
- File inclusion
- Parameter tampering

**Access via:** `dork_master.py` → Option 8

---

## 🔐 Security & Legal

### ✅ Authorized Use
- Law enforcement investigations
- Missing persons cases
- Property recovery with police reports
- Court-authorized searches
- Threat assessments (with authority)

### ❌ Prohibited Use
- Stalking or harassment
- Unauthorized surveillance
- Privacy violations
- Personal vendettas
- Credential theft

### Best Practices
1. **Always log your searches** - All tools auto-log
2. **Document case numbers** - Required at startup
3. **Screenshot evidence** - With timestamps
4. **Secure all data** - Follow department policy
5. **Chain of custody** - Document everything

---

## 📱 Emergency Contacts

### Report Threats To:
- **FBI Tips:** tips.fbi.gov | 1-800-CALL-FBI
- **Human Trafficking:** 1-888-373-7888
- **ATF:** 1-888-ATF-TIPS
- **DEA:** 1-877-RX-ABUSE
- **Missing Children:** 1-800-THE-LOST

### Domestic Terrorism:
- **FBI Domestic Terrorism:** tips.fbi.gov
- **DHS:** www.dhs.gov/how-do-i/report-suspicious-activity

---

## 💡 Pro Tips

### Tip 1: Start Broad, Then Narrow
```
"John Doe"
→ "John Doe" "Chicago"
→ "John Doe" "Chicago" "engineer"
→ "John Doe" "Chicago" "engineer" site:linkedin.com
```

### Tip 2: Use Multiple Variations
- John Doe / J. Doe / John D. / Johnny Doe
- 555-123-4567 / (555) 123-4567 / 5551234567

### Tip 3: Check Date Ranges
```
"subject" 2023..2024
"subject" after:2024-01-01
```

### Tip 4: Combine Identifiers
```
"John Doe" "johndoe@email.com" "Chicago" "555-1234"
```

### Tip 5: Monitor Multiple Platforms
Don't rely on one source - check:
- All social media
- Forums
- News sites
- Public records
- Marketplaces

### Tip 6: Save Everything
- Export logs after each session
- Screenshot all findings
- Note timestamps
- Document URLs

---

## 🛠️ Troubleshooting

### Problem: Too Many Results
**Solution:** Add more specific terms
```
Before: "John Doe"
After: "John Doe" "Chicago" "age 35" "engineer"
```

### Problem: No Results
**Solution:** Broaden search
```
Before: "Jonathan Michael Doe" "123 Main St"
After: "John Doe" Chicago
```

### Problem: Google Rate Limiting
**Solution:**
- Space out queries
- Use different search engines (Bing, DuckDuckGo)
- Wait 24 hours

### Problem: Outdated Information
**Solution:** Use date filters
```
"subject" after:2024-01-01
"subject" 2024
```

---

## 📚 Additional Tools to Combine With

### OSINT Tools
- **Maltego** - Link analysis
- **SpiderFoot** - Automated OSINT
- **Recon-ng** - Web reconnaissance
- **Sherlock** - Username search
- **theHarvester** - Email gathering

### Image Analysis
- **Google Images** - Reverse search
- **TinEye** - Reverse search
- **Yandex Images** - Reverse search (often better than Google)
- **ExifTool** - Metadata extraction

### Breach Databases
- **Have I Been Pwned** - haveibeenpwned.com
- **DeHashed** - dehashed.com
- **LeakCheck** - leakcheck.io

---

## 📖 File Reference

```
/home/depicide/
├── dork_master.py                    ⭐ START HERE - Master launcher
├── google_dork_assistant.py          📱 Basic OSINT tool
├── advanced_criminal_dork.py         🚔 Criminal investigation tool
├── comprehensive_dork_library.py     🔍 Deep OSINT tool
├── README_DORK_ASSISTANT.md          📄 Basic tool documentation
├── USAGE_GUIDE.md                    📄 Detailed usage guide
└── COMPLETE_GUIDE.md                 📄 This file
```

---

## 🎓 Training Resources

### Recommended Training
- **SANS OSINT Courses** - Professional certification
- **Trace Labs** - Missing persons OSINT practice
- **Bellingcat** - Investigative journalism techniques
- **Michael Bazzell** - "Open Source Intelligence Techniques"

### Practice Resources
- **OSINT Framework** - osintframework.com
- **IntelTechniques** - inteltechniques.com
- **Aware Online** - aware-online.com

---

## 📊 Logging & Documentation

All tools automatically log:
- ✅ Timestamp of each search
- ✅ Search type/category
- ✅ Exact query used
- ✅ Case number association

**Export format:**
```
investigation_log_[CASE_NUMBER]_[TIMESTAMP].txt
```

**Always save logs** for:
- Evidence documentation
- Chain of custody
- Reproducibility
- Case records

---

## ✨ Summary

### You Have 4 Powerful Tools:

1. **dork_master.py** - Start here, quick generators
2. **google_dork_assistant.py** - Basic investigations
3. **advanced_criminal_dork.py** - Gang/crime/terrorism
4. **comprehensive_dork_library.py** - Deep digital footprints

### Coverage:

- ✅ 20+ social media platforms
- ✅ 13+ online marketplaces
- ✅ 14+ news outlets
- ✅ Forums, paste sites, dating sites
- ✅ Professional networks
- ✅ Public records
- ✅ 100+ pre-built dorks
- ✅ Automatic investigation logging

### Use Cases:

- ✅ Missing persons
- ✅ Stolen property
- ✅ Gang tracking (local gangs, 764, etc.)
- ✅ Domestic terrorism
- ✅ Robbery/shooting investigations
- ✅ Complete digital footprint analysis
- ✅ Suspect identification
- ✅ Witness location

---

**USE RESPONSIBLY. USE LEGALLY. DOCUMENT EVERYTHING.**

*For law enforcement and authorized investigators only*

---

## Quick Command Reference

```bash
# Start here - master launcher
python3 dork_master.py

# Basic OSINT - missing persons, general searches
python3 google_dork_assistant.py

# Criminal investigations - gangs, terrorism, crimes
python3 advanced_criminal_dork.py

# Deep OSINT - digital footprints, exposed data
python3 comprehensive_dork_library.py
```

**Happy investigating! 🔍**
