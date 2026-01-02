# <img src="static/img/icon-doxygen.png" alt="MeasureKit Logo" width="32"/> MeasureKit

![Python Version](https://img.shields.io/badge/python-3.14%2B-blue?logo=python&logoColor=white)
[![License](https://img.shields.io/github/license/oheyek/MeasureKit?color=green)](LICENSE)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
[![Docker Pulls](https://img.shields.io/docker/pulls/oheyek/measure-kit)](https://hub.docker.com/r/oheyek/measure-kit)
[![Documentation](https://img.shields.io/badge/docs-github.io-blue)](https://oheyek.github.io/MeasureKit/)
[![Live Demo](https://img.shields.io/badge/live-demo-brightgreen)](https://measure-kit-latest.onrender.com/)

A powerful web application for unit conversions with an intuitive interface.

## ✨ Features

- **Multi-Unit Conversions**: Convert lengths, temperatures, and weights with precision.
- **Real-Time Calculations**: Instant conversions as you type.
- **Web-Based Interface**: Accessible from any device with a browser.
- **Accurate Results**: High-precision calculations for all supported units.
- **Simple and Fast**: Convert any unit in the blink of an eye.
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux.
- **Containerized**: Available as a Docker image for easy deployment.
- **Comprehensive Testing**: Thoroughly tested for reliability.

## 🛠️ Installation

### Using Docker (Recommended)

1. Pull the Docker image:
   ```bash
   docker pull oheyek/measure-kit
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 oheyek/measure-kit
   ```
3. Open your browser and go to `http://localhost:5000`

### Running from Source

```bash
# Clone the repository
git clone https://github.com/oheyek/MeasureKit.git
cd MeasureKit

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🎯 Usage

1. Open the application in your browser (locally or online at [https://measure-kit-latest.onrender.com/](https://measure-kit-latest.onrender.com/)).
2. Select the type of conversion: Length, Temperature, or Weight.
3. Enter the value and select the units.
4. View the converted result instantly.

## 📋 Supported Conversions

| Category        | Units Available                         |
| --------------- | --------------------------------------- |
| **Length**      | Meters, Feet, Inches, Centimeters, etc. |
| **Temperature** | Celsius, Fahrenheit, Kelvin             |
| **Weight**      | Kilograms, Pounds, Ounces, Grams, etc.  |

## 🔧 Technical Details

- **Language**: Python 3.14+
- **Web Framework**: Flask 3.1.2+
- **WSGI Server**: Gunicorn 23.0.0+
- **Testing**: pytest 9.0.2+
- **Deployment**: Docker, Render

### Key Dependencies

```
flask>=3.1.2
gunicorn>=23.0.0
pytest>=9.0.2
```

## 🏗️ Building from Source

### Docker Build

```bash
# Build the Docker image
docker build -t measure-kit .

# Run the container
docker run -p 5000:5000 measure-kit
```

## 🗂️ Project Structure

```
MeasureKit/
├── app.py                     # Flask application entry point
├── src/
│   ├── __init__.py
│   ├── base.py                # Base conversion logic
│   ├── convertion_handler.py  # Conversion handler
│   ├── length.py              # Length conversions
│   ├── temperatures.py        # Temperature conversions
│   ├── weight.py              # Weight conversions
│   └── tests/
│       ├── __init__.py
│       ├── test_lengths.py    # Length tests
│       ├── test_temperatures.py # Temperature tests
│       └── test_weights.py    # Weight tests
├── static/
│   ├── css/
│   │   └── style.css          # Stylesheets
│   └── img/
│       ├── icon-doxygen.png
│       ├── icon.ico
│       └── icon.png           # Icons
├── templates/
│   ├── base.html              # Base template
│   ├── index.html             # Home page
│   ├── length.html            # Length converter
│   ├── temperature.html       # Temperature converter
│   └── weight.html            # Weight converter
├── pyproject.toml             # Project configuration
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## 🧪 Testing

The project includes comprehensive unit tests for all conversion functions.

### Running Tests

```bash
# Install test dependencies
pip install pytest

# Run all tests
pytest

# Run specific test file
pytest tests/test_lengths.py

# Run with verbose output
pytest -v
```

### Test Coverage

- **Length Tests**: Various unit conversions and edge cases
- **Temperature Tests**: Celsius, Fahrenheit, Kelvin conversions
- **Weight Tests**: Kilograms, pounds, ounces, etc.

## 🤝 Contributions

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

**Happy Converting! 🎉**

## Author

Made with ❤️ by ohey<br>
[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/ohey)

---

If you find this project useful, consider buying me a coffee! ☕
