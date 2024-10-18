import tkinter as tk

class WeatherUI:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Real-Time Weather Monitoring")
        self.weather_label = tk.Label(self.root, text="Fetching weather data...", font=("Helvetica", 14))
        self.weather_label.pack(pady=20)

    def update_ui(self, weather_data, summary):
        display_text = "Current Weather Data:\n"
        for city in weather_data:
            name = city['name']
            temp = city['main']['temp']
            condition = city['weather'][0]['main']
            display_text += f"{name}: {temp}°C, {condition}\n"

        display_text += "\nDaily Summaries:\n"
        for city, stats in summary.items():
            display_text += f"{city}: Avg {stats['average_temp']:.2f}°C, Max {stats['max_temp']}°C, Min {stats['min_temp']}°C, Dominant Condition: {stats['dominant_condition']}\n"

        self.weather_label.config(text=display_text)
        self.root.update()

    def run_ui(self):
        self.root.geometry("400x400")
        self.root.mainloop()