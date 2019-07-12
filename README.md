 # HitchHike
 
This is a Django web app that allows people to help other people get from one place to another by offering them a ride.
The project its still in development and with the help of people we could deploy it and make it available for the whole wolrd.

**You can have a look here:**  [HitchHike photos](https://tiki92.github.io/HitchHike/)

    
 **Usage**
   1.  Clone the reposetory
   2.  Create virtual enviroment with python3.6
       - Change directory to HitchHike `cd HitchHike`
       - Create an virtual enviroment `virutalenv -p python3.6 venv`
   3.  Activate virtual enviroment
       - `source venv/bin/activate`
   4.  pip install requirements.txt
       - `pip install -r requrements.txt`
   5.  Set up a [postgresql](https://www.digiean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04) database 
       - In this tutorial is not specified how to add a password when creating a role, don't forget to add the `-P` flag when creating a new role, like this `createuser --interactive -P`
   6.  Set up [OSRM](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-osrm-server-on-ubuntu-14-04)
       - When dowloading the map export insted of "map.osm" you should name the export "map.som.pbf"
       - I used the map export (great-britan), you can find it here [map](http://download.geofabrik.de/europe/great-britain-latest.osm.pbf)
       
   7.  Go to HitchHike and run python manage.py runserver
   
