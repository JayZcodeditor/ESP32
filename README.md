
# 🚑 Activity-based risk monitoring system for elderly people

## 📖 Project Description
This project aims to forecast human accidents using a **CNN+LSTM model**. The system utilizes an **ESP32 board** for data collection and processes the data using Python. It includes a web interface for monitoring and visualizing predictions.

---

## 🛠️ Technologies Used

### Hardware
- **🔌 ESP32 Board**
  - Programmed using MicroPython
  - Collects sensor data related to human activity

### Software
- **⚙️ MicroPython**: For programming the ESP32
- **🐍 Python**: For data processing and model creation
- **🌐 Web Interface**: For monitoring results
- **💾 Frameworks:**
  - TensorFlow (for CNN+LSTM model)
  - Flask (for serving the web application)

---

## 🚀 Getting Started

### 🔧 Prerequisites
Ensure the following are installed or available:
- **Python** (v3.8 or later)
- **MicroPython** on ESP32 board
- Required Python libraries (listed in `requirements.txt`)

### 📥 Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Flash MicroPython onto ESP32:
   - Follow [this guide](https://micropython.org/) to flash MicroPython firmware onto your ESP32 board.
   - Upload `esp32_data_collector.py` to the ESP32 using tools like **ampy** or **Thonny**.

4. Set up the environment variables for the web application:
   - Create a `.env` file:
     ```
     FLASK_APP=app.py
     FLASK_ENV=development
     ```



---

## 👨‍💻 Development and Usage


### Using the ESP32
1. Upload the MicroPython script to the ESP32.
2. Start the board to begin data collection.

---

## 🌟 Features
- 📊 **Real-time data collection** from ESP32 sensors
- 🧠 **Forecasting human accidents** using a hybrid CNN+LSTM model
- 🌐 **Web-based monitoring** for visualization
- 🔄 **Model retraining** with updated datasets

---

## 🔑 Notes
- Make sure the ESP32 is connected to the same network as your computer for data transmission.
- Use reliable sensor modules to ensure accurate data collection.
- Flask should run in a virtual environment for better dependency management.

---

## 📜 Future Improvements
- Extend the model to include more sensor data.
- Deploy the web application to a cloud platform for wider accessibility.
- Add mobile compatibility for monitoring on smartphones.

Happy Coding! 🎉
