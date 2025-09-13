
import numpy as np
import matplotlib.pyplot as plt

Te = 0.01  # Sampling period
N = 100    # Number of samples
t = np.arange(0, N) * Te  # Time vector from 0 to (N-1)*Te

f = 5  
sine_wave = np.sin(2 * np.pi * f * t)

print("First 10 samples of sine wave:")
print(sine_wave[:10])

x1 = 1-np.sin(2 * np.pi * f * t)  # Sine wave
x2 = np.cos(2 * np.pi * f * t)  # Cosine wave

plt.figure(figsize=(14, 8))
plt.plot(t, x1, label='1-sin(2π·5t)')
plt.plot(t, x2, label='cos(2π·5t)')
plt.plot(t, sine_wave, label='Sampled Sine')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine and Cosine Waves')
plt.legend()
plt.grid(True)
plt.show()
