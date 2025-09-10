# DR-Rescue-Search-and-Rescue-Drone
DR Rescue is a system where a drone and a rover work collaboratively to navigate challenging environments. The drone captures aerial images of the area and uses a pathfinding algorithm to identify a safe route. This route is then relayed to the rover, which follows the path to reach and retrieve an object or assist in a rescue, ultimately delivering it to the designated destination.

![DR Rescue Drone](https://github.com/user-attachments/assets/686b0c9f-0c9d-4045-9267-1ba6a24d2710)

# System Overview
* Drone Hardware: The drone is equipped with a GPS module, Inertial Measurement Unit (IMU), and a suite of sensors including LiDAR and cameras. These enable real-time terrain mapping and obstacle detection. The drone autonomously navigates to the target area, scanning for terrain features such as slopes, obstructions, and elevation changes.
* Communication Module: A reliable communication system ensures continuous data transmission between the drone, the rover, and a central server. This allows real-time sharing of terrain data and obstacle information, enabling coordinated action.
* Data Processing: A central server processes the drone’s incoming data to determine optimal navigation paths. It identifies hazards and adapts the route accordingly to maximize safety and efficiency for the rover.
* User Interface: A streamlined, intuitive interface provides rescue operators with live terrain data and control over the drone’s flight plan. Designed for ease of use, the interface supports rapid deployment in time-critical situations.

# Features
* Raspberry Pi: included a raspberry pi as the source of communication between ground control station and pixahawk flight controller. Designed battery-powered capabilities to power up raspberry pi while flying the drone. Used a battery eliminator circuit to reduce high voltage from Li-po battery down to 5 Volts to properly power on raspberry pi.
* Mission Planner: used to configure parameters of user's choice for drone and monitor drone status. Installed on ground control station.
* Mavproxy: installed on raspberry pi to ensure proper communication between ground control station and drone. Initiated from ground control station using SSH (Secure shell) and TCP (transmission Control Protocol) protocols.
  
# Design Constraints
* Environmental – The environment had to be perfect for the drone to be safe to fly.
* Safety & welfare – Had to be clear of any objects or humans for safety.

# Future Improvements
* Path finding algorithm implementation
* Camera upgrade
