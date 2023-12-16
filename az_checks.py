# locations = az account list-locations -o table
import regex

locations = ["eastus", "eastus", "eastus2", "southcentralus", "westus2", "westus3", "australiaeast", "southeastasia",
             "northeurope", "swedencentral", "uksouth", "westeurope", "centralus", "southafricanorth", "centralindia",
             "eastasia", "japaneast", "koreacentral", "canadacentral", "francecentral", "germanywestcentral",
             "italynorth", "norwayeast", "polandcentral", "switzerlandnorth", "uaenorth", "brazilsouth",
             "centraluseuap", "israelcentral", "qatarcentral", "centralusstage", "eastusstage", "eastus2stage",
             "northcentralusstage", "southcentralusstage", "westusstage", "westus2stage", "asia", "asiapacific",
             "australia", "brazil", "canada", "europe", "france", "germany", "global", "india", "japan", "korea",
             "norway", "singapore", "southafrica", "sweden", "switzerland", "uae", "uk", "unitedstates",
             "unitedstateseuap", "eastasiastage", "southeastasiastage", "brazilus", "eastusstg", "northcentralus",
             "westus", "jioindiawest", "eastus2euap", "westcentraz account list-locations -o tablealus", "southafricawest", "australiacentral",
             "australiacentral2", "australiasoutheast", "japanwest", "jioindiacentral", "koreasouth", "southindia",
             "westindia", "canadaeast", "francesouth", "germanynorth", "norwaywest", "switzerlandwest", "ukwest",
             "uaecentral", "brazilsoutheast"]
rg_name_pattern = "^[A-Za-z0-9_-]*$"


def location_is_valid(location: str) -> bool:
    if location in locations:
        return True
    else:
        return False


def resource_group_name_is_valid(rg_name: str) -> bool:
    return bool(regex.match(rg_name_pattern, rg_name))
