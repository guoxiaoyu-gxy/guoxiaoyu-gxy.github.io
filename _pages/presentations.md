---
layout: page
title: Presentations
permalink: /presentations/
nav: true
nav_order: 3
---

Conference presentations and recordings. You can also browse [my speaker profile on Underline](https://underline.io/speakers/39884-xiaoyu-guo). Some recordings may require an Underline account or institutional access.

<div class="presentations">
{% assign presentations = site.data.presentations | sort: 'year' | reverse %}
{% for presentation in presentations %}
  <section class="presentation">
    <h2>{{ presentation.title }}</h2>
    <p class="presentation-venue">{{ presentation.venue }}</p>
    <div class="presentation-links">
      {% for recording in presentation.recordings %}
      <a class="btn btn-sm z-depth-0" href="{{ recording.url }}" target="_blank" rel="noopener noreferrer" aria-label="{{ recording.label }}: {{ presentation.title | escape }}">{{ recording.label }}</a>
      {% endfor %}
      <a class="btn btn-sm z-depth-0" href="{{ presentation.paper }}" target="_blank" rel="noopener noreferrer" aria-label="Paper: {{ presentation.title | escape }}">Paper</a>
      {% if presentation.slides %}
      <a class="btn btn-sm z-depth-0" href="{{ presentation.slides }}" target="_blank" rel="noopener noreferrer" aria-label="Slides: {{ presentation.title | escape }}">Slides</a>
      {% endif %}
    </div>
  </section>
{% endfor %}
</div>
