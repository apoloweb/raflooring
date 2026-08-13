# -*- coding: utf-8 -*-
"""Generates the static pages for the RA Flooring site.
Run:  python build.py   (writes the .html files next to this script)
"""
import io, os

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE = "(754) 246-2843"
TEL = "tel:+17542462843"
EMAIL = "roque@raflooringusa.com"
REVIEWS = "https://www.google.com/search?q=RA+Contractor+Flooring+Inc+reviews"
IG = "https://www.instagram.com/racontractorfloor/"
FB = "https://www.facebook.com/racontractorfloor/"

CARET = '<svg width="11" height="7" viewBox="0 0 11 7" fill="none"><path d="M1 1l4.5 4.5L10 1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2-.1-1.3-.1-1.7-.1-4.9s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4 1.3-.1 1.7-.1 4.9-.1zm0 2c-3.1 0-3.5 0-4.8.1-1.1.1-1.4.2-1.7.3-.4.2-.7.3-1 .6-.3.3-.5.6-.6 1-.1.3-.3.6-.3 1.7-.1 1.3-.1 1.6-.1 4.8s0 3.5.1 4.8c.1 1.1.2 1.4.3 1.7.2.4.3.7.6 1 .3.3.6.5 1 .6.3.1.6.3 1.7.3 1.3.1 1.6.1 4.8.1s3.5 0 4.8-.1c1.1-.1 1.4-.2 1.7-.3.4-.2.7-.3 1-.6.3-.3.5-.6.6-1 .1-.3.3-.6.3-1.7.1-1.3.1-1.6.1-4.8s0-3.5-.1-4.8c-.1-1.1-.2-1.4-.3-1.7-.2-.4-.3-.7-.6-1-.3-.3-.6-.5-1-.6-.3-.1-.6-.3-1.7-.3-1.3-.1-1.6-.1-4.8-.1zm0 3.4a5.4 5.4 0 110 10.8 5.4 5.4 0 010-10.8zm0 2a3.4 3.4 0 100 6.8 3.4 3.4 0 000-6.8zm5.6-3.5a1.25 1.25 0 110 2.5 1.25 1.25 0 010-2.5z"/></svg>'
FB_SVG = '<svg viewBox="0 0 24 24"><path d="M13.5 21v-7.5h2.5l.5-3h-3V8.6c0-.9.3-1.6 1.6-1.6H17V4.2c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.4H8.5v3h2.3V21h2.7z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>'


def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
'''


def navlink(href, label, active):
    cls = ' class="active"' if active == href else ''
    return f'<a href="{href}"{cls}>{label}</a>'


def header(active=''):
    return f'''<header class="site-header" id="siteHeader">
  <div class="container nav-wrap">
    <a href="index.html" class="brand">
      <img src="assets/img/logo-white.png" alt="RA Flooring logo">
      <span class="brand-text"><strong>RA Flooring</strong><small>Carpet · Vinyl · Hardwood · Tile</small></span>
    </a>
    <nav class="nav" id="mainNav">
      {navlink('index.html', 'Home', active)}
      {navlink('about.html', 'About', active)}
      <div class="nav-drop">
        <a href="services.html" class="drop-toggle">Services {CARET}</a>
        <div class="drop-menu">
          <a href="services.html">Flooring Services</a>
          <a href="kitchen-remodeling.html">Kitchen Remodeling</a>
          <a href="bathroom-remodeling.html">Bathroom Remodeling</a>
          <a href="painting-services.html">Painting Services</a>
        </div>
      </div>
      {navlink('gallery.html', 'Gallery', active)}
      {navlink('contact.html', 'Contact', active)}
      <a class="btn btn-primary nav-cta" href="contact.html">Get a Free Quote</a>
      <a class="nav-phone" href="{TEL}"><span>Call us</span>{PHONE}</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>
'''


def contact_band(location="Davenport, FL"):
    return f'''<section class="contact-band" style="background-image:url('assets/img/contact-bg.webp')">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <h2>Let's get in touch.</h2>
        <p class="sub">Don't hesitate to contact us for more information.</p>
        <div class="info-item"><div class="k">Have any question?</div><div class="v"><a href="{TEL}">Call: {PHONE}</a></div></div>
        <div class="info-item"><div class="k">E-mail support</div><div class="v"><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
        <div class="info-item"><div class="k">Location</div><div class="v">{location}</div></div>
        <div class="social-row">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_SVG}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a>
        </div>
      </div>
      <div class="reveal reveal-d1">
        <div class="contact-photo"><img src="assets/img/cellphone.jpg" alt="Contact RA Flooring" loading="lazy"></div>
        <div class="badges-row on-dark">
          <img src="assets/img/badge-insured-w.png" alt="Fully Insured" loading="lazy">
          <img src="assets/img/badge-top-search-w.png" alt="Google Top Search" loading="lazy">
          <img src="assets/img/badge-guaranteed-w.png" alt="Google Guaranteed" loading="lazy">
          <img src="assets/img/badge-licensed-w.png" alt="Licensed" loading="lazy">
        </div>
      </div>
    </div>
  </div>
</section>
'''


def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="index.html" class="brand">
          <img src="assets/img/logo-white.png" alt="RA Flooring logo">
          <span class="brand-text"><strong>RA Flooring</strong><small>Carpet · Vinyl · Hardwood · Tile</small></span>
        </a>
        <p>RA Contractor Flooring Inc. — the trusted choice for high-quality flooring solutions in Central Florida. Expert vinyl, carpet, hardwood, epoxy and tile installations.</p>
        <div class="social-row">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_SVG}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a>
        </div>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="services.html">Flooring Services</a></li>
          <li><a href="kitchen-remodeling.html">Kitchen Remodeling</a></li>
          <li><a href="bathroom-remodeling.html">Bathroom Remodeling</a></li>
          <li><a href="painting-services.html">Painting Services</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Davenport, FL</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year"></span> RA Contractor Flooring Inc. All rights reserved.</span>
      <span><a href="privacy-policy.html">Privacy Policy</a> · <a href="terms-of-use.html">Terms of Use</a></span>
    </div>
  </div>
</footer>
<a href="{TEL}" class="float-call" aria-label="Call RA Flooring">{PHONE_SVG}</a>
<script src="assets/js/main.js"></script>
</body>
</html>
'''


def svc_card(img, title, desc, pill=None, link="contact.html", link_text="Learn more"):
    p = f'<span class="pill">{pill}</span>' if pill else ''
    return f'''<article class="svc-card reveal">{p}
  <div class="thumb"><img src="assets/img/{img}" alt="{title}" loading="lazy"></div>
  <div class="body"><h3>{title}</h3><p>{desc}</p><a class="link" href="{link}">{link_text} →</a></div>
</article>'''


def feat(icon, title, desc):
    return f'''<div class="feat reveal"><img src="assets/img/{icon}" alt="" loading="lazy"><div><h3>{title}</h3><p>{desc}</p></div></div>'''


def video_card(src, title, desc):
    return f'''<article class="video-card reveal">
  <video src="assets/video/{src}" controls preload="metadata" playsinline></video>
  <div class="body"><h3>{title}</h3><p>{desc}</p></div>
</article>'''


pages = {}

# ---------------------------------------------------------------- HOME
pages['index.html'] = head(
    "RA Flooring – Carpet, Vinyl, Hardwood & Tile in Davenport, FL",
    "RA Contractor Flooring Inc. — #1 in flooring and remodeling services for beautiful, lasting results. Expert vinyl, carpet, hardwood, epoxy and tile installations in Central Florida."
) + header('index.html') + f'''
<section class="hero" style="background-image:url('assets/img/hero-home.webp')">
  <div class="hero-slides" aria-hidden="true">
    <div class="slide active" style="background-image:url('assets/img/hero-slide-1.webp')"></div>
    <div class="slide" style="background-image:url('assets/img/hero-slide-2.jpg')"></div>
    <div class="slide" style="background-image:url('assets/img/hero-slide-3.jpg')"></div>
    <div class="slide" style="background-image:url('assets/img/hero-slide-4.webp')"></div>
    <div class="slide" style="background-image:url('assets/img/hero-slide-5.jpeg')"></div>
  </div>
  <div class="container">
    <div class="hero-grid">
      <div class="hero-inner">
        <div class="stars">★★★★★</div>
        <span class="eyebrow">RA Contractor Flooring</span>
        <h1>#1 in Flooring and Remodeling Services for Beautiful, Lasting Results</h1>
        <p>Explore our exceptional flooring services at RA Contractor Flooring Inc., the trusted choice for high-quality flooring solutions for your home or business.</p>
        <ul class="hero-check">
          <li><span class="tick">✓</span>Free in-home estimates</li>
          <li><span class="tick">✓</span>Same-day installation for your convenience</li>
          <li><span class="tick">✓</span>Satisfaction guaranteed</li>
        </ul>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-primary">Get a Free Quote</a>
          <a href="{TEL}" class="btn btn-ghost">Call: {PHONE}</a>
        </div>
      </div>
      <form class="hero-form" action="https://formsubmit.co/{EMAIL}" method="POST">
        <h3>Fast Free Quote</h3>
        <p class="hint">Tell us about your project — we reply the same day.</p>
        <input type="hidden" name="_subject" value="New quick quote — raflooring website">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="">
        <div class="form-row">
          <div class="field"><input name="name" type="text" required placeholder="Your name *" aria-label="Name"></div>
          <div class="field"><input name="phone" type="tel" required placeholder="Phone *" aria-label="Phone"></div>
        </div>
        <div class="field"><input name="email" type="email" required placeholder="Email *" aria-label="Email"></div>
        <div class="field"><input name="address" type="text" placeholder="Project address (street, city, ZIP)" aria-label="Project address"></div>
        <div class="field">
          <select name="service" aria-label="Service">
            <option value="" disabled selected>Which service?</option>
            <option>Carpet Flooring</option>
            <option>Vinyl / Luxury Vinyl Plank</option>
            <option>Hardwood Flooring</option>
            <option>Hardwood Refinishing</option>
            <option>Epoxy Flooring</option>
            <option>Tile Flooring</option>
            <option>Kitchen Remodeling</option>
            <option>Bathroom Remodeling</option>
            <option>Painting</option>
            <option>Other</option>
          </select>
        </div>
        <div class="form-row">
          <div class="field"><label for="hf-date">Preferred date</label><input id="hf-date" name="preferred_date" type="date" aria-label="Preferred date"></div>
          <div class="field"><label for="hf-time">Preferred time</label>
            <select id="hf-time" name="preferred_time" aria-label="Preferred time">
              <option value="" disabled selected>Any time</option>
              <option>Morning (8am – 12pm)</option>
              <option>Afternoon (12pm – 4pm)</option>
              <option>Evening (4pm – 7pm)</option>
            </select>
          </div>
        </div>
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Request My Quote</button>
      </form>
    </div>
  </div>
</section>

<div class="materials-strip">
  <div class="container badges-row" style="padding:6px 0">
    <img src="assets/img/badge-insured.png" alt="Fully Insured" loading="lazy">
    <img src="assets/img/badge-top-search.png" alt="Google Top Search" loading="lazy">
    <img src="assets/img/badge-guaranteed.png" alt="Google Guaranteed" loading="lazy">
    <img src="assets/img/badge-licensed.png" alt="Licensed" loading="lazy">
    <img src="assets/img/badge-angi.png" alt="Angi Super Service Award" loading="lazy">
  </div>
</div>

<div class="stats">
  <div class="container stats-grid">
    <div class="stat reveal"><div class="num" data-count="12" data-suffix="+">0</div><div class="label">Years of Experience</div></div>
    <div class="stat reveal reveal-d1"><div class="num" data-count="512" data-suffix="+">0</div><div class="label">Successful Projects</div></div>
    <div class="stat reveal reveal-d2"><div class="num" data-count="1120" data-suffix="+">0</div><div class="label">Satisfied Customers</div></div>
    <div class="stat reveal reveal-d3"><div class="num" data-count="4.9">0</div><div class="label">Client Reviews</div></div>
  </div>
</div>

<section class="ready" style="background-image:url('assets/img/ready-bg.webp')">
  <div class="container">
    <div class="reveal">
      <h2>Ready to Start?</h2>
      <p>Our team of experts is ready to listen to your ideas and needs, ensuring personalized and high-quality service. From small renovations to major construction projects, we are committed to delivering exceptional results that exceed your expectations. Click below to schedule a free consultation and discover how we can help create the perfect space for you and your family. Let's start this journey together!</p>
      <a href="contact.html" class="btn btn-primary">Contact us today to get started!</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Projects</span>
      <h2>Our Latest Works &amp; Clients</h2>
      <div class="divider"></div>
    </div>
    <div class="works-grid">
      <a href="gallery.html" class="reveal"><img src="assets/img/work-1.jpg" alt="RA Flooring project" loading="lazy"></a>
      <a href="gallery.html" class="reveal reveal-d1"><img src="assets/img/work-2.jpg" alt="RA Flooring project" loading="lazy"></a>
      <a href="gallery.html" class="reveal reveal-d2"><img src="assets/img/work-3.jpg" alt="RA Flooring project" loading="lazy"></a>
      <a href="gallery.html" class="reveal reveal-d3"><img src="assets/img/work-4.jpg" alt="RA Flooring project" loading="lazy"></a>
      <a href="gallery.html" class="reveal"><img src="assets/img/work-5.jpg" alt="RA Flooring project" loading="lazy"></a>
      <a href="gallery.html" class="reveal reveal-d1"><img src="assets/img/work-6.jpg" alt="RA Flooring project" loading="lazy"></a>
      <a href="gallery.html" class="reveal reveal-d2"><img src="assets/img/work-7.jpg" alt="RA Flooring project" loading="lazy"></a>
      <a href="gallery.html" class="reveal reveal-d3"><img src="assets/img/work-8.jpg" alt="RA Flooring project" loading="lazy"></a>
    </div>
    <div class="center-cta"><a href="gallery.html" class="btn btn-dark">See More Projects</a></div>
  </div>
</section>

<section class="reviews-band">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Testimonial</span>
      <h2>Client Feedback &amp; Reviews.</h2>
      <div class="review-score" style="margin-top:26px">
        <div class="big">5.0+</div>
        <div><div class="stars">★★★★★</div><div class="tag">Excellent Score</div></div>
      </div>
      <img class="google-badge" src="assets/img/google-badge.png" alt="Google Reviews" loading="lazy">
      <div><a href="{REVIEWS}" target="_blank" rel="noopener" class="btn btn-primary">Read Reviews</a></div>
    </div>
    <div class="reveal reveal-d1"><div class="review-shot"><img src="assets/img/reviews-home.jpg" alt="RA Flooring finished project" loading="lazy"></div></div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">★★★★★ Rated As "Excellent"</span>
      <h2>Learn About the Greatest Flooring Company</h2>
      <p style="margin:18px 0">At RA Flooring, we specialize in flooring installations. Our dedicated team is committed to delivering outstanding results in carpet, vinyl, epoxy and tile flooring installations. With over 1,000 successful projects, we focus on providing exceptional quality and timely service, all at affordable prices.</p>
      <h3 style="font-size:20px;margin-bottom:10px">Transform Your Space with Our Excellence!</h3>
      <p style="color:var(--text-soft);margin-bottom:26px">Discover the difference that professional flooring installation can make in your home. At RA Flooring, we offer expert installation of vinyl, carpet, and tile flooring to enhance the beauty and functionality of your space.</p>
      <a href="contact.html" class="btn btn-primary">Get a Free Estimate</a>
    </div>
    <div class="reveal reveal-d1"><div class="photo-frame"><img src="assets/img/team.jpeg" alt="RA Flooring team" loading="lazy"></div></div>
  </div>
</section>

<div class="materials-strip"><div class="container"><p>Always use the best materials to make your project perfect.</p></div></div>

<section class="band-light">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Why choose our service</span>
      <h2>We Deliver Results That Impress</h2>
      <p style="margin:18px 0">With a proven track record in vinyl, carpet, and tile flooring installations, we're confident in our ability to meet and exceed your expectations. Your satisfaction is our priority, and we value your feedback to ensure exceptional outcomes every time.</p>
      <div style="display:grid;gap:18px;margin-top:26px">
        <div class="feat on-card"><div><h3>Efficiency at Work</h3><p>With our experienced team, we ensure that every flooring installation is completed on time, with minimal disruption and maximum quality. Your home is in good hands with RA Contractor Flooring Inc.</p></div></div>
        <div class="feat on-card"><div><h3>Satisfaction Guaranteed</h3><p>We maintain a low rejection rate by focusing on client satisfaction and clear communication. Every project is completed to the highest standard, ensuring our customers are always happy with the results.</p></div></div>
      </div>
    </div>
    <div class="reveal reveal-d1"><div class="photo-frame"><img src="assets/img/values-bg.jpeg" alt="RA Flooring at work" loading="lazy"></div></div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Our Services</span>
      <h2>See what our company can do for your home</h2>
      <div class="divider"></div>
    </div>
    <div class="svc-grid">
      {svc_card('svc-carpet.jpg', 'Carpet Flooring', 'Revitalize your home with plush carpet flooring, tailored to your style. Achieve the perfect blend of comfort and aesthetics with our expert installation services.', pill='Most Popular', link='services.html')}
      {svc_card('svc-vinyl.jpg', 'Vinyl Flooring', "Achieve the ideal look and durability with our expert vinyl flooring installation services, perfect for enhancing your home's style, comfort, and functionality.", link='services.html')}
      {svc_card('svc-hardwood.jpg', 'Hardwood Flooring', 'Enhance your space with our hardwood flooring services, offering timeless style and exceptional durability for a perfect finish.', link='services.html')}
      {svc_card('svc-epoxy.png', 'Epoxy Flooring', "Transform your space with epoxy flooring. Our expert installation services will enhance any room's elegance, adding a sleek and modern touch to your home.", link='services.html')}
      {svc_card('svc-tile.jpg', 'Tile Flooring', "Tile flooring offers durability, style, and easy upkeep. Perfect for any space, it enhances your home's look with long-lasting performance and versatile design options.", link='services.html')}
      {svc_card('svc-refinishing.jpeg', 'Hardwood Refinishing', 'Restore the natural beauty of your hardwood floors. We sand away scratches and old finishes, then apply stain and a protective finish to bring your floors back to life.', link='services.html')}
    </div>
  </div>
</section>

<section class="cta-band" style="background-image:url('assets/img/cta-bg.webp')">
  <div class="container">
    <div class="reveal">
      <h2>Upgrade Your Space! Transform Your Floors with Style and Quality!</h2>
      <p>Ready for an upgrade? Let's refresh your space with beautiful vinyl, carpet, or tile flooring. Our team is equipped to deliver professional, same-day installations that will make your property shine. Don't wait – let's get started today!</p>
      <a href="contact.html" class="btn btn-primary" style="margin-bottom:44px">Contact us today to get started!</a>
    </div>
    <div class="feat-grid">
      {feat('icon-consult.png', 'Free Consultations', "Request a quote today, and we'll get back to you as soon as possible.")}
      {feat('icon-support.png', 'Call Support', 'Need to discuss your project or have something urgent? Call us!')}
      {feat('icon-workers.png', 'Experienced Professionals', 'Our experienced professionals are committed to delivering unparalleled results.')}
    </div>
  </div>
</section>

<section class="band-light">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">See some comparisons</span>
      <h2>Discover how we transform spaces through our projects</h2>
      <p style="margin:18px 0">Discover how RA Flooring transforms spaces through expert flooring solutions. Visit our gallery to explore inspiring projects and see how we've helped clients elevate their properties. You'll find countless ideas to help you envision your next flooring upgrade.</p>
      <a href="gallery.html" class="btn btn-dark">View Our Projects</a>
    </div>
    <div class="reveal reveal-d1">
      <div class="ba-wrap">
        <img src="assets/img/before.jpg" alt="Before">
        <img class="ba-after" src="assets/img/after.jpg" alt="After">
        <span class="ba-label before">Before</span>
        <span class="ba-label after">After</span>
        <div class="ba-handle"></div>
      </div>
    </div>
  </div>
</section>
''' + contact_band() + footer()

# ---------------------------------------------------------------- ABOUT
pages['about.html'] = head(
    "About Us – RA Flooring",
    "Learn about RA Contractor Flooring Inc. — our vision, mission and values. Over a decade of experience delivering exceptional flooring and remodeling results."
) + header('about.html') + f'''
<section class="hero hero-page" style="background-image:url('assets/img/team.jpeg')">
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow">About Us</span>
      <h1>Where Efficiency Meets Expertise: Your Vision, Our Craftsmanship</h1>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2>We offer installation services that exceed your expectations.</h2>
      <p style="margin:18px 0">RA Flooring provides top-notch installation services tailored to your specific needs. Our team is committed to delivering exceptional results that enhance the beauty and functionality of your spaces.</p>
      <h3 style="font-size:20px;margin-bottom:8px">Exceptional Flooring Services</h3>
      <p style="color:var(--text-soft);margin-bottom:26px">At RA Flooring, we deliver excellence in flooring solutions tailored to your needs. From stunning designs to durable materials, trust us to enhance your space.</p>
      <a href="contact.html" class="btn btn-primary">Get a Free Quote</a>
    </div>
    <div class="reveal reveal-d1" style="display:grid;gap:18px">
      {feat('icon-vision.png', 'Our Vision', 'At RA Flooring, our vision is to be the forefront innovators in transforming spaces, setting new standards for excellence in flooring and remodeling.')}
      {feat('icon-goal.png', 'Our Mission', 'Our mission at RA Flooring is to passionately dedicate ourselves to the art of craftsmanship, working collaboratively with our clients to bring their visions to life.')}
      {feat('icon-diamond.png', 'Our Motto', 'At RA Flooring, we transform dreams into reality. Trust our dedicated team of professionals to elevate your space with quality, precision, and a touch of artistic brilliance.')}
    </div>
  </div>
</section>

<div class="stats">
  <div class="container stats-grid">
    <div class="stat reveal"><div class="num" data-count="7" data-suffix="+">0</div><div class="label">Years of Experience</div></div>
    <div class="stat reveal reveal-d1"><div class="num" data-count="530" data-suffix="+">0</div><div class="label">Happy Clients</div></div>
    <div class="stat reveal reveal-d2"><div class="num" data-count="10" data-suffix="+">0</div><div class="label">Team Members</div></div>
    <div class="stat reveal reveal-d3"><div class="num" data-count="4.9">0</div><div class="label">Client Reviews</div></div>
  </div>
</div>

<section class="ready" style="background-image:url('assets/img/values-bg.jpeg')">
  <div class="container">
    <div class="reveal" style="max-width:760px">
      <span class="eyebrow">Our Value</span>
      <h2>Alone we can do so little, together we can do so much.</h2>
      <p>RA Flooring believes in the power of collaboration and teamwork. We strive to work closely with our clients to achieve their goals and exceed their expectations. Our dedication to excellence and innovation sets us apart in the industry.</p>
      <div style="display:grid;gap:18px;margin-top:10px">
        <div class="feat" style="background:rgba(255,255,255,.07);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.14)"><div><h3 style="color:#fff">Opportunity to Shape Beautiful Spaces</h3><p style="color:rgba(255,255,255,.75)">At RA Flooring, we see every project as an opportunity to create something extraordinary. Our team is dedicated to pushing the boundaries of design and craftsmanship.</p></div></div>
        <div class="feat" style="background:rgba(255,255,255,.07);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.14)"><div><h3 style="color:#fff">Cross-Disciplinary Learning</h3><p style="color:rgba(255,255,255,.75)">We believe in the importance of continuous learning and growth. By embracing cross-disciplinary approaches, we stay ahead of the curve and deliver innovative solutions that make a real difference in our clients' lives.</p></div></div>
        <div class="feat" style="background:rgba(255,255,255,.07);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.14)"><div><h3 style="color:#fff">Impactful, Lasting Solutions</h3><p style="color:rgba(255,255,255,.75)">RA Flooring is committed to providing impactful solutions that enhance the beauty, functionality, and durability of your spaces. From flooring installation to full remodeling, we deliver results that stand the test of time.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Why choose our service</span>
      <h2>Why Choose RA Flooring?</h2>
      <ul class="check-list" style="margin:22px 0 28px">
        <li><span class="tick">✓</span>Years of Professional Experience</li>
        <li><span class="tick">✓</span>Passion for Excellence in Every Detail</li>
        <li><span class="tick">✓</span>High-Quality Materials for Enduring Results</li>
        <li><span class="tick">✓</span>Comprehensive and Transparent Project Management</li>
        <li><span class="tick">✓</span>Satisfaction Guaranteed</li>
      </ul>
      <a href="{TEL}" class="btn btn-primary">Call Us Now!</a>
    </div>
    <div class="reveal reveal-d1"><div class="photo-frame"><img src="assets/img/team-photo.jpg" alt="RA Flooring team" loading="lazy"></div></div>
  </div>
</section>
''' + contact_band() + footer()

# ---------------------------------------------------------------- SERVICES
svc2 = [
    ('svc2-carpet-install.webp', 'Carpet Installation & Repair', 'Keep your carpets looking their best with our installation and repair services, providing quality solutions for style and longevity.', 'Request a Quote'),
    ('svc2-carpet-tile.jpg', 'Carpet Tile', 'Elevate your floors with our carpet tile services, offering flexible, easy-to-maintain options for a modern and functional finish.', 'Get a Free Estimate'),
    ('reviews-home.jpg', 'Luxury Vinyl Plank', 'Upgrade your space with our luxury vinyl plank flooring, combining sleek design, durability, and water resistance for any room.', 'Request a Quote'),
    ('svc2-hardwood.jpg', 'Hardwood Flooring', 'Add timeless charm and unmatched durability to your home with our hardwood flooring services, tailored for perfection.', 'Get a Free Estimate'),
    ('svc-refinishing.jpeg', 'Hardwood Refinishing', 'Restore the natural beauty of your hardwood floors with professional sanding, staining and a durable protective finish.', 'Request a Quote'),
    ('svc-epoxy.png', 'Epoxy Flooring', 'Opt for our epoxy flooring services for a seamless, durable, and low-maintenance solution perfect for garages and industrial spaces.', 'Request a Quote'),
    ('svc2-tile.jpg', 'Tile', "Enhance your home's style and functionality with our expert tile services, offering precision and long-lasting quality.", 'Get a Free Estimate'),
    ('svc2-drywall.jpg', 'Drywall', 'Ensure flawless walls and ceilings with our drywall services, delivering smooth, durable finishes ready for painting or decor.', 'Request a Quote'),
    ('svc2-painting.png', 'Painting', 'Refresh your space with our professional painting services, offering vibrant colors and clean finishes for any interior or exterior.', 'Get a Free Estimate'),
]
svc2_html = '\n'.join(svc_card(i, t, d, link='contact.html', link_text=l) for i, t, d, l in svc2)

pages['services.html'] = head(
    "Services – RA Flooring",
    "Carpet, carpet tile, luxury vinyl plank, hardwood, epoxy, tile, drywall and painting — explore RA Flooring's full range of services."
) + header('services.html') + f'''
<section class="hero hero-page" style="background-image:url('assets/img/hero-services.jpg')">
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow">Our Services</span>
      <h1>Elevate Your Space with RA Flooring Services</h1>
      <p>At RA Flooring, we take pride in transforming your living spaces with our expert flooring services. Our commitment to quality and customer satisfaction makes us the premier choice for all your flooring needs.</p>
      <div class="hero-actions"><a href="contact.html" class="btn btn-primary">Get a Free Estimate</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head center reveal">
      <h2>Transform Your Home with Our Flooring Services</h2>
      <div class="divider"></div>
    </div>
    <div class="svc-grid">
      {svc2_html}
    </div>
  </div>
</section>

<section class="band-light">
  <div class="container split">
    <div class="reveal reveal-d1"><div class="photo-frame"><img src="assets/img/svc-refinishing.jpeg" alt="Hardwood floor refinishing in progress" loading="lazy"></div></div>
    <div class="reveal">
      <span class="eyebrow">Featured Service</span>
      <h2>Hardwood Refinishing</h2>
      <p style="margin:16px 0">Restore the natural beauty of your hardwood floors with our professional refinishing services. We sand away scratches, wear, old finishes, and surface imperfections, then apply a high-quality stain and protective finish to bring your floors back to life.</p>
      <p style="margin-bottom:18px">Whether you want to refresh the original look or change the color of your hardwood, our team delivers a smooth, durable, and beautiful finish that can completely transform your space.</p>
      <h3 style="font-size:19px;margin-bottom:8px">Our Hardwood Refinishing Services Include:</h3>
      <ul class="check-list" style="margin-bottom:20px">
        <li><span class="tick">✓</span>Professional sanding</li>
        <li><span class="tick">✓</span>Scratch and surface damage removal</li>
        <li><span class="tick">✓</span>Staining and color change</li>
        <li><span class="tick">✓</span>Protective finish application</li>
        <li><span class="tick">✓</span>Residential and commercial refinishing</li>
      </ul>
      <p style="color:var(--text-soft);margin-bottom:24px">Give your hardwood floors a fresh new look without the cost of replacing them.</p>
      <a href="contact.html" class="btn btn-primary">Get a Free Estimate</a>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="reveal">
      <h2>Request Your Free Estimate</h2>
      <p style="margin:16px 0 28px">Discover the difference that quality flooring and home remodeling services can make. Contact RA Flooring to start your project and experience exceptional craftsmanship and service.</p>
      <a href="contact.html" class="btn btn-primary">Get a Free Estimate</a>
    </div>
    <div class="reveal reveal-d1">
      <h2 style="font-size:26px">Need Assistance?</h2>
      <p style="margin:14px 0 22px">Ready to transform your home? Contact RA Flooring today to schedule a consultation. We look forward to helping you create the home of your dreams.</p>
      <div class="feat on-card" style="background:#fff"><img src="assets/img/icon-support.png" alt=""><div><h3>Customer Support</h3><p><a href="{TEL}" style="font-weight:800;color:var(--orange)">{PHONE}</a></p></div></div>
      <div class="feat on-card" style="background:#fff;margin-top:16px"><img src="assets/img/icon-consult.png" alt=""><div><h3>Email Support</h3><p><a href="mailto:{EMAIL}" style="font-weight:800;color:var(--orange)">{EMAIL}</a></p></div></div>
    </div>
  </div>
</section>

<section class="reviews-band">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Testimonial</span>
      <h2>Client Feedback &amp; Reviews.</h2>
      <div class="review-score" style="margin-top:26px">
        <div class="big">4.9+</div>
        <div><div class="stars">★★★★★</div><div class="tag">Excellent Score</div></div>
      </div>
      <img class="google-badge" src="assets/img/google-badge.png" alt="Google Reviews" loading="lazy">
      <div><a href="{REVIEWS}" target="_blank" rel="noopener" class="btn btn-primary">Read Reviews</a></div>
    </div>
    <div class="reveal reveal-d1"><div class="review-shot"><img src="assets/img/reviews-services.jpg" alt="RA Flooring project" loading="lazy"></div></div>
  </div>
</section>
''' + contact_band() + footer()

# ---------------------------------------------------------------- GALLERY
videos = [
    ('vinyl-stairs.mp4', 'Vinyl Stairs', '100% Waterproof SPC. Check out the process!'),
    ('residential-carpet.mp4', 'Residential Carpet', 'Click and watch the installation process!'),
    ('vinyl.mp4', 'Vinyl', 'Click and watch the installation process!'),
    ('porcelain-tile.mp4', 'Porcelain Tile', 'Check out the amazing job done at this bathroom!'),
    ('carpet-tile-vinyl.mp4', 'Carpet Tile & Vinyl', 'See the amazing work RA Flooring did for Care ai Orlando!'),
    ('waterproof-vinyl-plank.mp4', '100% Waterproof Vinyl Plank', 'Check out this job done for another happy customer!'),
    ('barnes-noble.mp4', 'Barnes & Noble', 'Tile, Carpet, Wall Subway Tile VCT, Epoxy coat.'),
    ('vinyl-stairs-2.mp4', 'Vinyl Stairs Transformation', "Looks like magic, but it's just our daily work!"),
]
videos_html = '\n'.join(video_card(s, t, d) for s, t, d in videos)
works_html = '\n'.join(
    f'<a href="assets/img/work-{n}.jpg" target="_blank" class="reveal"><img src="assets/img/work-{n}.jpg" alt="RA Flooring project" loading="lazy"></a>'
    for n in range(1, 9)
)

pages['gallery.html'] = head(
    "Gallery – RA Flooring",
    "Explore RA Flooring's gallery: finished installations, before & after transformations and videos of our daily work."
) + header('gallery.html') + f'''
<section class="hero hero-page" style="background-image:url('assets/img/svc2-carpet-tile.jpg')">
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow">Gallery</span>
      <h1>Explore our gallery where efficiency meets expertise.</h1>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Complete Projects</span>
      <h2>Browse Some of Our Finished Installations</h2>
      <div class="divider"></div>
    </div>
    <div class="works-grid">
      {works_html}
    </div>
  </div>
</section>

<section class="band-light">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Our daily work</span>
      <h2>Learn more about how we can transform your space</h2>
      <div class="divider"></div>
    </div>
    <div class="video-grid">
      {videos_html}
    </div>
  </div>
</section>

<section class="reviews-band" style="background:#fff">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Testimonial</span>
      <h2>Client Feedback &amp; Reviews.</h2>
      <div class="review-score" style="margin-top:26px">
        <div class="big">5.0+</div>
        <div><div class="stars">★★★★★</div><div class="tag">Excellent Score</div></div>
      </div>
      <img class="google-badge" src="assets/img/google-badge.png" alt="Google Reviews" loading="lazy">
      <div><a href="{REVIEWS}" target="_blank" rel="noopener" class="btn btn-primary">Read Reviews</a></div>
    </div>
    <div class="reveal reveal-d1"><div class="review-shot"><img src="assets/img/reviews-gallery.png" alt="RA Flooring reviews" loading="lazy"></div></div>
  </div>
</section>
''' + contact_band() + footer()

# ---------------------------------------------------------------- CONTACT
pages['contact.html'] = head(
    "Contact – RA Flooring",
    "Get in touch with RA Flooring for a free quote. Call (754) 246-2843 — Davenport, FL. Fully insured, licensed and Google Guaranteed."
) + header('contact.html') + f'''
<section class="hero hero-page" style="background-image:url('assets/img/hero-contact.jpg')">
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow">Contact</span>
      <h1>Start the conversation to establish a good relationship and business.</h1>
    </div>
  </div>
</section>

<section class="contact-band" style="background-image:url('assets/img/contact-bg.webp')">
  <div class="container">
    <div class="split" style="align-items:flex-start">
      <div class="reveal">
        <h2>Let's get in touch.</h2>
        <p class="sub">Don't hesitate to contact us for more information.</p>
        <div class="info-item"><div class="k">Have any question?</div><div class="v"><a href="{TEL}">Call: {PHONE}</a></div></div>
        <div class="info-item"><div class="k">E-mail support</div><div class="v"><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
        <div class="info-item"><div class="k">Location</div><div class="v">Davenport, FL</div></div>
        <div class="social-row">
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_SVG}</a>
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a>
        </div>
        <div class="badges-row on-dark" style="justify-content:flex-start">
          <img src="assets/img/badge-insured-w.png" alt="Fully Insured" loading="lazy">
          <img src="assets/img/badge-top-search-w.png" alt="Google 5-Star Reviews" loading="lazy">
          <img src="assets/img/badge-guaranteed-w.png" alt="Google Guaranteed" loading="lazy">
          <img src="assets/img/badge-licensed-w.png" alt="Licensed" loading="lazy">
        </div>
      </div>
      <div class="reveal reveal-d1">
        <form class="form-card" action="https://formsubmit.co/{EMAIL}" method="POST">
          <h3>Request a Free Quote</h3>
          <p class="hint">Fill out the form and we'll get back to you as soon as possible. All our quotes are personalized.</p>
          <input type="hidden" name="_subject" value="New quote request — raflooring website">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_next" value="">
          <div class="form-grid">
            <div class="field"><label for="f-name">Name *</label><input id="f-name" name="name" type="text" required placeholder="Your name"></div>
            <div class="field"><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" required placeholder="(000) 000 0000"></div>
            <div class="field full"><label for="f-email">Email *</label><input id="f-email" name="email" type="email" required placeholder="you@email.com"></div>
            <div class="field full"><label for="f-address">Project address</label><input id="f-address" name="address" type="text" placeholder="Street, city, ZIP"></div>
            <div class="field"><label for="f-sqft">Total square feet (approx.)</label><input id="f-sqft" name="square_feet" type="number" min="1" placeholder="e.g. 1200"></div>
            <div class="field"><label for="f-service">Service</label>
              <select id="f-service" name="service">
                <option>Carpet Flooring</option>
                <option>Vinyl / Luxury Vinyl Plank</option>
                <option>Hardwood Flooring</option>
                <option>Hardwood Refinishing</option>
                <option>Epoxy Flooring</option>
                <option>Tile Flooring</option>
                <option>Kitchen Remodeling</option>
                <option>Bathroom Remodeling</option>
                <option>Painting</option>
                <option>Other</option>
              </select>
            </div>
            <div class="field full"><label for="f-msg">Message</label><textarea id="f-msg" name="message" placeholder="Tell us about your project..."></textarea></div>
            <div class="full"><button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Send Request</button></div>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>
''' + footer()

# ---------------------------------------------------------------- REMODELING PAGES
def remodel_page(title_tag, desc_tag, hero_img, hero_title, hero_text, svc_title, cards, about_title, review_img, score, location="Orlando, FL"):
    cards_html = '\n'.join(svc_card(i, t, d, link='contact.html', link_text=l) for i, t, d, l in cards)
    return head(title_tag, desc_tag) + header('') + f'''
<section class="hero hero-page" style="background-image:url('assets/img/{hero_img}')">
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow">RA Flooring</span>
      <h1>{hero_title}</h1>
      <p>{hero_text}</p>
      <div class="hero-actions"><a href="contact.html" class="btn btn-primary">Get a Free Estimate</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head center reveal">
      <h2>{svc_title}</h2>
      <div class="divider"></div>
    </div>
    <div class="svc-grid">
      {cards_html}
    </div>
  </div>
</section>

<section class="band-light">
  <div class="container split">
    <div class="reveal">
      <h2>Request Your Free Estimate</h2>
      <p style="margin:16px 0 28px">Discover the difference that quality flooring and home remodeling services can make. Contact RA Flooring to start your project and experience exceptional craftsmanship and service.</p>
      <a href="contact.html" class="btn btn-primary">Get a Free Estimate</a>
    </div>
    <div class="reveal reveal-d1">
      <h2 style="font-size:26px">Need Assistance?</h2>
      <p style="margin:14px 0 22px">Ready to transform your home? Contact RA Flooring today to schedule a consultation. We look forward to helping you create the home of your dreams.</p>
      <div class="feat on-card" style="background:#fff"><img src="assets/img/icon-support.png" alt=""><div><h3>Customer Support</h3><p><a href="{TEL}" style="font-weight:800;color:var(--orange)">{PHONE}</a></p></div></div>
      <div class="feat on-card" style="background:#fff;margin-top:16px"><img src="assets/img/icon-consult.png" alt=""><div><h3>Email Support</h3><p><a href="mailto:{EMAIL}" style="font-weight:800;color:var(--orange)">{EMAIL}</a></p></div></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">About Us</span>
      <h2>{about_title}</h2>
      <p>Discover the story behind RA Flooring and learn what sets us apart. Our dedication to quality, integrity, and customer satisfaction drives everything we do.</p>
      <div class="divider"></div>
    </div>
    <div class="feat-grid">
      {feat('icon-consult.png', 'Expert Craftsmanship', 'Our team has extensive experience, ensuring that your project is in capable hands.')}
      {feat('icon-support.png', 'Customer Satisfaction', 'Your satisfaction is our top priority. We work closely with you to understand your vision and bring it to life.')}
      {feat('icon-workers.png', 'Quality Materials', 'We use only the highest quality materials to ensure durability and long-lasting beauty.')}
    </div>
    <div class="center-cta"><a href="about.html" class="btn btn-dark">Learn More About Us</a></div>
  </div>
</section>

<section class="reviews-band">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Testimonial</span>
      <h2>Client Feedback &amp; Reviews.</h2>
      <div class="review-score" style="margin-top:26px">
        <div class="big">{score}</div>
        <div><div class="stars">★★★★★</div><div class="tag">Excellent Score</div></div>
      </div>
      <img class="google-badge" src="assets/img/google-badge.png" alt="Google Reviews" loading="lazy">
      <div><a href="{REVIEWS}" target="_blank" rel="noopener" class="btn btn-primary">Read Reviews</a></div>
    </div>
    <div class="reveal reveal-d1"><div class="review-shot"><img src="assets/img/{review_img}" alt="Project" loading="lazy"></div></div>
  </div>
</section>

<section class="band-light" style="padding-top:0">
  <div class="container center-cta">
    <span class="eyebrow">Inspiration Gallery</span>
    <h2 style="margin:10px 0 24px">Projects that boost your creativity</h2>
    <a href="gallery.html" class="btn btn-dark">See All Projects</a>
  </div>
</section>
''' + contact_band(location) + footer()


pages['bathroom-remodeling.html'] = remodel_page(
    "Bathroom Remodeling – RA Flooring",
    "Transform your bathroom into a spa-like oasis. Bathtubs, showers, walk-in tubs, tub-to-shower conversions and accessible bathrooms by RA Flooring.",
    'hero-bath.webp',
    'Transform Your Bathroom into a Spa-like Oasis',
    'Enhance the comfort and style of your bathroom with our comprehensive remodeling services. At RA Flooring, we specialize in creating luxurious, functional spaces tailored to your needs and preferences.',
    'Our Bathroom Remodeling Services',
    [
        ('bath-1.webp', 'Bathtubs', "Relax and unwind in a new, stylish bathtub. Choose from a variety of designs that complement your bathroom's aesthetics and provide ultimate comfort.", 'Explore Bathtub Options'),
        ('bath-2.webp', 'Showers', 'Upgrade your shower experience with our custom shower installations. We offer a range of options, from sleek glass enclosures to multi-head showers, to create a spa-like atmosphere.', 'Upgrade Your Shower'),
        ('bath-3.webp', 'Walk-in Tubs', 'Enhance safety and convenience with our walk-in tubs, perfect for those with mobility issues. Enjoy a relaxing soak without the hassle of stepping over high tub walls.', 'Schedule a Consultation'),
        ('bath-4.webp', 'Tub-to-Shower Conversions', 'Maximize space and functionality with a tub-to-shower conversion. This service is ideal for those who prefer showers over baths or need a more accessible option.', 'Convert Your Tub'),
        ('bath-5.webp', 'Bathtub/Shower Combos', 'Enjoy the best of both worlds with a bathtub/shower combo. This versatile option allows you to soak or shower as per your convenience, making it perfect for families.', 'Choose a Combo'),
        ('bath-6.webp', 'Accessible Bathrooms', 'Create a bathroom that meets the needs of all users with our accessible bathroom solutions. From grab bars to barrier-free showers, we ensure your bathroom is both stylish and functional for everyone.', 'Design an Accessible Bathroom'),
    ],
    'Crafting Beautiful Homes with Expertise and Care',
    'bath-3.webp', '4.9+',
)

pages['kitchen-remodeling.html'] = remodel_page(
    "Kitchen Remodeling – RA Flooring",
    "Redefine your kitchen with RA Flooring: cabinet refacing, countertop replacement, cabinet painting and accessories.",
    'hero-kitchen.webp',
    'Redefine Your Kitchen with RA Flooring',
    'Upgrade your kitchen with our comprehensive remodeling services. At RA Flooring, we specialize in creating functional and stylish kitchen spaces that meet your needs and exceed your expectations.',
    'Our Kitchen Remodeling Services',
    [
        ('kit-1.webp', 'Cabinets Refacing', 'Transform the look of your kitchen cabinets without the cost of full replacement. Our cabinet refacing service gives your cabinets a fresh, updated appearance while maintaining the existing layout.', 'Revitalize Your Cabinets'),
        ('kit-2.webp', 'Countertop Replacement', 'Enhance the beauty and functionality of your kitchen with new countertops. Choose from a variety of materials, styles, and colors to create a stunning focal point in your space.', 'Upgrade Your Countertops'),
        ('kit-3.webp', 'Cabinets Painting', 'Give your kitchen cabinets a new lease on life with our professional painting services. Whether you prefer a classic white or a bold color choice, our expert painters deliver flawless results.', 'Transform Your Cabinets'),
        ('kit-4.webp', 'Cabinet Accessories', 'Maximize storage and organization in your kitchen with custom cabinet accessories. From pull-out shelves to spice racks, we offer innovative solutions to make your kitchen more efficient.', 'Explore Accessories'),
    ],
    'Why Choose RA Flooring?',
    'kit-4.webp', '5.0+',
)

pages['painting-services.html'] = remodel_page(
    "Painting Services – RA Flooring",
    "Interior, exterior, residential and commercial painting services by RA Flooring. Top-quality painting solutions tailored to your needs.",
    'hero-paint.webp',
    'Transform Your Space with RA Flooring',
    "Bring new life to your home or business with our professional painting services. At RA Flooring, we offer top-quality painting solutions tailored to meet your specific needs and preferences. Whether you're looking to refresh a single room or give your entire property a makeover, our expert team is here to help.",
    'Our Painting Services',
    [
        ('paint-1.webp', 'Interior Painting', 'Revitalize your living spaces with our interior painting services. We handle everything from color consultation to meticulous preparation and flawless finishes, ensuring your home looks its best.', 'Book Interior Painting'),
        ('paint-2.webp', 'Exterior Painting', "Enhance your home's curb appeal with our exterior painting services. Our durable and weather-resistant paint ensures your home looks beautiful and stands up to the elements.", 'Schedule Exterior Painting'),
        ('paint-3.webp', 'Residential Painting', 'Our residential painting services are designed to make your home feel fresh and new. From single rooms to whole house painting, we provide a seamless and stress-free experience.', 'Schedule a Consultation'),
        ('paint-4.webp', 'Commercial Painting', "Make a great impression with our commercial painting services. We work around your schedule to minimize disruptions, delivering professional results that reflect your business's quality and style.", 'Upgrade Your Business'),
    ],
    'Why Choose RA Flooring?',
    'paint-1.webp', '4.9+',
)

# ---------------------------------------------------------------- THANK YOU
pages['thank-you.html'] = head(
    "Thank You – RA Flooring",
    "Thank you for your interest in RA Flooring's services. We will reply to your request shortly."
) + header('') + f'''
<div class="thanks" style="background-image:url('assets/img/thankyou-bg.webp')">
  <div class="inner">
    <span class="eyebrow">RA Flooring</span>
    <h1>Thank you for your interest in our services</h1>
    <p>We will reply to your form shortly. Please bear with us as all our quotes are personalized.</p>
    <a href="index.html" class="btn btn-primary">Back To Home</a>
  </div>
</div>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

# ---------------------------------------------------------------- LEGAL
LEGAL_PRIVACY = f'''
<p>Your privacy is important to us. It is RA Contractor Flooring Inc.'s policy to respect your privacy regarding any information we may collect from you across our website and other sites we own and operate.</p>
<h2>1. Information we collect</h2>
<p>We only ask for personal information when we truly need it to provide a service to you — for example, your name, phone number and email address when you request a quote. We collect it by fair and lawful means, with your knowledge and consent. We also let you know why we're collecting it and how it will be used.</p>
<h2>2. Use of information</h2>
<p>We use the information you provide solely to respond to your requests, prepare personalized quotes, schedule services and communicate with you about your project. We do not sell or share your personal information with third parties, except when required to deliver a service you requested or when required by law.</p>
<h2>3. Data retention</h2>
<p>We only retain collected information for as long as necessary to provide you with your requested service. What data we store, we protect within commercially acceptable means to prevent loss and theft, as well as unauthorized access, disclosure, copying, use or modification.</p>
<h2>4. Links to other sites</h2>
<p>Our website may link to external sites that are not operated by us. Please be aware that we have no control over the content and practices of these sites, and cannot accept responsibility or liability for their respective privacy policies.</p>
<h2>5. Your rights</h2>
<p>You are free to refuse our request for your personal information, with the understanding that we may be unable to provide you with some of your desired services. You may also request access to, correction of, or deletion of the personal data we hold about you by contacting us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>6. Contact</h2>
<p>Your continued use of our website will be regarded as acceptance of our practices around privacy and personal information. If you have any questions about how we handle user data and personal information, feel free to contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or {PHONE}.</p>
'''

LEGAL_TERMS = '''
<h2>1. Terms</h2>
<p>By accessing this website, you are agreeing to be bound by these terms of service, all applicable laws and regulations, and agree that you are responsible for compliance with any applicable local laws. If you do not agree with any of these terms, you are prohibited from using or accessing this site.</p>
<h2>2. Use license</h2>
<p>Permission is granted to temporarily view the materials (information, images and videos) on RA Contractor Flooring Inc.'s website for personal, non-commercial use only. This is the grant of a license, not a transfer of title, and under this license you may not:</p>
<ul>
<li>modify or copy the materials;</li>
<li>use the materials for any commercial purpose, or for any public display;</li>
<li>remove any copyright or other proprietary notations from the materials;</li>
<li>transfer the materials to another person or "mirror" the materials on any other server.</li>
</ul>
<p>This license shall automatically terminate if you violate any of these restrictions and may be terminated by RA Contractor Flooring Inc. at any time.</p>
<h2>3. Disclaimer</h2>
<p>The materials on this website are provided on an "as is" basis. RA Contractor Flooring Inc. makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.</p>
<h2>4. Limitations</h2>
<p>In no event shall RA Contractor Flooring Inc. or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on this website.</p>
<h2>5. Accuracy of materials</h2>
<p>The materials appearing on this website could include technical, typographical, or photographic errors. RA Contractor Flooring Inc. does not warrant that any of the materials on its website are accurate, complete or current, and may make changes to the materials at any time without notice.</p>
<h2>6. Modifications</h2>
<p>RA Contractor Flooring Inc. may revise these terms of service at any time without notice. By using this website you are agreeing to be bound by the then-current version of these terms of service.</p>
<h2>7. Governing law</h2>
<p>These terms and conditions are governed by and construed in accordance with the laws of the State of Florida and you irrevocably submit to the exclusive jurisdiction of the courts in that state.</p>
'''

for fname, title, body in (
    ('privacy-policy.html', 'Privacy Policy', LEGAL_PRIVACY),
    ('terms-of-use.html', 'Terms of Use', LEGAL_TERMS),
):
    pages[fname] = head(f"{title} – RA Flooring", f"{title} for the RA Contractor Flooring Inc. website.") + header('') + f'''
<div style="background:var(--dark);height:90px"></div>
<div class="container">
  <div class="legal">
    <h1>{title}</h1>
    <p class="updated">RA Contractor Flooring Inc. — Davenport, FL</p>
    {body}
  </div>
</div>
''' + footer()

# ---------------------------------------------------------------- write
for fname, html_content in pages.items():
    with io.open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('wrote', fname, len(html_content), 'bytes')
