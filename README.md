<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<div align="center">

[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



![Contributors][contributors-shield] <br>
[Michael Smith](https://github.com/onticinc) <br>
[Patrick Brennan](https://github.com/pambonian)<br>

Special Thanks to:
Justin - Helping debug route. 
Roland - Helping debug. 
Avery - Implimenting pagination 
Eric - Help with parsing rss feed. 


<bold>Extra Special thanks to:</bold> 
Rome - For Kickin ass and taking names, in a very professional manner.

</div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/onticinc/podcast_template">
    <img src="https://i.imgur.com/gi4BvGD.png" alt="Logo" width="80" height="80">
  </a>



  
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With:</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#appearance">Appearance</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#general-approach">General Approach</a></li>
    <li><a href="#user-stories">User Stories</a></li>
    <li><a href="#project-wireframes">Project Wireframes</a></li>
    <li><a href="#roadblocks">Roadblocks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<br>

<!-- ABOUT THE PROJECT -->
## About The Project

#### Link to Linode deployment:
http://173.230.133.42:8000/


Initial Build was from this series. 
https://www.youtube.com/watch?v=UmljXZIypDc

Poll App is from Django Tutorial Docs. 
https://docs.djangoproject.com/en/4.0/intro/tutorial01/

Rss App is parsed and designed by:
[Michael Smith](https://github.com/onticinc) <br>
[Patrick Brennan](https://github.com/pambonian)


scrapper.py referenced from here:
https://www.youtube.com/watch?v=ng2o98k983k






<p align="right">(<a href="#top">back to top</a>)</p>



### Built With



* [Python.js](https://www.python.org/)
* [Django.js](https://www.djangoproject.com/)
* [Postgres.js](https://www.postgresql.org/)
* [Crispy_forms.js](https://github.com/django-crispy-forms/django-crispy-forms)
* [Aws3](https://aws.amazon.com/s3/)
* [Node.js](https://nodejs.org/en/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Fork and Clone this repository
   ```sh
   git clone https://github.com/onticinc/podcast_template.git
   ```
2. Install packages
   ```sh
   <!-- Put Sequences here.  -->
   ```
3. 

   ```
5. 
6. 
    

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<!-- Add Content Here -->

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- SCREENSHOT OF THE SITE -->

## Appearance
<div align="center">

![Alt text]()

![Alt text](https://i.imgur.com/8WLMDBO.png)

![Alt text](https://i.imgur.com/RIHWR92.png)

![Alt text](https://i.imgur.com/MQasQ3v.png)

![Alt text](https://i.imgur.com/uSVZVhr.png)

</div>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- TECHNOLOGIES USED -->

## Technologies Used

## Python.js

- Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0. 

Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). 

Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.

Python consistently ranks as one of the most popular programming languages.

Referenced from:
https://en.wikipedia.org/wiki/Python_(programming_language)

## Postgres

- PostgreSQL (/ˈpoʊstɡrɛs ˌkjuː ˈɛl/, POHST-gres kyoo el), also known as Postgres, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley. 

In 1996, the project was renamed to PostgreSQL to reflect its support for SQL. After a review in 2007, the development team decided to keep the name PostgreSQL and the alias Postgres.]

PostgreSQL features transactions with Atomicity, Consistency, Isolation, Durability (ACID) properties, automatically updatable views, materialized views, triggers, foreign keys, and stored procedures. It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users. It is the default database for macOS Server and is also available for Windows, Linux, FreeBSD, and OpenBSD.

Referenced from:
https://en.wikipedia.org/wiki/PostgreSQL

## Django
- Axios, which is a popular library is mainly used to send asynchronous HTTP requests to REST endpoints. This library is very useful to perform CRUD operations.
- This popular library is used to communicate with the backend. Axios supports the Promise API, native to JS ES6.
- Using Axios we make API requests in our application. Once the request is made we get the data in Return, and then we use this data in our project. 
- This library is very popular among developers.

## MongoDB
- MongoDB is an open-source document-oriented database that is designed to store a large scale of data and also allows you to work with that data very efficiently.
- MongoDB stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time
- The document model maps to the objects in your application code, making data easy to work with
- Ad hoc queries, indexing, and real time aggregation provide powerful ways to access and analyze your data

## bcrypt
- bcrypt is a password-hashing function designed by Niels Provos and David Mazières, based on the Blowfish cipher and presented at USENIX in 1999. Besides incorporating a salt to protect against rainbow table attacks, bcrypt is an adaptive function: over time, the iteration count can be increased to make it slower, so it remains resistant to brute-force search attacks even with increasing computation power.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GENERAL APPROACH -->

## General Approach

Our frontend and backend teams collaboratively built the idea for Mercer. We wanted an online-store application where we could innovate on ideas we thought could interact well on a single platform.

We began by creating our wireframe and laying out our user stories. With these as the foundation, our backend team built out the database tools necessary to provide functionality to the app. Our frontend began creating components and pages to address the requirements we had produced from our wireframes. 

Over time, the backend was connected in these pages and components, and the basic functionality of the app emerged. From there, both teams worked to add the more complex (but awesome) features we’d set out to create. Up until the time of our deployment, we continued working to build out and improve our UI and UX. 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LINK TO USER STORIES -->

## User Stories

View our user stories page by following [this link](https://github.com/onticinc/mercer/blob/main/USERSTORIES.md)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- WIREFRAMES -->

## Project Wireframes

![Alt text](https://i.imgur.com/elBrbgk.png)

![Alt text](https://i.imgur.com/ID426sI.png)

![Alt text](https://i.imgur.com/shUjrcg.png)

![Alt text](https://i.imgur.com/jKftZkX.png)

![Alt text](https://i.imgur.com/qGrHgpc.png)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADBLOCKS -->

## Roadblocks

Frontend:
- Creating a functional map tool to allow users to view how near/far they are from the listings. We were able to produce the nonfunctional map element on the app, but making it functional in our timeframe was not tenable.

- Bidding/Haggling/Reservation interaction. We wanted to allow potential buyers to post their best offer on an item, or make counteroffers, or pay extra to the seller to be able to reserve a product. We did not have enough time during the timeframe to attempt to implement these features.

- Instant-listing. We wanted sellers to be able to take a big mass of things they want to sell (a ton of old equipment in the garage, for example), whip out their phone - and make dozens of listings quickly and easily. We did not have the time to address this functionality.

- Wanted the items on the home page to populate with recent items postes... We ran out of time to be able to adress this issue.  


See the [open issues](https://github.com/onticinc/mercer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>