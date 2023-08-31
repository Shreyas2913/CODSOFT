import tkinter as tk

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        
        self.city_label = tk.Label(root, text="City:")
        self.city_label.pack()
        
        self.city_entry = tk.Entry(root)
        self.city_entry.pack()
        
        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.display_weather)
        self.get_weather_button.pack()
        
        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack()
        
    def display_weather(self):
        city = self.city_entry.get()
        
        # Simulated weather data
        temperature = "25°C"
        weather_condition = "Sunny"
        
        weather_info = f"Weather in {city}:\nTemperature: {temperature}\nCondition: {weather_condition}"
        self.weather_label.config(text=weather_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
