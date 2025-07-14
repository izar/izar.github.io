---
layout: post
title: Vibe Coding an the rise of PR-Fatigue
author: Izar Tarandach
---

<figure><img alt="" src="/assets/img/merge.png" /></figure>

July 14, 2025

(disclaimer: AI was used to review and improve this article, as well as some helpful humans. AI also drew the banner, because I don't know any humans willing to do that for my writings.)

**Vibe Coding and the rise of PR-Fatigue**

Vibe Coding (interestingly enough…”VC”) is the next big thing, and also the current thing. Code is arriving faster and easeir, it looks convincingly good, it seems to work... but underneath? It's a mess of vibes.

Thanks to AI copilots and coding agents, we're no longer spending a crazy amount of time  writing code from scratch. Instead, we’re reading code, lots and lots of it. But here’s a revelation: reading code is *harder* than writing code. That’s not just a gut feeling. Research shows that understanding existing code requires significantly more cognitive effort than composing new logic (“Reading, Writing, and Code”, Diomidis Spinellis, [https://queue.acm.org/detail.cfm?id=957782](https://queue.acm.org/detail.cfm?id=957782) and “Code Readability in the Age of Large Language Models: An Industrial Case Study from Atlassian”, [https://arxiv.org/abs/2501.11264](https://arxiv.org/abs/2501.11264) among others). I especially like Spinellis explanation, where to him, writing code is a filtering exercise that leads to a definite outcome (the code working) because the choices are narrowing towards the chosen solution, while reading code is an exercise in trying to understand the choices of someone else where these choices keep multiplying. 

Now we’re doing all this reading in chunks of systems, as pull requests (PRs), which are our main vehicle for collaboration, scrutiny, and, increasingly, exhaustion. As vibe-coded PRs pile up, sometimes faster than you can say “auto-merge”, developers are beginning to experience a new version of alert fatigue. 

“Those who cannot remember the past are condemned to repeat it” (George Santayana) aaaaand here he goes recycling that old one, right? And you’d be right. But I think I am right too. 

In Security, we've seen what happens when tools fire off too many alerts. People stop caring. Click-through becomes the default (“‘Security Fatigue’ Can Cause Computer Users to Feel Hopeless and Act Recklessly, New Study Suggests“ [https://www.nist.gov/news-events/news/2016/10/security-fatigue-can-cause-computer-users-feel-hopeless-and-act-recklessly](https://www.nist.gov/news-events/news/2016/10/security-fatigue-can-cause-computer-users-feel-hopeless-and-act-recklessly)). The study is from 2016, but it could have been written today, and while it focuses on password management, it can be easily translated other areas of Security: “Participants expressed a sense of resignation, loss of control, fatalism, risk minimization, and decision avoidance, all characteristics of security fatigue. The authors found that the security fatigue users experience contributes to their cost-benefit analyses in how to incorporate security practices and reinforces their ideas of lack of benefit for following security advice”.

I have the feeling that this will happen to development as well. PRs that "look ok" will get rubber-clicked with minimal scrutiny, not because reviewers are lazy, but because they’re overwhelmed, and reading code is hard.

But the cost is very real. PR fatigue will create mounting technical debt, and worse, security debt. A few unclear lines might not seem like a big deal now, but stack up enough of them and you’ve built a brittle, unmaintainable Frankenstein monster of a system. That’s your future outage—or breach—just waiting for a Friday (5pm, not the 13th) to come by.

Debt compounds. The faster you ship vibe-coded changes without careful review, the higher the interest. And like any bad loan, the payment comes due when you least expect (or want) it.

We will trust more and more machine-written code. Which means less reading, less understanding, less building of mental models of how these systems click together. When code fails, we’ll fix it with more machine-written code, leading to less understanding of the fix and its trade-offs or failings. And over time we will become over-confident, tired, or simply realize we don’t know enough to fairly judge the proposed fix…and just click through it. 

This isn’t a “get off my lawn” rant against AI-assisted development. Vibe coding *can* free us from boilerplate and let us focus on the fun and important stuff: threat modeling, reasoning, real innovation. But only if we rebuild our habits around code review:

* Start by taking the time to REALLY understand the vibe-coded code. Kill the “looks good, ship it” temptation  
* Review AI-generated code as a main task, not a janitorial activity  
* Use robust guardrails, like the “rules” capability (.cursorrules, .windsurfrules, etc.)  for quality and security  
* Demand clarity: understandability should be a requirement, not a bonus  
* Document, document, document. Make understanding out of context PRs easier by supplying meta-knowledge: data dictionaries, access rules, limitations and restrictions, edge cases.

Vibing is fine. But let’s not vibe-read before we vibe-approve.

