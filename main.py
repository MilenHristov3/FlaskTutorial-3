#https://www.youtube.com/watch?v=4nzI4RKwb5I
""""
In this flask tutorial I will be showing how to add bootstrap to a flask website and how to use something called template inheritance. This is useful as often times you have the same HTML components that you want to show on all or many different web pages. Template inheritance allows you to make a base template that other templates can inherit from.
Text-Based Tutorial: https://techwithtim.net/tutorials/fla...

Bootstrap Website: https://getbootstrap.com/docs/4.3/get...

Nav-Bar Code: https://getbootstrap.com/docs/4.3/com...

Playlist:

 • Flask Tutorial #1 - How to Make Websi...

◾◾◾◾◾
💻 Enroll in The Fundamentals of Programming w/ Python
https://tech-with-tim.teachable.com/p...

📸 Instagram:

 / tech_with_tim
🌎 Website https://techwithtim.net
📱 Twitter:

 / techwithtimm
⭐ Discord:

 / discord
📝 LinkedIn:

 / tim-rusci.  .
📂 GitHub: https://github.com/techwithtim
🔊 Podcast: https://anchor.fm/tech-with-tim

💵 One-Time Donations: https://www.paypal.com/donate/?token=...
💰 Patreon:

 / techwithtim
◾◾◾◾◾◾

⚡ Please leave a LIKE and SUBSCRIBE for more content! ⚡


Tags:
- Tech With Tim
- Python Tutorials
- Flask Add Bootstrap
- Add Bootstrap Flask
- Template Inheritance

#Python #Flask #Bootstrap

"""

from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug =True) # allow to not have re-run the server any time when we make changes
