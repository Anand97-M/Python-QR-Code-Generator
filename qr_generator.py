import qrcode
from pathlib import Path

def generate_qr():
    print("\n===== PYTHON QR CODE GENERATOR =====")

    # Get information from the user
    data = input("Enter text, website URL or any information: ").strip()

    if not data:
        print("Please enter valid information.")
        return

    # Get QR code filename
    filename = input("Enter QR code filename (without extension): ").strip()

    if not filename:
        filename = "my_qr_code"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create QR image
    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Save QR code
    output_file = Path(f"{filename}.png")
    image.save(output_file)

    print("\nQR Code generated successfully!")
    print("Saved at:", output_file.resolve())

    # Display QR code
    image.show()


if __name__ == "__main__":
    generate_qr()
