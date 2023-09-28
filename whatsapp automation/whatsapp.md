# WhatsApp Message Sender

This Python script demonstrates how to send a WhatsApp message to a specific phone number using the `pywhatkit` library. It allows you to automate the process of sending messages to WhatsApp contacts at a specific time.

## How to Use

1. Ensure you have Python installed on your computer.

2. Install the `pywhatkit` library by running the following command in your terminal or command prompt:

   ```
   pip install pywhatkit
   ```

3. Replace the following parameters in the code with your own information:

   - `"Phone_Number"`: Replace this with the recipient's phone number, including the country code (e.g., `+1234567890`).
   - `"Your_Message"`: Replace this with the message you want to send.
   - `16` and `40`: These represent the time at which you want to send the message (hours and minutes in 24-hour format). Modify these values as needed.

4. Run the script in your Python environment.

5. The script will use the `pywhatkit` library to send the specified message to the specified phone number at the designated time.

## Example Usage

```python
import pywhatkit as kit

# Send a message to the specified number at 16:40
kit.sendwhatmsg("+1234567890", "Hey, this is an automated message!", 16, 40)
```

In this example, the script will send the message "Hey, this is an automated message!" to the phone number `+1234567890` at 16:40 (4:40 PM).

## Note

- Make sure that the recipient's phone number is valid and accessible on WhatsApp.
- Ensure that you have an active internet connection while running the script.
- The script uses your default web browser to access WhatsApp Web, so you may need to log in to WhatsApp Web if you are not already logged in.

Feel free to use and modify this script for your specific WhatsApp messaging needs.