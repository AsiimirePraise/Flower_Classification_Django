# 🌸 Flower Classifier with CNN & Django

This project uses a Convolutional Neural Network (CNN) to classify flowers into categories and integrates the trained model with a Django web application for real-time predictions via a web interface.

---

## 📁 Project Structure
FLOWER_CLASSIFICATION/

## Key Files and Directories

- **CNN/**: Contains Convolutional Neural Network model and training code
- **Detect/**: Likely contains detection/classification scripts
- **Flowers/**: Probably contains flower image datasets
- **media/**: Django media uploads directory
- **static/**: Static files (CSS, JS, images)
- **templates/**: Django HTML templates
- **User/**: User-related functionality (authentication, profiles)
- **venv/**: Python virtual environment
- **.gitignore**: Specifies intentionally untracked files
- **db.sqlite3**: Django's default database file
- **manage.py**: Django's command-line utility
- **requirements.txt**: Project dependencies

  ## 🚀 Usage Guide

### 1. **Setup the Environment**
```bash
# Clone the repository
git clone https://github.com/yourusername/flower-classification.git
cd flower-classification

# Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

  ```
###3. ***Run the Django Web App***

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver



Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👤 User Authentication

- **Signup**: Go to `/signup/` or click "Register" to create a new user account.
- **Login**: Go to `/login/` and log in with your credentials.
- **Logout**: Use the "Logout" link in the navbar to sign out.

---

## 🌸 Upload & Classify Flower Image

1. Log in to your account.
2. Navigate to the **Upload Page** via the navigation bar or visit `/upload/`.
3. Select a flower image file (e.g., `.jpg`, `.png`).
4. Click **Submit**.
5. The model will classify the image and return a predicted flower category (e.g., *Rose*, *Sunflower*, *Daisy*).

---

## 🧠 How the App Works

- The image you upload is saved to the `media/` directory.
- The CNN model (stored in the `CNN/` folder) is loaded at runtime.
- The image is resized, normalized, and passed through the model.
- The app displays the top prediction on a result page.

---

## ✅ Features

- User Registration & Login System
- Secure Image Upload
- Real-Time Flower Prediction using CNN
- Django Admin Panel
- Responsive Frontend Design

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Django**
- **TensorFlow / Keras**
- **HTML5 + css**
- **pillow**
- **SQLite3 (default Django DB)**
- **Pillow** (image handling)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♀️ Contact

For questions or support(contribution), please email: `praiseasiimire38@gmail.com`
## Looking forward to advance this more
