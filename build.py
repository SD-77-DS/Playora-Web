#!/usr/bin/env python3
"""Generates the static Playora site. Each page is served at its own clean path: /privacy/, /data-safety/ ..."""
import os, html

# Production settings (override via environment in CI):
#   BASE_PATH  "" for a custom domain / user site, "/Playora-Web" for a GitHub Pages project site
#   SITE_URL   public origin + base path, used for canonical links, robots.txt and sitemap.xml
BASE = os.environ.get("BASE_PATH", "").rstrip("/")
OUT = os.environ.get("OUT_DIR", "site")  # "client" for Zoho Catalyst
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")

UPDATED = "November 16, 2026"
CONTACT = "sasiamrit@gmail.com"

NAV = [("/", "Home"), ("/privacy/", "Privacy Policy"), ("/data-safety/", "Data Safety"),
       ("/content-rating/", "Content Rating"), ("/audience-and-ads/", "Audience & Ads"),
       ("/permissions/", "Permissions"), ("/contact/", "Contact")]

def layout(path, title, body):
    CANON = f'<link rel="canonical" href="{SITE_URL}{path}">' if SITE_URL else ""
    links = "".join(f'<a href="{h}"{" class=active" if h == path else ""}>{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Playora</title>
<meta name="description" content="Playora: a local and network media player. {html.escape(title)}.">
<link rel="icon" href="/assets/icon.png">
{CANON}
<link rel="stylesheet" href="/assets/style.css">
</head><body>
<header><a class="brand" href="/"><img src="/assets/icon.png" alt="" width="36" height="36"> Playora</a>
<nav>{links}</nav></header>
<main>{body}</main>
<footer>© 2026 Playora · Last updated {UPDATED}</footer>
</body></html>""".replace('href="/', f'href="{BASE}/').replace('src="/', f'src="{BASE}/')

def table(rows, head):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'

pages = {}

pages["/"] = ("Home", f"""
<section class="hero"><img src="/assets/icon.png" alt="Playora icon" width="120" height="120">
<h1>Playora</h1>
<p class="lead">A fast, private media player for the videos and music on your device, and for links you open.</p></section>
<section class="cards">
<a class="card" href="/privacy/"><h3>Privacy Policy</h3><p>What Playora accesses and what it never collects.</p></a>
<a class="card" href="/data-safety/"><h3>Data Safety</h3><p>Answers to Google Play's data safety questions.</p></a>
<a class="card" href="/content-rating/"><h3>Content Rating</h3><p>Why Playora has a simple content profile.</p></a>
<a class="card" href="/audience-and-ads/"><h3>Audience &amp; Ads</h3><p>Target audience and the no-ads declaration.</p></a>
<a class="card" href="/permissions/"><h3>Permissions</h3><p>Foreground service, media files and notifications explained.</p></a>
<a class="card" href="/contact/"><h3>Contact</h3><p>Privacy and support questions.</p></a>
</section>
<h2>Features</h2>
<ul>
<li>Plays local video and audio from your device.</li>
<li>Plays network streams and links (HLS, DASH and direct files).</li>
<li>Background playback with lock-screen and notification controls.</li>
<li>Picture-in-Picture, audio-only mode, equalizer, sleep timer and playback speed.</li>
<li>No ads, no analytics and no account.</li>
</ul>""")

pages["/privacy/"] = ("Privacy Policy", f"""
<h1>Privacy Policy</h1>
<p class="muted">Last updated {UPDATED}</p>
<p>Playora is a media player. This policy explains what the app accesses, what it does with that information and how to reach us.</p>

<h2>1. What information Playora accesses</h2>
<ul>
<li><b>Local video and audio files.</b> With your permission, Playora reads the media stored on your device so you can browse and play it.</li>
<li><b>Files or links you open.</b> When you open a file from another app, share a file to Playora or enter a URL, Playora reads only that item to play it.</li>
<li><b>Playback state.</b> Playback position, history, playlists and your settings are saved <b>on your device only</b> so playback can resume.</li>
</ul>

<h2>2. Personal information</h2>
<p>Playora does <b>not</b> collect personal information. It has no accounts, sign-in or registration, and it does not collect your name, email address, location or contacts.</p>

<h2>3. Sharing with third parties</h2>
<p>Playora does not sell or share your information with anyone. It does not upload your media files or your listening and viewing history to any server.</p>

<h2>4. How local media files are accessed</h2>
<p>Playora uses Android's media permissions (<code>READ_MEDIA_VIDEO</code> and <code>READ_MEDIA_AUDIO</code> on Android 13+, and storage read access on older versions) to list and play the media you choose. Files are read on your device and are never copied off it. You can revoke the permission at any time in Android Settings, and files opened through another app need no broad permission.</p>

<h2>5. Network streams</h2>
<p>If you enter a URL, Playora connects directly from your device to the server hosting that stream, as any player or browser would. That server may receive your IP address and normal request information. Playora has no control over third-party servers, so review their privacy policies.</p>

<h2>6. Analytics, advertising and crash reporting</h2>
<p>Playora includes <b>no</b> analytics, advertising or crash-reporting services, and no third-party tracking. If this changes, this policy and the Play Store declarations will be updated first.</p>

<h2>7. Data retention and deletion</h2>
<p>Everything Playora stores (history, playlists, settings) lives on your device. Clear it from Android Settings → Apps → Playora → Storage, or uninstall the app.</p>

<h2>8. Children</h2>
<p>Playora is a general-purpose utility and does not knowingly collect any information from anyone, including children.</p>

<h2>9. Changes to this policy</h2>
<p>We will post any changes on this page and update the date above.</p>

<h2>10. Contact</h2>
<p>For privacy questions, write to <a href="/contact/">the contact page</a>.</p>""")

pages["/data-safety/"] = ("Data Safety", f"""
<h1>Data Safety</h1>
<p class="muted">Reference answers for the Google Play Console data safety form, based on the app's actual implementation. Last updated {UPDATED}</p>
<div class="note">Accessing media on the device is <b>not</b> the same as collecting or sharing it. Data is "collected" only when it leaves the device.</div>
{table([
 ["Does the app upload videos or audio files to a server?", "<b>No.</b> Files are read and played on the device only."],
 ["Does it collect device identifiers?", "<b>No.</b>"],
 ["Does it collect analytics?", "<b>No.</b> No analytics SDK is included."],
 ["Does it use third-party advertising SDKs?", "<b>No.</b>"],
 ["Does it collect crash reports?", "<b>No.</b> No crash-reporting SDK is included."],
 ["Does it collect personal info, location, contacts or financial data?", "<b>No.</b>"],
 ["Is any data shared with third parties?", "<b>No.</b>"],
 ["Is data encrypted in transit?", "Playora sends no user data. Streams are fetched from the server you choose, over HTTPS when the link uses it."],
 ["Can users request data deletion?", "Nothing is stored off-device. Local data is removed by clearing storage or uninstalling."],
], ["Question", "Playora's answer"])}
<h2>Suggested form selections</h2>
<ul><li>Data collected: <b>None</b></li><li>Data shared: <b>None</b></li><li>Security practices: no data collected, so no account or deletion mechanism is needed.</li></ul>
<p class="muted">Re-check these answers whenever an SDK is added (for example analytics or AdMob).</p>
<p>See also the <a href="/privacy/">Privacy Policy</a>.</p>""")

pages["/content-rating/"] = ("Content Rating", f"""
<h1>Content Rating</h1>
<p class="muted">Reference answers for the Play Console content rating questionnaire. Last updated {UPDATED}</p>
<p>Playora is a media player. It plays media the user already owns or links to, and it does not publish or host any content itself.</p>
{table([
 ["Violence", "No"], ["Sexual content", "No"], ["Profanity / crude humor", "No"],
 ["Gambling", "No"], ["Controlled substances", "No"],
 ["User-generated content shared between users", "No. There is no social, chat or upload feature."],
 ["Location sharing", "No"], ["In-app purchases", "No"],
 ["Provides access to content the user chooses", "Yes. The user supplies local files or URLs; the app does not curate content."],
], ["Category", "Answer"])}
<p class="muted">Because the app plays user-selected media, it generally receives the lowest age rating. Answer the questionnaire based on the app's own behavior.</p>""")

pages["/audience-and-ads/"] = ("Audience & Ads", f"""
<h1>Target Audience &amp; Ads</h1>
<h2>Target audience</h2>
<p>Playora is a general-purpose utility app for <b>users aged 13 and over</b>. It is not designed for children and does not contain content aimed at them. In Play Console, choose the 13+ age groups.</p>
<h2>Ads declaration</h2>
<p><b>Playora contains no advertisements.</b> In Play Console, answer "No" to "Does your app contain ads?".</p>
<div class="note">If you add AdMob or any ad SDK later, update this declaration, the <a href="/data-safety/">data safety form</a> and the <a href="/privacy/">privacy policy</a> before releasing the update.</div>""")

pages["/permissions/"] = ("Permissions", f"""
<h1>Permissions Explained</h1>
<p class="muted">Justifications for the Play Console declarations. Last updated {UPDATED}</p>

<h2 id="foreground-service">Foreground service: media playback</h2>
<p><code>FOREGROUND_SERVICE</code> and <code>FOREGROUND_SERVICE_MEDIA_PLAYBACK</code></p>
<p><b>Why it is essential:</b> Playora's core function is playing audio and video. When you start playback and then minimize the app or lock your phone, Android needs a foreground service of type <code>mediaPlayback</code> to keep playing. Without it, the system would stop playback as soon as the screen turns off.</p>
<ol><li>Open a video or song in Playora and start playing.</li><li>Minimize the app or lock the phone.</li><li>Playback continues and can be controlled from the notification and lock screen.</li></ol>
<p>The service runs only while media is playing or paused by the user, and stops when the app is closed with nothing playing. It does nothing else.</p>

<h2 id="media">Photo and video permissions</h2>
<p><code>READ_MEDIA_VIDEO</code> and <code>READ_MEDIA_AUDIO</code> (Android 13+), and <code>READ_EXTERNAL_STORAGE</code> up to Android 12L</p>
<p><b>Why it is essential:</b> A media player must show the user's local library so they can pick something to play. Playora cannot offer this using the system photo picker alone, because its job is to browse and play whole libraries of video and music, with folders, albums, artists and queues.</p>
<ol><li>The user opens Playora and is asked for media access.</li><li>The user grants permission.</li><li>Playora lists the videos and music available on the device.</li><li>The user selects an item and Playora plays it.</li></ol>
<p>Media is read only on the device and is never uploaded. Playora does not request access to photos or images. It also works without the permission for files opened from other apps or share sheets.</p>
<div class="note">Google Play restricts broad media permissions. A media player is a relevant core use case, but approval is not guaranteed, so describe this flow clearly in the declaration form.</div>

<h2 id="notifications">Notifications</h2>
<p><code>POST_NOTIFICATIONS</code></p>
<p><b>Why:</b> To show the media playback notification, so you can control Playora without opening it:</p>
<ul><li>Play / Pause</li><li>Next and previous track</li><li>Playback information (title, artist and artwork)</li></ul>
<p>Playora does not send marketing or promotional notifications.</p>

<h2 id="other">Other permissions</h2>
{table([
 ["<code>INTERNET</code>, <code>ACCESS_NETWORK_STATE</code>", "Play network streams and links you enter, and detect connectivity."],
 ["<code>WAKE_LOCK</code>", "Keep playback running while the screen is off."],
], ["Permission", "Purpose"])}""")

pages["/contact/"] = ("Contact", f"""
<h1>Contact</h1>
<p>Questions about privacy, permissions or the app? Reach out by email:</p>
<p class="big"><a href="mailto:{CONTACT}">{CONTACT}</a></p>
<p class="muted">Include your Android version and device model for support requests.</p>""")

for path, (title, body) in pages.items():
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(layout(path, title, body))
open(OUT + "/404.html", "w").write(layout("/404", "Page not found",
    '<h1>Page not found</h1><p>That page does not exist. <a href="/">Back to home</a>.</p>').replace(
    f'<link rel="canonical" href="{SITE_URL}/404">', '').replace("</head>", '<meta name="robots" content="noindex"></head>'))
open(OUT + "/robots.txt", "w").write("User-agent: *\nAllow: /\n" + (f"Sitemap: {SITE_URL}/sitemap.xml\n" if SITE_URL else ""))
if SITE_URL: open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"<url><loc>{SITE_URL}{p}</loc></url>\n" for p in pages) + "</urlset>\n")
print("built", len(pages), "pages")
