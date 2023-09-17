import qrcode
import urllib.parse


# List of names
names = list()
with open("new_list.txt") as file:
    for i in file:
        i = i.rstrip()
        if i not in names:
            names.append(i)


# URL that all QR codes will point to
url = "https://teddycodex-guest-manager.onrender.com/guest_list"


# Function to generate QR codes
def generate_qr_codes(names, url):
    qr_codes = []
    for name in names:
        query_param = urllib.parse.urlencode({"guest_name": name})
        full_url = f"{url}?{query_param}"
        qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=4,
        )
        qr.add_data(full_url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_codes.append((name, qr_img))
    return qr_codes


# Generate QR codes
qr_codes = generate_qr_codes(names, url)

# Save QR codes
for name, qr_code in qr_codes:
    qr_code.save(f"{name}_qr_code.png")

print("QR codes generated successfully!")
