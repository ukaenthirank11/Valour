$root = 'D:\Company\Vakour Website'
$homePath = Join-Path $root 'index.html'
$serviceFiles = @(
  (Join-Path $root 'seo-services\index.html'),
  (Join-Path $root 'web-design-services\index.html'),
  (Join-Path $root 'social-media-marketing\index.html'),
  (Join-Path $root 'google-ads-management\index.html'),
  (Join-Path $root 'content-writing-services\index.html'),
  (Join-Path $root 'graphic-design-services\index.html'),
  (Join-Path $root 'video-editing-services\index.html'),
  (Join-Path $root 'photography-services\index.html')
)

$homeFaq = @(
  @{
    name = 'Why should I choose a full-service digital marketing agency instead of hiring freelancers?'
    answer = 'A full-service agency gives your business one coordinated team across SEO, website design, social media, content, ads, branding, photography, videography, and analytics. That keeps the strategy aligned, reduces communication gaps, and makes results easier to track.'
  }
  @{
    name = 'How can digital marketing help my business generate more leads?'
    answer = 'Digital marketing helps you reach people who are already searching for your services while also building awareness with new audiences. At Valour, we combine SEO, Meta Ads, social media, content, and conversion-focused web design to attract better traffic and turn more visitors into enquiries.'
  }
  @{
    name = 'What digital marketing services are essential for startups and small businesses?'
    answer = 'The strongest starting mix usually includes a professional website, SEO, Meta Ads, social media management, content writing, branding, local SEO, photography, and conversion tracking. This gives small businesses a balanced setup for visibility, trust, and lead generation.'
  }
  @{
    name = 'How do I know if my marketing investment is delivering a good ROI?'
    answer = 'A good return shows up in measurable business results, not only in traffic numbers. We track rankings, leads, conversion rate, cost per acquisition, return on ad spend, customer acquisition cost, and revenue impact so you can see what the marketing is actually doing.'
  }
  @{
    name = 'Why should I choose Valour Digital Agency for my digital marketing needs?'
    answer = 'Valour Digital Agency builds custom strategies, works with experienced specialists, communicates clearly, and focuses on ethical, data-driven growth. We help brands get stronger visibility, better enquiries, and long-term returns through integrated digital marketing.'
  }
)

function Escape-Html {
  param([string]$Text)
  if ($null -eq $Text) { return '' }
  return [System.Net.WebUtility]::HtmlEncode($Text)
}

function Build-ServicesBlock {
  param([string]$Base)
@"
      <div class="footer-col">
        <h3>Our Services</h3>
        <a href="${Base}seo-services/">SEO Service</a>
        <a href="${Base}web-design-services/">Website Design Service</a>
        <a href="${Base}social-media-marketing/">Social Media Marketing</a>
        <a href="${Base}google-ads-management/">Meta Ads Management</a>
        <a href="${Base}content-writing-services/">Content Writing</a>
        <a href="${Base}graphic-design-services/">Graphic Design</a>
        <a href="${Base}video-editing-services/">Video Editing</a>
        <a href="${Base}photography-services/">Photography</a>
      </div>
      <div class="footer-col footer-contact">
"@
}

function Build-ExploreDropdown {
  param([string]$Base)
@"
      <div class="nav-dropdown">
        <button class="nav-dropdown-toggle" type="button" aria-expanded="false" aria-haspopup="true">
          EXPLORE US
        </button>
        <div class="nav-dropdown-menu" role="menu" aria-label="Explore our services">
          <a href="${Base}seo-services/">SEO Service</a>
          <a href="${Base}web-design-services/">Website Design Service</a>
          <a href="${Base}social-media-marketing/">Social Media Marketing</a>
          <a href="${Base}google-ads-management/">Meta Ads Management</a>
          <a href="${Base}content-writing-services/">Content Writing</a>
          <a href="${Base}graphic-design-services/">Graphic Design</a>
          <a href="${Base}video-editing-services/">Video Editing</a>
          <a href="${Base}photography-services/">Photography</a>
        </div>
      </div>
"@
}

function Build-FooterContact {
  param([string]$Place)
@"
        <h3>Contact Info</h3>
        <a href="tel:+918667439645"><span>Phone</span><strong>+91 86674 39645</strong></a>
        <a href="mailto:valourdigitalagency@gmail.com"><span>Email</span><strong>valourdigitalagency@gmail.com</strong></a>
        <p><span>Place</span><strong>$Place</strong></p>
        <a href="https://www.instagram.com/valour_digital_agency" target="_blank" rel="nofollow noopener noreferrer"><span>Insta</span><strong>@valour_digital_agency</strong></a>
        <a href="https://www.facebook.com/share/1DjDntTMdN/" target="_blank" rel="nofollow noopener noreferrer"><span>Facebook</span><strong>Valour Digital Agency</strong></a>
        <a href="https://www.linkedin.com/company/valour-digitalagency/" target="_blank" rel="nofollow noopener noreferrer"><span>LinkedIn</span><strong>Valour Digital Agency</strong></a>
"@
}

function Update-Navigation {
  param(
    [string]$Text,
    [string]$Base
  )
  if ($Text -match 'class="nav-dropdown"') {
    return $Text
  }
  $needle = "      <a href=""${Base}#services"">WHAT WE DO</a>"
  if ($Text.Contains($needle)) {
    return $Text.Replace($needle, $needle + "`r`n" + (Build-ExploreDropdown $Base))
  }
  return $Text
}

function Update-Footer {
  param(
    [string]$Text,
    [string]$Base
  )
  $pattern = '(?s)<div class="footer-col">\s*<h3>Our Services</h3>.*?<div class="footer-col footer-contact">'
  $replacement = Build-ServicesBlock $Base
  $Text = [regex]::Replace($Text, $pattern, $replacement, 1)
  $Text = [regex]::Replace($Text, '(<p><span>Place</span><strong>)([^<]*)(</strong></p>)', '$1Chennai, India$3')
  return $Text
}

function Remove-Sections {
  param(
    [string]$Text,
    [switch]$RemoveFaq
  )
  if ($RemoveFaq) {
    $Text = [regex]::Replace($Text, '(?s)\r?\n\s*<section class="faq section-pad">.*?\r?\n\s*</section>\r?\n', "`r`n")
    $Text = [regex]::Replace($Text, '(?s)\r?\n\s*<section class="service-section faq-section">.*?\r?\n\s*</section>\r?\n', "`r`n")
    $Text = [regex]::Replace($Text, '(?s)\r?\n\s*<script type="application/ld\+json">\s*\{\s*"@context"\s*:\s*"https://schema.org",\s*"@type"\s*:\s*"FAQPage".*?\}\s*</script>\r?\n', "`r`n")
  }
  return $Text
}

function Update-Home {
  $text = Get-Content -Path $homePath -Raw
  $text = $text.Replace('Google Ads', 'Meta Ads')
  $text = $text.Replace(
    '<h3>Performance Ads</h3>' + "`r`n" + '          <p>Meta and Google campaigns planned, launched, and optimized for leads, conversions, and better return on spend.</p>' + "`r`n" + '          <a class="service-card-link" href="google-ads-management/">Explore Performance Ads</a>',
    '<h3>Meta Ads</h3>' + "`r`n" + '          <p>Meta ad campaigns planned, launched, and optimized for leads, conversions, and better return on spend.</p>' + "`r`n" + '          <a class="service-card-link" href="google-ads-management/">Explore Meta Ads</a>'
  )
  $text = $text.Replace(
    '<p class="service-intro reveal">We deliver focused digital services for brands that want stronger visibility, better creative, and more qualified enquiries. From websites and SEO to graphic design, social media, content, video, photography, and performance ads, every service is built to support growth.</p>',
    '<p class="service-intro reveal">We deliver focused digital services for brands that want stronger visibility, better creative, and more qualified enquiries. From websites and SEO to graphic design, social media, content, video, photography, and Meta Ads, every service is built to support growth.</p>'
  )
  $text = Update-Navigation $text ''
  $text = Remove-Sections $text -RemoveFaq
  $text = Update-Footer $text ''
  Set-Content -Path $homePath -Value $text -Encoding UTF8
}

function Update-ServiceFile {
  param([string]$Path)
  $text = Get-Content -Path $Path -Raw
  $text = $text.Replace('Google Ads', 'Meta Ads')
  $text = $text.Replace('<p class="kicker">GOOGLE ADS MANAGEMENT</p>', '<p class="kicker">META ADS MANAGEMENT</p>')
  $text = Update-Navigation $text '../'
  $text = Update-Footer $text '../'
  $text = Remove-Sections $text -RemoveFaq
  Set-Content -Path $Path -Value $text -Encoding UTF8
}

Update-Home
foreach ($file in $serviceFiles) {
  Update-ServiceFile $file
}
