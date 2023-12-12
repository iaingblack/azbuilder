from az_checks import *
import resource_az_group

rg_name = 'azbuilder'
location = 'northeurope'

if location_is_valid(location):
    if resource_group_name_is_valid(rg_name):
        rg = resource_az_group.CREATE(rg_name, location)
        print(rg.create_command())
    else:
        print(f"RG Name {rg_name} is not valid")
else:
    print("Location is not valid")
