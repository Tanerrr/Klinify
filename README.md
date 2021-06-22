# **Klinify**

## **Introduction**

This project has been realized as a graduation project within the scope of Refugeeks project. Refugeeks is a training program organized by Hochschule Hannover, which aims to train IT experts in the field of Web technologies and Data science as a result of 9 months of theoretical training including a graduation project. Within the scope of the program, the lectures were given by professors and professional staff who are experts in their field between June 2020 - March 2021 in Hochschule Hannover.

This project, Klinify,  the information of which is given below as a graduation project at the end of the training, has been realized. Klinify was completed in 4 weeks as 2 sprints, each lasting 2 weeks. During the project, scrum methodology and philosophy were applied, and daily review, sprint review, sprint retro-respective meetings were held. Git, Github, Jira and Scrum were used in project management.

## **Goal**

Within the scope of the Klinify project, it was aimed to re-evaluate the rating and reviews of some hospitals in Niedersachsen with our own algorithms. In this context, the relevant data were scraped from the internet, machine learning methods were used, and the new data obtained by re-evaluation of the data was presented on a web page. The relevant data are taken from maps.google.com and Klinikbewertungen.de.


## **Technology and Method**

1. Scraping of Data

At the first web scraping method has been used to obtain the data. This data was taken with Selenium, BeautifulSoup, and Google Chrome web driver.

2. Data Science Phase

Second step the obtained data was cleaned using Python, Jupyter notebook, and  Pandas, Numpy libraries, and converted to JSON format for inserting to the database.
Sentiment analysis is used as machine learning. In order to better analyze the German comments, the data with the textblob library, which is a special library for german, were analyzed. In order to obtain a project-specific hospital score from the scraped data, scores were clustered by including the number of comments. 
Appropriate calculations were made on the new data obtained, and the data was brought to the latest state to be presented on the web application and converted into JSON format.

3. Web Technology Phase

The first step as the web technology phase, draft drawings were made for the web application, the relevant logo was designed and the information to be given to the user was determined. Then, with Google Firebase technology as a backend, the data was stored in the cloud (Cloudfirestore) and transferred to the github.io web application as JSON data. It has been deployed as github pages using React, the javascript library, as the frontent.


## **Result**

The project has reached its goals and has been published as a web application. With this project, users were able to compare the scores obtained from patient comments about hospitals in the state of Niedersachsen.
As a team, we have increased our working skills with scrum methodology, application of machine learning algorithms, web scrapling operations, frontent and back end technologies. Within the scope of Refugeeks project, we applied the theory and practical knowledge we learned from university professors and expert instructors in web technologies and data science education, which lasted for 9 months, in this project.
