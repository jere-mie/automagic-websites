# Automagic-Websites
A digital CV/website platform specifically tailored to CS students

## Project description
In today's world as a developer, having an online presence is a necessity. However, many developers don't have the time, experience, or interest in learning the fundamentals of web development to create a sleek website on their own. While there are many platforms for making websites on the market, they aren't tailored specifically to CS students and developers, and often look like they were made from a web platform. Automagic Websites hopes to change this, by offering CS students a platform to quickly create, edit, publish, and export their own simple, yet sleek, website in a matter of minutes.

## Goals for this project/features to be included
  * full user authentication
  * ability to fill in specific fields for basic information
  * ability to post projects
  * ability to have custom areas for user content, styled using markdown
  * ability to edit all fields and posts
  * ability to host website on the platform
  * ability to export and download the completed static website as a zip archive
  * ability to customize user's URL extension
  * multiple templates for the user to choose from
  * light/dark mode toggle
  * different themes and customizability options
    * accent colours
    * font family
    * animations/no animations

## 10 step plan moving forward
  1. implement user authentication and account creation
  2. set up classes for models and forms for the database
  3. create routes and logic behind receiving user input from forms
  4. set up logic for using user input to generate website
  5. polish and design final user website template
  6. implement website generation and hosting
  7. implement exporting of websites into zip archives
  8. launch project on GCP
  9. release to public for beta and testing
  10. release final product

## Tech stack
  * Flask
  * Flask-wtf
  * PostgreSQL
  * Bootstrap (styling)
  * GCP (host)
  * Gunicorn (server)
  * Caddy V2 (reverse proxy)
  
#### This project is being developed as part of the University of Windsor DSC
##### If you are interested in contributing to this project, please contact the project lead: Jeremie Bornais, borna113@uwindsor.ca
