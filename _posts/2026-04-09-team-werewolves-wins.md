---
layout: post
title: Team Werewolves Wins!
author: Izar Tarandach
---

<figure><img alt="" src="/assets/img/werewolves.png" /></figure>

April 9, 2026

# Team Werewolves Wins\!

Supposedly, silver bullets kill werewolves. And for some time now, people have been declaring that AI is the silver bullet against depending on expertise, on discussion, on exploration and creativity,  things that are inherently human. The werewolves, those threat modelers running around your system's design asking uncomfortable questions, are apparently about to go away. No more being scared of the full moon, unless it coincides with a big release day.

Spoiler: the werewolves will be fine. Silver bullet deflected. Threat modeling as a discipline is not going away.

What *is* struggling is the idea that we could just... hand the whole messy, creative, deeply human process of thinking adversarially about a system to an AI model and walk away. That the werewolves were the problem all along, and now we've solved them.

We haven't. Here's why.

## Garbage In, Garbage Out

Before we ask whether AI can find threats in your system, let's ask a more uncomfortable question: does AI actually know what your system *is*?

Petra Vukmirovic, in her great piece ["What You Feed the Model Is the Model"](https://www.devarmor.com/blog/what-you-feed-the-model-is-the-model) (and it isn’t great just because it cites Kim, Matt and myself, I swear\!), makes the point with surgical (\#iykyk) precision: an LLM presented with incomplete or conflicting input doesn't stop and ask for clarification. It fills the gaps, synthesizes something that sounds coherent, then it hands you a threat model that describes a system that is *close to yours but not yours*. Exactly the kind of threat model that gives you false confidence at the worst possible moment.

Petra is right that structured, precise input produces better output. But she's describing a best-case scenario where there *is* good structured input to give. And here's where threat modeling's fundamental timing problem bites us: the only truly authoritative, complete, and accurate representation of a system is its code. And that code doesn't exist yet, if you’re doing threat modeling right.

Threat modeling is supposed to happen at ideation and design time. Before the code. Before the infrastructure. Before anyone has written a single line of anything. What we have at that stage are design documents, artifacts of language, full of good intentions, version conflicts, security promises that may or may not survive contact with implementation, and a generous helping of "we'll figure that out when we get there." We hand this beautifully ambiguous pile to an AI and expect it to tell us what threats we face. And it will. Oh, it absolutely will. Confidently. Specifically. Probably with STRIDE categories.

The question you should be asking is: threats to *what*, exactly?

Now, some will argue that you can feed AI-led threat modeling with artifacts of existing systems  infrastructure-as-code, source code and deployed configurations. But then we need to be honest about what we're doing. If your input is the running system, you're not threat modeling. You're doing automated design review. Which is valuable, but it's a different thing. It happens after the architectural decisions have been made, after the trust boundaries have been laid (or not), after the expensive stuff has been locked in. The window where threat modeling has its highest return of investment, where finding a flaw costs a conversation instead of a rewrite: that window has closed.

So we start with a system description that is, by definition, incomplete. We feed it to a model that will confidently assume what it doesn't know. And we get output that is authoritative about a system that doesn't quite exist. Garbage in, garbage out. Very articulate garbage.

## The Creativity Gap

Here's a question that recently surfaced in the OWASP community's Slack, and it's been sitting in my head: *Has AI quietly broken the Threat Modeling Manifesto?*

The Manifesto, which a group of us put together after a lot of experience, argument and energy drinks, was built around values like *people and collaboration over tools*, and threat modeling as a *journey of understanding*. The person who raised the question put it plainly: AI-assisted threat modeling, as it's being practiced today, quietly undermines both. The tool does the reasoning, and the journey collapses into a prompt.

Matt Coles, who has been thinking about this longer and harder than most, didn't sugarcoat his answer: the rush to AI-ify everything means doing much more, much faster, with fewer hands involved, but along with tooling that either lacks the ability to be introspective or to be collaborative in the way the Manifesto suggests threat modeling should be. The Manifesto, Matt points out, tried to solve a previously human-focused effort. Whether an AI-focused effort could even implement its principles is an open question. Maybe, if agents are instructed to do so, but would it carry the same meaning?

His question, ‘*would it carry the same meaning’* is the one I want to poke at here.

Threat modeling's value is not just in the list of threats it produces. It is in what happens to the people in the room while they produce it. The arguments about trust boundaries. The moment someone from the backend team realizes the payments team has been assuming something that isn't true. The "wait, what does this component actually *do*?" that unravels an assumption baked in six months ago that nobody quite recalls because Carl left the team five months ago without documenting it. These are not inefficiencies to be optimized away. They are the point. The journey of understanding *is* the threat model, not a side quest of it.

Creativity, in this context, is not a nice-to-have. It is the mechanism by which teams discover threats that no checklist contains, because those threats emerge from the *specific, unrepeatable combination* of this team, this system, this set of decisions, this moment. An AI working from a dry system description will find the threats that look like other threats it has seen before. It will apply STRIDE. It will dutifully enumerate injection risks and authentication gaps. It will be thorough and it will be predictable. What it will not do is look at your architecture and say "you know what's weird about this?" because noticing what's weird requires having an intuition about what *secure* looks like, built from years of sitting in rooms with humans arguing about systems.

The Manifesto specifically warns against the hero threat modeler anti-pattern, the single expert who sweeps in, produces a report, and saves the day, leaving a team that understands or cares not about their own system than they did before. Making AI the hero doesn't solve that anti-pattern but solidifies it.

## The Illusion of Consistency

Large language models don't compute or intuit  answers, they predict them. At each step, the model assigns probabilities to possible next tokens and samples from that distribution. There is a parameter, “temperature”, that controls how much randomness is injected into that sampling. Make it zero and the model becomes more deterministic, always picking the highest-probability token. Turn it up and the outputs get more varied, more "creative." Most production systems run somewhere in between, because pure determinism produces stilted, robotic output and pure randomness produces word salad.

The practical consequence for threat modeling is this: run the same prompt against the same system description twice, and you will not get the same list of threats. Some will appear in one run and not the other. Some will be framed differently, with different severity, different mitigations. Note: this is not a stand-in for creativity. It is just probabilistic variation. The low-hanging fruit — the obvious stuff, the things that should always show up — will vary. Not dramatically, not always, but enough to matter. Enough that you cannot treat the output as a stable artifact that a team can build on, track against, or use to demonstrate coverage over time.

But wait, why not put another layer and have an LLM judge the output of a number of rounds of prediction ? You know why. Because non-determinism is inherent to the architecture. It is non-deterministic all the way down to the last turtle.

This would be a manageable problem if the solution were simple. And in a sense it is: you critique the output. You don't blindly accept what the model gives you. You review it, challenge it, filter it. Everyone working seriously with LLMs has arrived at this same conclusion, it is not even controversial at this point.

But here is where the mask slips. To critique an LLM's threat modeling output, you need to know enough about security to recognize what's missing, what's wrong, and what's hallucinated with confidence. You need to understand the threat categories well enough to notice when the model skipped one. You need to know your system well enough to catch the assumptions the model made about it. You need, in other words, exactly the security expertise that AI-led threat modeling was supposed to render unnecessary.

The original problem hasn't been solved. It's been pushed one step to the right. Instead of "we need security expertise to do threat modeling," we now have "we need security expertise to validate the threat modeling our AI did." The werewolves didn't go anywhere. We just gave them a different job title (and no, it isn’t “vampires”).

## So What's AI Actually Good For?

Quite a bit, as it turns out. Just not what the silver bullet crowd is selling.

**The checklist checker.** There is a class of threat that is obvious, well-documented, and reliably identified by anyone who has read the OWASP Top 10 at least once. Injection risks. Missing authentication checks. Predictable identifiers. These are the low-hanging fruit, and they are genuinely low-hanging, they don't require creativity, they don't require deep system knowledge, and they don't require a seasoned threat modeler in the room, only the presence of certain constructs. This is work AI can do well, and it is worth automating, not because it is unimportant, but because it is repeatable and should not be consuming the time of people who can do harder things. Use AI to sweep the floor, just don't confuse sweeping the floor with protecting the building.

**The sounding board.** Here is where AI earns its keep in a way that is genuinely underappreciated. In an ideal world, every development team would have a security expert available whenever a design question comes up. In the actual world, that person is stretched across twelve teams, booked solid, and using stall time to read about the latest technical advances. What AI can do in that gap is help you play security tennis and act as a wall to practice against, not a doubles partner, but something that bounces the ball back, forces you to react, and surfaces angles you might not have considered on your own.

I've written about this at length in the context of Continuous Threat Modeling — [using LLMs in CTM](https://threatmodeling.dev/ctm-and-llms/) as a way to keep security thinking embedded in the daily rhythm of development without requiring a security guru for every user story. The model won't own the system, won't make the decisions, and won't replace the responsibility. But it can ask awkward questions at exactly the right moment, and that has real value.

**The technology deep-dive.** This is perhaps the most underused application. When a team is threat modeling a system built on a technology they don't fully understand, the gap in their threat model isn't creativity. It's knowledge. What are the configuration pitfalls? What does the attack surface look like for this specific implementation? What have other people gotten wrong here? This is reference knowledge, the kind that lives in documentation and post-mortems and CVE databases, and AI is genuinely good at synthesizing it on demand. Not as a replacement for expertise, but as a way to get a team to a baseline of understanding fast enough that their threat modeling conversation is actually about *their* system rather than "wait, how does this thing work again?"

**The AI-infused aspect.** I am going to call it out here because that’s the only place I have seen it actually used and making sense: when Chris Romeo started Devici (now a Security Compass thing), he created a threat modeling tool that used AI as the helping hand. In part like I mention above, in part to bring together formats and inputs and other usually hard to parse and automate “things”. The AI was not the engine, it was the wheels, the transmission, the windshield wipers. AI is great to put you in a repeatable position to being a threat model, to create formally consistent output, to bring order to chaos in a world of disparate artifacts. Use it.

The werewolves, as it turns out, were never the problem. The issue is that we keep looking for a way to not need them — to replace the uncomfortable, slow, creative, deeply human work of thinking adversarially about systems with something faster and cheaper and more scalable. And every few years, something new gets cast as the silver bullet. AI is just the latest candidate.

But the bullet isn't silver. And the werewolves, the threat modelers, the security advocates, the people who sit in your design reviews and ask "have you considered what happens when someone does *this*?" are still very much in the building.

Every time I am confronted with this kind of “challenge”, there comes a clear image of a master werewolf \- experienced, full of battle scars, but really just a big Australian Shepperd with bigger fangs. We don’t need to do away with it. We need to understand its value and his place. Werewolves are not going away. They're just waiting for you to stop trying to shoot them with bullets that will only, ultimately, hurt yourself.  

