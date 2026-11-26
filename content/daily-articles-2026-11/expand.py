from blocks import *
from nov_articles import nc

# extra sections inserted before the FAQ heading, extra FAQ pairs appended after the last FAQ answer,
# extra sources appended
X = {}

# ------------------------------------------------------------------ domain owner
s = 'psg-domain-owner'
X['check-who-owns-a-domain'] = dict(
sections=[
    H2('What do domain status codes mean?'),
    P('The &ldquo;Status&rdquo; line in a lookup uses short codes set by the registrar or the registry. They look technical, but a few of them tell you a lot about the health of a domain. ICANN publishes a full list with explanations. These are the ones business owners see most often:'),
    TABLE(['Status code', 'What it means', 'Should you worry?'], [
        ['clientTransferProhibited', 'The registrar has locked the domain against transfers', 'No. This is normal protection; it is removed only when you move registrar'],
        ['clientDeleteProhibited / clientUpdateProhibited', 'Extra locks against deletion or changes', 'No. Good security'],
        ['serverTransferProhibited', 'The registry (not your registrar) has blocked transfers', 'Sometimes. Ask your registrar why'],
        ['clientHold / serverHold', 'The domain is not active in DNS, so the website and email do not work', 'Yes. Often caused by non-payment, unverified contact details or a dispute'],
        ['redemptionPeriod', 'The domain has expired and been deleted, but can still be restored for a fee', 'Yes. Contact your registrar today'],
        ['pendingDelete', 'The domain is about to be released', 'Yes. It may soon be registrable by anyone'],
        ['pendingTransfer', 'A transfer to another registrar is in progress', 'Only if you did not request it'],
    ]),
    P('If you see a &ldquo;hold&rdquo; status on your own domain, check the email address on the registrar account. Registrars must ask domain holders to verify their contact details, and an unanswered verification email is a common reason a domain is suspended.'),
    H2('How to check a domain with a country extension (.uk, .au, .ca, .ph)'),
    P('Country-code domains are run by national registries, and each one sets its own rules about what lookup results show. ICANN Lookup works best for generic extensions such as .com, .net and .org. For a country-code domain, search for the country&rsquo;s official domain registry (for example, the registry for .uk or .au) and use its lookup tool. The results are usually similar: registrar, dates and status, with personal details hidden.'),
    H2('How to protect your domain once you know who owns it'),
    UL(['<strong>Use an email that does not depend on the domain itself.</strong> If your registrar account email is on the same domain and the domain lapses, you can lose the very inbox you need to recover it. Add a backup email on a different provider.',
        '<strong>Turn on auto-renew and keep the card up to date.</strong> Registrars send renewal reminders before a domain expires, but they go to the account email, so make sure someone reads it.',
        '<strong>Renew for several years.</strong> A multi-year renewal gives you a buffer if a card expires or a reminder is missed.',
        '<strong>Keep the transfer lock on.</strong> Only turn it off when you are moving the domain yourself.',
        '<strong>Turn on two-factor login</strong> for the registrar account and store the password in a password manager.',
        '<strong>Give access, not ownership.</strong> Most registrars let you add a web designer or IT contact as a user or delegate without handing over the whole account.']),
    H2('Watch out for fake domain renewal notices'),
    P('Many business owners receive official-looking letters or emails warning that their domain is about to expire and asking them to pay. Some come from companies that are not your registrar and are trying to get you to transfer your domain to them, often at a much higher price. Others are simple phishing.'),
    P('The fix is simple: never pay a domain invoice from a link or letter. Log in to your registrar directly (type its address yourself) and check the real expiry date there. The lookup you just did tells you which registrar is genuine.'),
    H2('Want to buy a domain someone else owns?'),
    P('If the domain you want is taken, the lookup shows it is registered but usually not who owns it. Here is a safe way to approach it:'),
    OL(['Visit the domain. If it shows a &ldquo;for sale&rdquo; page, it may list a price or a broker.',
        'If not, many registrars offer a way to contact the registrant through a relay form, or a paid brokerage service.',
        'Check the domain&rsquo;s history on the <a href="https://web.archive.org/">Wayback Machine</a> so you know what it was used for before.',
        'Search for trademarks on the name in your country before you make an offer.',
        'Pay through a reputable escrow service, not a direct bank transfer, and only release the money once the domain is in your registrar account.']),
    P('Often it is cheaper and faster to choose a different name. Our ' + il('how-to-choose-a-domain-name', 'guide to choosing a domain name') + ' has a checklist for that.'),
    H2('Domain ownership checklist for business owners'),
    TABLE(['Check', 'Done when'], [
        ['Registrar found', 'You know which company the domain is with'],
        ['Account access', 'You can log in, and the account is in your business&rsquo;s name'],
        ['Contact details', 'Registrant details are your business; account email is one you will keep'],
        ['Auto-renew', 'On, with a valid card, ideally for several years'],
        ['Security', 'Transfer lock on, two-factor login on, password stored safely'],
        ['Access for others', 'Designer or IT contact added as a user, not the owner'],
        ['Calendar reminder', 'Expiry date noted 60 days ahead'],
    ]),
],
faq=[
    ('How long does a domain transfer take?', 'Transfers between registrars for common extensions usually finish within about a week once you have approved them. Your website and email keep working during the transfer if the DNS settings stay the same.'),
    ('Does transferring a domain move my website?', 'No. The domain and the hosting are separate. Transferring the domain changes where it is registered, not where the website files live.'),
    ('What happens if my domain expires?', 'Your website and email stop working. Most registrars offer a grace period to renew at the normal price, then a redemption period with a restore fee. After that, the domain can be released to the public.'),
],
sources=[('ICANN: EPP status codes, what do they mean and why should I know?', 'https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en')],
)

# ------------------------------------------------------------------ who hosts
s = 'psg-who-hosts'
X['who-hosts-a-website'] = dict(
sections=[
    H2('The 4 companies behind most websites'),
    P('Part of the confusion is that a typical small business website relies on up to four different services, and they are often with different companies. Knowing which is which makes every lookup easier to read.'),
    TABLE(['Service', 'What it does', 'How to find it'], [
        ['Domain registrar', 'Holds the registration of your domain name', 'The &ldquo;Registrar&rdquo; line in ICANN Lookup'],
        ['DNS provider', 'Points the domain to your website and email', 'The name servers'],
        ['Web host', 'Stores and serves your website files', 'Name servers, IP address lookup, invoices'],
        ['Email provider', 'Runs your business inbox', 'The domain&rsquo;s MX (mail) records'],
    ]),
    P('A common setup looks like this: the domain is registered with a registrar, the DNS is managed at Cloudflare, the website is on a hosting company, and email is on Google Workspace or Microsoft 365. Each one has its own login, and each one needs to be in your name.'),
    H2('How to read common name server patterns'),
    P('Name servers are just addresses, but their names give strong clues. Some patterns you will see often:'),
    UL(['<strong>Names that include a hosting company&rsquo;s domain</strong> (for example ns1.<em>hostname</em>.com): the host probably manages DNS and the website.',
        '<strong>Names ending in ns.cloudflare.com</strong>: DNS is at Cloudflare. The host could be anyone; use the Cloudflare dashboard or Method 1.',
        '<strong>Names ending in registrar-servers.com</strong>: Namecheap&rsquo;s default DNS. The domain is likely at Namecheap, but the website could be hosted elsewhere.',
        '<strong>Names ending in domaincontrol.com</strong>: GoDaddy&rsquo;s DNS. Same idea: it shows where DNS is managed, not necessarily the host.',
        '<strong>Generic or white-label names</strong> (such as ns1.<em>somethingserver</em>.com): many resellers and agencies use their own names. The IP lookup usually reveals the real network.']),
    H2('Bonus method: check the response headers'),
    P('Some hosts add their name to the technical information a server sends with every page. To see it, open the website in Chrome, press F12 to open DevTools, go to the <strong>Network</strong> tab, reload the page and click the first item (your domain). Under <strong>Response Headers</strong>, look at lines such as <code>server</code>, <code>x-powered-by</code> or headers that mention a host or cache brand. It is not always there, but when it is, it is a quick confirmation.'),
    H2('Why one IP address can belong to hundreds of websites'),
    P('On shared hosting, many websites live on the same server and share one IP address. That is normal and does not mean anything is wrong with your site. It does mean that &ldquo;reverse IP&rdquo; tools listing other sites on the same address are not a reliable way to judge your host. Focus on the network owner, not the neighbours.'),
    H2('What if you can&rsquo;t get into the hosting account?'),
    OL(['Contact the host&rsquo;s support team and explain that you are the owner of the domain and the business.',
        'Be ready to prove it: hosts usually ask for things like the account email, a recent invoice, the last four digits of the card used, or proof that you control the domain.',
        'If the account belongs to a former designer or agency, ask them to transfer it to you or to give you a full backup of the website and database.',
        'If nobody can access the account, you may need to rebuild the site on new hosting from a backup or the live site. Keep the domain in your control so you can point it to the new host.']),
    H2('Website handover checklist: what to collect'),
    P('Whenever a website changes hands (a designer finishes a project, an employee leaves, you buy a business), collect these details and store them in a password manager:'),
    TABLE(['Item', 'Why you need it'], [
        ['Domain registrar login', 'To renew the domain and change DNS'],
        ['DNS provider login (if different, e.g. Cloudflare)', 'To point the domain to a new host or email provider'],
        ['Hosting account login', 'To renew, restore backups and get support'],
        ['Website admin login (e.g. WordPress)', 'To update content and plugins'],
        ['Email admin login', 'To add users and reset passwords'],
        ['Recent full backup', 'So you can rebuild the site if anything goes wrong'],
        ['Google Business Profile, Analytics and Search Console access', 'So your marketing data stays with you'],
        ['List of paid plugins, themes and licences', 'So renewals and updates don&rsquo;t lapse'],
    ]),
    H2('Before you move to a new host'),
    UL(['Download a full backup (files and database) before you change anything.',
        'Check where your email is hosted. If it is on the old host, plan the email move separately so you don&rsquo;t lose messages.',
        'Don&rsquo;t cancel the old hosting until the new site is live, DNS has updated and you have checked forms and email.',
        'Test the new site on a temporary address before switching the domain.']),
],
faq=[
    ('Is it legal to look up who hosts a website?', 'Yes. Name servers and IP address ownership are public information that anyone can look up.'),
    ('Can I change my web host without changing my domain?', 'Yes. You move the website files to the new host, then update the DNS or name servers so the domain points there. The domain can stay at the same registrar.'),
    ('How do I find out who hosts my email?', 'Look up the domain&rsquo;s MX records with a DNS tool such as Google&rsquo;s Admin Toolbox Dig. They usually name the email provider.'),
],
sources=[],
)

# ------------------------------------------------------------------ mobile
s = 'psg-check-mobile'
X['check-website-on-mobile'] = dict(
sections=[
    H2('Why checking mobile matters for Google too'),
    P('It is not only about visitors. Google says it uses the mobile version of a site&rsquo;s content for indexing and ranking, known as mobile-first indexing. If something is missing, hidden or broken on your mobile pages, Google may not see it either. So text, headings, images with alt text and links that matter should be on the mobile version, not only on desktop.'),
    H2('Method 4: Safari Responsive Design Mode (Mac)'),
    OL(['Open Safari and go to <strong>Settings</strong> &gt; <strong>Advanced</strong>.',
        'Tick the option to show the Develop menu (called &ldquo;Show features for web developers&rdquo; in recent versions).',
        'Open your website, then choose <strong>Develop</strong> &gt; <strong>Enter Responsive Design Mode</strong>.',
        'Pick an iPhone or iPad size from the list to preview your page.']),
    P('This is useful because Safari is the browser most iPhone users see, and small differences between browsers do show up in fonts, forms and video.'),
    H2('How to test a slow mobile connection on your computer'),
    P('Your office Wi-Fi is probably much faster than a customer&rsquo;s phone signal. Chrome lets you simulate a slower connection:'),
    OL(['Open DevTools (F12) and go to the <strong>Network</strong> tab.',
        'Find the throttling menu (it usually says &ldquo;No throttling&rdquo;) and choose a slower preset such as a 4G or 3G option.',
        'Reload the page and watch how long it takes before text and buttons appear.',
        'Set it back to &ldquo;No throttling&rdquo; when you&rsquo;re done.']),
    P('If the page stays blank for several seconds on a slower setting, large images, web fonts or third-party scripts are usually the cause.'),
    H2('Advanced: inspect your real phone from your computer'),
    P('If something looks wrong only on your phone, you can connect an Android phone to your computer with a USB cable, turn on USB debugging in the phone&rsquo;s developer options, and open <code>chrome://inspect</code> in Chrome on your computer. You can then see and inspect the exact page your phone is showing. Safari offers a similar feature for iPhones through the Develop menu on a Mac. Most owners won&rsquo;t need this, but it is very handy for a web designer fixing a phone-only bug.'),
    H2('Common mobile problems and how to fix them'),
    H3('The page is zoomed out or too wide'),
    P('If your whole page appears tiny on a phone, the page may be missing the viewport tag, which tells phones to use the device width. Modern themes include it, but older or custom sites sometimes don&rsquo;t. The standard tag is <code>&lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;</code> in the page head. Sideways scrolling is usually caused by a single wide element, such as a large image, a table or an embedded video with a fixed width.'),
    H3('Buttons and links are hard to tap'),
    P('Small links placed close together make people tap the wrong thing. The WCAG 2.2 accessibility guidelines set a minimum target size of 24 by 24 CSS pixels (with some exceptions), and bigger is better for main buttons such as Call and Book. Add space between menu items and links in the footer.'),
    H3('Text is too small or hard to read'),
    P('Body text around 16 pixels is a common starting point for phones. Check contrast too: light grey text on white looks elegant on a big monitor but is hard to read outdoors on a phone.'),
    H3('A pop-up covers the content'),
    P('Google&rsquo;s guidance on page experience warns against intrusive interstitials, pop-ups that make content hard to reach on mobile. Cookie notices and legally required notices are fine. For offers and newsletter sign-ups, use a small banner or show the pop-up later, and make sure the close button is easy to tap.'),
    H3('The layout looks fine on desktop but breaks on mobile'),
    P('Page builders such as Elementor let you set different sizes, spacing and visibility for mobile in their responsive mode. A heading that fits on desktop may need a smaller font size on mobile. Check each breakpoint after you edit a page.'),
    H2('Also test landscape mode and large text'),
    P('Turn your phone sideways and reload the page: menus and fixed headers sometimes cover half the screen in landscape. Then increase the text size in your phone&rsquo;s accessibility settings and check again. Many visitors use larger text, and a well-built site should still be readable and usable, which also supports the ' + il('law-firm-website-accessibility', 'accessibility basics') + ' every business site should meet.'),
    H2('A simple monthly mobile check routine'),
    TABLE(['When', 'What to do', 'Time'], [
        ['Every month', 'Open the homepage and top 3 pages on your phone; tap call, book and form buttons', '10 minutes'],
        ['Every month', 'Send a test form and check it arrives', '5 minutes'],
        ['After any update', 'Check changed pages in Chrome device mode and on your phone', '10 minutes'],
        ['Every quarter', 'Run PageSpeed Insights on mobile for the homepage and a key service page', '10 minutes'],
        ['Every quarter', 'Test on a different phone (iPhone vs Android) and in landscape', '10 minutes'],
    ]),
],
faq=[
    ('Does Google still have a Mobile-Friendly Test?', 'Google no longer offers the standalone Mobile-Friendly Test tool. Use Lighthouse in Chrome DevTools, PageSpeed Insights and a real phone instead.'),
    ('What screen size should I design for?', 'Don&rsquo;t design for one size. Check a small phone, a large phone and a tablet, and make sure the layout adapts smoothly between them.'),
    ('My site looks fine on my phone but a customer says it&rsquo;s broken. Why?', 'They may use a different browser, an older phone, larger text settings or a slower connection. Ask for a screenshot and their phone model, then test that setup in device mode.'),
],
sources=[('Google Search Central: Mobile-first indexing best practices', 'https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing'),
         ('W3C: Understanding WCAG 2.2 Target Size (Minimum)', 'https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html'),
         ('Google Search Central: Page experience', 'https://developers.google.com/search/docs/appearance/page-experience')],
)

# ------------------------------------------------------------------ QR
X['google-reviews-qr-code'] = dict(
sections=[
    H2('How to design a review card customers actually scan'),
    P('A QR code on its own is easy to ignore. A simple card or sign with a clear reason to scan works much better. Keep it to three elements:'),
    OL(['<strong>A short headline</strong> that speaks to the customer, such as &ldquo;How did we do?&rdquo;',
        '<strong>The QR code</strong>, large and with plenty of white space around it.',
        '<strong>One line of instruction</strong>, such as &ldquo;Point your phone camera here to leave a Google review.&rdquo;']),
    P('Add your logo and business name so people know it&rsquo;s genuine. Free design tools such as Canva have business card and table-tent templates you can drop the saved QR image into.'),
    H2('QR code printing tips'),
    UL(['<strong>Size:</strong> a common rule of thumb is to print the code at least 2 cm (about 0.8 in) wide for something held in the hand, and larger for signs read from a distance. A rough guide is about 1 cm of code width for every 10 cm of scanning distance.',
        '<strong>Quiet zone:</strong> leave a clear white margin around the code. Don&rsquo;t place it on a busy photo or pattern.',
        '<strong>Contrast:</strong> dark code on a light background scans best. Avoid light colours and don&rsquo;t invert it.',
        '<strong>Don&rsquo;t stretch it:</strong> resize it evenly, keeping it square.',
        '<strong>Test before printing in bulk:</strong> print one copy and scan it with an iPhone and an Android phone, in the light where it will be used.',
        '<strong>Glossy surfaces:</strong> strong glare can stop phones reading the code. A matte finish is safer for counter signs.']),
    H2('Copy-paste messages to share your review link'),
    P('The QR code is perfect in person. For customers you deal with online, send the review link instead. Ask everyone the same way, soon after the job is done. Some ready-to-use messages:'),
    H3('Email'),
    P('<em>Subject: Thank you from [Business name]</em><br>Hi [Name], thank you for choosing us. If you have a minute, we&rsquo;d really appreciate an honest review on Google. It helps other people find us: [review link]. Thank you! [Your name]'),
    H3('Text message or WhatsApp'),
    P('<em>Hi [Name], thanks again for visiting [Business name] today. Would you mind sharing your experience on Google? [review link] Thank you!</em>'),
    H3('In person'),
    P('<em>&ldquo;Thanks so much. If you have a moment later, we&rsquo;d love an honest Google review. Just scan this code with your camera.&rdquo;</em>'),
    P('Keep it short, polite and the same for every customer. Don&rsquo;t ask only the people you think will leave five stars, which Google&rsquo;s policy prohibits.'),
    H2('How to reply to the reviews you get'),
    P('Replying shows future customers that you care. Keep replies short, personal and calm:'),
    UL(['<strong>Positive review:</strong> &ldquo;Thank you, [Name]! We&rsquo;re so glad you enjoyed [specific thing]. See you next time.&rdquo;',
        '<strong>Mixed review:</strong> thank them, acknowledge the issue, and say what you are doing about it.',
        '<strong>Negative review:</strong> stay polite, don&rsquo;t argue or share private details, apologise for the experience and invite them to contact you directly to sort it out.']),
    P('If a review breaks Google&rsquo;s policies (for example spam, or a review clearly about a different business), you can report it from your Business Profile. A review simply being negative is not a reason Google will remove it.'),
    H2('Troubleshooting: QR code not working'),
    TABLE(['Problem', 'Likely cause', 'Fix'], [
        ['No &ldquo;Get more reviews&rdquo; option', 'Not signed in as an owner or manager, or using a phone', 'Use a computer and the account that manages the profile'],
        ['Phone won&rsquo;t scan the printed code', 'Too small, low contrast, glare or no white margin', 'Print larger on matte paper with a clear border'],
        ['Code opens the wrong business', 'Code saved from a different profile or location', 'Download a fresh code from the correct profile'],
        ['Customers say they can&rsquo;t post', 'They aren&rsquo;t signed in to a Google account', 'Mention in your message that a Google account is needed'],
        ['Reviews don&rsquo;t appear', 'Google may hold or filter reviews it flags', 'Don&rsquo;t offer incentives or ask in bulk from one device; reviews may take time to show'],
    ]),
    H2('Have more than one location?'),
    P('Each location has its own Business Profile, so each needs its own review link and QR code. Label the files clearly (for example, &ldquo;reviews-qr-downtown.png&rdquo;) so the right code goes on the right counter. Reviews should go to the location the customer actually visited.'),
    H2('How to measure whether it&rsquo;s working'),
    P('Note your total number of reviews and average rating on the day you put the QR code out. Check again every month. If you use the review link in emails, you can see how many people you sent it to compared with how many new reviews arrived. A steady trickle of recent reviews is worth more than a burst, because people reading reviews look at how recent they are.'),
],
faq=[
    ('Do I need a verified Business Profile to get a review QR code?', 'You need to manage the profile with an owner or manager account. If the review options don&rsquo;t appear, finish verification first.'),
    ('Can I change the design or colour of Google&rsquo;s QR code?', 'You can place it on any design, but keep the code itself dark on light and unstretched so phones can scan it reliably.'),
    ('Should I use a paid QR generator instead?', 'You don&rsquo;t need to. Google&rsquo;s own code is free and points straight to your review form. Paid tools are only useful if you want scan tracking.'),
],
sources=[],
)


def expand(article):
    x = X[article['slug']]
    orig = article['body']
    faq_h = H2('FAQ')
    concl = H2('Conclusion')
    def body():
        b = orig()
        i = b.index(faq_h)
        b = b[:i] + x['sections'] + b[i:]
        j = b.index(concl)
        extra = []
        for q, ans in x['faq']:
            extra += [H3(q), P(ans)]
        return b[:j] + extra + b[j:]
    article['body'] = body
    article['sources'] = article['sources'] + x['sources']
    return article

# ---- second round of additions
X['check-website-on-mobile']['sources'][2] = ('Google Search Central: Avoid intrusive interstitials and dialogs', 'https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials')
X['check-website-on-mobile']['sections'] += [
    H2('What to check on each type of page'),
    P('Different pages fail in different ways on a phone. When you test, go through your most important pages with these points in mind:'),
    TABLE(['Page', 'What to check on mobile'], [
        ['Homepage', 'Is it clear what you do and where you work within the first screen? Is the main button visible without scrolling?'],
        ['Service or product pages', 'Do prices, photos and the enquiry button show properly? Do long lists or tables fit?'],
        ['Contact page', 'Does the phone number start a call when tapped? Does the map load? Does the address open in a maps app?'],
        ['Booking or checkout', 'Can you complete the whole process with your thumb, including payment fields and confirmation?'],
        ['Blog posts', 'Are headings, images and links readable? Are embedded videos the right width?'],
        ['Menu', 'Does the mobile menu open, scroll if it is long, and close again? Can you reach every page?'],
    ]),
    H2('Make your forms easy to fill on a phone'),
    P('Forms are where most mobile visitors give up. A few small details make a big difference:'),
    UL(['<strong>Use the right field types.</strong> Phone fields should open the number keypad, and email fields should open a keyboard with the @ sign. Most form plugins do this when you choose the &ldquo;phone&rdquo; or &ldquo;email&rdquo; field type instead of plain text.',
        '<strong>Ask for less.</strong> Every extra field is more typing on a small screen. Name, contact details and a short message are often enough for a first enquiry.',
        '<strong>Allow autofill.</strong> Phones can fill in names, emails and addresses automatically when fields are labelled properly.',
        '<strong>Show clear errors.</strong> If something is missing, the message should appear next to the field, not only at the top of the page.',
        '<strong>Make the submit button big</strong> and show a clear thank-you message after sending.']),
    H2('Images and video on mobile'),
    P('Large images are the most common reason a page is slow on a phone. Upload images at a sensible size (a photo that will display at most around 1,200 pixels wide rarely needs to be 4,000 pixels), compress them, and use a modern format such as WebP where your site supports it. WordPress automatically creates smaller versions of uploaded images and serves the right size to each screen when your theme supports it. For video, use an embedded player that adapts to the screen width, and avoid autoplaying videos with sound.'),
]
X['who-hosts-a-website']['sections'] += [
    H2('What kind of hosting have you found?'),
    P('Once you know the company, it helps to know what type of hosting you are on, because it affects what you can change and who is responsible for updates:'),
    TABLE(['Type', 'What it means for you'], [
        ['Shared hosting', 'Low cost; many sites on one server. You (or your designer) handle WordPress updates and most fixes'],
        ['Managed WordPress hosting', 'The host handles server tuning, backups and often updates. Usually more expensive, with better support'],
        ['VPS or cloud server', 'A server set aside for you. Flexible, but someone technical must manage it'],
        ['Website builder (Wix, Squarespace, WordPress.com, Shopify)', 'Hosting is included in the plan. Fewer technical tasks, but moving away can take more work'],
    ]),
]
X['google-reviews-qr-code']['sections'] += [
    H2('Review link or QR code: which should you use?'),
    TABLE(['Situation', 'Best option', 'Why'], [
        ['Customer is in front of you', 'QR code', 'They scan it with their camera, no typing'],
        ['Follow-up email or text', 'Review link', 'One tap on the device they are already using'],
        ['Website or email signature', 'Review link as a button', 'Scanning a code on the same screen is awkward'],
        ['Printed invoice or receipt', 'QR code', 'Paper can&rsquo;t be tapped'],
        ['Social media post', 'Review link', 'Most people browse social media on their phone'],
    ]),
    H2('When is the best time to ask for a review?'),
    P('Ask when the customer is most satisfied and the experience is fresh: right after a job is finished, a product is delivered or a problem is solved. For services that take time, such as a renovation or a long project, ask at the end and again at a natural milestone if appropriate. Avoid asking while a complaint or payment issue is still open. Sort the issue out first.'),
    P('Whatever timing you choose, apply it to every customer. Building the request into your normal process, such as a line in every final invoice or a standard follow-up email, keeps it consistent and within Google&rsquo;s rules.'),
    H2('Get your team on board'),
    P('If customers deal with staff rather than you, a short team briefing helps more than any sign:'),
    UL(['Explain why reviews matter: they help new customers trust the business.',
        'Agree on one simple sentence everyone uses when they mention the QR code.',
        'Make clear that staff must never offer discounts or freebies for reviews, or write reviews themselves.',
        'Put a card where staff can point to it easily, so asking feels natural rather than pushy.',
        'Share new positive reviews with the team. It is good for morale and keeps the habit going.']),
    H2('Where not to put your review QR code'),
    UL(['On a page or screen people are already looking at on their phone, such as your website. Use the link there instead.',
        'Somewhere customers see it before they have experienced your service, such as the front door, so they have nothing to review yet.',
        'On materials that will be used for years, such as vehicle signage, unless you are sure the profile and code will not change.',
        'Next to anything that sounds like a reward, such as a prize draw or discount offer.']),
]
X['google-reviews-qr-code']['faq'] += [
    ('Can customers leave a review without a Google account?', 'No. Google requires reviewers to be signed in to a Google account. Most Android users and many iPhone users already are, but it helps to mention it in your message.'),
    ('Can I ask a customer to change or remove a negative review?', 'You can reply publicly and try to solve the problem, and a happy customer may choose to update their review. Don&rsquo;t pressure them or offer anything in return for changing it.'),
    ('How often should I download a new QR code?', 'Only if your profile changes, for example if you create a new profile for a moved business. Otherwise the same code keeps working. Test it every few months.'),
]
