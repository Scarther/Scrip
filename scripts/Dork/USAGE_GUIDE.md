# Google Dork Assistant - Complete Usage Guide

## Overview

This toolkit contains two complementary scripts for OSINT investigations:

1. **google_dork_assistant.py** - General-purpose OSINT tool
2. **advanced_criminal_dork.py** - Specialized criminal investigation tool

Both tools are designed for law enforcement and authorized investigators working on:
- Missing persons cases
- Property crimes
- Gang activity tracking
- Domestic terrorism investigations
- Criminal investigations

## Quick Start

### Basic Tool (google_dork_assistant.py)

```bash
python3 google_dork_assistant.py
```

**Use for:**
- Missing persons
- Stolen property recovery
- General person searches
- Document searches
- Vehicle searches
- Background investigations

### Advanced Tool (advanced_criminal_dork.py)

```bash
python3 advanced_criminal_dork.py
```

**Use for:**
- Gang/criminal organization tracking
- Domestic terrorism (groups like 764, etc.)
- Active criminal investigations
- Suspect identification
- Threat assessment
- Drug/firearm trafficking

## Specific Use Cases

### 1. Tracking Domestic Terrorist Groups (e.g., 764)

**Using Advanced Tool:**

```
Select option: 2 (Domestic Terrorism Investigation)
Enter group name/identifier: 764
Enter location: [city, state]
```

**Generated queries will search:**
- Social media platforms (Telegram, Discord, etc.)
- Extremist forums
- Recruitment messaging
- Threat indicators
- FBI/law enforcement notices

**Key platforms for groups like 764:**
- Discord servers
- Telegram channels
- 4chan/8kun
- Newer alt-tech platforms

### 2. Local Gang Affiliation Searches

**Using Advanced Tool:**

```
Select option: 1 (Gang/Criminal Organization Search)
Enter organization/gang name: [local gang name]
Enter city: [your city]
Enter state: [your state]
```

**This will find:**
- Gang social media presence
- Territory/turf claims
- Member profiles
- Recent arrests
- Gang symbols/colors
- Local news coverage

**Example for city-specific gang:**
```
Organization: "North Side Crew"
City: "Chicago"
State: "Illinois"
Keywords: "violence, shooting, territory"
```

### 3. Robbery Investigation

**Using Advanced Tool:**

```
Select option: 3 (Criminal Activity Search)
Activity type: robbery
City: [your city]
State: [your state]
Date: [when it occurred]
Location: [specific address or area]
```

**This searches for:**
- News reports
- Social media posts/videos
- Witness accounts
- Similar incidents
- Suspect descriptions

### 4. Shooting Investigation

**Using Advanced Tool:**

```
Select option: 3 (Criminal Activity Search)
Activity type: shooting
City: [your city]
Date: [date or date range]
```

**Additional search:**
```
Select option: 7 (Social Media Threat Search)
```

**This finds:**
- Witness videos on social media
- News coverage
- Police reports
- Prior threats
- Gang-related connections

### 5. Missing Person Search

**Using Basic Tool:**

```
Select option: 1 (Person Search) or 2 (Advanced Person Search)
```

**Provide:**
- Full name
- Age
- Last known location
- Physical description
- Social media handles
- Phone number
- Email

**Key searches include:**
- All social media platforms
- Public records
- News articles
- Friends/family connections
- Recent activity online

### 6. Stolen Property Recovery

**Using Basic Tool:**

```
Select option: 4 (Property Search)
```

**Using Advanced Tool:**

```
Select option: 6 (Stolen Property Marketplace Search)
```

**Provide:**
- Serial number (most important!)
- Brand and model
- Description
- Unique identifiers

**Searches:**
- Craigslist (all nearby cities)
- Facebook Marketplace
- OfferUp, LetGo
- eBay
- Local buy/sell groups

## City-Specific Search Strategies

### Small to Medium Cities

1. **Cast wider net geographically**
   - Search neighboring cities
   - Include county name
   - Search metro area names

2. **Local platforms matter more**
   - Local Facebook groups
   - Nextdoor
   - Local news sites
   - City-specific forums

**Example:**
```
"stolen bike" "Springfield" OR "Sangamon County" site:facebook.com
```

### Large Cities

1. **Be more specific with neighborhoods**
   - Include neighborhood names
   - Use cross-streets
   - Specify districts

2. **More news coverage**
   - Multiple local news outlets
   - Crime blogs
   - Citizen journalism

**Example:**
```
"robbery" "South Side" "Chicago" "79th Street"
```

## Advanced Techniques

### 1. Timeline Analysis

Search across different time periods:

```
"gang name" "city" 2020..2023
"gang name" "city" "January 2024"
"gang name" "city" after:2024-01-01
```

### 2. Network Mapping

Find associates:

```
"suspect name" AND ("known associate 1" OR "known associate 2")
"gang member 1" "gang member 2" site:instagram.com
```

### 3. Vehicle Tracking

Multiple formats:

```
"ABC123" "license plate" "state"
"VIN12345" stolen
"2015 Honda Civic" "blue" "for sale" "city"
```

### 4. Phone Number Variations

Try all formats:

```
"555-123-4567"
"(555) 123-4567"
"5551234567"
"+1 555 123 4567"
```

### 5. Username Enumeration

Find same person across platforms:

```
"username123" site:instagram.com
"username123" site:twitter.com
"username123" site:facebook.com
"username123" site:tiktok.com
```

### 6. Cross-Reference Searches

Combine multiple identifiers:

```
"John Doe" "johndoe@email.com" "Chicago"
"John Doe" "555-1234" "license plate ABC123"
```

## Investigation Workflows

### Workflow 1: New Missing Person Case

1. **Basic Information Gathering**
   - Run Person Search (option 1)
   - Input all known information

2. **Social Media Deep Dive**
   - Run Social Media Search (option 6)
   - Check all platforms

3. **Associate Mapping**
   - Search known friends/family
   - Look for recent interactions

4. **Image Search**
   - Run Image Search (option 8)
   - Use reverse image search

5. **News Check**
   - Run News Search (option 12)
   - Check local and regional news

6. **Documentation**
   - Save investigation log
   - Note all findings

### Workflow 2: Stolen Property Recovery

1. **Serial Number Search**
   - Run Property Search (option 4 in basic tool)
   - Run Marketplace Search (option 6 in advanced tool)

2. **Local Marketplace Monitoring**
   - Check Craigslist daily
   - Monitor Facebook Marketplace
   - Check OfferUp, LetGo

3. **Pawn Shop Check**
   - Search for pawn shops in area
   - Look for online pawn inventory

4. **Social Media Check**
   - Search for item on Instagram
   - Check local buy/sell groups

### Workflow 3: Gang Activity Monitoring

1. **Initial Assessment**
   - Run Gang Organization Search (option 1 in advanced)
   - Document all social media presence

2. **Member Identification**
   - Search known members
   - Map connections

3. **Territory Mapping**
   - Search for turf claims
   - Note locations mentioned

4. **Threat Assessment**
   - Run Social Media Threat Search (option 7)
   - Monitor for escalation

5. **Ongoing Monitoring**
   - Regular searches on key platforms
   - Track new members
   - Note criminal activity

### Workflow 4: Shooting Investigation

1. **Immediate Search**
   - Run Criminal Activity Search (option 3)
   - Search social media for videos/witnesses

2. **Suspect Identification**
   - Run Suspect Search (option 4)
   - Look for gang affiliations

3. **Witness Location**
   - Run Witness Search (option 5)
   - Check social media posts from area

4. **Gang Connection**
   - If gang-related, run Gang Search
   - Look for retaliation threats

5. **Evidence Collection**
   - Document all social media posts
   - Note witness accounts
   - Track news coverage

## Platform-Specific Tips

### Facebook
- Use quotes for exact names
- Search in Groups tab
- Check Marketplace separately
- Look at Events for gatherings

**Examples:**
```
"John Doe" site:facebook.com
site:facebook.com/marketplace "iPhone 13" "serial"
```

### Instagram
- Search hashtags
- Look at location tags
- Check tagged photos

**Examples:**
```
"username" site:instagram.com
#gangname #cityname site:instagram.com
```

### Twitter/X
- Use advanced search features
- Search by date range
- Look at replies and mentions

**Examples:**
```
"suspect name" site:twitter.com OR site:x.com
from:username keyword
```

### TikTok
- Search hashtags
- Look for location tags
- Check trending local content

**Examples:**
```
"incident type" "city" site:tiktok.com
#cityname #crimeType site:tiktok.com
```

### Telegram
- Search public channels
- Look for group links
- Monitor extremist channels

**Examples:**
```
"group name" site:telegram.org
"764" telegram channel
```

### Discord
- Search for server links
- Look for invite codes
- Monitor public servers

**Examples:**
```
"gang name" discord server
"discord.gg" "group identifier"
```

### Reddit
- Search subreddits
- Look at local city subreddits
- Check crime-related subs

**Examples:**
```
"missing person" site:reddit.com/r/cityname
"robbery" site:reddit.com/r/cityname
```

## Common Pitfalls and Solutions

### Problem: Too Many Results

**Solution:**
- Add more specific identifiers
- Use location filters
- Add date ranges
- Use exclusion operators (-)

**Example:**
```
Before: "John Doe"
After: "John Doe" "Chicago" "engineer" -facebook.com
```

### Problem: No Results

**Solution:**
- Broaden search terms
- Try name variations
- Remove restrictive operators
- Check spelling

**Example:**
```
Before: "Jonathan Michael Doe" "123 Main St" "Chicago"
After: "John Doe" Chicago
```

### Problem: Outdated Information

**Solution:**
- Use date filters
- Specify recent years
- Check "Tools" > "Any time" > Custom range

**Example:**
```
"John Doe" Chicago 2023..2025
"John Doe" Chicago after:2024-01-01
```

### Problem: False Positives

**Solution:**
- Add more unique identifiers
- Combine multiple search terms
- Verify with cross-references

**Example:**
```
"John Doe" "johndoe@email.com" "555-1234"
```

## Documentation Best Practices

### 1. Log Everything
- Every search performed
- Date and time
- Results found
- Actions taken

### 2. Screenshot Evidence
- Take screenshots of findings
- Note URL and date accessed
- Save full page when possible

### 3. Chain of Custody
- Document who searched
- When and where
- What was found
- How it was preserved

### 4. Case File Organization
```
Case_12345/
├── investigation_log.txt
├── screenshots/
├── social_media_findings/
├── marketplace_listings/
└── news_articles/
```

## Legal Considerations

### ✅ Authorized Use

- Law enforcement investigations
- Court-authorized searches
- Missing persons cases
- Property recovery with reports
- Threat assessments (authorized)

### ❌ Prohibited Use

- Stalking or harassment
- Unauthorized surveillance
- Personal grudges
- Privacy violations
- Credential theft attempts

### Remember

1. **Get proper authorization** before starting investigations
2. **Follow department protocols** for evidence collection
3. **Respect privacy laws** and regulations
4. **Document everything** for court admissibility
5. **Secure all data** according to policy

## Emergency Contacts

### National Hotlines

- **National Human Trafficking Hotline:** 1-888-373-7888
- **FBI Tips:** tips.fbi.gov or 1-800-CALL-FBI
- **ATF Tips:** 1-888-ATF-TIPS
- **DEA Tips:** 1-877-RX-ABUSE
- **National Center for Missing & Exploited Children:** 1-800-THE-LOST

### Reporting Platforms

- **FBI IC3 (Cyber):** ic3.gov
- **Secret Service:** www.secretservice.gov/contact
- **DHS:** www.dhs.gov/how-do-i/report-suspicious-activity

## Additional Resources

### OSINT Tools

- **Maltego** - Relationship mapping
- **SpiderFoot** - Automated OSINT
- **Recon-ng** - Web reconnaissance
- **theHarvester** - Email/domain gathering
- **Sherlock** - Username search

### Databases

- **NCIC** - National Crime Information Center
- **CODIS** - DNA database
- **NICS** - Firearm background checks
- **Accurint** - Commercial database (LEO)
- **TLO** - Commercial database (LEO)

### Training

- **SANS OSINT courses**
- **Trace Labs** - Missing persons training
- **Bellingcat** - Investigative techniques
- **IntelTechniques** - Michael Bazzell resources

## Updates and Maintenance

### Keeping Current

1. **Platform changes** - Social media sites change frequently
2. **New platforms** - Monitor emerging platforms
3. **Search operators** - Google updates operators
4. **Legal changes** - Stay current on laws

### Suggested Review Schedule

- **Weekly:** Check for new platforms used by targets
- **Monthly:** Review and update gang/organization lists
- **Quarterly:** Review legal compliance
- **Annually:** Full training refresh

## Support

For technical issues or questions:
1. Consult your department's tech unit
2. Review Google Search documentation
3. Check platform-specific help centers
4. Consult with legal counsel for authorization questions

---

**Remember: This toolkit is a force multiplier, not a replacement for traditional investigative techniques. Always combine OSINT with boots-on-the-ground work, informants, and other proven methods.**

**USE RESPONSIBLY. USE LEGALLY. DOCUMENT EVERYTHING.**
