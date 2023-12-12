# https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest
# az group create --location
#   --name
#   [--managed-by]
#   [--tags]

class CREATE:
    # description = "Creates an Azure Resource Group"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"RG is called '{self.name}' and is located in '{self.location}'"

    def get_name(self) -> str:
        return f"{self.name}"

    def get_location(self) -> str:
        return f"{self.location}"

    def create_command(self) -> str:
        return f"az group create --name {self.name} --location {self.location}"
