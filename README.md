# IoT Assignment 3 - Sensor Data Simulation and Publishing to ThingSpeak

This Python script is designed to simulate sensor data generation for temperature, humidity, and CO2 levels and publish the data to a ThingSpeak channel using MQTT. It is tailored for microcontrollers that support Python, such as ESP32 or ESP8266, and are equipped with networking capabilities.

## Features

- Simulates temperature, humidity, and CO2 readings.
- Publishes the data to specific fields in a ThingSpeak channel.
- Utilizes MQTT for data transmission.
- Connects to Wi-Fi networks for internet access.

## Prerequisites

Before running this script, ensure you have:

- Created a circuit using an ESP32 and a DHT22 Sensor for the simulation on WOKWI.
- A ThingSpeak account and a channel created for posting the data.

## ThingSpeak Configuration

1. Update `mqtt_client_id`, `mqtt_user`, and `mqtt_password` with your ThingSpeak MQTT API credentials.
2. Adjust `mqtt_topic_temperature`, `mqtt_topic_humidity`, and `mqtt_topic_co2` to match the field IDs of your ThingSpeak channel.

## Usage

Run the script on your microcontroller. The script will automatically:

1. Connect to the Wi-Fi network.
2. Generate random sensor data for temperature, humidity, and CO2 levels.
3. Publish this data to your ThingSpeak channel every 10 seconds.
