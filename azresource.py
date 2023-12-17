class AZResource:
    def __init__(self, name, resource_group, **kwargs):
        self.name = name
        self.resource_group = resource_group

    def display_info(self):
        return f"Name: {self.length}, Resource Group: {self.resource_group}"

    def make_fruits_lower_case(list_of_fruits : list) -> list:
        if isinstance(list_of_fruits, list):
            return [fruit.lower() for fruit in list_of_fruits]
        raise TypeError('list_of_fruits must be a of type list')