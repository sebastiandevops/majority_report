# Majority Report

Majority Report is an academic initiative that arises with the purpose of creating a portal where users can interactively view crime rates in the city of Medellín. The data used to generate the displayed graphics were taken from the open data portal of the Ministry of Information Technologies and Communications and were provided by the Secretary of Security and Coexistence of the Mayor's Office of Medellín. The data contains the information of the complaints actually made for the crime "theft of persons" since 2003. The last update of the database was made on December 23, 2020.

## Members

Sebastián Valencia Sierra.

## Technologies

* i) __libraries__: Pandas, Django, Plotly
* ii) __languages__: Python
* iii) __platforms__: MySQL
* iv) __frameworks__: Django

## Challenge

* i) __Problem to solve__: The website of the national police has a portal to download the data of the crimes committed throughout the national territory and that were effectively reported. This project consists of organizing, filtering, cleaning and displaying the data contained in this database, specifically those that refer to theft of persons between the period 2010 to 2020 in the Aburrá Valley. The final result will be a portal to visualize and analyze this data, in the portal it will be possible to display multiple interactive plots using either bokeh or plotly library, in this way the user will be able to interact with this data and analyze it from different perspectives.
* ii) __What the Portfolio Project will not solve__: This project will only use the data contained in the database of the national police, that is, it only has data resulting from complaints that were actually made by the victims of the crimes. Therefore, the data are representative of the complaints, however, the actual data is beyond the scope of this project since it does not have data different from those previously stated.
* iii) __Users to whom the project is directed__: People who want to visualize the data of the crime of theft from people in the metropolitan area of ​​Valle de Aburrá.
* iv) __Is this project relevant or dependent on a specific locale?__ This project is limited to the metropolitan area of ​​Valle de Aburrá

## Risks

* i) __Technical risks, the potential impact, and safeguards__: There are no technical risks since the data that the portal will use does not have the character of sensitive data and is of a public nature.
* ii) __Non-technical risks, the potential impact, and strategies to prevent negative outcomes__: As the application data is representative of the complaints made but not of the crimes committed but not reported, the graphs can generate in users a perception of security or insecurity that does not fully correspond to reality. For this reason, the source of the data will be reported and the representativeness of the data will be explicitly clarified.

## IInfrastructure

* i) __Process for branching and merging in team’s repository__: English
There will only be one repository contained in github
* ii) __Strategy for deployment__: The data is stored using MySQL, the organization and cleaning of the data will be done with python, the data will be displayed using the Python MatplotLib library and the portal will be displayed with Flask.
* iii) __Data source for the application__: National Police databases.
* iv) __Tools, automation and process for testing__: The automation of the scripts will be done with the linux tool, crontab.

## Existing Solutions

There is no automatic tool to view the data in this project, there is only the national police tool, which only allows you to download the data in csv or xmls format.
