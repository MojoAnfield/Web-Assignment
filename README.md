# Web page with Baidu Map API
24 Dec,2016

The final submission is a totally static page without any python programming. It all comes down to html editing.
Here's the [link](https://mojoanfield.github.io/Web-Assignment/Final.html)
--
22 Dec, 2016

Check out this URL and view [web page](https://mojoanfield.github.io/Web-Assignment/build/index.html)
(if you encounter "unsafe scripts" block, do remember to activate this access)

Basically, I created a very very simple web page to visually present ZJU, zijingang Campus. The index page shows a wide view of campus from the map. I marked several my favourite places with pins. Clicking on the pin, a short note pops up; you can then follow the links and find out more for places of your interest.

Inspired by an [IRE tutorial](http://first-news-app.readthedocs.io) , this project is built with Flask microframework in python. To implement, the following are essential for this assignment:

* Sublime Text 3
* Python (I'm using Python 3, and presumably it's also fine with other versions)
* Baidu Map API (an AK key is required)
* Git

First I wrote an app.py to include Flask. Once it's initiated in CLI, the webpage shows up on localhost:5000. There's nothing to present initially, but we'll make it look a bit nicer later.

A very large part of this assignment is associated with html. It may seem very silly - the thing is, I created two html documents *manually*. It's boring. It's dull. It took a lot of time. Strangely enough, somehow I enjoyed it when approaching the end. They are listed as index.html and detail.html. Now you may well ask, it's supposed to be at least 8 html files, isn't it? Here's the trick - earlier I stored all the details(location, coordinates and so forth) in a separate csv file. Since detail pages look pretty much the same, jinja (a language that works with Flask, I assume?) will duplicate the pages automatically for each record.

Just a word on Baidu Map API. Like Google Maps, it's completely free. To use it, you have to go and register at baidu. Once you've done that bit, you'll get unlimited access to Baidu Map API(before that, get a key). It provides a JavaScript interface, so I included it in all my html files.

The final part is a freeze.py to render a whole set of pages using app.py, html templates and info.csv. I don't know for sure what mechanism behind Freezer module is as of yet. Maybe I'll try and figure it out after final exams.


