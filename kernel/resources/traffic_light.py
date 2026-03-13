from enum import Enum
import time


class TrafficLightState(Enum):
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"


class TrafficLight:
    def __init__(self):
        self.state = TrafficLightState.RED

    def transition(self):
        """Move to the next state in the traffic light cycle."""
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN

        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW

        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.RED

    def display(self):
        print(f"Traffic Light: {self.state.value}")


def run_traffic_light(cycles=5):
    light = TrafficLight()

    for _ in range(cycles):
        light.display()

        if light.state == TrafficLightState.RED:
            time.sleep(3)

        elif light.state == TrafficLightState.GREEN:
            time.sleep(3)

        elif light.state == TrafficLightState.YELLOW:
            time.sleep(1)

        light.transition()


if __name__ == "__main__":
    run_traffic_light()