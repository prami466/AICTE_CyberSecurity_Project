# AICTE Cybersecurity Internship - Image Steganography

## Overview
This project demonstrates **image steganography**, a technique to hide a secret message inside an image. The message is encrypted into pixel values and can only be decrypted using a passcode.

## Features
- **Message Encryption**: Hides a text message inside an image by modifying pixel values.
- **Passcode Protection**: Ensures only authorized users can decrypt the message.
- **Decryption**: Recovers the original message when the correct passcode is entered.

## How It Works
1. The user inputs a **secret message** and a **passcode**.
2. Each character of the message is stored in the image pixels.
3. The encrypted image is saved as `encryptedImage.jpg`.
4. To decrypt, the user must enter the correct passcode to retrieve the message.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- OS module
