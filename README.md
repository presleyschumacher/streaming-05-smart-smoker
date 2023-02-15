## Week 5: Smart Smoker

> Use RabbitMQ to create a producer that will be used to monitor data from the sensors of a running barbeque smoker. Read one value every 30 seconds

* Smoker-temps.csv has 4 columns:
  * [0] Time = Date-time stamp for the sensor reading
  * [1] Channel1 = Smoker Temp --> send to message queue "01-smoker"
  * [2] Channel2 = Food A Temp --> send to message queue "02-food-A"
  * [3] Channel3 = Food B Temp --> send to message queue "03-food-B"
  
* In week 5, the system will be designed and the producer will be implemented
* In week 6, the consumers will be added and an alert will be raised when interesting events are detected.

## Before You Begin
- [x] Fork this starter repo into your GitHub.
- [x] Clone your repo down to your machine.
- [x] View / Command Palette - then Python: Select Interpreter
- [x] Select your conda environment. 

## Prerequisites
* RabbitMQ Server running
* Pika
* Sys
* Webbrowser
* CSV
* Time

## Usage

> Streaming data is the continuous, constant flow of data being generated and processed. The immediate benefit of the abilities provided by streaming data is the instant feedback when an event, anomaly, or trend begins to occur. In our project example, we are using streaming data to monitor the temperatures of a smoker and the food to ensure everything turns out perfect (or as close to perfect as possible).

1. Sensors
    1. Use temperature sensors to track temperatures and record them to generate a history of both the smoker and the food over time. 

1. Significant Events
    1. We want to know if:
        1. The smoker temperature decreases by more than 15 degrees F in 2.5 minutes
        1. Any food temperature changes less than 1 degree F in 10 minutes
 
 1. Smart System
     1. Use Python to:
         1. Simulate a streaming series of temperature readings from our smart smoker and two foods.
         1. Create a producer to send these temperature readings to RabbitMQ.
         1. Create three consumer processes, each one monitoring one of the temperature streams. 
         1. Perform calculations to determine if a significant event has occurred.
  

## Execution

1. Import the necessary modules
2. Define your variables
3. Offer to open the RabbitMQ Admin Website to monitor our queues
4. Define delete_queue
    1. We use delete_queue and queue_declare to create a pattern to ensure that a queue is empty and ready to use
5.  Define the message we will send later
6.  Create a connection to RabbitMQ
7.  Declare our queue
8.  Publish the message to the queue
9.  Print the message
10.  Close the Connection
11.  Read in the CSV File
12.  Create the CSV reader
13.  Skip the header row
14.  Convert the columns that are numbers to floats
15.  Construct a string message for the columns that could be converted
16.  If it couldn't be converted, we will skip it
17.  Send the messsage to the queue
18.  Use our standard Python idiom to indicate main program entry point
19.  Ask the user if they would like to open RabbitMQ
20.  Send Messages
21.  Sleep for 30 seconds

## Sources
https://www.tibco.com/reference-center/what-is-streaming-data
https://www.rabbitmq.com
