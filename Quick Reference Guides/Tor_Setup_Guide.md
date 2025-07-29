# Tor Browser Setup Guide

## Download Tor
**Download the Tor Browser from the [Tor Project](https://www.torproject.org/)**

# Settings

## *Privacy and Security* Tab

**Go to settings when the browser is downloaded. *DO NOT CONNECT JUST YET***
**Click on *Privacy & Security***
* Go to History: Change to *Never remember history*
* Go to *Permissions*, change the folling by clicking *Settings* and checking the box:
**Block new requests asking to access your location**
- *Location*
- *Camera*
- *Microphone*
- *Notifications*
- *Virtual Reality*
**Make sure *Block pop-up windows* and *Warn you when websites try to install add-ons* are also checked
- Make sure there are no exceptions in those boxes, in the *Exceptions* tab.

## Security
  **Make sure that the *Security Level* is on the *Safest* choice.
  * Make sure that in the *Deceptive Content and Dangerous Software Protection* All *3* boxes are checked
- *Block dangerous and deceptive content*
- *Block dangerous donwloads*
- *Warn you about unwanted and uncommon software*

## HTTPS-Only Mode
**Double check that *Enable HTTPS-Only Mode in all windows* is checked**
**Double check the *Manage Exceptions* does not have any exception to websites already**


 # *Connections* 

## *Bridges* Section 
**Click on *Select a built-in bridge***
**Select *Snowflake* as your bridge**

# In main *Search Bar*, type *about:config*

## *about:config*
**Type in *Search preference name*, *java*
** Look for *javascript.enabled***
- If it says *true* = click the arrow to disable
- Should say *false*

# Connect to Tor Network

This has configured your Tor network to work in the safest form and disabled ALL javascript. 
By doing this, it disables the use of specific Ads that may be attempting to upload malware
