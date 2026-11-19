"""Gutenberg block helpers matching the existing ProSiteGuide post format."""
import json, html

AFF = {
    "wpcom": "https://automattic.pxf.io/c/8231073/1919834/22744",
    "jetpack": "https://automattic.pxf.io/c/8231073/1946458/22744",
    "pressable": "https://automattic.pxf.io/c/8231073/2021364/22744",
    "woo": "https://automattic.pxf.io/c/8231073/1946431/22744",
    "akismet": "https://automattic.pxf.io/c/8231073/2021511/22744",
    "sensei": "https://automattic.pxf.io/c/8231073/2021367/22744",
    "wpjm": "https://automattic.pxf.io/c/8231073/2021366/22744",
}
SITE = "https://prositeguide.com"


def a(key, text, sub):
    return f'<a href="{AFF[key]}?subId1={sub}" target="_blank" rel="sponsored nofollow noopener">{text}</a>'


def il(slug, text):
    return f'<a href="{SITE}/{slug}/">{text}</a>'


def P(t, cls=None):
    if cls:
        return f'<!-- wp:paragraph {{"className":"{cls}"}} --><p class="{cls}">{t}</p><!-- /wp:paragraph -->'
    return f'<!-- wp:paragraph --><p>{t}</p><!-- /wp:paragraph -->'


def H2(t): return f'<!-- wp:heading --><h2 class="wp-block-heading">{t}</h2><!-- /wp:heading -->'
def H3(t): return f'<!-- wp:heading {{"level":3}} --><h3 class="wp-block-heading">{t}</h3><!-- /wp:heading -->'


def UL(items):
    return '<!-- wp:list --><ul class="wp-block-list">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul><!-- /wp:list -->'


def OL(items):
    return '<!-- wp:list {"ordered":true} --><ol class="wp-block-list">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol><!-- /wp:list -->'


def TABLE(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<!-- wp:table --><figure class="wp-block-table"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></figure><!-- /wp:table -->'


DISCLOSURE = ('<!-- wp:paragraph {"className":"psg-aff-note"} -->\n<p class="psg-aff-note"><em>This guide contains affiliate links. '
              'If you buy through them, we may earn a commission at no extra cost to you. It never changes our recommendations. '
              '<a href="https://prositeguide.com/affiliate-disclosure/">Learn more</a>.</em></p>\n<!-- /wp:paragraph -->')


def QUICK(lead, link_html):
    return ('<!-- wp:html --><aside class="psg-aff-top" aria-label="Quick pick"><span class="psg-aff-top-k">Quick pick</span>'
            f'<p><strong>{lead}</strong> {link_html}</p><p class="psg-aff-top-d">We may earn a commission at no extra cost to you. '
            'It never changes our recommendations.</p></aside><!-- /wp:html -->')


def FAQ(pairs):
    out = [H2('FAQ')]
    for q, ans in pairs:
        out += [H3(q), P(ans)]
    return out


def BRANDS(tags):
    links = ''.join(f'<a href="{SITE}/tag/{slug}/">{name}</a>' for name, slug in tags)
    return f'<!-- wp:html --><nav class="psg-brands" aria-label="Brands in this guide"><span>Brands in this guide:</span>{links}</nav><!-- /wp:html -->'


def SOURCES(items):
    return [H2('Sources'), UL([f'<a href="{u}">{t}</a>' for t, u in items])]


def BREAD(cat_name, cat_slug, title, slug):
    d = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": cat_name, "item": f"{SITE}/category/{cat_slug}/"},
        {"@type": "ListItem", "position": 3, "name": title, "item": f"{SITE}/{slug}/"}]}
    return f'<!-- wp:html --><script type="application/ld+json" class="psg-breadcrumb">{json.dumps(d)}</script><!-- /wp:html -->'


CONSULT = P('Want this handled for you? ProSiteGuide builds and maintains fast, secure WordPress sites. '
            '<a href="mailto:prositeguidejayce@gmail.com?subject=Website%20consultation">Book a free consultation</a>.')


def IMG(mid, url, alt, cap, w, h):
    return (f'<!-- wp:image {{"id":{mid},"sizeSlug":"full","linkDestination":"none"}} -->\n'
            f'<figure class="wp-block-image size-full"><img src="{url}" alt="{html.escape(alt)}" class="wp-image-{mid}" width="{w}" height="{h}" loading="lazy"/>'
            f'<figcaption class="wp-element-caption">{cap}</figcaption></figure>\n<!-- /wp:image -->')
