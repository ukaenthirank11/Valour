from __future__ import annotations

from pathlib import Path
import json
import re


ROOT = Path(r"D:\Company\Vakour Website")
HOME = ROOT / "index.html"
SERVICE_FILES = [
    ROOT / "seo-services" / "index.html",
    ROOT / "web-design-services" / "index.html",
    ROOT / "social-media-marketing" / "index.html",
    ROOT / "google-ads-management" / "index.html",
    ROOT / "content-writing-services" / "index.html",
    ROOT / "graphic-design-services" / "index.html",
    ROOT / "video-editing-services" / "index.html",
    ROOT / "photography-services" / "index.html",
]


HOME_FAQ_SCHEMA = [
    {
        "name": "Why should I choose a full-service digital marketing agency instead of hiring freelancers?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "A full-service agency gives your business one coordinated team across SEO, website design, social media, content, ads, branding, photography, videography, and analytics. That keeps the strategy aligned, reduces communication gaps, and makes results easier to track."
        },
    },
    {
        "name": "How can digital marketing help my business generate more leads?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Digital marketing helps you reach people who are already searching for your services while also building awareness with new audiences. At Valour, we combine SEO, Meta Ads, social media, content, and conversion-focused web design to attract better traffic and turn more visitors into enquiries."
        },
    },
    {
        "name": "What digital marketing services are essential for startups and small businesses?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "The strongest starting mix usually includes a professional website, SEO, Meta Ads, social media management, content writing, branding, local SEO, photography, and conversion tracking. This gives small businesses a balanced setup for visibility, trust, and lead generation."
        },
    },
    {
        "name": "How do I know if my marketing investment is delivering a good ROI?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "A good return shows up in measurable business results, not only in traffic numbers. We track rankings, leads, conversion rate, cost per acquisition, return on ad spend, customer acquisition cost, and revenue impact so you can see what the marketing is actually doing."
        },
    },
    {
        "name": "Why should I choose Valour Digital Agency for my digital marketing needs?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Valour Digital Agency builds custom strategies, works with experienced specialists, communicates clearly, and focuses on ethical, data-driven growth. We help brands get stronger visibility, better enquiries, and long-term returns through integrated digital marketing."
        },
    },
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def build_services_block(base: str) -> str:
    return (
        f'''      <div class="footer-col">
        <h3>Our Services</h3>
        <a href="{base}seo-services/">SEO Service</a>
        <a href="{base}web-design-services/">Website Design Service</a>
        <a href="{base}social-media-marketing/">Social Media Marketing</a>
        <a href="{base}google-ads-management/">Meta Ads Management</a>
        <a href="{base}content-writing-services/">Content Writing</a>
        <a href="{base}graphic-design-services/">Graphic Design</a>
        <a href="{base}video-editing-services/">Video Editing</a>
        <a href="{base}photography-services/">Photography</a>
      </div>
      <div class="footer-col footer-contact">'''
    )


def build_footer_contact(place: str) -> str:
    return (
        f'''        <h3>Contact Info</h3>
        <a href="tel:+918667439645"><span>Phone</span><strong>+91 86674 39645</strong></a>
        <a href="mailto:valourdigitalagency@gmail.com"><span>Email</span><strong>valourdigitalagency@gmail.com</strong></a>
        <p><span>Place</span><strong>{place}</strong></p>
        <a href="https://www.instagram.com/valour_digital_agency" target="_blank" rel="nofollow noopener noreferrer"><span>Insta</span><strong>@valour_digital_agency</strong></a>
        <a href="https://www.facebook.com/share/1DjDntTMdN/" target="_blank" rel="nofollow noopener noreferrer"><span>Facebook</span><strong>Valour Digital Agency</strong></a>
        <a href="https://www.linkedin.com/company/valour-digitalagency/" target="_blank" rel="nofollow noopener noreferrer"><span>LinkedIn</span><strong>Valour Digital Agency</strong></a>'''
    )


def build_home_faq_schema() -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["name"],
                "acceptedAnswer": item["acceptedAnswer"],
            }
            for item in HOME_FAQ_SCHEMA
        ],
    }
    return (
        '<script type="application/ld+json">\n'
        f'{json.dumps(payload, ensure_ascii=False, indent=2)}\n'
        '</script>'
    )


def build_home_faq_section() -> str:
    items = []
    for index, item in enumerate(HOME_FAQ_SCHEMA):
        open_attr = " open" if index == 0 else ""
        items.append(
            f'''        <details class="reveal"{open_attr}>
          <summary>{item["name"]}</summary>
          <p>{item["acceptedAnswer"]["text"]}</p>
        </details>'''
        )
    details = "\n".join(items)
    return f'''    <section class="faq section-pad">
      <div class="section-title reveal">
        <p>FAQs</p>
        <h2>Questions People Ask Before Starting</h2>
      </div>
      <div class="faq-layout">
        <div class="faq-copy reveal">
          <p>We keep the answers clear, practical, and search-friendly so visitors can quickly understand how Valour works, what each service does, and how to move forward with confidence.</p>
          <ul class="faq-points">
            <li>SEO, Meta Ads, web design, and creative support in one place</li>
            <li>Clear reporting and measurable outcomes</li>
            <li>Built for startups, small businesses, and growth-focused brands</li>
          </ul>
        </div>
        <div class="faq-list">
{details}
        </div>
      </div>
    </section>'''


def build_service_faq_section(questions: list[dict[str, str]], heading: str) -> str:
    items = []
    for index, item in enumerate(questions):
        open_attr = " open" if index == 0 else ""
        items.append(
            f'''        <details class="reveal"{open_attr}>
          <summary>{item["name"]}</summary>
          <p>{item["acceptedAnswer"]["text"]}</p>
        </details>'''
        )
    details = "\n".join(items)
    return f'''    <section class="service-section faq-section">
      <div class="section-title reveal">
        <p>FAQS</p>
        <h2>{heading}</h2>
      </div>
      <p class="service-intro service-intro-wide reveal">These quick answers help visitors understand the service clearly, compare options faster, and move toward enquiry with more confidence.</p>
      <div class="faq-list">
{details}
      </div>
    </section>'''


def update_footer(text: str, base: str) -> str:
    services_pattern = re.compile(
        r'      <div class="footer-col">\n        <h3>Our Services</h3>\n.*?\n      </div>\n      <div class="footer-col footer-contact">',
        re.S,
    )
    text = services_pattern.sub(build_services_block(base), text, count=1)
    text = re.sub(
        r'(<p><span>Place</span><strong>)([^<]*)(</strong></p>)',
        lambda m: f"{m.group(1)}Chennai, India{m.group(3)}",
        text,
        count=1,
    )
    return text


def add_visible_faq(text: str, section_html: str) -> str:
    marker = '\n\n    <section class="contact section-pad"'
    if marker not in text:
        return text
    return text.replace(marker, f'\n\n{section_html}\n\n    <section class="contact section-pad"', 1)


def add_head_faq_schema(text: str) -> str:
    marker = "\n  </head>"
    if marker not in text:
        return text
    schema = build_home_faq_schema()
    return text.replace(marker, f"\n  {schema}\n  </head>", 1)


def parse_faq_questions(html_text: str) -> list[dict[str, str]]:
    scripts = re.findall(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', html_text, re.S)
    for raw in scripts:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if data.get("@type") == "FAQPage" and isinstance(data.get("mainEntity"), list):
            items = []
            for entity in data["mainEntity"]:
                q = entity.get("name", "").strip()
                a = entity.get("acceptedAnswer", {}).get("text", "").strip()
                if q and a:
                    items.append({"name": q, "acceptedAnswer": {"text": a}})
            return items
    return []


def update_home() -> None:
    text = read(HOME)
    text = text.replace("Google Ads", "Meta Ads")
    text = text.replace(
        '<h3>Performance Ads</h3>\n          <p>Meta and Google campaigns planned, launched, and optimized for leads, conversions, and better return on spend.</p>\n          <a class="service-card-link" href="google-ads-management/">Explore Performance Ads</a>',
        '<h3>Meta Ads</h3>\n          <p>Meta ad campaigns planned, launched, and optimized for leads, conversions, and better return on spend.</p>\n          <a class="service-card-link" href="google-ads-management/">Explore Meta Ads</a>',
    )
    text = text.replace(
        '<p class="service-intro reveal">We deliver focused digital services for brands that want stronger visibility, better creative, and more qualified enquiries. From websites and SEO to graphic design, social media, content, video, photography, and performance ads, every service is built to support growth.</p>',
        '<p class="service-intro reveal">We deliver focused digital services for brands that want stronger visibility, better creative, and more qualified enquiries. From websites and SEO to graphic design, social media, content, video, photography, and Meta Ads, every service is built to support growth.</p>',
    )
    text = add_head_faq_schema(text)
    text = add_visible_faq(text, build_home_faq_section())
    text = update_footer(text, "")
    write(HOME, text)


def update_service_page(path: Path) -> None:
    text = read(path)
    text = text.replace("Google Ads", "Meta Ads")
    text = update_footer(text, "../")
    faq_items = parse_faq_questions(text)
    if faq_items:
        if "Frequently Asked Questions" in text or "These quick answers help visitors understand the service clearly" in text:
            pass
        else:
            heading = "Frequently Asked Questions"
            if path.name == "google-ads-management":
                heading = "Frequently Asked Questions"
            section_html = build_service_faq_section(faq_items, heading)
            text = add_visible_faq(text, section_html)
    write(path, text)


def main() -> None:
    update_home()
    for path in SERVICE_FILES:
        update_service_page(path)


if __name__ == "__main__":
    main()
