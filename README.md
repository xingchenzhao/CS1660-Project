# Cloud Computing Project 1



## Project Option 1

Recommend running the docker on Mac OS, but should be able to run on Windows and Linux as well.

## How to Use

- Install Docker on your OS
- Install Socat and XQuartz if you are using Mac, otherwise consider to install, for example,X11.
- Set the DISPLAY variable to {current IP}:0  in gui service of the `docker-compose.yml` file.

    ```bash
    services:
     gui:
      build: .
       environment:
 	    - DISPLAY={IP}:0
    ```

- Run `socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"`
- Then open a new terminal tab, and run `docker-compose up --build`
- Now the GUI should pop up, and you can use all tools in the application.
- Some apps require password.
- - e
- When done, click the X button, and run `docker-compose stop` and `docker-compose down`

## Video Walkthrough
