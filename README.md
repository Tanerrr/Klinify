# **Klinify**

This project has been prepared as a graduation project within the scope of Refugeeks project. Refugeeks is a training program organized by Hochschule Hannover, which aims to train participants in the field of Web technologies and Data science after 9 months of theoretical training and 3 months of practical training as IT experts . Within the scope of the program, between June 2020 - March 2021, lectures were given by university lecturers and professional staff who are experts in their field in Hochschule Hanover. This project, which is given below as a graduation project at the end of the training, has been realized.

## **Goal**
The Klinify project is a project of collecting data from the internet, re-scoring by using machine learning methods, and presenting the new data obtained to the user via a web service. The relevant data are taken from the websites googlemaps and Klinikbewertungen.de.

## **Technology Used**
Sentiment analysis is used as machine learning. In order to better analyze the German comments, the data collected using the textblob library were analyzed.
As a web service react and  abc Used.

## **Method**
The studied data was first scraped from the web pages related to the selenium google web driver.
The obtained data was cleared and converted to the relevant format with Pyhton and its Pandas, Numpy libraries via juniper notebook.
Sentiment analysis was performed on the obtained data and new scores were obtained.
Appropriate calculations are made on the new data obtained, and the data is brought to the latest state to be presented on the web service and converted into the relevant data format.
Draft drawings were made for the web service, the relevant logo was designed and the information to be given to the user was determined.
The draft was carried out using React.
The data were converted to json format and kept in the cloud using back-end technology and brought to the query screen.

## **Challenges**
Data formats are not compatible with each other on web pages used as a source. Inconsistencies between Googlemaps comments and Klinikbeweetungen.de comments posed difficulties in data clearing and formatting.
The absence of a widespread library of sentiment analysis for the German language made it difficult to work with other libraries and compare data.

## **Result**
Using Scrum methodology, this project was completed in 2 sprints with the help of git version system on github and jira project management software. During the project, it was adhered to the scrum methodology and philosophy, and all relevant meetings were held.
