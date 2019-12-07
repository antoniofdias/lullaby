# Lullaby

## Table of Contents

- [Lullaby](#lullaby)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [License](#license)
  - [Contributing](#contributing)
    - [Contributors](#contributors)
  - [Acknowledgements](#acknowledgements)

## About The Project

A simple IoT sensor that uses facial recognition to publish updates referring to the drowsiness of a subject.
Built for the MATE35 course, Topics in Distributed Systems, at UFBA (Federal University of Bahia).

### Built With

-   Python 3
-   SciPy
-   Imutils
-   OpenCV
-   CMake
-   Dlib
-   Paho-MQTT

## Getting Started

Be mindful that the commands below are to be used with Linux and similar operational systems.

### Prerequisites

-   Python 3 Compiler and pip

    ```
    sudo apt-get install python3
    sudo apt install python3-pip
    ```

-   SciPy

    ```
    pip3 install scipy
    ```

-   Imutils

    ```
    pip3 install imutils
    ```

-   OpenCv

    ```
    pip3 install opencv-python
    ```

-   CMake

    ```
    sudo apt-get install cmake
    ```

-   Dlib

    ```
    pip3 install dlib
    ```

-   Paho-MQTT

    ```
    pip3 install paho-mqtt
    ```

## Usage

Be sure that your mosquitto server is running and **mqtt_client.py** is configured properly.

-   Running

    ```
    python3 main.py
    ```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some amazing-feature'`)
4. Push to the Branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contributors

-   Antônio Dias - [antoniofdias](https://github.com/antoniofdias)
-   Pedro Pontes - [pedroccrp](https://github.com/pedroccrp)

See [contributors](https://github.com/antoniofdias/lullaby/graphs/contributors) page for more info.

## Acknowledgements
* [Eye blink detection](https://www.pyimagesearch.com/2017/04/24/eye-blink-detection-opencv-python-dlib/)
