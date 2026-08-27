#!/usr/bin/env python3
"""Generate the DNZ Consulting LLC legal + security policy site.

Edit COMPANY or DOCS, then run:  python3 build.py
Every HTML page is rebuilt from this file. Do not edit the HTML by hand.
"""
import html, os, pathlib

COMPANY = {
    "name": "DNZ Consulting LLC",
    "state": "New York, United States",
    "reg": "7798491",
    "address": "45 Meadow Lane, Lawrence, NY 11559, United States",
    "contact": "privacy@dancykier.com",
    "effective": "August 27, 2026",
    "review": "August 27, 2027",
}

CSS = """
:root{--bg:#ffffff;--fg:#16181d;--muted:#5b6270;--line:#e3e6ec;--accent:#1f5fd0;--card:#f7f8fa}
@media (prefers-color-scheme:dark){:root{--bg:#0f1115;--fg:#e7e9ee;--muted:#9aa2b1;--line:#242833;--accent:#7aa7ff;--card:#161a21}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-text-size-adjust:100%}
.wrap{max-width:760px;margin:0 auto;padding:48px 24px 96px}
header.site{border-bottom:1px solid var(--line);padding-bottom:20px;margin-bottom:36px}
header.site a.brand{color:var(--fg);text-decoration:none;font-weight:650;letter-spacing:-.01em;font-size:17px}
header.site .sub{color:var(--muted);font-size:13px;margin-top:4px}
h1{font-size:30px;line-height:1.2;letter-spacing:-.02em;margin:0 0 6px}
h2{font-size:19px;letter-spacing:-.01em;margin:38px 0 10px;padding-top:4px}
h3{font-size:16px;margin:24px 0 6px}
p,li{color:var(--fg)}
.meta{color:var(--muted);font-size:14px;margin:0 0 28px}
ul{padding-left:22px}
li{margin:6px 0}
a{color:var(--accent)}
.docs{list-style:none;padding:0;margin:24px 0 0}
.docs li{margin:0 0 10px}
.docs a{display:block;border:1px solid var(--line);background:var(--card);border-radius:10px;padding:14px 16px;text-decoration:none;color:var(--fg)}
.docs a:hover{border-color:var(--accent)}
.docs .t{font-weight:600}
.docs .d{color:var(--muted);font-size:14px;margin-top:2px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:var(--card);font-weight:600}
footer{margin-top:64px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:13px}
.back{display:inline-block;margin-bottom:26px;font-size:14px}
@media print{body{background:#fff;color:#000}.wrap{max-width:none;padding:0}header.site,.back,footer a{color:#000}a{color:#000;text-decoration:none}}
"""

def page(slug, title, body, is_index=False):
    back = "" if is_index else '<a class="back" href="./">&larr; All policies</a>'
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — {COMPANY['name']}</title>
<meta name="description" content="{html.escape(title)} of {COMPANY['name']}.">
<style>{CSS}</style>
</head><body><div class="wrap">
<header class="site">
  <a class="brand" href="./">{COMPANY['name']}</a>
  <div class="sub">Policies and compliance &middot; NY registration {COMPANY['reg']}</div>
</header>
{back}
{body}
<footer>
  {COMPANY['name']} &middot; {COMPANY['address']}<br>
  New York State registration number {COMPANY['reg']}<br>
  Contact: <a href="mailto:{COMPANY['contact']}">{COMPANY['contact']}</a>
</footer>
</div></body></html>
"""

def head(title, purpose):
    return (f"<h1>{html.escape(title)}</h1>\n"
            f"<p class='meta'>{COMPANY['name']} &middot; Effective {COMPANY['effective']} &middot; "
            f"Next review {COMPANY['review']}</p>\n{purpose}\n")

OWNER = ("<h2>1. Scope and ownership</h2>"
         "<p>This policy applies to every system, device, and person that "
         f"{COMPANY['name']} uses to do business. {COMPANY['name']} is a small company. "
         "The Managing Member owns this policy. The Managing Member also acts as the "
         "Security Officer and the Data Protection Officer.</p>"
         "<p>The Managing Member reviews this policy one time each year. "
         "The Managing Member also reviews it after any security incident.</p>")

DOCS = [
 ("privacy", "Privacy Policy",
  "How we collect, use, and protect personal data.",
  head("Privacy Policy",
   "<p>This policy explains how " + COMPANY['name'] + " handles personal data. "
   "It applies to our websites, our applications, and our work as a technology partner "
   "for e-commerce merchants.</p>") +
  """
<h2>1. Who we are</h2>
<p>DNZ Consulting LLC is a limited liability company. New York State registered the
company under number 7798491. Our address is 45 Meadow Lane, Lawrence, NY 11559,
United States.</p>
<p>The Managing Member acts as our Data Protection Officer. Write to
<a href="mailto:privacy@dancykier.com">privacy@dancykier.com</a> for any privacy question.</p>

<h2>2. What personal data we process</h2>
<p>We process only the data that a task needs. The categories are:</p>
<table>
<tr><th>Category</th><th>Examples</th><th>Why we process it</th></tr>
<tr><td>Merchant account data</td><td>Shop name, shop identifier, authorization tokens</td><td>To connect to a merchant platform on the merchant's instruction</td></tr>
<tr><td>Order data</td><td>Order number, items, quantity, price, status</td><td>To show and manage orders for the merchant</td></tr>
<tr><td>Buyer contact data</td><td>Name, shipping address, phone, email</td><td>To create shipping labels and to answer customer service requests</td></tr>
<tr><td>Support correspondence</td><td>Email content you send us</td><td>To answer your request</td></tr>
<tr><td>Technical data</td><td>Error logs, request timestamps</td><td>To keep the service working and secure</td></tr>
</table>
<p>We do not process special category data. We do not process children's data on purpose.
We do not collect payment card numbers.</p>

<h2>3. How we get the data</h2>
<p>We get merchant and order data from the merchant. The merchant authorizes our
application on their platform account. The merchant can cancel that authorization at
any time. We get support data directly from the person who writes to us.</p>

<h2>4. Our legal role</h2>
<p>For merchant and buyer data we act as a data processor. The merchant is the
controller. We act only on the merchant's documented instruction. For our own website
visitors and for people who email us, we act as the controller.</p>

<h2>5. Why we are allowed to process the data</h2>
<ul>
<li>To perform a contract with the merchant.</li>
<li>To follow a legal obligation, such as tax or accounting law.</li>
<li>For our legitimate interest in keeping the service secure and working.</li>
<li>With consent, where the law requires consent.</li>
</ul>

<h2>6. Who we share data with</h2>
<p>We do not sell personal data. We do not share personal data for advertising.
We share data only with:</p>
<ul>
<li>The e-commerce platform that the merchant already uses.</li>
<li>Infrastructure suppliers that host or transmit the data for us.</li>
<li>A government authority, when the law compels us.</li>
</ul>
<p>Every supplier works under a written contract. The contract requires confidentiality
and appropriate security.</p>

<h2>7. Where we store the data</h2>
<p>We store and process personal data in the United States. If we ever transfer
personal data out of its country of origin, we use a lawful transfer mechanism first.</p>

<h2>8. How long we keep the data</h2>
<p>We keep personal data only as long as the purpose needs it.</p>
<ul>
<li>Merchant and order data: for the life of the contract, then 30 days.</li>
<li>Support email: 24 months.</li>
<li>Records that tax or accounting law requires: 7 years.</li>
</ul>
<p>At the end of a contract we delete all customer data in our possession. We do this
within 30 days. We confirm the deletion in writing if the customer asks.</p>

<h2>9. How we protect the data</h2>
<p>We encrypt personal data in transit with TLS. We encrypt personal data at rest.
We give access only to the people who need it. We store secrets and access tokens in an
encrypted keystore. Our <a href="information-security.html">Information Security
Policy</a> describes the controls in full.</p>

<h2>10. Your rights</h2>
<p>You can ask us to do the following with your personal data:</p>
<ul>
<li>Give you a copy of it.</li>
<li>Correct it.</li>
<li>Delete it.</li>
<li>Restrict how we use it.</li>
<li>Object to how we use it.</li>
<li>Move it to another provider.</li>
</ul>
<p>Write to <a href="mailto:privacy@dancykier.com">privacy@dancykier.com</a>. We answer
within 30 days. We do not charge a fee. If we hold your data for a merchant, we pass
your request to that merchant and we help them answer it.</p>
<p>You can also complain to your data protection authority.</p>

<h2>11. Cookies</h2>
<p>Our policy website uses no cookies. It runs no analytics and no advertising trackers.</p>

<h2>12. Changes</h2>
<p>We review this policy one time each year. We publish every change on this page and
we update the effective date. We tell affected merchants about a material change.</p>
"""),

 ("information-security", "Information Security Policy",
  "Our security program, controls, and responsibilities.",
  head("Information Security Policy",
   "<p>This policy states how " + COMPANY['name'] + " protects information. It covers "
   "company data, merchant data, and personal data.</p>") + OWNER + """
<h2>2. Objectives</h2>
<ul>
<li>Keep information confidential. Only authorized people see it.</li>
<li>Keep information correct. Nobody changes it without authority.</li>
<li>Keep information available. Authorized people can reach it when they need it.</li>
<li>Meet our legal and contractual duties.</li>
</ul>

<h2>3. Supporting policies</h2>
<p>These documents form the security program together with this policy:</p>
<ul>
<li><a href="access-control.html">Access Control Policy</a></li>
<li><a href="data-classification.html">Data Classification and Encryption Policy</a></li>
<li><a href="endpoint-security.html">Endpoint Security Policy</a></li>
<li><a href="network-security.html">Network Security Policy</a></li>
<li><a href="security-baseline.html">Operational Security Baseline</a></li>
<li><a href="incident-response.html">Incident Response Policy</a></li>
<li><a href="vulnerability-management.html">Vulnerability and Threat Management Procedure</a></li>
<li><a href="data-protection.html">Personal Data Protection Policy</a></li>
</ul>

<h2>4. Core rules</h2>
<ul>
<li>Encrypt all data in transit. Use TLS 1.2 or higher.</li>
<li>Encrypt all data at rest on every device and in every database.</li>
<li>Give each account the least privilege that the work needs.</li>
<li>Protect every account with multi-factor authentication where the service offers it.</li>
<li>Store every secret, key, and token in an encrypted keystore. Never store a secret in source code.</li>
<li>Keep source code in private repositories unless the code is meant to be public.</li>
<li>Patch operating systems and dependencies. See the vulnerability procedure.</li>
<li>Log administrative actions and keep the logs.</li>
</ul>

<h2>5. Suppliers</h2>
<p>We assess a supplier before we send them any personal data. We check their security
statement and their privacy terms. We sign a data processing agreement when the
supplier processes personal data for us.</p>

<h2>6. People</h2>
<p>Every person who works for the company reads this policy before they get access.
They read it again each year. Access ends on the same day that the work ends.</p>

<h2>7. Breaking this policy</h2>
<p>A breach of this policy ends the person's access. It can also end the contract.</p>

<h2>8. Review</h2>
<p>The Managing Member reviews this policy one time each year, and after any incident.</p>
"""),

 ("network-security", "Network Security Policy",
  "Segregation, firewalls, and threat monitoring.",
  head("Network Security Policy",
   "<p>This policy states how " + COMPANY['name'] + " separates its networks and how it "
   "watches for network threats.</p>") + OWNER + """
<h2>2. Network segregation</h2>
<ul>
<li>We run separate networks for different trust levels.</li>
<li>Work devices sit on the primary network.</li>
<li>Guests use a guest network. The guest network cannot reach a work device.</li>
<li>Internet-of-things devices sit on their own network. They cannot reach a work device.</li>
<li>No production database accepts a direct connection from the open internet.</li>
</ul>

<h2>3. Perimeter controls</h2>
<ul>
<li>The router firewall stays on. It denies all inbound traffic by default.</li>
<li>The operating system firewall stays on for every endpoint.</li>
<li>We open an inbound port only for a stated business need. We record the reason.</li>
<li>We disable remote administration of the router from the internet.</li>
<li>We change the default administrator password on every network device.</li>
<li>We keep router and access point firmware current.</li>
</ul>

<h2>4. Remote access</h2>
<ul>
<li>Remote access to a server uses SSH with a public key. Password login is off.</li>
<li>Administrative interfaces are not published to the open internet.</li>
<li>We use a virtual private network to reach a private corporate network.</li>
</ul>

<h2>5. Monitoring</h2>
<ul>
<li>The platform firewall logs blocked connections.</li>
<li>Our hosting and database suppliers provide request logs and alerting. We review them.</li>
<li>We alert on a failed authentication burst and on an unexpected administrative change.</li>
<li>We review network and access logs every month, and immediately after an alert.</li>
</ul>

<h2>6. Wireless</h2>
<ul>
<li>Every wireless network uses WPA2 or WPA3.</li>
<li>We do not use WEP. We do not run an open network.</li>
<li>We disable WPS.</li>
</ul>

<h2>7. Review</h2>
<p>The Managing Member reviews this policy one time each year.</p>
"""),

 ("endpoint-security", "Endpoint Security Policy",
  "Anti-malware and device protection.",
  head("Endpoint Security Policy",
   "<p>This policy states how " + COMPANY['name'] + " protects the computers and phones "
   "that touch company data.</p>") + OWNER + """
<h2>2. Anti-malware</h2>
<ul>
<li>Every endpoint runs anti-malware protection at all times.</li>
<li>macOS endpoints run the built-in Apple protection: XProtect, XProtect Remediator, Gatekeeper, and Notarization checks. Apple updates the signatures automatically.</li>
<li>System Integrity Protection stays on.</li>
<li>Any Windows or Linux endpoint runs a maintained anti-malware product with automatic signature updates.</li>
<li>Nobody may disable anti-malware protection.</li>
</ul>

<h2>3. Software sources</h2>
<ul>
<li>Install software only from the vendor, an official app store, or a trusted package manager.</li>
<li>Do not install unsigned software unless the Managing Member approves it and records the reason.</li>
<li>Remove software that the business no longer needs.</li>
</ul>

<h2>4. Device hardening</h2>
<ul>
<li>Full-disk encryption stays on. macOS uses FileVault.</li>
<li>The operating system firewall stays on.</li>
<li>Automatic security updates stay on.</li>
<li>The device locks after 5 minutes of inactivity, and it needs a password to unlock.</li>
<li>Remote wipe stays enabled. macOS and iOS use Find My.</li>
<li>Backups run automatically and the backup is encrypted.</li>
</ul>

<h2>5. Mobile devices</h2>
<ul>
<li>A phone that reads company email uses a passcode and biometric unlock.</li>
<li>The operating system must still receive security updates from the vendor.</li>
<li>A jailbroken or rooted device may not hold company data.</li>
</ul>

<h2>6. Loss or theft</h2>
<p>Report a lost or stolen device immediately. Follow the
<a href="incident-response.html">Incident Response Policy</a>. Lock the device
remotely, then wipe it, then rotate every credential it held.</p>

<h2>7. Disposal</h2>
<p>Erase a device with a cryptographic erase before disposal or resale.</p>

<h2>8. Review</h2>
<p>The Managing Member reviews this policy one time each year.</p>
"""),

 ("security-baseline", "Operational Security Baseline",
  "Screen locking, passwords, MFA, and clear desk.",
  head("Operational Security Baseline",
   "<p>This baseline states the minimum security settings for daily work at "
   + COMPANY['name'] + ". Every device and every account must meet it.</p>") + OWNER + """
<h2>2. Screen locking</h2>
<ul>
<li>The screen locks after 5 minutes of inactivity.</li>
<li>Unlocking needs a password or a biometric check.</li>
<li>Lock the screen before you leave the device, even for a moment.</li>
</ul>

<h2>3. Password complexity</h2>
<ul>
<li>A password is at least 14 characters long.</li>
<li>A password is unique. Never reuse a password across services.</li>
<li>A password manager generates and stores every password. We use the macOS Keychain and Apple Passwords.</li>
<li>Never write a password in a document, a chat message, or source code.</li>
<li>Change a password immediately if it may have leaked.</li>
</ul>

<h2>4. Multi-factor authentication</h2>
<ul>
<li>Turn on multi-factor authentication for every account that offers it.</li>
<li>This is mandatory for email, cloud hosting, source control, the domain registrar, banking, and every merchant platform.</li>
<li>Prefer an authenticator application or a hardware key. Avoid SMS codes where an alternative exists.</li>
<li>Store recovery codes in the encrypted password manager.</li>
</ul>

<h2>5. Clear desk and clear screen</h2>
<ul>
<li>Do not leave a printed document that holds personal data on the desk.</li>
<li>Store paper records in a locked drawer.</li>
<li>Shred a paper record that holds personal data before disposal.</li>
<li>Position the screen so that a visitor cannot read it.</li>
</ul>

<h2>6. Secrets</h2>
<ul>
<li>Store every API key, token, and certificate in the macOS Keychain or in the platform secret store.</li>
<li>Never commit a secret to source control.</li>
<li>Rotate a secret immediately if it appears in a log, a chat, or a file.</li>
</ul>

<h2>7. Email and phishing</h2>
<ul>
<li>Check the sender address before you act on a request.</li>
<li>Never approve a payment or a credential change from an email alone. Confirm on a second channel.</li>
<li>Report a suspected phishing message under the incident response policy.</li>
</ul>

<h2>8. Review</h2>
<p>The Managing Member reviews this baseline one time each year.</p>
"""),

 ("access-control", "Access Control Policy",
  "Least privilege and account lifecycle.",
  head("Access Control Policy",
   "<p>This policy states who may reach a system at " + COMPANY['name'] + ", and how "
   "we grant and remove that access.</p>") + OWNER + """
<h2>2. Least privilege</h2>
<ul>
<li>Grant the smallest permission that lets the person do the work.</li>
<li>Grant access to personal data only when the task needs that data.</li>
<li>Do not use an administrator account for daily work.</li>
<li>Do not share an account. Every person uses their own account.</li>
<li>Request the narrowest scope when you authorize an application on a third-party platform.</li>
</ul>

<h2>3. Database access</h2>
<ul>
<li>Row Level Security stays on for every table that holds user data.</li>
<li>An application uses a restricted key. It never uses an administrative key.</li>
<li>We use an administrative key only for a named maintenance task, and never from client code.</li>
</ul>

<h2>4. Granting access</h2>
<ul>
<li>The Managing Member approves every access request.</li>
<li>We record what we granted, to whom, and why.</li>
<li>Access to production data needs a written business reason.</li>
</ul>

<h2>5. Removing access</h2>
<ul>
<li>Remove access on the last day of the work.</li>
<li>Remove access immediately after a suspected compromise.</li>
<li>Rotate every shared credential that the person could reach.</li>
</ul>

<h2>6. Review</h2>
<ul>
<li>We review every account and every permission every 6 months.</li>
<li>We remove an account that nobody has used for 90 days.</li>
<li>We review third-party application authorizations at the same time. We revoke the ones we no longer use.</li>
</ul>

<h2>7. Authentication</h2>
<p>Every account follows the <a href="security-baseline.html">Operational Security
Baseline</a> for password strength and multi-factor authentication.</p>

<h2>8. Review of this policy</h2>
<p>The Managing Member reviews this policy one time each year.</p>
"""),

 ("data-classification", "Data Classification and Encryption Policy",
  "Data levels, handling rules, and encryption.",
  head("Data Classification and Encryption Policy",
   "<p>This policy sorts information into levels. It states how to handle each level "
   "and how to encrypt it.</p>") + OWNER + """
<h2>2. Classification levels</h2>
<table>
<tr><th>Level</th><th>What it covers</th><th>Handling rule</th></tr>
<tr><td>Restricted</td><td>Personal data, buyer contact data, access tokens, API keys, credentials, financial records</td><td>Encrypt at rest and in transit. Access by named person only. Never send by plain email. Never place in source code.</td></tr>
<tr><td>Confidential</td><td>Merchant business data, order data, pricing, source code, contracts</td><td>Encrypt in transit. Store in a private repository or a private bucket. Share only with a business need.</td></tr>
<tr><td>Internal</td><td>Internal notes, drafts, configuration that holds no secret</td><td>Keep inside company systems. Do not publish.</td></tr>
<tr><td>Public</td><td>Published policies, marketing pages, public documentation</td><td>No restriction.</td></tr>
</table>

<h2>3. Encryption in transit</h2>
<ul>
<li>Every connection uses TLS 1.2 or higher.</li>
<li>Every website uses HTTPS. We redirect HTTP to HTTPS.</li>
<li>Server administration uses SSH with a public key.</li>
<li>We never send Restricted data over an unencrypted channel.</li>
</ul>

<h2>4. Encryption at rest</h2>
<ul>
<li>Every laptop and desktop uses full-disk encryption. macOS uses FileVault with AES-256.</li>
<li>Every mobile device uses the platform hardware encryption.</li>
<li>Managed databases use encryption at rest through the hosting provider.</li>
<li>Backups are encrypted.</li>
<li>Secrets live in the macOS Keychain or in the platform secret store. They are never in a plain file.</li>
</ul>

<h2>5. Labelling</h2>
<p>Store Restricted data in a location that only holds Restricted data. Name the
location clearly. Do not mix levels in one folder.</p>

<h2>6. Deleting data</h2>
<ul>
<li>Delete Restricted data when its retention period ends.</li>
<li>Use a cryptographic erase for a device.</li>
<li>Shred paper that holds Restricted data.</li>
</ul>

<h2>7. Review</h2>
<p>The Managing Member reviews this policy one time each year.</p>
"""),

 ("incident-response", "Incident Response Policy",
  "Roles, steps, timelines, and notification.",
  head("Incident Response Policy",
   "<p>This policy states what " + COMPANY['name'] + " does when a security incident or "
   "a personal data breach happens.</p>") + OWNER + """
<h2>2. What counts as an incident</h2>
<ul>
<li>Somebody reaches a system or data without authority.</li>
<li>Personal data goes to the wrong person, or becomes public.</li>
<li>A device that holds company data is lost or stolen.</li>
<li>Malware runs on an endpoint or a server.</li>
<li>A credential, key, or token leaks.</li>
<li>A supplier tells us that they had a breach that touches our data.</li>
</ul>

<h2>3. Roles</h2>
<table>
<tr><th>Role</th><th>Who</th><th>Responsibility</th></tr>
<tr><td>Incident Manager</td><td>Managing Member</td><td>Declares the incident. Runs the response. Makes every decision.</td></tr>
<tr><td>Security Officer</td><td>Managing Member</td><td>Contains and investigates the incident. Collects evidence.</td></tr>
<tr><td>Data Protection Officer</td><td>Managing Member</td><td>Decides on regulator and customer notification. Answers data subjects.</td></tr>
<tr><td>Communications</td><td>Managing Member</td><td>Writes and sends every external message.</td></tr>
</table>
<p>The company is small, so one person holds these roles. The company appoints a
second responder in writing if it grows.</p>

<h2>4. How to report an incident</h2>
<ul>
<li>Email <a href="mailto:privacy@dancykier.com">privacy@dancykier.com</a>. Use the subject line "SECURITY INCIDENT".</li>
<li>Report within 1 hour of discovery. Report a suspicion. Do not wait for proof.</li>
<li>Anyone may report: a worker, a merchant, a platform, a supplier, or a member of the public.</li>
</ul>

<h2>5. Response steps</h2>
<ol>
<li><strong>Record.</strong> Write down the time, the reporter, and what they saw.</li>
<li><strong>Assess.</strong> Decide the severity within 4 hours. Decide whether personal data is involved.</li>
<li><strong>Contain.</strong> Isolate the system. Revoke the credential. Rotate the key. Block the account.</li>
<li><strong>Investigate.</strong> Find the cause and the scope. Identify every record that the incident touched.</li>
<li><strong>Notify.</strong> Follow section 6.</li>
<li><strong>Recover.</strong> Restore the service from a clean state. Confirm that the attacker is out.</li>
<li><strong>Review.</strong> Hold a review within 10 working days. Write the lessons. Change the controls.</li>
</ol>

<h2>6. Notification</h2>
<ul>
<li>We notify the affected platform and the affected merchants <strong>without undue delay, and within 24 hours</strong> of confirming a breach that touches their data.</li>
<li>We notify a supervisory authority within <strong>72 hours</strong> where the law requires it.</li>
<li>We notify affected individuals without undue delay when the breach creates a high risk to them.</li>
<li>Every notification states what happened, what data it touched, what we did, and what the reader should do.</li>
<li>We give a contact point for questions in every notification.</li>
</ul>

<h2>7. Records</h2>
<p>We record every incident, including the ones that need no notification. We keep the
record for 5 years. The record holds the facts, the effect, and the action we took.</p>

<h2>8. Testing</h2>
<p>We walk through this plan one time each year with a test scenario. We record the
result and we fix any gap.</p>

<h2>9. Review</h2>
<p>The Managing Member reviews this policy one time each year, and after every incident.</p>
"""),

 ("vulnerability-management", "Vulnerability and Threat Management Procedure",
  "Finding, ranking, and fixing weaknesses.",
  head("Vulnerability and Threat Management Procedure",
   "<p>This procedure states how " + COMPANY['name'] + " finds security weaknesses and "
   "how fast it fixes them.</p>") + OWNER + """
<h2>2. How we find vulnerabilities</h2>
<ul>
<li>Operating systems report available security updates automatically.</li>
<li>GitHub Dependabot alerts us to a vulnerable dependency in a repository.</li>
<li>Our hosting and database suppliers send security advisories. We read them.</li>
<li>We review our own code before we merge it.</li>
<li>We accept a report from any outside researcher at <a href="mailto:privacy@dancykier.com">privacy@dancykier.com</a>.</li>
</ul>

<h2>3. How we rank a vulnerability</h2>
<p>We use the CVSS score and the real exposure of the affected system.</p>
<table>
<tr><th>Severity</th><th>CVSS</th><th>Fix within</th></tr>
<tr><td>Critical</td><td>9.0 - 10.0</td><td>7 days</td></tr>
<tr><td>High</td><td>7.0 - 8.9</td><td>30 days</td></tr>
<tr><td>Medium</td><td>4.0 - 6.9</td><td>90 days</td></tr>
<tr><td>Low</td><td>0.1 - 3.9</td><td>Next planned release</td></tr>
</table>
<p>A vulnerability with a public exploit that touches personal data is Critical. We fix
it immediately, whatever the score says.</p>

<h2>4. Patching</h2>
<ul>
<li>Automatic security updates stay on for every operating system.</li>
<li>We update dependencies at least every month.</li>
<li>We test a patch before we deploy it to production, when a test is possible.</li>
<li>We record the date of every applied patch.</li>
</ul>

<h2>5. Accepting a risk</h2>
<p>We fix a vulnerability by default. The Managing Member may accept a risk instead.
That decision is written down. It states the reason, the compensating control, and a
review date. We review an accepted risk every 6 months.</p>

<h2>6. Threat monitoring</h2>
<ul>
<li>We watch supplier status pages and security advisories.</li>
<li>We review access and error logs every month.</li>
<li>We investigate an unexpected administrative change immediately.</li>
</ul>

<h2>7. Review</h2>
<p>The Managing Member reviews this procedure one time each year.</p>
"""),

 ("data-protection", "Personal Data Protection Policy",
  "Internal rules for handling personal data.",
  head("Personal Data Protection Policy",
   "<p>This is the internal policy of " + COMPANY['name'] + " for personal data. The "
   "public <a href='privacy.html'>Privacy Policy</a> explains the same subject to "
   "people outside the company.</p>") + OWNER + """
<h2>2. Principles</h2>
<ul>
<li><strong>Lawful and fair.</strong> Process personal data only with a legal basis.</li>
<li><strong>Purpose limited.</strong> Use the data only for the stated purpose.</li>
<li><strong>Minimal.</strong> Collect the smallest amount that the purpose needs.</li>
<li><strong>Accurate.</strong> Correct data that is wrong.</li>
<li><strong>Time limited.</strong> Delete the data when the purpose ends.</li>
<li><strong>Secure.</strong> Protect the data as the security policies require.</li>
<li><strong>Accountable.</strong> Record what we do and be able to show it.</li>
</ul>

<h2>3. Data Protection Officer</h2>
<p>The Managing Member acts as the Data Protection Officer. The contact address is
<a href="mailto:privacy@dancykier.com">privacy@dancykier.com</a>. The Data Protection
Officer approves any new processing of personal data before it starts.</p>

<h2>4. Our role as a processor</h2>
<p>When we process personal data for a merchant, the merchant is the controller. We:</p>
<ul>
<li>Act only on the merchant's documented instruction.</li>
<li>Keep the data confidential.</li>
<li>Use only sub-processors that the merchant permits.</li>
<li>Help the merchant answer a data subject request.</li>
<li>Help the merchant meet their breach notification duty.</li>
<li>Delete or return the data at the end of the contract.</li>
<li>Give the merchant the information they need to show compliance.</li>
</ul>

<h2>5. Data subject requests</h2>
<ul>
<li>Send every request to <a href="mailto:privacy@dancykier.com">privacy@dancykier.com</a> on the day it arrives.</li>
<li>Verify who the person is before you act.</li>
<li>Answer within 30 days.</li>
<li>Pass a request to the merchant when the merchant is the controller. Help them answer it.</li>
<li>We assist sellers and platform operators with any request to provide, correct, or delete data.</li>
</ul>

<h2>6. Records of processing</h2>
<p>We keep a record of every processing activity. The record holds the purpose, the
categories of data and people, the recipients, the retention period, and the security
measures.</p>

<h2>7. Assessing a new activity</h2>
<p>Before a new processing activity starts, the Data Protection Officer checks the legal
basis, the data minimization, the retention period, and the security controls. A
high-risk activity gets a written impact assessment.</p>

<h2>8. Retention and deletion</h2>
<p>The <a href="privacy.html">Privacy Policy</a> states the retention periods. At the
end of a contract we delete all customer personal data within 30 days. We confirm the
deletion in writing when the customer asks.</p>

<h2>9. Breaches</h2>
<p>A personal data breach follows the <a href="incident-response.html">Incident Response
Policy</a>. We notify the platform and affected merchants within 24 hours of
confirmation, and a supervisory authority within 72 hours where the law requires it.</p>

<h2>10. Training</h2>
<p>Every person who handles personal data reads this policy before they get access, and
again each year.</p>

<h2>11. Review</h2>
<p>The Managing Member reviews this policy one time each year.</p>
"""),
]

INDEX_BODY = f"""
<h1>Policies and compliance</h1>
<p class="meta">{COMPANY['name']} &middot; New York registration {COMPANY['reg']} &middot;
Effective {COMPANY['effective']}</p>
<p>{COMPANY['name']} publishes the policies below. They govern how we protect
information and how we handle personal data. We review every document one time each
year, and after any security incident.</p>
<p>Send any security or privacy question to
<a href="mailto:{COMPANY['contact']}">{COMPANY['contact']}</a>. The Managing Member acts
as our Data Protection Officer and answers within 30 days.</p>
<ul class="docs">
""" + "\n".join(
    f'<li><a href="{s}.html"><span class="t">{html.escape(t)}</span>'
    f'<span class="d">{html.escape(d)}</span></a></li>'
    for s, t, d, _ in DOCS
) + """
</ul>
<h2>Certifications</h2>
<p>We hold no ISO 27001, ISO 27701, SOC 2 Type 2, or ePrivacy certification today.</p>
<h2>Where we process data</h2>
<p>We store and process personal data in the United States.</p>
"""

out = pathlib.Path(__file__).parent
(out / "index.html").write_text(page("index", "Policies and compliance", INDEX_BODY, True))
for slug, title, _desc, body in DOCS:
    (out / f"{slug}.html").write_text(page(slug, title, body))
(out / "CNAME").write_text("legal.dancykier.com\n")
print(f"built {len(DOCS) + 1} pages in {out}")
