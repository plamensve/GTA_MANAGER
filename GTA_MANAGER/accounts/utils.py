from GTA_MANAGER.accounts.models import Vehicles, VehicleFullDetails


def get_all_vehicles():
    all_vehicles = Vehicles.objects.all()

    return all_vehicles


def vehicle_full_details_info(pk):
    try:
        vehicle_details = VehicleFullDetails.objects.get(vehicle=pk)
    except VehicleFullDetails.DoesNotExist:
        vehicle_details = None

    return vehicle_details
