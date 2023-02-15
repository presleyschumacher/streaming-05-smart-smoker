# Week 5: Creating a Producer
#### Presley Schumacher - February 14, 2023

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
> Streaming data is the continuous, constant flow of data being generated and processed. The immediate benefit of the abilities provided by streaming data is the instant feedback when an event, anomaly, or trend begins to occur. In our project example, we are using streaming data to monitor the temperature of a 

## Execution
* Run the task emitter and open the web page to launch the admin panel

## 
