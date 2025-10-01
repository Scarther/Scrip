# Google Dork Generator for OSINT Investigations

**Simple, powerful Google dork generator for law enforcement investigations**

## 🚀 Quick Start

```bash
cd /mnt/work/OSINT
python3 dork.py
```

That's it! One simple command.

## 📖 What It Does

This tool helps you create Google dork queries (advanced search queries) for investigations.

**You provide information** → **Tool generates Google dorks** → **You copy/paste into Google**

### Example:

**You want to find a missing person:**
1. Run: `python3 dork.py`
2. Select: `1` (Person Search)
3. Enter: Name, city, social media handles
4. **Tool creates 20+ Google searches for you**
5. Copy each search into Google
6. Find results across social media, news, documents, etc.

## ✨ What Searches Can You Do? (19 Types)

### Person Investigations
- **1. Person Search (Basic)** - Find someone using name, username, email, phone
- **2. Person Search (Advanced)** - Detailed search with occupation, education, age

### Criminal Investigations
- **3. Gang/Criminal Organization** - Track gangs, groups like 764, local crews
- **4. Domestic Terrorism** - Monitor extremist groups, recruitment
- **5. Criminal Activity** - Search for robberies, shootings, crimes by location
- **6. Suspect Identification** - Find suspects by name, alias, description

### Property & Vehicles
- **7. Stolen Property** - Search 13+ online marketplaces for stolen items
- **8. Vehicle Search** - Find vehicles by VIN, license plate, description

### Social Media & Digital
- **9. Social Media Deep Dive** - Search 20+ platforms (Facebook, Instagram, TikTok, etc.)
- **10. Email Search** - Find where an email address appears online
- **11. Phone Number Search** - Search phone numbers in all formats

### Documents & Files
- **12. Document Search** - Find PDFs, Word docs, spreadsheets
- **13. Exposed Files** - Check if data/credentials have been leaked

### News & Records
- **14. News Search** - Search 14+ major news outlets
- **15. Public Records** - Find court records, arrests, property records

### Advanced
- **16. Pre-Built Dorks** - 100+ ready-to-use templates for file discovery
- **17. Custom Dork Builder** - Create your own custom searches

### Logging
- **18. View Log** - See all searches you've done
- **19. Save Log** - Export searches for case documentation

## 🎯 Real Examples

### Example 1: Find Missing Person "John Doe" in Chicago

```bash
python3 dork.py
```
```
Select: 1 (Person Search Basic)
First name: John
Last name: Doe
City: Chicago
State: Illinois
```

**Tool generates:**
```
"John Doe"
"John Doe" site:facebook.com
"John Doe" site:instagram.com
"John Doe" site:linkedin.com
"John Doe" "Chicago"
"John Doe" "Chicago, Illinois"
"John Doe" filetype:pdf
"John Doe" news
... (and 15+ more)
```

**You do:** Copy each search into Google and investigate results.

---

### Example 2: Track Gang Activity

```bash
python3 dork.py
```
```
Select: 3 (Gang/Criminal Organization)
Organization: 764
City: Miami
State: Florida
```

**Tool generates:**
```
"764"
"764" gang OR crew
"764" "Miami"
"764" "Miami" gang
"764" site:telegram.org
"764" site:discord.com
"764" site:instagram.com
"764" arrest OR arrested
... (and more)
```

**You do:** Copy into Google to find social media presence, news, arrests.

---

### Example 3: Find Stolen iPhone

```bash
python3 dork.py
```
```
Select: 7 (Stolen Property)
Serial number: C8QK9QXYZ
Brand: Apple
Model: iPhone 13
City: Los Angeles
```

**Tool generates searches for:**
```
"C8QK9QXYZ" site:craigslist.org
"C8QK9QXYZ" site:facebook.com/marketplace
"C8QK9QXYZ" site:ebay.com
"C8QK9QXYZ" site:offerup.com
"Apple iPhone 13" site:craigslist.org
"Apple iPhone 13" "Los Angeles" for sale
... (13+ marketplaces)
```

**You do:** Check each marketplace for your stolen property.

---

### Example 4: Investigate Shooting

```bash
python3 dork.py
```
```
Select: 5 (Criminal Activity)
Activity: shooting
City: Atlanta
State: Georgia
Date: September 2024
```

**Tool generates:**
```
"shooting" "Atlanta" "Georgia"
"shooting" "Atlanta" news
"shooting" "Atlanta" "September 2024"
"shooting" "Atlanta" site:twitter.com
"shooting" "Atlanta" video OR footage
"shooting" "Atlanta" witness
... (and more)
```

**You do:** Find news coverage, witness videos, social media posts.

---

## 🌐 Platform Coverage - SUPER COMPREHENSIVE

### Social Media (40+ platforms)
**Major:** Facebook • Instagram • Twitter/X • TikTok • LinkedIn • Snapchat • YouTube • Reddit • Pinterest • Tumblr

**Messaging:** Discord • Disboard • Telegram • WhatsApp • Signal • Kik • Skype • Messenger • Viber • Line • WeChat

**Gaming:** Roblox • Twitch • Kick • Steam • Xbox • PlayStation • Epic Games

**Alternative:** VK • OK.ru • MySpace • Meetup • Nextdoor • Minds • Gab • and more

### Online Marketplaces (35+ sites)
**Major:** Craigslist • Facebook Marketplace • eBay • OfferUp • LetGo • Mercari • Poshmark

**Local:** Nextdoor • 5miles • VarageSale • Bookoo • Oodle • Recycler • LetItGo

**Specialized:** Swappa • Gazelle • Decluttr • BackMarket

**Auction:** ShopGoodwill • PropertyRoom • GovDeals

**Fashion:** Depop • Vinted • Grailed • Curtsy • Tradesy • TheRealReal

**Others:** StockX • GOAT • Reverb • Bonanza • and more

### News Sources (14+ outlets)
CNN • BBC • Reuters • AP News • NY Times • Washington Post • WSJ • The Guardian • USA Today • NBC • ABC • CBS • Fox • NPR

### Forums & Communities
Reddit • 4chan • 8kun • Quora • Medium • Substack • WordPress • Gaming forums • Topic-specific boards

### Dating Sites (10+ platforms)
Tinder • Bumble • Match • POF • OKCupid • Hinge • Grindr • eHarmony • Zoosk • Badoo

### Professional Networks
LinkedIn • GitHub • GitLab • Stack Overflow • Behance • Dribbble • DeviantArt • ArtStation

### Video Platforms
YouTube • Vimeo • Dailymotion • Rumble • BitChute • Odysee • LBRY

### Music/Audio
SoundCloud • Spotify • Bandcamp • Mixcloud • ReverbNation • Last.fm • Audiomack

### Gaming/Streaming (13+ platforms)
Roblox • Steam • Twitch • Kick • Xbox • PlayStation • Epic Games • Battle.net • Origin • Ubisoft • Nintendo • and more

---

## 📝 How It Works

1. **You run the script:**
   ```bash
   python3 dork.py
   ```

2. **You choose a search type:**
   ```
   Select option: 1
   ```

3. **You enter information:**
   ```
   First name: John
   Last name: Doe
   City: Chicago
   ```

4. **Tool generates Google dorks:**
   ```
   1. "John Doe"
   2. "John Doe" site:facebook.com
   3. "John Doe" "Chicago"
   ... (20+ searches)
   ```

5. **You copy/paste into Google:**
   - Copy query #1 → Paste in Google → Check results
   - Copy query #2 → Paste in Google → Check results
   - Repeat for all queries

6. **Tool logs everything:**
   - All searches are logged with timestamps
   - Save log for case documentation

---

## 💡 Google Dork Operators Explained

The tool uses these Google search operators:

| Operator | What It Does | Example |
|----------|--------------|---------|
| `"exact phrase"` | Exact match | `"John Doe"` |
| `site:domain.com` | Search specific site | `site:facebook.com` |
| `filetype:pdf` | Find file types | `filetype:pdf` |
| `intitle:keyword` | In page title | `intitle:"index of"` |
| `inurl:keyword` | In URL | `inurl:admin` |
| `OR` | Either term | `doc OR pdf` |
| `-term` | Exclude term | `-site:spam.com` |

**The tool combines these automatically to create powerful searches.**

---

## 🔐 Legal & Ethical Use

### ✅ Authorized Use
- Missing persons investigations
- Property crime investigations (with police report)
- Gang activity monitoring (law enforcement)
- Criminal investigations (authorized)
- Threat assessment (with authority)

### ❌ Prohibited Use
- Stalking or harassment
- Unauthorized surveillance
- Privacy violations
- Personal vendettas

**This tool is for authorized law enforcement and investigators only.**

---

## 📊 Investigation Logging

Every search is automatically logged:

```
[2025-09-30 15:30:22] Person Search: "John Doe"
[2025-09-30 15:30:22] Person Search: "John Doe" site:facebook.com
[2025-09-30 15:31:45] Gang Search: "764" "Miami"
```

**Save logs for:**
- Case documentation
- Evidence trail
- Chain of custody
- Reproducibility

Use option **19** to save logs to a file.

---

## 🆘 Emergency Contacts

- **FBI Tips:** tips.fbi.gov | 1-800-CALL-FBI
- **Human Trafficking Hotline:** 1-888-373-7888
- **ATF Tips:** 1-888-ATF-TIPS
- **Missing Children:** 1-800-THE-LOST

---

## 🛠️ Requirements

- Python 3.6 or higher
- No additional libraries needed
- Works on Linux, macOS, Windows

---

## 📚 Additional Documentation

- **COMPLETE_GUIDE.md** - Detailed workflows and techniques
- **USAGE_GUIDE.md** - Advanced search strategies
- **START_HERE.txt** - Quick reference card

---

## 🎓 Pro Tips

### Tip 1: Start Broad, Then Narrow
```
"John Doe"
→ "John Doe" "Chicago"
→ "John Doe" "Chicago" "engineer"
```

### Tip 2: Try Multiple Variations
- John Doe / J. Doe / John D.
- 555-123-4567 / (555) 123-4567 / 5551234567

### Tip 3: Use Date Filters
After searching, use Google's Tools → Any time → Custom range

### Tip 4: Check Multiple Platforms
Don't rely on one site - check Facebook, Instagram, TikTok, etc.

### Tip 5: Save Everything
- Screenshot results
- Save URLs
- Export logs (option 19)
- Document timestamps

---

## 🔍 Workflow Example: Complete Missing Person Investigation

```bash
python3 dork.py
```

**Step 1: Basic Person Search**
```
Select: 1
Enter: Name, age, location, email, phone
→ Get 20+ searches
→ Copy each into Google
```

**Step 2: Social Media Deep Dive**
```
Select: 9
Enter: Username
→ Searches 20+ platforms
→ Find social media profiles
```

**Step 3: Phone/Email Search**
```
Select: 10 (Email)
Select: 11 (Phone)
→ Find where contact info appears
```

**Step 4: News Check**
```
Select: 14
→ Search news outlets
```

**Step 5: Public Records**
```
Select: 15
→ Check court, property records
```

**Step 6: Save Log**
```
Select: 19
→ Export all searches for case file
```

---

## ❓ Troubleshooting

**Q: Too many results?**
A: Add more specific information (city, age, occupation)

**Q: No results?**
A: Try broader searches, check spelling, use variations

**Q: Google blocking me?**
A: Space out searches, take breaks, use different search engines (Bing, DuckDuckGo)

**Q: How do I use the generated searches?**
A: Simply copy each line and paste it directly into Google Search

---

## 📞 Support

For issues:
1. Check COMPLETE_GUIDE.md for detailed help
2. Review USAGE_GUIDE.md for workflows
3. Consult with your department's tech unit

---

## 🚀 Get Started Now

```bash
cd /mnt/work/OSINT
python3 dork.py
```

**That's the only command you need!**

---

**Simple. Powerful. Effective.**

Generate Google dorks for any investigation in seconds.

*For law enforcement and authorized investigators only*
*Use responsibly and legally*
*Version 1.0 - 2025-09-30*
