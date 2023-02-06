import math

def main():
    name = []
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 7.62]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
   
    # canvas = start(radius, height)

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return(volume)

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return(surface_area)

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area

main()