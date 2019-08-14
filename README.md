 # HitchHike
 
This is a Django web app that allows people to help other people get from one place to another by offering them a ride.
The project its still in development and with the help of people we could deploy it and make it available for the whole world.

**You can have a look here:**  [HitchHike photos](https://tiki92.github.io/HitchHike/)

    
 **Installation on Linux**
   1.  Clone the reposetory
   - Install apache-dev `sudo apt-get install apache2-dev`
   - Install libgdal `sudo apt-get install libgdal-dev gdal-bin libproj-dev`
   - Modify in `HitchHike/setting.py` GDAL_LIBRARY_PATH to the path of your libgdal
   
   2.  Create virtual enviroment with python3.6
       - Change directory to HitchHike `cd HitchHike`
       - Create an virtual enviroment `virutalenv -p python3.6 venv`
   3.  Activate virtual enviroment
       - `source venv/bin/activate`
   4.  pip install requirements.txt
       - `pip install -r requrements.txt`
   5.  Set up a [postgresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04) database
   -  Install postgis `sudo apt-get install postgresql-10-postgis-2.4`
   -  Install postgis-scripts `sudo apt-get install postgis postgresql-9.3-postgis-scripts`
       - In this tutorial is not specified how to add a password when creating a role, don't forget to add the `-P` flag when creating a new role, like this `createuser --interactive -P`
   6.  Set up [OSRM](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-osrm-server-on-ubuntu-14-04)
       - When dowloading the map export insted of "map.osm" you should name the export "map.som.pbf"
       - I used the map export (great-britan), you can find it here [map](http://download.geofabrik.de/europe/great-britain-latest.osm.pbf)
       - When extracting the map use the "-p" flag to specifie the profile.lua(`osrm-extract map.osm.pbf -p profile.lua`), if the symbolic link dosen't work copy the file car.lua from `/osrm/osrm-backend/profiles/car.lua` into `/osrm`.
       - How to build the data for osrm is a little outdated in this tutorial so when building the data you should use this commands:
        - osrm-extract map.osm.pbf
        - osrm-partition map.osrm
        - osrm-customize map.osrm
        - And to run the osrm server use: osrm-routed --algorithm=MLD map.osrm
   7.  Change some things in `HitchHike/HitchHike/settings.py`:
   Uncomment:
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'FreeRides/media')
   of the bottom at the page.
   8.  Run `python manage.py makemigrations`, `python manage.py makemigrations FreeRides` and `python manage.py migrate`
   7.  Go to HitchHike and run python manage.py runserver
   
