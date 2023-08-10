from pyaudiounit import AUGraph, AudioComponentDescription
import numpy as np

# Define the gain factor (amplification factor)
GAIN_FACTOR = 2.0
# Define the noise suppression threshold
NOISE_THRESHOLD = 0.2

class NoiseSuppressor:
    def __init__(self):
        self.graph = AUGraph()
        self.effect_unit = self.graph.add_unit(AudioComponentDescription(kAudioUnitType_Effect, kAudioUnitSubType_GenericEffect))
        self.input_unit = self.graph.add_unit(AudioComponentDescription(kAudioUnitType_Output, kAudioUnitSubType_DefaultOutput))

        self.graph.connect(self.effect_unit, 0, self.input_unit, 0)

        # Set the render callback function
        self.graph.set_render_callback(self.render_callback)

        # Initialize the audio graph
        self.graph.initialize()

    def render_callback(self, num_frames, buffer_list, time_stamp, bus_number):
        # Loop through all the audio buffers
        for buffer in buffer_list:
            samples = np.frombuffer(buffer, dtype=np.float32)

            # Amplify the audio signal
            samples *= GAIN_FACTOR

            # Apply noise suppression
            samples[np.abs(samples) < NOISE_THRESHOLD] = 0.0

    def start(self):
        # Start the audio graph
        self.graph.start()

    def stop(self):
        # Stop the audio graph
        self.graph.stop()

if __name__ == "__main__":
    # Create an instance of the NoiseSuppressor class
    suppressor_plugin = NoiseSuppressor()

    # Start the audio graph
    suppressor_plugin.start()

    try:
        # Keep the plugin running until the user terminates the script
        while True:
            pass
    except KeyboardInterrupt:
        pass

    # Stop the audio graph
    suppressor_plugin.stop()
