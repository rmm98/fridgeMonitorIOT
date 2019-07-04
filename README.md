This project focuses on two implementations to monitor and alert about fridge temperature:

-Monitor the temperature, use Polynomial Regression for prediction and send Email to recepient when temperature crosses Threshold
-Or instead of using hard-coded thresholds, using Z-score concept of ML to detect anomaly and send Email that somebody has opened the Fridge door

The requirements are LM35 temperature sensor, BOLT device based on ESP8266, BOLT Cloud, Python.

Reading.py is the Thresholding implementation. Anomaly.py is the z-score implementation.

Images have been included for reference about hardware and results.