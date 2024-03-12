import strawberry


@strawberry.type
class Country:
    name: str
    code: str


@strawberry.type
class City:
    name: str
    code: str
    country: Country


@strawberry.type
class Coordinates:
    latitude: float
    longitude: float


@strawberry.type
class Location:
    city: City
    address: str
    building: str
    floor: int
    inner_code: str
    coordinates: Coordinates
    additional_info: str


@strawberry.type
class PropertyIngestion:
    id: str
    agent_id: str
    status: str
    location: Location
    property_type: str
    property_subtype: str
    rooms: int
    bathrooms: int
    parking_spaces: int
    construction_area: float
    land_area: float
    price: float
    currency: str
    price_per_m2: float
    price_per_ft2: float
    property_url: str
    property_images: str


########################################################################################################################
# This is the input schema for the property ingestion mutation.
########################################################################################################################

@strawberry.input
class CountryInput:
    name: str
    code: str


@strawberry.input
class CityInput:
    name: str
    code: str
    country: CountryInput


@strawberry.input
class CoordinatesInput:
    latitude: float
    longitude: float


@strawberry.input
class LocationInput:
    city: CityInput
    address: str
    building: str
    floor: str
    inner_code: str
    coordinates: CoordinatesInput
    additional_info: str


@strawberry.input
class PropertyIngestionInput:
    agent_id: str
    location: LocationInput
    property_type: str
    property_subtype: str
    rooms: int
    bathrooms: int
    parking_spaces: int
    construction_area: float
    land_area: float
    price: float
    currency: str
    price_per_m2: float
    price_per_ft2: float
    property_url: str
    property_images: str
