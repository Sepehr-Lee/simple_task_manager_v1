<h1> simple_task_manager_v1 </h1>

A small and simple CRUD web application "task manager" for coding ability demonstration.
Built using Flask for backend and Sass/HTML5/Jinja for frontend.
The database uses SQLite with SQLAlchemy ORM.

This is my first time coding a real application. Go EZ on me! :))
Followed a guide for the implementation—no AI was used except for visual design suggestions since I'm bad at UI/UX.

Features:

1. Flask Backend: Minimal Python web server for local development
2. Sass Integration: Modern CSS with variables and nesting
3. Auto-Refresh: Live Sass compilation with browser reload
4. Semi-clean Architecture: Organized static/templates structure

Project Structure:
The task manager consists of 4 main parts:

1. App.py - Main Flask application and routing
2. Static folder - CSS, JavaScript, and other assets
3. Templates folder - HTML templates with Jinja2 syntax
4. SQLite database - Created automatically on first use

How It Works:

1. The App.py code acts as a "controller hub" for fetching and displaying different elements based on which webpage the user is currently viewing.
(Note that there are only 2 pages: index.html for the landing/homepage/main screen, and edit.html for task modification.)

2. The HTML pages are designed to inherit their main structure and styling from base.html (the parent template) using Jinja2 templating. This approach allows for efficient page creation and maintenance by:

Backend Design: Implementing the desired user actions (create, read, update, delete) in Python

Frontend Design: Creating HTML files that inherit global elements from the base template

Global Updates: Modifying visual/functional elements in one place without editing each HTML page individually


Installation and use:

    Clone or create the project

    Set up virtual environment

    Install dependencies: pip3 install -r requirements.txt

    VS Code Extensions:

        Sass (.sass only) by syler

        Live Sass Compiler by glenn2223
