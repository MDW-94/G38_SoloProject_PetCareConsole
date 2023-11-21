Pet Care Console

This project was the first solo project of the CodeClan / CodeBase 16-Week Professional Software Development course. The purpose of the application is for veterinary practices to be able to admit and register pets to different vet services around the Glasgow area. Each pet admission has data concerning their age, gender, name and treatment notes associated. This data is stored in a Postgres SQL, relational database. During development I declared primary and foreign keys to the different tables so that a user could assign pets to different owners and vet services. 

See below for the project brief on the course

### Brief: Vet

A local veterinary practice has asked you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet. 

App must be built using only:

- HTML/CSS
- Python
- Flask
- PostgreSQL and psycopg2

It must not use:

- Any Object Relational Mapper (e.g. ActiveRecord)
- JavaScript
- Any pre-built CSS libraries, such as Bootstrap
- Authentication

  #### Setup + Installation

 - in terminal, file path: G38_projects/vet_app
 - dropdb vet_manager
 - createdb vet_manager
 - psql -d vet_manager -f /G38_project1_vetApp/vet_app/db/vet_manager.sql
 - psql -d vet_manager
 - type sql in here to view tables

 - in terminal, file path: G38_projects/vet_app
 - flask run

#### MVP

- The practice wants to be able to register/track animals. 
- Pets should have the following information associated to them: 
    -Name
    -Date Of Birth (use a VARCHAR initially)
    -Gender
    -Type of animal
    -Contact details for the owner
    -Treatment notes

- Animals should be able to be assigned to vets
- CRUD actions for vets/animals - What views should be there for the user?

#### Extension

- Owners can be registered/unregistered from the Vet - unregistered owners wont be able to add any more animals

- Owner contact details should be consistent for each pet they own - they shouldn't need to be updated each time a new pet is registered

- Handle check-in/check-out dates

- Let the practice see all animals currently in the practice (is the present day's date between check-in and check-out times?)

- Sometimes an owner does not know the DOB - allow them to enter an age instead. Keep this up-to-date, if they visit again a year later this hsould be reflected in the pets age (if the pet was 3 on first admission it will be 4 on the year-later admission)

- Add extra functionality to your app: assigning treatments,  comprehensive ways  of maintaining treatment notes over time, appointments, pricing/billing


##### Initial Thoughts on MVP

- contact details for owner could be substituted for owner_id - another table could be made
- user should be able to add, delete, save and update pets and vets
- convert str value of pet DOB to datetime

##### Initial Thoughts of Extra Functionality:

- Location information of the veterinary practices, reflected in the front-end with a map image highlighting the district of the city where the practice is located (ie Battlefield, Glasgow highlighted on map)

- Feedings times including a note of completion. Feedings times could be noted for all pets and monitored (completed/not completed) for pets currently checked in

- Allow vets to add a "wild" animal. An animal admitted that does not necessarily have an owner (or the owner/owner id is unknown) 

- Timestamping option for the treatment notes. Allow users to input information regarding the animal and update it continuously whilst in treatment (keeping a record of the time note was uploaded)

- Clear, minimal interface to navigate from home page to either: practice, owner or pet (each containing the respective index) - include lots of pictures of animals!

- Add timezone function - allows inputted data, users, pets etc interaction with vets to be recorded with a time feature

- Add a filter function for the pets index to find specific pets - maybe this filter function can detect certain text within the treatment notes

- If photo of animal is not available use a unicode image substitute for the animal to appear in the show and index pages - unicode dependent upon type of animal


#### Testing

#### My Process

- Diagrams link: https://www.figma.com/file/7lg3FDk1aKOEeGpsKyVq3A/Welcome-to-FigJam?type=whiteboard&node-id=0%3A1&t=9veJL0FM4aQyftR0-1



