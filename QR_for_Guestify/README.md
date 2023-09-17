# QR Code Generator for Guestify

This script is designed to generate QR codes for guests in an event management context. Each QR code points to a URL which, when scanned, facilitates automated guest verification by embedding the guest's name as a query parameter.

## Features

- **Name Extraction**: Extracts unique names from a provided text file.
- **Dynamic URL Creation**: Embeds each guest name into a base URL as a query parameter.
- **QR Code Generation**: Generates a QR code for each guest pointing to their personalized URL.

## Usage

### Prerequisites

- Ensure you have the `qrcode` Python library installed. If not, install it using:

```
    pip install qrcode[pil]
```

### Steps

- Names Input: Populate the new_list.txt file with the names of the guests, one name per line.
- Run the Script: Execute the Python script:

```
    python [script_name].py
```

- Output: The script will generate a QR code for each guest and save it as an image file named `[guest_name]_qr_code.png`

## Customization

- **URL Endpoint**: Modify the url variable in the script to point to your desired endpoint.
- **QR Code Properties**: Adjust properties like version, box_size, and border in the `qrcode.QRCode()` instantiation for custom QR code configurations.

## License

[MIT](https://choosealicense.com/licenses/mit/)
