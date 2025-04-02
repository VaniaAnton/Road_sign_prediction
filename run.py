import requests
import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk

# API Credentials
token = "sf5pu2u2cl40jgs5dg30o2bkr2"
project_id = "67410"
model = "object-detection-model-1"
headers = {"X-Auth-token": token, "Content-Type": "application/octet-stream"}

# Function to Upload Image
def upload_image():
    # Ask user to select a single image file
    file_path = filedialog.askopenfilename(filetypes=[("Png Files", "*.png")])
    if not file_path:
        return
    
    # Display the selected image
    img = Image.open(file_path)
    img.thumbnail((500, 500))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img
    
    # Send image to API
    with open(file_path, 'rb') as handle:
        r = requests.post(f'https://platform.sentisight.ai/api/predict/{project_id}/{model}/',
                          headers=headers, data=handle)
    
    if r.status_code == 200:
        result_label.config(text=f"Prediction: {r.text}")
    else:
        result_label.config(text=f"Error: {r.status_code}\n{r.text}")

# GUI Setup
root = tk.Tk()
root.title("Image Upload and Object Detection")

upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

image_label = Label(root)
image_label.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()

