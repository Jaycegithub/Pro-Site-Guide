# Settings before speed work (2026-11-21)
Elementor > Settings:
- elementor_google_font=1, elementor_font_display=swap, elementor_css_print_method=external
- elementor_optimized_image_loading=1, elementor_optimized_gutenberg_loading=1, elementor_lazy_load_background_images=1
- elementor_local_google_fonts=0, elementor_element_cache_ttl=24
- experiments: e_optimized_css_files=default, e_font_icon_svg=default, e_optimized_markup=default
WP Fastest Cache: every option OFF.
Jetpack Boost: see later section.

## Changes made (2026-11-21)
- Elementor: Element Caching -> disabled; Load Google Fonts locally -> on; Inline font icons (SVG) -> active; CSS print method -> internal (required by WP Fastest Cache).
- WP Fastest Cache: Cache, Preload (home/posts/pages/categories), no cache for logged-in users, clear on new/updated post, Minify HTML, Minify CSS, Gzip, Browser caching, Disable emojis.
- Jetpack Boost (free plan): Critical CSS (manual, regenerate after design changes), Defer non-essential JS, Optimize LCP images. Concatenate CSS/JS tried and turned OFF (broke styling together with WPFC minify).
- WPCode header: GTM now loads on first interaction or after 8s (original saved in speed-2026-11-21-wpcode-header-before.html).
- WPCode PHP snippet #868 "PSG speed: lazy-load Latest Posts images".
- Homepage (page 28): small.g colour #16A34A -> #15803D (contrast).
- 8 posts: affiliate note link text "Learn more" -> "Read our affiliate disclosure".
- Glossary (page 131): descriptive "Learn more about <term>" links; letter headings moved out of <dl>.
Backups of edited content: site-backups/speed-2026-11-21/
