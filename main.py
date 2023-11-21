from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import uniqueid, battery
class FlightModeApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        flight_mode_button = Button(text='Включить режим полета', on_press=self.toggle_flight_mode)
        layout.add_widget(flight_mode_button)

        battery_status_label = Button(text='Статус батареи', on_press=self.show_battery_status)
        layout.add_widget(battery_status_label)

        return layout

    def toggle_flight_mode(self, instance):
        # Здесь вы можете вставить код для включения/выключения режима полета
        # Например, можно воспользоваться сторонней библиотекой для автоматизации действий на устройстве

        # Пример использования Plyer для получения уникального идентификатора устройства
        device_id = uniqueid.id
        print(f'Уникальный идентификатор устройства: {device_id}')

    def show_battery_status(self, instance):
        # Пример использования Plyer для получения статуса батареи
        battery_status = battery.status
        battery_percentage = battery.percentage
        print(f'Статус батареи: {battery_status}, Заряд батареи: {battery_percentage}%')


if __name__ == '__main__':
    FlightModeApp().run()
