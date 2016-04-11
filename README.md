# PlanR.

##sol45.pythonanywhere.com

I created 'PlanR' as a simple dynamic website to teach myself basic web development
while also to solving the problem of students not being able to remember their timetable.#
PlanR is a web service that will send you a text each morning of what lessons you have 
that day. 

PlanR is still a work in progress, so far I have:

>• created a web page containing a html form where students can enter their lessons (templates/websiteform.html)
>• used css to style the webpage (static/style.css)
>• used basic javascript to manipulate the form (static/javascript.js)
>• hosted the web page using the flask python app and pythonanywhere.com (hello.py)
>• used python and json to 'GET' the data sent by the form, edit it and then save it to
a file (in the folder 'data').

I still plan to:
>• use python and json to read the data stored in the files
>• use python to send the data to the text message service twilio.com 
>• use twilio to send the text messages containing their lessons to the students

