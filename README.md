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

- Allow vets to add a "wild" animal. An animal admitte that does not necessarily have an owner (or the owner/owner id is unknown) 

- Timestamping option for the treatment notes. Allow users to input information regarding the animal and update it continuously whilst in treatment (keeping a record of the time note was uploaded)

- Clear, minimal interface to navigate from home page to either: practice, owner or pet (each containing the respective index) - include lots of pictures of animals!

- Add timezone function - allows inputted data, users, pets etc interaction with vets to be recorded with a time feature

- Add a filter function for the pets index to find specific pets - maybe this filter function can detect certain text within the treatment notes

- If photo of animal is not available use a unicode image substitute for the animal to appear in the show and index pages


#### Testing

#### Setup + Installation

#### My Process

