import os
>>>>>>> 30e49b9181e963273a7d7f8e7484884c7de21080

<<<<<<< HEAD
file_path = "index.html"
required_img_tag = '<img src="footer-image.png" alt="Footer Logo" width="100">'

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found!")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Check if the footer image is already present
if 'src="footer-image.png"' in content:
    print("Footer image is already present. No fix needed!")
else:
    print("Footer image is missing! Restoring footer image...")

    # Look for the closing footer tag and insert the image before </footer>
    if "</footer>" in content:
        updated_content = content.replace("</footer>", f"    {required_img_tag}\n</footer>")
    else:
        # Fallback: append at the end of the body if no footer tag exists
        updated_content = content.replace("</body>", f"<footer>\n    {required_img_tag}\n</footer>\n</body>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Footer image successfully restored!")
=======
file_path = "index.html"
required_img_tag = '<img src="footer-image.png" alt="Footer Logo" width="100">'

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found!")
    exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

if 'src="footer-image.png"' in content:
    print("Footer image is already present. No fix needed!")
else:
    print("Footer image is missing! Restoring footer image...")
    if "</footer>" in content:
        updated_content = content.replace("</footer>", f"    {required_img_tag}\n</footer>")
    else:
        updated_content = content.replace("</body>", f"<footer>\n    {required_img_tag}\n</footer>\n</body>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Footer image successfully restored!")

>>>>>>> 30e49b9181e963273a7d7f8e7484884c7de21080