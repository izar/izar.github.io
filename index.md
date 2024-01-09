---
layout: default
---

{% seo %}

## Available December 2020

Did you ever ask yourself what is Threat Modeling, how can it help you bake security into your system, and what is your role as a development team member in the whole process?

If so, <a href="https://www.amazon.com/Threat-Modeling-Identification-Avoidance-Secure/dp/1492056553/ref=sr_1_1?dchild=1&keywords=tarandach&sr=8-1">this</a> is the book for you.

{% if site.posts.size != 0 %}

We also have some of our ongoing writings here:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

{% endif %}


Available at <a href="https://www.amazon.com/Threat-Modeling-Identification-Avoidance-Secure/dp/1492056553/ref=sr_1_1?dchild=1&keywords=tarandach&qid=1605115844&sr=8-1">Amazon</a>, <a href="https://www.barnesandnoble.com/w/threat-modeling-izar-tarandach/1137728005?ean=9781492056553">Barnes&Noble</a> and other book sellers.


You should also check out the <a href="https://www.threatmodelingmanifesto.org/">Threat Modeling Manifesto</a>.
