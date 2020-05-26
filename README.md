# CS300Project
Project summary
After some research it became apparent that students at Calvin University who lived on campus (in the dorms or KE apartments) had no way to determine if their housemates/roommates were in the bathroom or not. In order to avoid being walked in on, some students resort to running the tap/shower to provide auditory feedback of their presence in the bathroom. While effective this leads to gallons of water being wasted each day.

The solution, a simple in-obtrusive system of sensors that adequately detects the presence of a person in the bathroom & discreetly displays this occupancy to webserver and updates a website for remote information access.

Social, security, or privacy issues
Stewardship
The primary social motivation was that of the design norm Stewardship. As stated in the problem definition the old method of determining the presence of someone in the bathroom led to gallons of daily water wastage. We as students were being terrible stewards of our water resources, and this project was aimed at mitigating that wastage.
Privacy
Privacy was of paramount concern in the design of the Occupod project. It was of paramount importance that none of the sensing systems developed be obtrusive in any way as such no audio and video feeds or image sensing was used in the creation of this project. 
Security
Another aspect of the project was security. It was decided that connecting the obtained sensor data to a secure google sheet was the best way of implementing the security for this project for the following reasons: 1. Low probability of server side attacks. The only way to intercept the data is with the unique json value that allows the python program to interface with the google sheet. 2. Google's user authentication system on the user side added an extra layer of security.



Fritzing Diagram: ![alt text](https://github.com/Mawuay/CS300Project/blob/master/Images/Occupod_diagram.png)

A fritzing diagram of the hardware and a photo of the finished prototype.


Completed Prototype: ![alt text](https://github.com/Mawuay/CS300Project/blob/master/Images/Occupod.jpg)


Reflection:
Overall this was a very enjoyable project. As the final project for the class I was encouraged to use a wide variety of the techniques that we had learned throughout the course in order to complete my project. In addition having the project open ended in the sense where students were allowed to use different property hardware drew me back to one of the preliminary lectures we had about determining the best hardware for the project. In an ideal world I might have done some things differently with regards to parts and functionality, but due to the current teaching and learning paradigm we are in I had to devise cleaver alternatives. On a whole I believe this was an amazingly well instructed class.
