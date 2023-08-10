# Noise Suppressor Audio Plugin

The **Noise Suppressor Audio Plugin** is a simple Python script that demonstrates noise suppression for audio samples. It processes audio input and applies noise suppression by setting low-amplitude samples below a certain threshold to zero. This plugin showcases basic noise reduction techniques.

## Features

- **Noise Suppression:** The plugin processes audio samples and suppresses noise by zeroing out low-amplitude samples below a specified threshold.

## Getting Started

To use the Noise Suppressor Audio Plugin, follow these steps:

1. **Installation:** Make sure you have Python installed on your system. Install the required dependencies using the following command:

    ```
    pip install pyaudiounit numpy
    ```

2. **Running the Plugin:** Run the provided Python script `noise_suppressor.py` to start the plugin. It will process audio input and suppress noise based on the threshold and gain factor.

3. **Adjustment:** You can modify the `NOISE_THRESHOLD` and `GAIN_FACTOR` variables in the script to control the noise suppression threshold and the amplification factor applied to the remaining signal.

## Usage

1. Run the `noise_suppressor.py` script using Python.

2. The plugin will process the audio input, applying noise suppression and amplification as specified.

## Configuration

Adjust the following variables in the script to customize the behavior of the plugin:

- `NOISE_THRESHOLD`: Set the threshold below which samples will be suppressed.
- `GAIN_FACTOR`: Set the amplification factor applied to the remaining signal after noise suppression.

## Contributing

If you're interested in contributing to the Noise Suppressor Audio Plugin, feel free to fork this repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

The Noise Suppressor Audio Plugin showcases basic noise suppression techniques using Python. The provided code demonstrates the application of noise suppression and amplification to audio samples, which can be useful for various audio processing tasks.
