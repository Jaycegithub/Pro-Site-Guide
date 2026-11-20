# Reddit posts, ready to paste

Before each post:
- Read the subreddit's rules. If links to your own site aren't allowed, delete the last "longer version" line.
- Post 1 per week, each in a different subreddit. Reply to every comment for the first 2 hours.
- Change anything in [brackets] to your real experience. Only share stories that really happened (no client names).

Recommended order: 1 → 2 → 3 → 4 → 5 → 6 → 7.

---

## Post 1 · r/smallbusiness
**Title:** I've built websites for small businesses for 8+ years. The most expensive mistake I keep seeing has nothing to do with design.

**Body:**
```
It's not owning your own domain name.

Over and over I meet owners whose web designer, nephew or old agency registered the domain under their own account. Everything works fine until that person disappears, the card on the account expires, or there's a falling out. Then the business can lose its website AND its email overnight, and getting the domain back can take weeks, if it's possible at all.

[Optional: one short true story, no names. E.g. "A client of mine lost two weeks of leads because..."]

A 5-minute check you can do today:

1. Look up who your domain is registered with (your designer or IT person can tell you, or search "WHOIS lookup" and enter your domain).
2. Make sure YOU can log in to that registrar account with your own email.
3. Turn ON auto-renew and make sure the card on file is current.
4. Turn on two-factor login.
5. Do the same for your hosting and website admin login: you should have your own account, not just "the designer's password".

Your designer can still have access. They just shouldn't be the only one holding the keys.

Happy to answer questions in the comments if you're not sure where your domain is or what you're looking at.
```
**Optional last line (only if links allowed):** `I wrote a longer guide on choosing and registering a domain here: https://prositeguide.com/best-domain-registrars-law-firms/ (my site)`

---

## Post 2 · r/Wordpress
**Title:** The checklist I run before launching every WordPress site (after 1,000+ builds)

**Body:**
```
Sharing my pre-launch checklist. It's boring, but every item is on here because skipping it bit me or a client at some point.

Before launch
1. "Discourage search engines" is OFF (Settings → Reading). The #1 "why isn't my site on Google" cause.
2. Permalinks set to Post name before you publish anything.
3. HTTPS works on every page, no mixed-content warnings.
4. Contact forms tested: submit one, confirm it arrives, check spam too.
5. Automatic backups scheduled AND one restore tested.
6. Unused themes and plugins deleted (not just deactivated).
7. Every admin has their own login; no shared "admin" account; 2FA on.
8. Site checked on a real phone, not just the browser's mobile view.
9. Homepage hero image resized and compressed (the usual cause of slow mobile scores).
10. Site title, tagline and favicon set; 404 page looks OK.

After launch
- Add the site to Google Search Console and submit the sitemap.
- Check PageSpeed Insights on mobile.
- Set a monthly reminder for updates and a quick backup check.

What's on your list that isn't on mine?
```
**Optional last line:** `Longer version with the "why" behind each step: https://prositeguide.com/how-to-start-a-wordpress-website/ (my site)`

---

## Post 3 · r/localseo (or r/smallbusiness)
**Title:** If you're a local business, your Google Business Profile probably matters more than your website. Here's what I'd fix first.

**Body:**
```
When someone searches "plumber near me" or "accountant in [city]", the map results usually show before any website. That box is your Google Business Profile, and most small businesses set it up once and never touch it again.

What I check first for clients:

1. Primary category: the most specific one that fits (this matters a lot).
2. Name, address and phone exactly match your website and other listings.
3. Hours are correct, including holiday hours.
4. Real photos: storefront, team, work you've done. Add new ones regularly.
5. Every review gets a reply, good and bad. Keep replies short and professional.
6. Services and a description filled in, in plain language.
7. The website link goes to the right page, and that page loads fast on a phone.

None of this costs anything. It just takes an afternoon.

Drop your business type below and I'll tell you which category and first fix I'd look at.
```
**Optional last line:** `Full setup guide: https://prositeguide.com/google-business-profile-law-firms/ (my site; examples are for professional firms but the steps apply to any local business)`

---

## Post 4 · r/Entrepreneur (or r/smallbusiness)
**Title:** How I actually use AI in client work as a web designer (and where I don't trust it)

**Body:**
```
Lots of hype about AI, so here's the honest version from someone who uses it daily for websites, SEO and design work.

Where it saves me real time
- First drafts: page copy outlines, FAQs, meta descriptions. I always rewrite them.
- Turning messy client notes into a clear brief or sitemap.
- Writing alt text and image descriptions in bulk.
- Brainstorming headline and layout options before I design.
- Explaining technical stuff (DNS, SPF records, speed reports) in plain English for clients.
- Small code snippets and fixes, which I test before they go live.

Where I don't trust it
- Prices, laws, statistics and "facts" about specific companies. It confidently makes things up. I check every number against an official source.
- Final copy that's supposed to sound like the business owner.
- Design decisions. It's fine for ideas, but taste and brand still need a human.
- Anything with client passwords or private data. That never goes in.

My rule: AI does the first 60%, I do the last 40%, and I'm responsible for 100% of what ships.

How are you using it in your business? Curious what's actually working for people.
```
(No link needed. This one builds profile visits.)

---

## Post 5 · r/smallbusiness
**Title:** Your business emails landing in spam? It's usually 3 settings most small businesses never set up.

**Body:**
```
If clients keep saying "your email went to my junk folder", the cause is often missing email authentication on your domain. Gmail and Yahoo have gotten much stricter about this.

The three settings, in plain English:

- SPF: a list of which services are allowed to send email for your domain (e.g. Google Workspace, Microsoft 365, your website's contact form).
- DKIM: a digital signature that proves the email wasn't changed on the way.
- DMARC: tells inboxes what to do if an email fails the two checks above, and sends you reports.

How to check yours for free: search for an "SPF DKIM DMARC checker", enter your domain, and it shows what's missing.

How to fix: whoever manages your domain (or your email provider's setup guide) adds three DNS records. It's usually a 15-30 minute job. Your email provider's help pages have the exact values.

One tip: if you use a @gmail.com address for your business, none of this applies, but a domain email (you@yourbusiness.com) looks far more trustworthy to clients.

Ask below if you're stuck. Tell me who hosts your email and I'll point you to the right setup page.
```
**Optional last line:** `Step-by-step version: https://prositeguide.com/law-firm-business-email/ (my site)`

---

## Post 6 · r/smallbusiness (or r/Entrepreneur)
**Title:** What files you should get from your logo/brand designer (most small businesses only get a PNG)

**Body:**
```
As a designer, I see this constantly: a business pays for a logo and receives one PNG. Six months later they need it for a sign, a T-shirt or a website and have nothing usable.

Ask your designer for:

1. Vector files (SVG, AI or EPS, and a PDF): these scale to any size without going blurry. Printers and sign makers need them.
2. PNG with a transparent background: for websites, social media and documents.
3. Versions for light AND dark backgrounds (full colour, all-white, all-black).
4. A horizontal and a stacked version, plus a small icon version (for favicons and profile pictures).
5. Your exact colours: HEX codes for screens and CMYK for print.
6. The font names (and whether you need a licence for them).
7. Written confirmation that you own the rights to the final logo.

Put it all in one shared folder you control (Google Drive, Dropbox), not just in an old email.

If you've already lost your files, a designer can often recreate a vector version from a good-quality image.
```
(No link needed. Builds trust for your design work.)

---

## Post 7 · r/smallbusiness or r/Entrepreneur (ONLY where the rules allow feedback/review threads; some subs only allow it in a weekly thread)
**Title:** Free website reviews for small businesses: drop your link and I'll give you 3 quick fixes

**Body:**
```
I've designed and built websites for 8+ years (design, WordPress, SEO). I have a few hours free today, so I'll review as many small business sites as I can.

Drop your link and tell me:
- What your business does
- What you want the site to do (calls, bookings, sales, enquiries)

I'll reply with 3 specific things you can fix yourself, covering speed, mobile, trust and Google basics. No sales pitch, no DMs unless you ask.
```
Then reply to every single one, publicly and specifically. This post usually brings the most profile visits.

---

## Track what works
| Date | Subreddit | Post # | Upvotes | Comments | Profile visits / site clicks |
|---|---|---|---|---|---|
| | | | | | |
