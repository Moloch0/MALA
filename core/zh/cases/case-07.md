# case-07: policy-ops

来源 benchmark bucket：`deep`

## 原始输入

```text
How do I ensure my content doesn't get scraped by AI researchers?
```

## 不用 MALA

```text
You cannot *ensure* that public web content will not be scraped. If someone can view it anonymously in a browser, a determined scraper can usually copy it. What you can do is reduce compliant crawling, create an enforceable “do not scrape / do not train” record, and make noncompliant scraping technically harder.

**The Only Strong Control**

Put the content behind access control.

Use login, paid access, expiring signed URLs, per-user authorization, and server-side checks. `robots.txt` is a request to crawlers, not a security boundary. The Robots Exclusion Protocol RFC explicitly says robots rules are “not a form of access authorization” [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309). For sensitive, unpublished, premium, or legally risky material, do not publish it on a public URL.

**For Public Content**

Add AI crawler rules to `https://yourdomain.com/robots.txt`.

A conservative baseline:

```txt
# AI model training / dataset crawlers

User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

# Optional: block AI search, answer, and user-fetch agents too.
# This may reduce visibility in ChatGPT, Claude, Perplexity, etc.

User-agent: OAI-SearchBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: Claude-SearchBot
Disallow: /

User-agent: Claude-User
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: Perplexity-User
Disallow: /
```

The distinction matters:

`GPTBot` is OpenAI’s training crawler; OpenAI says disallowing it indicates the site’s content should not be used for training, while `OAI-SearchBot` controls appearance in ChatGPT search-style results [OpenAI crawler docs](https://developers.openai.com/api/docs/bots).

`Google-Extended` is Google’s control token for Gemini model training and grounding, and Google says blocking it does not affect inclusion in Google Search [Google crawler docs](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers).

`ClaudeBot` is Anthropic’s training-related crawler; Anthropic documents separate bots for training, user-directed access, and search quality [Anthropic crawler docs](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler).

`CCBot` is Common Crawl. This one is especially important because many AI researchers and labs use Common Crawl-derived datasets. Common Crawl documents `User-agent: CCBot` / `Disallow: /` as the way to block future crawls [Common Crawl CCBot docs](https://blog.commoncrawl.org/ccbot).

**Do Not Accidentally Kill Search**

If you want normal search traffic, do not broadly use:

```txt
User-agent: *
Disallow: /
```

That blocks ordinary search crawlers too. Also be careful blocking `Googlebot` or `bingbot`: those affect Google/Bing search visibility, not just AI uses. Prefer purpose-specific tokens like `Google-Extended` where available.

**Enforce At The Edge**

Because some scrapers ignore or spoof `robots.txt`, add network controls:

Use a WAF/CDN bot product such as Cloudflare, Fastly, Akamai, etc. Cloudflare’s managed AI crawler controls can generate AI-focused robots directives and block AI bots at the edge [Cloudflare managed robots.txt](https://blog.cloudflare.com/control-content-use-for-ai-training/).

Block or challenge suspicious traffic patterns: high request rate, no cookies, no referrer, sequential URL walking, unusual ASN/cloud provider traffic, repeated `HEAD`/`GET` sweeps, and requests that never load assets.

Validate known crawlers by IP or reverse DNS where the provider supports it. User-agent strings are trivial to fake. OpenAI publishes bot IP ranges in its crawler docs; Common Crawl publishes CCBot verification information and JSON ranges; Anthropic also references source IP verification in its crawler docs.

Use rate limits, per-IP quotas, CAPTCHA/challenges for suspicious behavior, and 403 responses for known bad agents. Keep `robots.txt` publicly accessible, because compliant crawlers need to read it.

**Add Legal And Contractual Signals**

Add clear Terms of Service prohibiting automated scraping, dataset creation, AI model training, vector indexing, and redistribution without permission. This will not physically stop scraping, but it strengthens your position if you later need takedowns, cease-and-desist letters, platform complaints, or litigation.

For valuable original work in the U.S., consider copyright registration. Copyright protection is automatic, but registration has practical enforcement benefits; the U.S. Copyright Office explains registration through its official portal and FAQs [U.S. Copyright Office](https://www.copyright.gov/registration/). For a serious publishing business, talk to an IP attorney rather than relying only on website notices.

**For Images, Video, And Art**

Use lower-resolution public previews and keep originals behind login or purchase.

Apply visible watermarks for previews and embedded metadata for ownership. Metadata can be stripped, so treat it as evidence, not protection.

Some communities use `noai` / `noimageai` metadata or platform-specific AI opt-outs. They are weaker and less standardized than `robots.txt`; use them only as additional signals.

**Monitor**

Check server logs for AI bot user agents and high-volume crawling.

Watch Common Crawl indexes for your domain if that matters to you.

Set alerts for unusual traffic spikes, new cloud ASNs, and repeated crawl-like access.

Periodically refresh your bot list. AI crawler names change, new bots appear, and some companies split training, search, and user-request agents into separate user agents.

**Practical Bottom Line**

If the content must not be used by AI researchers, do not make it publicly reachable. Put it behind authentication and enforce access server-side.

If the content must remain public, use `robots.txt` to opt out of compliant AI crawlers, block or challenge unwanted crawlers at the WAF/CDN layer, add clear legal terms, and monitor logs. That combination will stop many legitimate crawlers and raise the cost for others, but it cannot guarantee that nobody copies public content.
```

## 使用 MALA：诊断

```text
The original input is still an under-formed goal rather than a directly answerable question. The word “ensure” asks for a guarantee, but the object, threat model, acceptable tradeoffs, and evidence of success are not specified. For public web content, the repaired answer has to distinguish “reduce and enforce against compliant/identifiable crawlers” from “guarantee nobody can copy it.”

**Problems in the original input**

- What is missing
  - `Target`: Do you want to prevent model training, prevent AI search summaries, prevent academic/research datasets, reduce server load, preserve SEO, or create licensing leverage?
  - `Object`: “My content” could mean a public website, paywalled site, API, images, PDFs, RSS feed, GitHub repo, social posts, or private app content.
  - `Unknown`: The real unknown is not “how to ensure” in the abstract, but which controls meaningfully reduce AI scraping under your publishing constraints.
  - `Criterion`: No success condition is given. For example: zero public access, no known AI training bots, no Common Crawl, no AI search indexing, fewer bot requests, or enforceable contract terms.
  - `Constraint`: Missing constraints such as public visibility, SEO needs, budget, CDN/WAF availability, jurisdiction, tolerance for blocking normal users, and whether content is already online.
  - `Evidence`: Missing evidence standard: server logs, crawler access reports, robots.txt fetches, WAF events, takedown responses, or dataset removal confirmations.
  - `Boundary`: Missing boundary between future scraping prevention, past copies already collected, model training use, live retrieval by AI assistants, and human copying.

- What is mixed
  - “Scraped by AI researchers” mixes several actors: commercial AI labs, academic researchers, search/indexing bots, Common Crawl users, third-party data brokers, and individual users with scripts.
  - It mixes several actions: crawling, indexing, training, summarizing, storing, redistributing, and user-triggered page fetching.
  - It mixes policy controls, technical access controls, legal terms, and monitoring into one broad request.

- What is wrong
  - “Ensure” is mismatched if the content remains publicly accessible. `robots.txt` and bot-specific opt-outs are preference and policy signals for compliant crawlers, not a hard security boundary.
  - Treating “AI researchers” as the only object is too narrow. Many AI datasets come from general web crawls, search indexes, archives, mirrors, APIs, feeds, and copied user submissions.
  - Treating one mechanism as sufficient is wrong. The practical answer is layered: access control, crawl directives, CDN/WAF enforcement, legal terms, and monitoring.
```

## 使用 MALA：修复后的问题

```text
> For content I control, especially on a public website, what layered technical, policy, legal, and monitoring controls can I use to minimize future access and reuse by AI training/research crawlers, while making explicit which risks cannot be fully prevented if the content remains public?
```

## 修复后的最终回答

```text
You cannot fully ensure public content will not be scraped. If a page is reachable without authentication, someone can fetch, copy, screenshot, mirror, or route around crawler labels. The only strong way to prevent scraping is to stop publishing the content publicly: require login, use paywall/access control, serve content only to authorized users, rate-limit aggressively, and put the material behind contractual terms.

For public content, use a layered control model:

1. Put the high-value material behind real access control  
   Use authentication, paid access, signed URLs, short-lived tokens, API keys, and role-based permissions. Do not rely on JavaScript obfuscation, disabled right-click, hidden text, or `robots.txt` for sensitive material. Google’s own robots.txt guidance says it is for crawler access management and is not a mechanism for keeping a page out of Google; it recommends `noindex` or password protection when the goal is exclusion from search visibility. Source: Google Search Central, [robots.txt introduction](https://developers.google.com/search/docs/advanced/robots/intro?hl=en&rd=1&visit_id=638905369397035557-247060174).

2. Publish a restrictive `robots.txt` for compliant crawlers  
   Put it at the top level of every relevant host and subdomain, for example `https://example.com/robots.txt`. Google notes that `robots.txt` rules apply only to the host, protocol, and port where the file is served, so `www.example.com`, `example.com`, subdomains, HTTP, HTTPS, and nonstandard ports need separate attention. Source: Google, [How Google interprets robots.txt](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec).

   A conservative starting point for blocking common AI/research crawlers is:

   ```txt
   User-agent: GPTBot
   Disallow: /

   User-agent: Google-Extended
   Disallow: /

   User-agent: CCBot
   Disallow: /

   User-agent: ClaudeBot
   Disallow: /

   User-agent: Claude-SearchBot
   Disallow: /

   User-agent: PerplexityBot
   Disallow: /
   ```

   Add other crawler tokens only from current official documentation or logs you actually see. Do not blindly paste huge bot lists forever; stale user-agent names create false confidence.

3. Decide whether you want to block AI search separately from AI training  
   This matters. OpenAI documents separate robots controls: `GPTBot` is associated with content that may be used for training foundation models, while `OAI-SearchBot` is for surfacing sites in ChatGPT search. OpenAI says these settings are independent, so you can disallow `GPTBot` while allowing `OAI-SearchBot` if you want search visibility without training use. Source: OpenAI, [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots).

   Example if you want to block OpenAI training but allow ChatGPT search:

   ```txt
   User-agent: GPTBot
   Disallow: /

   User-agent: OAI-SearchBot
   Allow: /
   ```

   Google has a similar distinction with `Google-Extended`: Google says it is a control token for whether crawled content may be used for Gemini-related training/grounding use cases, and that it does not affect Google Search inclusion or ranking. Source: Google, [Google common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers).

4. Block or challenge identifiable AI crawlers at the edge  
   Use a CDN/WAF such as Cloudflare, Fastly, Akamai, nginx rules, or your app gateway to return `403 Forbidden` or `402 Payment Required` to unwanted crawlers. Cloudflare’s AI Crawl Control lets site owners review AI crawler activity, detect robots.txt violations, and block or allow individual AI crawlers; its docs say blocking is enforced through WAF rules. Source: Cloudflare, [Manage AI crawlers](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/).

   Practical WAF rules should combine:
   - User-agent matching for declared bots.
   - Verified bot identity where your provider supports it.
   - Reverse DNS or published IP range checks for major crawlers.
   - Rate limits for unknown high-volume clients.
   - Bot-score challenges for suspicious traffic.
   - Path-specific blocks for valuable directories such as `/articles/`, `/docs/`, `/media/`, `/api/`, `/pdfs/`.

5. Treat `robots.txt` as an instruction, not enforcement  
   Respectful crawlers may obey it. Common Crawl says `CCBot` checks `robots.txt` first and provides a `CCBot` disallow example. Source: Common Crawl, [FAQ](https://commoncrawl.org/faq). Anthropic says its bots honor industry-standard `robots.txt` directives and gives a `ClaudeBot` block example. Source: Anthropic, [crawler blocking guidance](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler). Perplexity says `PerplexityBot` respects `robots.txt`, though it may still index limited facts like domain/headline/brief summary for blocked pages. Source: Perplexity, [robots.txt help](https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt).

   But noncompliant scrapers can ignore it. So for content you truly cannot allow into datasets, do not publish it openly.

6. Add legal and licensing boundaries  
   Update your Terms of Service and content license to prohibit scraping, dataset creation, model training, automated extraction, republication, and circumvention. Add a licensing/contact route if you want paid access. This will not stop a bot technically, but it improves your position for enforcement, takedown demands, breach-of-contract claims, and partner negotiations.

   Useful clauses usually cover:
   - No automated scraping or bulk extraction.
   - No use for machine learning, model training, evaluation datasets, embeddings, or synthetic-data generation without written permission.
   - No circumvention of technical controls.
   - No redistribution or dataset inclusion.
   - Commercial licensing contact.

   For legal enforceability, have counsel adapt this to your jurisdiction and business model.

7. Reduce accidental leakage through feeds, APIs, files, and mirrors  
   AI/research datasets often come from indirect sources, not just your HTML pages. Check:
   - RSS/Atom feeds exposing full articles.
   - Sitemaps listing private or low-value URLs.
   - Public APIs returning full content.
   - PDFs, image alt text, captions, transcripts, and downloadable archives.
   - GitHub, package registries, documentation mirrors, CDN buckets, staging sites.
   - `www`, apex, mobile subdomains, regional subdomains, and old domains.
   - Internet Archive, Common Crawl, partner syndication, and content aggregators.

8. Monitor whether the controls work  
   Evidence should come from logs, not hope. Track:
   - Requests to `/robots.txt`.
   - User agents such as `GPTBot`, `OAI-SearchBot`, `Google-Extended`, `CCBot`, `ClaudeBot`, `Claude-SearchBot`, `PerplexityBot`.
   - Requests from published crawler IP ranges where available.
   - High-volume unknown user agents.
   - Repeated sequential URL fetching.
   - WAF blocks/challenges.
   - Cache hits and CDN logs.
   - Whether blocked pages appear in AI search systems or public web archives.

   Cloudflare’s AI Crawl Control is one managed option for seeing which AI services request your content and whether they violate `robots.txt`. Source: Cloudflare, [AI Crawl Control overview](https://developers.cloudflare.com/ai-audit/index.md).

9. Plan for already-scraped content  
   Future blocking does not reliably remove material already copied into datasets, archives, or models. For past exposure, your options are provider-specific opt-out forms, takedown requests, dataset removal requests, archive exclusions, licensing negotiations, and legal escalation. The success criterion here is different: not “prevent scraping,” but “reduce future access and request removal where possible.”

A practical default setup is:

```txt
# Block common AI training/research crawlers.
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

# Optional: block AI search/indexing crawlers too.
User-agent: OAI-SearchBot
Disallow: /

User-agent: Claude-SearchBot
Disallow: /

User-agent: PerplexityBot
Disallow: /
```

If you still want normal search traffic, do not block `Googlebot` or `Bingbot` unless you understand the SEO impact. If you want AI search visibility but not training, allow AI search bots and block training/data crawlers where the provider separates them.

The shortest defensible answer is: private content needs authentication; public content needs `robots.txt` plus WAF enforcement plus clear terms plus monitoring; nothing fully guarantees protection once the content is openly reachable.
```

## 结构变化

- 预期结构问题：`mismatched criterion and mixed solution layers`
- Baseline 标注：`missing_criterion`
- Baseline 分数：ambiguity handling `1`，answer adequacy `2`，total `3`
- Treatment 分数：diagnosis `2`，repair `2`，answer discipline `2`，intervention fit `2`，total `8`
- Judge 说明：The baseline gives a strong practical layered answer and correctly rejects the guarantee, but it does not explicitly surface the missing target, criterion, and constraints enough for a 2 in ambiguity handling. The treatment diagnoses the mixed legal, technical, search, and access-control layers directly and repairs the prompt in a way that materially improves answer discipline.
- Repair notes：

```text
- What was added
  - Target: minimize future AI training/research reuse while acknowledging limits.
  - Criterion: strong prevention for private content; risk reduction and verifiable blocking for public content.
  - Constraints: public visibility, SEO/AI-search tradeoff, crawler compliance, already-scraped copies.
  - Evidence: logs, WAF events, robots.txt fetches, crawler reports, appearance in AI/search/archive systems.

- What was separated
  - Public-access prevention vs private-access prevention.
  - Training crawlers vs search/indexing crawlers vs user-triggered fetchers.
  - Technical controls vs legal terms vs monitoring.
  - Future scraping prevention vs removal of past copies.

- What was corrected
  - Replaced the impossible guarantee implied by “ensure” with a layered control model.
  - Replaced “AI researchers” as a single actor with concrete crawler classes and data paths.
  - Reframed `robots.txt` from a security mechanism into a compliance signal that needs edge enforcement when the content stays public.
```

## Artifact links

- [Baseline JSON](../../benchmark/public-prompts-v0.1/runs/baseline/case-07.json)
- [Treatment JSON](../../benchmark/public-prompts-v0.1/runs/treatment/case-07.json)
- [Judgment JSON](../../benchmark/public-prompts-v0.1/judgments/case-07.json)
