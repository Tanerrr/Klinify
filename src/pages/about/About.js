import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Avatar from '@material-ui/core/Avatar';
import Taner from '../../assets/images/taner.jpeg';
import Fatih from '../../assets/images/fatih.jpeg';
import Eftal from '../../assets/images/eftal.jpeg';
import Mehmet from '../../assets/images/mehmet.jpeg';
import "./style.css";


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        '& > *': {
            margin: theme.spacing(2),
        },
    },
    large: {
        width: '12vw',
        height: '12vw',
    }
}));

const About = () => {
    const classes = useStyles();
    return (
        <div id="about">
            <h2>About Us</h2>
            <div className={classes.root}>
                <div class="item">
                    <Avatar className={classes.large} alt="Taner" src={Taner} />
                    <span class="caption">Taner</span>
                </div>
                <div class="item">
                    <Avatar className={classes.large} alt="Fatih" src={Fatih} />
                    <span class="caption">Fatih</span>
                </div>
                <div class="item">
                    <Avatar className={classes.large} alt="Eftal" src={Eftal} />
                    <span class="caption">Eftal</span>
                </div>
                <div class="item">
                    <Avatar className={classes.large} alt="Mehmet" src={Mehmet} />
                    <span class="caption">Mehmet</span>
                </div>







            </div>
            <h2>Klinify Project</h2>
            <p>
                This project has been realized as a <b> graduation project</b> within the scope of Refugeeks project.
                Refugeeks is a program organized by Hochschule Hannover, which aims to train IT experts in the field of Web technologies and Data science as a result of 9 months of theoretical education including a graduation project.
            </p>
            <p>
                The lectures of program were given by professors and professional staff who are experts in their field between June 2020 - March 2021 in Hochschule Hannover. This project, the information of which is given below as a graduation project at the end of the program, has been realized and was completed in 4 weeks as 2 sprints, each lasting 2 weeks.
            </p>
            
            <h3>Goal </h3>
            <p>
                Within the scope of the Klinify project, it was aimed to re-evaluate the rating and reviews of some hospitals in Niedersachsen with our own algorithms. In this context, the relevant data were scraped from the internet, machine learning methods were used, and the new data obtained by re-evaluation of the data was presented on a web page. The relevant data are taken from maps.google.com and Klinikbewertungen.de.
            </p>
            <h3>Method and Technology </h3>
            <p>
                During the project, <b>scrum methodology and philosophy</b> were applied, and daily review, sprint review, sprint retro-respective meetings were held. <b>Git, Github, Jira and Scrum</b> were used in project management.
            </p>
            <p>
                A <b> web scraping </b>method has been used to obtain the data. This data was taken with Selenium and BeautifulSoup via Google Chrome Web Driver. The obtained data was cleaned using Python, Jupyter notebook, Numpy and Pandas libraries, and converted to JSON format for inserting to the database.
            </p>
            <p>
                As <b> machine learning </b>sentiment analysis and clustering are used.  In order to analyze comments in German better, the collected data were analyzed by using the textblob library. In order to obtain a project-specific hospital score (Klinify Score), scores obtained from different sources were clustered by including the number of comments. Appropriate calculations were made on the new data obtained, and the data was brought to the latest state to be presented on the web application and converted into the relevant data format.
            </p>
            <p>
                With Google <b>Firebase technology as a backend</b>, the data was stored in the cloud (Cloud Firestore). <b>For frontend used React,</b> the JavaScript library. This application has been deployed as Github Pages.
            </p>
            <h3>Result</h3>
            <p>
                The project has reached its goals and has been published as a web application. With this project, users were able to compare the scores obtained from patient comments about hospitals in the state of Niedersachsen.
            </p>
            <p>
                As a team, we have increased our working skills with scrum methodology, application of machine learning algorithms, web scrapping operations, frontend and backend technologies. Within the scope of Refugeeks project, we applied the theory and practical knowledge we learned from university professors and expert instructors in web technologies and data science education, which lasted for 9 months, in this project.
            </p>
        </div>

    );
}

export default About;




