#!/usr/bin/env python3
"""
OSINT Google Dork Suite - Complete Investigation Toolkit
All-in-one tool for law enforcement OSINT investigations

For: Missing persons, stolen property, gang tracking, criminal investigations,
     domestic terrorism monitoring, digital footprint analysis

For authorized law enforcement use only
"""

import sys
from datetime import datetime

class OSINTDorkSuite:
    def __init__(self):
        self.investigation_log = []
        self.case_number = ""

        # Pre-built dork templates
        self.prebuilt_dorks = {
            'media_files': [
                'intitle:"index.of" "parent directory" "size" "last modified" (mp4|mp3|avi|flac|aac|ape|ogg)',
                'parent directory DVDRip -xxx -html -htm -php -shtml',
                'parent directory MP3 -xxx -html -htm -php -shtml',
            ],
            'directory_listings': [
                'intitle:"index of" "parent directory"',
                'intitle:"index of" passwd',
                'intitle:"index of" "*.cert.pem" | "*.key.pem"',
                'intitle:"index of" "credentials.xml" | "credentials.txt"',
                'intitle:"index of" "dump.sql"',
                'intitle:"index of" "password.yml"',
            ],
            'file_exposure': [
                'filetype:sql "INSERT INTO" (pass|passwd|password)',
                'filetype:log "password"',
                'filetype:env "DB_PASSWORD"',
                'filetype:config "password"',
                'ext:sql intext:"-- phpMyAdmin SQL Dump --"',
                '"define(\'DB_PASSWORD\'," ext:txt',
            ],
            'web_servers': [
                'inurl:/phpmyadmin',
                'intitle:"phpinfo" "published by the PHP Group"',
                'inurl:":8088/cluster/apps"',
                'intitle:"Welcome to nginx!"',
            ]
        }

    def display_header(self):
        """Display main header"""
        print("\n" + "="*75)
        print("           OSINT GOOGLE DORK SUITE - INVESTIGATION TOOLKIT")
        print("="*75)
        print("  For Law Enforcement: Missing Persons, Gang Tracking, Investigations")
        print("="*75 + "\n")

    def log_search(self, search_type, query):
        """Log searches for investigation records"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.investigation_log.append(f"[{timestamp}] {search_type}: {query}")

    def save_log(self):
        """Save investigation log to file"""
        if not self.investigation_log:
            print("[i] No searches to log")
            return

        filename = f"investigation_log_{self.case_number}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write("OSINT Investigation Log\n")
            f.write("="*50 + "\n")
            f.write(f"Case Number: {self.case_number}\n")
            f.write("="*50 + "\n\n")
            for entry in self.investigation_log:
                f.write(entry + "\n")
        print(f"\n[+] Investigation log saved to: {filename}")

    def _display_queries(self, queries, search_type):
        """Display generated queries"""
        if not queries:
            print("\n[!] No queries generated")
            return

        print(f"\n[+] Generated {len(queries)} Google Dork(s) for {search_type}:")
        print("="*75)
        for i, query in enumerate(queries, 1):
            print(f"\n{i}. {query}")
            self.log_search(search_type, query)
        print("\n" + "="*75)
        print("\n[i] Copy queries into Google Search")
        print("[i] Use Google Tools > Date filter for time-specific searches")

    # ========== PERSON SEARCHES ==========

    def person_search_basic(self):
        """Basic person search"""
        print("\n=== PERSON SEARCH ===")

        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        username = input("Username (optional): ").strip()
        email = input("Email (optional): ").strip()
        phone = input("Phone (optional): ").strip()
        city = input("City (optional): ").strip()
        state = input("State (optional): ").strip()

        queries = []

        # Comprehensive platform list
        social_platforms = [
            # Major social media
            'facebook.com', 'instagram.com', 'twitter.com', 'x.com',
            'linkedin.com', 'tiktok.com', 'youtube.com', 'reddit.com',
            'snapchat.com', 'pinterest.com', 'tumblr.com',

            # Messaging/Communication
            'discord.com', 'telegram.org', 'whatsapp.com', 'signal.org',
            'discord.gg', 'disboard.org', 'kik.com', 'skype.com',

            # Gaming/Streaming
            'twitch.tv', 'roblox.com', 'steam.com', 'steamcommunity.com',
            'xbox.com', 'playstation.com', 'epicgames.com', 'kick.com',

            # Alternative social
            'vk.com', 'ok.ru', 'myspace.com', 'meetup.com', 'nextdoor.com',
            'quora.com', 'medium.com', 'substack.com',

            # Video platforms
            'vimeo.com', 'dailymotion.com', 'rumble.com', 'bitchute.com',
            'odysee.com', 'minds.com',

            # Professional
            'github.com', 'gitlab.com', 'stackoverflow.com', 'behance.net',
            'dribbble.com', 'deviantart.com',

            # Photo/Visual
            'flickr.com', 'imgur.com', '500px.com', 'photobucket.com',
        ]

        if first_name and last_name:
            full_name = f'"{first_name} {last_name}"'

            # Basic searches
            queries.append(full_name)

            # Social media - ALL platforms
            for platform in social_platforms:
                queries.append(f'{full_name} site:{platform}')

            # Location-based
            if city:
                queries.append(f'{full_name} "{city}"')
            if state:
                queries.append(f'{full_name} "{state}"')
            if city and state:
                queries.append(f'{full_name} "{city}, {state}"')

            # Documents
            queries.append(f'{full_name} filetype:pdf')
            queries.append(f'{full_name} filetype:doc OR filetype:docx')
            queries.append(f'{full_name} "resume" OR "cv"')

            # News and records
            queries.append(f'{full_name} news')
            queries.append(f'{full_name} arrest OR court')
            queries.append(f'{full_name} "public records"')

        if username:
            queries.append(f'"{username}"')
            # Username across ALL platforms
            for platform in social_platforms:
                queries.append(f'"{username}" site:{platform}')

        if email:
            queries.append(f'"{email}"')
            queries.append(f'"{email}" site:linkedin.com')
            queries.append(f'"{email}" site:github.com')

        if phone:
            queries.append(f'"{phone}"')
            clean = ''.join(filter(str.isdigit, phone))
            if len(clean) == 10:
                queries.append(f'"{clean[:3]}-{clean[3:6]}-{clean[6:]}"')

        self._display_queries(queries, "Person Search")

    def person_search_advanced(self):
        """Advanced person search with more options"""
        print("\n=== ADVANCED PERSON SEARCH ===")

        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        age = input("Age/age range (optional): ").strip()
        occupation = input("Occupation (optional): ").strip()
        education = input("School/University (optional): ").strip()
        city = input("City: ").strip()
        state = input("State: ").strip()

        queries = []

        if first_name and last_name:
            full_name = f'"{first_name} {last_name}"'

            # Location-based
            if city and state:
                queries.append(f'{full_name} "{city}, {state}"')

            # Occupation
            if occupation:
                queries.append(f'{full_name} "{occupation}"')
                queries.append(f'{full_name} "{occupation}" site:linkedin.com')

            # Education
            if education:
                queries.append(f'{full_name} "{education}"')

            # Age
            if age:
                queries.append(f'{full_name} age {age}')

            # Professional
            queries.append(f'{full_name} "profile" OR "bio"')
            queries.append(f'{full_name} site:linkedin.com')

            # Contact info
            queries.append(f'{full_name} "email" OR "contact"')

            # Public records
            if city and state:
                queries.append(f'{full_name} "{city}" "{state}" "public records"')

        self._display_queries(queries, "Advanced Person Search")

    # ========== CRIMINAL INVESTIGATIONS ==========

    def gang_organization_search(self):
        """Search for gang/criminal organization activity"""
        print("\n=== GANG/CRIMINAL ORGANIZATION SEARCH ===")
        print("[!] For authorized law enforcement investigations only\n")

        org_name = input("Organization/gang name: ").strip()
        city = input("City: ").strip()
        state = input("State: ").strip()

        if not org_name:
            print("[!] Organization name required")
            return

        queries = []

        # Basic searches
        queries.append(f'"{org_name}"')
        queries.append(f'"{org_name}" gang OR crew OR set')

        # Location-based
        if city:
            queries.append(f'"{org_name}" "{city}"')
            queries.append(f'"{org_name}" "{city}" gang')
        if state:
            queries.append(f'"{org_name}" "{state}"')
        if city and state:
            queries.append(f'"{org_name}" "{city}, {state}"')

        # Comprehensive social media platforms gangs use
        gang_platforms = [
            # Major social
            'facebook.com', 'instagram.com', 'twitter.com', 'x.com',
            'tiktok.com', 'youtube.com', 'snapchat.com',

            # Messaging/Chat
            'telegram.org', 't.me', 'discord.com', 'discord.gg',
            'disboard.org', 'whatsapp.com', 'signal.org',

            # Gaming (often used by younger gang members)
            'roblox.com', 'twitch.tv', 'kick.com', 'steam.com',

            # Video platforms
            'youtube.com', 'rumble.com', 'bitchute.com', 'odysee.com',

            # Forums/Communities
            'reddit.com', '4chan.org', '8kun.top',

            # Alternative/Underground
            'vk.com', 'minds.com', 'gab.com', 'parler.com', 'gettr.com'
        ]

        for platform in gang_platforms:
            queries.append(f'"{org_name}" site:{platform}')

        # Gang indicators
        queries.append(f'"{org_name}" "gang sign" OR "hand sign"')
        queries.append(f'"{org_name}" tattoo OR ink')
        queries.append(f'"{org_name}" colors OR flag OR territory')
        queries.append(f'"{org_name}" turf OR hood')

        # Criminal activity
        queries.append(f'"{org_name}" arrest OR arrested')
        queries.append(f'"{org_name}" shooting OR violence')
        queries.append(f'"{org_name}" investigation OR raid')
        queries.append(f'"{org_name}" indicted OR charged')

        # News and media
        if city:
            queries.append(f'"{org_name}" "{city}" news')
            queries.append(f'"{org_name}" "{city}" arrest')

        # Videos (gangs often post activity)
        queries.append(f'"{org_name}" site:youtube.com')
        queries.append(f'"{org_name}" site:tiktok.com')
        queries.append(f'"{org_name}" video OR footage')

        self._display_queries(queries, "Gang/Organization Search")

    def domestic_terrorism_search(self):
        """Search for domestic terrorism indicators"""
        print("\n=== DOMESTIC TERRORISM INVESTIGATION ===")
        print("[!] FOR AUTHORIZED LAW ENFORCEMENT ONLY")
        print("[!] Report all findings to FBI\n")

        group_id = input("Group name/identifier (e.g., 764): ").strip()
        location = input("Location (optional): ").strip()

        if not group_id:
            print("[!] Group identifier required")
            return

        queries = []

        # Basic searches
        queries.append(f'"{group_id}"')
        queries.append(f'"{group_id}" extremist')

        # Location
        if location:
            queries.append(f'"{group_id}" "{location}"')

        # Social media platforms extremists use
        platforms = ['telegram.org', 'discord.com', 'gab.com', '4chan.org',
                    '8kun.top', 'parler.com', 'gettr.com', 'facebook.com',
                    'twitter.com', 'x.com']

        for platform in platforms:
            queries.append(f'"{group_id}" site:{platform}')

        # Recruitment/propaganda
        queries.append(f'"{group_id}" recruit OR join')
        queries.append(f'"{group_id}" manifesto OR ideology')

        # Law enforcement
        queries.append(f'"{group_id}" FBI OR "law enforcement"')
        queries.append(f'"{group_id}" arrest OR investigation')

        self._display_queries(queries, "Domestic Terrorism Search")

    def criminal_activity_search(self):
        """Search for specific criminal activity"""
        print("\n=== CRIMINAL ACTIVITY SEARCH ===")

        activity = input("Activity type (robbery/shooting/burglary/assault): ").strip()
        city = input("City: ").strip()
        state = input("State: ").strip()
        date = input("Date or date range (optional): ").strip()
        location = input("Specific location/address (optional): ").strip()

        if not activity or not city:
            print("[!] Activity type and city required")
            return

        queries = []

        # Basic searches
        queries.append(f'"{activity}" "{city}" "{state}"')
        queries.append(f'"{activity}" "{city}" news')
        queries.append(f'"{activity}" "{city}" police')

        # Date-based
        if date:
            queries.append(f'"{activity}" "{city}" "{date}"')

        # Specific location
        if location:
            queries.append(f'"{activity}" "{location}" "{city}"')

        # Social media (witnesses, videos)
        queries.append(f'"{activity}" "{city}" site:twitter.com OR site:x.com')
        queries.append(f'"{activity}" "{city}" site:facebook.com')
        queries.append(f'"{activity}" "{city}" video OR footage')

        # Investigation info
        queries.append(f'"{activity}" "{city}" suspect')
        queries.append(f'"{activity}" "{city}" witness')

        self._display_queries(queries, "Criminal Activity Search")

    def suspect_identification(self):
        """Search for suspect identification"""
        print("\n=== SUSPECT IDENTIFICATION ===")

        name = input("Suspect name (if known): ").strip()
        alias = input("Alias/nickname (if known): ").strip()
        city = input("City: ").strip()
        crime = input("Crime type: ").strip()

        queries = []

        if name:
            queries.append(f'"{name}"')
            queries.append(f'"{name}" arrest')
            queries.append(f'"{name}" "{city}"')
            queries.append(f'"{name}" "{crime}"')
            queries.append(f'"{name}" mugshot')
            queries.append(f'"{name}" site:facebook.com')
            queries.append(f'"{name}" site:instagram.com')

        if alias:
            queries.append(f'"{alias}"')
            queries.append(f'"{alias}" "{city}"')
            if name:
                queries.append(f'"{name}" "{alias}"')

        self._display_queries(queries, "Suspect Identification")

    # ========== PROPERTY & VEHICLE ==========

    def stolen_property_search(self):
        """Search for stolen property"""
        print("\n=== STOLEN PROPERTY SEARCH ===")

        serial = input("Serial number: ").strip()
        brand = input("Brand: ").strip()
        model = input("Model: ").strip()
        city = input("City where stolen: ").strip()

        queries = []

        # Comprehensive marketplace list
        marketplaces = [
            # Major marketplaces
            'craigslist.org', 'facebook.com/marketplace', 'ebay.com',
            'offerup.com', 'letgo.com', 'mercari.com', 'poshmark.com',

            # Local/Community
            'nextdoor.com', '5miles.com', 'varagesale.com', 'bookoo.com',
            'oodle.com', 'recycler.com', 'letitgo.com',

            # Specialized
            'swappa.com', 'gazelle.com', 'decluttr.com', 'backmarket.com',

            # Auction/Bidding
            'shopgoodwill.com', 'propertyroom.com', 'govdeals.com',

            # Pawn/Second-hand
            'cashconverters.com', 'musicgoround.com', 'playsmart.com',

            # Electronics specific
            'newegg.com/marketplace', 'amazon.com/gp/offer-listing',

            # Jewelry/Luxury
            'tradesy.com', 'therealreal.com', 'vestiairecollective.com',

            # General classifieds
            'gumtree.com', 'kijiji.ca', 'locanto.com',

            # Social selling
            'depop.com', 'vinted.com', 'grailed.com', 'curtsy.com',

            # Others
            'bonanza.com', 'reverb.com', 'stockx.com', 'goat.com'
        ]

        if serial:
            for marketplace in marketplaces:
                queries.append(f'"{serial}" site:{marketplace}')
            queries.append(f'"{serial}" "for sale"')
            queries.append(f'"{serial}" "obo" OR "best offer"')
            if city:
                queries.append(f'"{serial}" "{city}"')
                queries.append(f'"{serial}" "{city}" for sale')

        if brand and model:
            search_term = f'"{brand} {model}"'
            for marketplace in marketplaces:
                queries.append(f'{search_term} site:{marketplace}')
            if city:
                queries.append(f'{search_term} "{city}" for sale')
                queries.append(f'{search_term} "{city}" "obo"')

        # Pawn shop searches
        queries.append(f'"{serial}" pawn' if serial else f'"{brand} {model}" pawn')

        # Social media selling groups
        queries.append(f'"{serial}" site:facebook.com "for sale"' if serial else f'"{brand} {model}" site:facebook.com "for sale"')

        self._display_queries(queries, "Stolen Property Search")

    def vehicle_search(self):
        """Search for vehicles"""
        print("\n=== VEHICLE SEARCH ===")

        vin = input("VIN (optional): ").strip()
        license_plate = input("License plate (optional): ").strip()
        plate_state = input("Plate state (optional): ").strip()
        make = input("Make (optional): ").strip()
        model = input("Model (optional): ").strip()
        year = input("Year (optional): ").strip()

        queries = []

        if vin:
            queries.append(f'"{vin}"')
            queries.append(f'"{vin}" for sale')
            queries.append(f'"{vin}" site:carfax.com')
            queries.append(f'"{vin}" site:craigslist.org')
            queries.append(f'"{vin}" site:facebook.com/marketplace')

        if license_plate:
            queries.append(f'"{license_plate}"')
            if plate_state:
                queries.append(f'"{license_plate}" "{plate_state}"')

        # Vehicle description
        desc_parts = [year, make, model]
        desc_parts = [p for p in desc_parts if p]
        if desc_parts:
            desc = " ".join(desc_parts)
            queries.append(f'"{desc}"')
            queries.append(f'"{desc}" for sale')
            queries.append(f'"{desc}" site:craigslist.org')

        self._display_queries(queries, "Vehicle Search")

    # ========== SOCIAL MEDIA & DIGITAL FOOTPRINT ==========

    def social_media_deep_dive(self):
        """Comprehensive social media search"""
        print("\n=== SOCIAL MEDIA DEEP DIVE ===")

        username = input("Username/handle: ").strip()
        real_name = input("Real name (optional): ").strip()

        if not username and not real_name:
            print("[!] Username or real name required")
            return

        search_term = username or real_name
        queries = []

        # COMPREHENSIVE platform list (100+ platforms)
        all_platforms = [
            # Major Social Media
            'facebook.com', 'instagram.com', 'twitter.com', 'x.com',
            'linkedin.com', 'tiktok.com', 'snapchat.com', 'youtube.com',
            'reddit.com', 'pinterest.com', 'tumblr.com',

            # Messaging/Communication
            'discord.com', 'discord.gg', 'disboard.org', 'telegram.org', 't.me',
            'whatsapp.com', 'signal.org', 'kik.com', 'skype.com',
            'messenger.com', 'viber.com', 'line.me', 'wechat.com',

            # Gaming/Streaming
            'twitch.tv', 'kick.com', 'roblox.com', 'steam.com', 'steamcommunity.com',
            'xbox.com', 'playstation.com', 'epicgames.com', 'battlenet.com',
            'origin.com', 'ubisoft.com', 'nintendo.com', 'mixer.com',

            # Video Platforms
            'vimeo.com', 'dailymotion.com', 'rumble.com', 'bitchute.com',
            'odysee.com', 'lbry.tv', 'dtube.com', 'peertube.tv',

            # Alternative/Niche Social
            'vk.com', 'ok.ru', 'weibo.com', 'qq.com', 'baidu.com',
            'myspace.com', 'friendster.com', 'hi5.com', 'tagged.com',
            'meetme.com', 'badoo.com', 'moco.com',

            # Forums/Community
            'quora.com', 'medium.com', 'substack.com', 'wordpress.com',
            'blogger.com', 'livejournal.com', 'minds.com',

            # Professional
            'github.com', 'gitlab.com', 'bitbucket.org', 'stackoverflow.com',
            'stackexchange.com', 'behance.net', 'dribbble.com', 'deviantart.com',
            'artstation.com', 'cgsociety.org',

            # Photo/Visual
            'flickr.com', 'imgur.com', '500px.com', 'photobucket.com',
            'imageshack.com', 'tinypic.com', 'postimage.org',

            # Dating/Meetup
            'tinder.com', 'bumble.com', 'match.com', 'pof.com', 'okcupid.com',
            'hinge.co', 'grindr.com', 'eharmony.com', 'zoosk.com',
            'meetup.com', 'eventbrite.com',

            # Music/Audio
            'soundcloud.com', 'spotify.com', 'bandcamp.com', 'mixcloud.com',
            'reverbnation.com', 'last.fm', 'audiomack.com',

            # Fashion/Shopping
            'depop.com', 'poshmark.com', 'vinted.com', 'grailed.com',
            'curtsy.com', 'tradesy.com', 'therealreal.com',

            # Fitness/Health
            'strava.com', 'myfitnesspal.com', 'fitbit.com', 'garmin.com',

            # Local/Community
            'nextdoor.com', 'meetup.com', 'yelp.com',

            # Alternative/Underground
            'gab.com', 'parler.com', 'gettr.com', 'truthsocial.com',
            '4chan.org', '8kun.top', 'somethingawful.com',

            # Educational
            'coursera.org', 'udemy.com', 'skillshare.com', 'khanacademy.org',
            'academia.edu', 'researchgate.net', 'mendeley.com',

            # Business/Review
            'glassdoor.com', 'indeed.com', 'ziprecruiter.com',
            'crunchbase.com', 'angellist.com', 'producthunt.com',

            # Misc
            'patreon.com', 'onlyfans.com', 'ko-fi.com', 'buymeacoffee.com',
            'cashapp.com', 'venmo.com', 'paypal.com',
            'linktree.com', 'beacons.ai', 'linktr.ee'
        ]

        for platform in all_platforms:
            queries.append(f'"{search_term}" site:{platform}')

        # Forums and boards
        queries.append(f'"{search_term}" inurl:forum')
        queries.append(f'"{search_term}" "member since"')
        queries.append(f'"{search_term}" "posted by"')
        queries.append(f'"{search_term}" inurl:profile')

        # Username variations
        queries.append(f'"{search_term}" profile OR account')
        queries.append(f'"{search_term}" "@{search_term}"')

        self._display_queries(queries, "Social Media Deep Dive")

    def email_search(self):
        """Search for email addresses"""
        print("\n=== EMAIL SEARCH ===")

        email = input("Email address: ").strip()

        if not email:
            print("[!] Email required")
            return

        queries = [
            f'"{email}"',
            f'"{email}" -site:pastebin.com',
            f'"{email}" profile',
            f'"{email}" site:linkedin.com',
            f'"{email}" site:facebook.com',
            f'"{email}" site:github.com',
            f'"{email}" filetype:pdf',
        ]

        # Extract username
        if "@" in email:
            username = email.split("@")[0]
            queries.append(f'"{username}" profile')

        self._display_queries(queries, "Email Search")

    def phone_search(self):
        """Search for phone numbers"""
        print("\n=== PHONE NUMBER SEARCH ===")

        phone = input("Phone number: ").strip()

        if not phone:
            print("[!] Phone required")
            return

        queries = [f'"{phone}"']

        # Format variations
        clean = ''.join(filter(str.isdigit, phone))
        if len(clean) == 10:
            formats = [
                clean,
                f"{clean[:3]}-{clean[3:6]}-{clean[6:]}",
                f"({clean[:3]}) {clean[3:6]}-{clean[6:]}",
            ]
            for fmt in formats:
                queries.append(f'"{fmt}"')

        queries.append(f'"{phone}" site:facebook.com')
        queries.append(f'"{phone}" site:linkedin.com')

        self._display_queries(queries, "Phone Search")

    # ========== DOCUMENTS & FILES ==========

    def document_search(self):
        """Search for documents"""
        print("\n=== DOCUMENT SEARCH ===")

        title = input("Document title/keywords: ").strip()
        author = input("Author (optional): ").strip()
        doc_type = input("Type (pdf/doc/xls/all) [default: all]: ").strip().lower() or "all"

        queries = []

        if title:
            if doc_type == "all":
                queries.append(f'"{title}" filetype:pdf')
                queries.append(f'"{title}" filetype:doc OR filetype:docx')
                queries.append(f'"{title}" filetype:xls')
            else:
                queries.append(f'"{title}" filetype:{doc_type}')

        if author:
            queries.append(f'"{author}" filetype:pdf')

        self._display_queries(queries, "Document Search")

    def exposed_files_search(self):
        """Search for exposed files and credentials"""
        print("\n=== EXPOSED FILES SEARCH ===")
        print("[!] Check if data has been exposed\n")

        target = input("Domain or identifier: ").strip()

        if not target:
            print("[!] Target required")
            return

        queries = [
            f'site:{target} filetype:sql',
            f'site:{target} filetype:log',
            f'site:{target} filetype:env',
            f'site:{target} filetype:config',
            f'site:{target} intitle:"index of"',
            f'"{target}" filetype:sql "INSERT INTO"',
            f'"{target}" ext:env "DB_PASSWORD"',
            f'"{target}" "password" filetype:log',
        ]

        self._display_queries(queries, "Exposed Files Search")

    # ========== NEWS & RECORDS ==========

    def news_search(self):
        """Search news sources"""
        print("\n=== NEWS SEARCH ===")

        subject = input("Person/topic: ").strip()
        location = input("Location (optional): ").strip()
        date_range = input("Date range (e.g., 2023..2024): ").strip()

        if not subject:
            print("[!] Subject required")
            return

        queries = [
            f'"{subject}" news',
            f'"{subject}" site:news.google.com',
        ]

        # Major news outlets
        for outlet in ['cnn.com', 'bbc.com', 'reuters.com', 'apnews.com',
                      'nytimes.com', 'washingtonpost.com']:
            queries.append(f'"{subject}" site:{outlet}')

        if location:
            queries.append(f'"{subject}" "{location}" news')

        if date_range:
            queries.append(f'"{subject}" {date_range}')

        self._display_queries(queries, "News Search")

    def public_records_search(self):
        """Search public records"""
        print("\n=== PUBLIC RECORDS SEARCH ===")

        name = input("Name: ").strip()
        city = input("City (optional): ").strip()
        state = input("State (optional): ").strip()

        if not name:
            print("[!] Name required")
            return

        queries = [
            f'"{name}" "public records"',
            f'"{name}" "court records"',
            f'"{name}" "arrest records"',
            f'"{name}" "criminal records"',
        ]

        if city and state:
            queries.append(f'"{name}" "{city}" "{state}" "public records"')

        queries.append(f'"{name}" "property records"')
        queries.append(f'"{name}" obituary')

        self._display_queries(queries, "Public Records Search")

    # ========== PRE-BUILT DORKS ==========

    def prebuilt_dorks_menu(self):
        """Display pre-built dork templates"""
        print("\n=== PRE-BUILT DORK TEMPLATES ===")
        print("\nSelect category:")
        print("  1. Media Files (Music, Videos)")
        print("  2. Directory Listings")
        print("  3. Exposed Files (Passwords, Configs)")
        print("  4. Web Servers")
        print("  0. Back")

        choice = input("\nSelect: ").strip()

        dork_map = {
            '1': ('media_files', 'Media Files'),
            '2': ('directory_listings', 'Directory Listings'),
            '3': ('file_exposure', 'Exposed Files'),
            '4': ('web_servers', 'Web Servers')
        }

        if choice in dork_map:
            key, name = dork_map[choice]
            dorks = self.prebuilt_dorks[key]
            print(f"\n[+] {name} - {len(dorks)} Pre-Built Dorks:")
            print("="*75)
            for i, dork in enumerate(dorks, 1):
                print(f"\n{i}. {dork}")
                self.log_search(name, dork)
            print("\n" + "="*75)
            print("\n[i] Customize these by adding your search terms")

    # ========== UTILITIES ==========

    def custom_dork_builder(self):
        """Build custom dork"""
        print("\n=== CUSTOM DORK BUILDER ===")
        print("\nOperators:")
        print("  site:       Search specific site")
        print("  filetype:   File type")
        print("  intitle:    In title")
        print("  inurl:      In URL")
        print("  intext:     In text")
        print("  \"quotes\"    Exact phrase")
        print("  OR          Either term")
        print("  -           Exclude")

        custom = input("\nEnter your custom dork: ").strip()

        if custom:
            print(f"\n[+] Custom Dork: {custom}")
            self.log_search("Custom Dork", custom)

    def view_log(self):
        """View investigation log"""
        print("\n=== INVESTIGATION LOG ===")
        if self.investigation_log:
            for entry in self.investigation_log:
                print(entry)
        else:
            print("[i] No searches logged yet")

    # ========== MAIN MENU ==========

    def main_menu(self):
        """Main menu"""
        self.display_header()

        self.case_number = input("Enter case number (optional): ").strip()
        if not self.case_number:
            self.case_number = "CASE_" + datetime.now().strftime('%Y%m%d_%H%M%S')

        while True:
            print("\n" + "="*75)
            print("MAIN MENU:")
            print("="*75)
            print("\n  PERSON INVESTIGATIONS:")
            print("  1.  Person Search (Basic)")
            print("  2.  Person Search (Advanced)")
            print("\n  CRIMINAL INVESTIGATIONS:")
            print("  3.  Gang/Criminal Organization Search")
            print("  4.  Domestic Terrorism Investigation")
            print("  5.  Criminal Activity Search")
            print("  6.  Suspect Identification")
            print("\n  PROPERTY & VEHICLES:")
            print("  7.  Stolen Property Search")
            print("  8.  Vehicle Search")
            print("\n  SOCIAL MEDIA & DIGITAL:")
            print("  9.  Social Media Deep Dive")
            print("  10. Email Search")
            print("  11. Phone Number Search")
            print("\n  DOCUMENTS & FILES:")
            print("  12. Document Search")
            print("  13. Exposed Files Search")
            print("\n  NEWS & RECORDS:")
            print("  14. News Search")
            print("  15. Public Records Search")
            print("\n  ADVANCED:")
            print("  16. Pre-Built Dork Templates")
            print("  17. Custom Dork Builder")
            print("\n  MANAGEMENT:")
            print("  18. View Investigation Log")
            print("  19. Save Investigation Log")
            print("  0.  Exit")
            print("="*75)

            choice = input("\nSelect option: ").strip()

            menu_actions = {
                '1': self.person_search_basic,
                '2': self.person_search_advanced,
                '3': self.gang_organization_search,
                '4': self.domestic_terrorism_search,
                '5': self.criminal_activity_search,
                '6': self.suspect_identification,
                '7': self.stolen_property_search,
                '8': self.vehicle_search,
                '9': self.social_media_deep_dive,
                '10': self.email_search,
                '11': self.phone_search,
                '12': self.document_search,
                '13': self.exposed_files_search,
                '14': self.news_search,
                '15': self.public_records_search,
                '16': self.prebuilt_dorks_menu,
                '17': self.custom_dork_builder,
                '18': self.view_log,
                '19': self.save_log,
            }

            if choice == '0':
                print("\n[+] Exiting OSINT Dork Suite")
                if self.investigation_log:
                    save = input("Save investigation log? (y/n): ").strip().lower()
                    if save == 'y':
                        self.save_log()
                print("[+] Use responsibly and legally")
                sys.exit(0)
            elif choice in menu_actions:
                menu_actions[choice]()
            else:
                print("\n[!] Invalid option")

            input("\nPress Enter to continue...")

def main():
    try:
        suite = OSINTDorkSuite()
        suite.main_menu()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
