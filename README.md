# Player-Analytics-Tool
Analytics tool that leverages AWS EC2 and RDS infrastructure. Uses python scrapper and PostgreSQL database to store data. Created Docker image of web scrapper and ran the container on my EC2 instance for rapid deployment and scalability

Created my own analytical tool for CSGO (video game) Pro Players. 

1. Created python scrapper using BeautifulSoup4 library that scrapes data off of a public website: https://profilerr.net/cs-go/pro-players/settings/.
2. Ran python scrapper inside Docker container on AWS EC2 instance.
3. Leveraged AWS RDS to host the PostgreSQL Database on the cloud.
4. Using psycopg2 package, python scrapper inputted data into PostgreSQL database.
5. Analytical tool (Local) pulled data from database on the cloud.

In Repository:
1. Dockerfile - Creating Docker image of scrapper.py 
2. requirements.txt - Libraries and packages required for Dockerfile 
3. scrapper.py - Web Scrapper - Inputs data
4. analytical_tool.py - Analytical tool - Pulls data
