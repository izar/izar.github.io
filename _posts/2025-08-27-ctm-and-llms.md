---
layout: post
title: CTM and LLMs - Hitting the Wall (In a Good Way)
author: Izar Tarandach
---

<figure><img alt="" src="/assets/img/tennis.png" /></figure>

August 27th, 2025

(disclaimer: AI was used to review and improve this article. AI also drew the banner.)

**CTM and LLMs: Hitting the Wall (In a Good Way)**

Remember Continuous Threat Modeling ([CTM](https://github.com/izar/continuous-threat-modeling))? It’s the methodology that says threat modeling doesn’t have to live in a separate ritual or a spreadsheet that fossilizes the day it’s created. Instead, **every** story is an opportunity to ask “what could go wrong?”, keeping the process lightweight, integrated into daily work, and owned by the people building the system, not just the security folks.

Now, remember how threat modeling is a **team sport** (check the Threat Modeling Manifesto if you forgot\!) ? Using LLMs in CTM is a bit like hitting tennis balls against a wall. You’re playing alone, but suddenly there’s something bouncing the ball back at you. It’s not the same as playing with a partner, but it forces you to react, analyze your shots, and experience angles you wouldn’t on your own just shooting balls into the court. The wall is, in some sense, a partner, with just enough knowledge to keep you learning.

That’s how I think about folding LLMs into CTM. They don’t replace the practice, and they’re not your team. They’re the wall: reflecting, prodding, occasionally unpredictable, and if you use them wisely, making you better at what you’re already trying to do.

So, going back to CTM, what you’re looking for in LLMs is that extra boost of security knowledge. The perennial question, “what would an attacker do” gets replaced in CTM by “does this story have a security value” and “how can this fail from a security point of view”. It also aims to plug those gaps using a principles-first approach via a if-this-then-that checklist for the developer. 

So for example you might give the LLM a user story and ask: “Does anything here smell like a security issue?” If the model replies, “This touches authentication” or “Possible data exposure here,” you’ve already saved yourself from scanning a pile of low-risk backlog items. (And really, who has the energy to label *every* story by hand?). Let’s see how it works (ChatGPT 5.0), prompt and answer:

| Taking into consideration the table you can find at https://github.com/izar/continuous-threat-modeling/blob/master/Secure\_Developer\_Checklist.md, given this user story, does it have a security value? ‘As a user I would like to be able to add, view and remove an item to the existing list.’ü
| :---- |
| The user story is: “As a user I would like to be able to add, view and remove an item to the existing list.” If we look at the [Secure Developer Checklist](https://github.com/izar/continuous-threat-modeling/blob/master/Secure_Developer_Checklist.md), it highlights areas such as **input validation, authentication, authorization, data integrity, logging, and error handling**. **Does the story have inherent *security value*?** By itself, no — this is a plain CRUD (Create, Read, Delete) feature request. It describes *what* the user wants to do, but it doesn’t raise any security-specific concern. **Where could security implications sneak in?** The moment you cross-reference the checklist, some things jump out: **Authorization**: Who is allowed to add, view, or remove items? Should all users see each other’s lists, or only their own?ª*Input handling**: What can “an item” contain? Is it just text? Could someone inject markup, scripts, or unexpected payloads?ª*Data integrity**: How do you ensure items aren’t tampered with?ª*Logging/auditability**: Do you log who added or removed items?ª*Error handling**: What happens if an unauthorized action is attempted? |

They’re also good at helping seed your brainstorming. For example (Gemini 2.5 Flash):

| *Given this user story, what could go wrong? ‘As a user I would like to be able to add, view and remove an item to the existing list.’*  |
| :---- |
| *Several things could go wrong with that user story, especially from an application security and secure design perspective. Here's a breakdown: **Confidentiality Issues**  **Unauthorized Access to Lists:** Without proper authentication and authorization, a user could view, add, or remove items from a list that doesn't belong to them. This is a classic access control issue. For instance, if the list is identified by a simple number in the URL (e.g., `app.com/list/123`), an attacker could try changing the number to access someone else's list. **Data Leakage:** The application could reveal sensitive information about a user's items or the list itself (e.g., who owns it, when it was created) to an unauthorized party. **Integrity Issues**  **Unauthorized Modification:** A malicious user could tamper with another user's list. This could include adding fraudulent items, deleting all items, or modifying existing ones in a way that corrupts the data. **Input Validation Flaws:** The application might not properly validate the data being added to the list. An attacker could inject malicious scripts (**Cross-Site Scripting (XSS)**) or SQL commands (**SQL Injection**) into an item's description or name, which could then execute when another user views the list. **Availability Issues**  **Denial of Service (DoS):** An attacker could abuse the "add" feature to overload the system. For example, they could repeatedly add a massive number of items to a list or create numerous new lists, consuming server resources and making the application slow or unavailable for legitimate users. **Accidental Deletion:** The "remove" feature might not have a confirmation step, leading to a user accidentally deleting an important item or their entire list with a single click.*  |

The model will spit out injection risks, and access violations. But not, “unprompted”, predictable identifiers, for example. That’s a bit more “advanced” than the obvious hanging fruit. The value isn’t in perfect accuracy—it’s in nudging you to consider angles you might have skipped. Think of it less as an expert review and more as that friend who always asks awkward questions at the worst time (I’m sorry\!).

Another aspect is clarity in communication. What is obvious today will be hermetic 6 months down the road. Anyone who’s had to reconcile five different ways of describing the same risk knows the pain. LLMs can normalize the language of tickets or notes, so folding findings back into the master threat model doesn’t feel like herding cats. (Threat modeling should be about *threats*, not deciphering your teammate’s leet speak.)

But probably where the biggest value resides is in answering “what will we do about it?” by first answering “what can we do about it?”.  Developers don’t need to pause the sprint for “Security 101.” Instead, the LLM can explain *why* something matters. Just-in-time education, without the detour. Handy—because no one is voluntarily signing up for another brown-bag session:

(Gemini 2.5 Flash):

| wait what do you mean an attacker can inject malicious scripts or SQL commands ? |
| :---- |
| Malicious scripts and SQL commands are pieces of code that an attacker injects into a web application through user input fields. Instead of the data being treated as plain text, the application executes it as code, which can have devastating consequences. **SQL Injection (SQLi)** This attack targets the **database**. Many applications use user input (like a username or a search term) to build a database query. A vulnerable application might create a query by simply combining strings. For example, a login query might look like this: `SELECT * FROM users WHERE username = 'user_input' AND password = 'password_input'` An attacker could enter `' OR 1=1; --` into the username field. The database query then becomes: `SELECT * FROM users WHERE username = '' OR 1=1; --' AND password = '...'` Because `1=1` is always true, the database returns all user records. The `--` is a SQL comment, so the rest of the original query is ignored. The attacker has just bypassed the login. They could also use similar techniques to delete entire tables or steal all the data. \[...\] |

---

## 

But as useful and as nice as these models can be, don’t go home thinking that all your problems are thus easily solved. Don’t go dumping the whole repo into a prompt (but hey feel free to build knowledge graphs and RAGs and base your answers on those. Context is king\!). Apart from obvious data-safety issues, CTM is story-focused, so keep the context small. (Also, no one wants to explain to Legal why your production secrets are floating around in model context data. Not that they should be in the repo to start with, but sometimes things happen. I’m looking at you, Carl. Dammit Carl.). If you need to enrich it by explaining that Medasus is the internal recipe databases and CherryPicker is the secrets management system, you can always add that at the prompt. Don’t feel like you need a wiki MCP here or anything.

**Don’t let the model file threats on autopilot**. That’s just vibe threat modeling, and it ages badly.

Don’t mistake confidence for accuracy. A model will always have an answer; it will speak confidently of things that are matters of opinion, and that doesn’t mean it’s useful (now stop thinking about your Uncle Carl. He is entitled to his opinions).

**Wrapping Up**

CTM works because it spreads security thinking into the fabric of development without slowing everything down. LLMs fit into that rhythm when you treat them as a wall to practice against: reflecting back questions, catching weak spots, keeping you sharp.

But they’re not your doubles partner. They don’t own the system, they don’t make the decisions, and they definitely don’t replace the responsibility. That’s still yours. (If you hand that over to an LLM, you might as well let it write your compliance items too—actually, don’t get any ideas.)

CTM is fast by definition. LLMs make it faster and more accessible by reducing the reliance on checklists and adding a partner where there might be none. But remember, LLMs know what all of us know but cannot imagine what none of us can. They will not divine new threats just because you showed them a story and asked “what”. That kind of higher level modeling and thinking is still on you. 

