"""
    This program sends a message to a queue on the RabbitMQ server from a CSV File to create alert notifications.

    Author: Presley Schumacher
    Date: February 14, 2023

"""

import pika
import sys
import webbrowser
import csv
import time

def offer_rabbitmq_admin_site(show_offer):
    """Offer to open the RabbitMQ Admin website by using True or False"""
    if show_offer == True:
        ans = input("Would you like to monitor RabbitMQ queues? y or n ")
        print()
        if ans.lower() == "y":
            webbrowser.open_new("http://localhost:15672/#/queues")
            print()

def send_message(host: str, queue_name: str, message: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        host (str): the host name or IP address of the RabbitMQ server
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue
    """

    try:
        # Establish a connection with RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters(host))
        ch = conn.channel()

        # use the channel to delete the queue
        # We use queue_delete to ensure that our queue_declare has been cleared and does not contain messages from previous usage.
        ch.queue_delete(queue="01-smoker")
        ch.queue_delete(queue="02-food-A")
        ch.queue_delete(queue="03-food-B")

        # use the channel to declare a durable queue
        # a durable queue will survive a RabbitMQ server restart
        # and help ensure messages are processed in order
        ch.queue_declare(queue="01-smoker", durable=True)
        ch.queue_declare(queue="02-food-A", durable=True)
        ch.queue_declare(queue="03-food-B", durable=True)

        # print a message to the console for the user
        print(f" [x] Sent {message}")
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        conn.close()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    # ask the user if they would like to open the RabbitMQ Admmin
    offer_rabbitmq_admin_site('False')

with open("smoker-temps.csv", "r") as file:
    reader = csv.reader(file)
    # read in the rows
    for row in reader:
        timestamp = f"{row[0]}"
        smoker_temp = f"{row[1]}"
        food_A_temp = f"{row[2]}"
        food_B_temp = f"{row[3]}"
    
    # Set up Messages
    message_smoker=f"[{timestamp},{smoker_temp}]"
    messge_food_A=f"[{timestamp},{food_A_temp}]"
    message_food_B=f"[{timestamp},{food_B_temp}]"

    send_message("localhost", "01-smoker", "message_smoker")
    send_message("localhost", "02-food-A", "message_food_A")
    send_message("localhost", "02-food-B", "message_food_B")

    # sleep for thirty seconds
    # we will use 3 seconds to test so it doesn't take as long
    time.sleep(3)