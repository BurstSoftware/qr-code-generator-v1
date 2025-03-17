import streamlit as st
import qrcode
from io import BytesIO


def generate_qr_code(url, business_name):
    """
    Generates a QR code with the given URL and adds a logo (optional).

    Args:
        url (str): The URL to encode in the QR code.
        business_name (str): The name of the business/product/service.

    Returns:
        BytesIO: A BytesIO object containing the QR code image (PNG format).
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Add a title/logo (simplified - replace with your actual logo loading)
    # You'd typically load an image here and paste it in the center
    # For simplicity, we'll just add text.

    # Save the image to a BytesIO object for download
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)  # Reset the buffer position to the beginning

    return img_bytes


def main():
    st.title("QR Code Generator")

    # User input
    url = st.text_input("Enter the URL:")
    business_name = st.text_input("Enter the Business/Product/Service Name:")

    if st.button("Generate QR Code"):
        if url and business_name:
            try:
                qr_code_image = generate_qr_code(url, business_name)

                st.image(qr_code_image, caption=f"QR Code for {business_name}", use_column_width=True)

                # Download button
                st.download_button(
                    label="Download QR Code",
                    data=qr_code_image,
                    file_name=f"{business_name}_qrcode.png",
                    mime="image/png",
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter both URL and Business Name.")


if __name__ == "__main__":
    main()
