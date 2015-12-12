{% extends "base.html" %}


{% load staticfiles %}


{% block title %}{{ title }}{% endblock title %}


{% block active_students %}active{% endblock active_students %}

{% block content %}
  <div class="container theme-showcase" role="main">

        {% if messages %}
            {% for message in messages %}
            <p>{{ message }}</p>
            {% endfor %}
        {% endif %}

    <h2>{{name_form}}</h2>
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="{{name_button}}" class="btn btn-primary"/>
      </form>
  </div>
{% endblock content %}
