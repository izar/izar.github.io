---
layout: default
---

{% seo %}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": "Threat Modeling: A Practical Guide for Development Teams",
  "isbn": "9781492056553",
  "author": [
    { "@type": "Person", "name": "Izar Tarandach" },
    { "@type": "Person", "name": "Matthew J. Coles" }
  ],
  "publisher": { "@type": "Organization", "name": "O'Reilly Media" },
  "image": "{{ "/cover.jpg" | absolute_url }}",
  "sameAs": [
    "https://www.amazon.com/Threat-Modeling-Identification-Avoidance-Secure/dp/1492056553/",
    "https://www.barnesandnoble.com/w/threat-modeling-izar-tarandach/1137728005?ean=9781492056553"
  ]
}
</script>

Threat modeling is how development teams find out what can go wrong with a system before an attacker does, and decide what to do about it. This site is the companion to our book on the subject, and a place where we keep writing about threat modeling practice, tools, and its collision with AI and LLMs.

Did you ever ask yourself what threat modeling is, how it can help you bake security into your system, and what your role as a development team member is in the whole process?

If so, <a href="https://www.amazon.com/Threat-Modeling-Identification-Avoidance-Secure/dp/1492056553/ref=sr_1_1?dchild=1&keywords=tarandach&sr=8-1">this</a> is the book for you. Available at <a href="https://www.amazon.com/Threat-Modeling-Identification-Avoidance-Secure/dp/1492056553/ref=sr_1_1?dchild=1&keywords=tarandach&qid=1605115844&sr=8-1">Amazon</a>, <a href="https://www.barnesandnoble.com/w/threat-modeling-izar-tarandach/1137728005?ean=9781492056553">Barnes&Noble</a> and other book sellers.

### Other sources of threat modeling wisdom:

* Check out the <a href="https://www.threatmodelingmanifesto.org/">Threat Modeling Manifesto</a>.
* These extensive lists of resources:

  * https://github.com/arnepadmos/threats
  * https://github.com/hysnsec/awesome-threat-modelling
* The #threat-modeling channel at the [OWASP Slack](https://owasp.org/slack/invite)
* [ThreatModelingConnect](https://www.threatmodelingconnect.com), the community for threat modeling!
* https://github.com/OWASP/pytm
* https://github.com/izar/continuous-threat-modeling
* https://shostack.org/blog
* https://www.toreon.com/tmi-threat-modeling/

{% if site.posts.size != 0 %}

<h3 id="writings">We also have some of our ongoing writings here:</h3>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <br><small>{{ post.date | date: "%b %-d, %Y" }}</small>
      {% if post.description %}
        <br>{{ post.description }}
      {% endif %}
    </li>
  {% endfor %}
</ul>

{% endif %}
