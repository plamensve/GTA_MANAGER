from GTA_MANAGER.accounts.models import Vehicles


def get_all_vehicles():
    all_vehicles = Vehicles.objects.all()

    return all_vehicles
