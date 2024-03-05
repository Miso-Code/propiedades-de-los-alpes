from uuid import UUID

from ..application.dto import PropertyPropertiesDTO
from ..domain.entities import Property


from ....seedwork.application.dto import Mapper as AppMapper
from ....seedwork.domain.repositories import Mapper as RepoMapper

class PropertyDTOJsonMapper(AppMapper):
    
    def dto_to_external(self, dto: PropertyPropertiesDTO) -> dict:
        return dto.__dict__
    
    def external_to_dto(self, external: dict) -> PropertyPropertiesDTO:
        return PropertyPropertiesDTO(**external)

class PropertyMapper(RepoMapper):
    
    def get_type(self) -> type:
        return Property.__class__
    
    def entity_to_dto(self, entity: Property) -> PropertyPropertiesDTO:
        return PropertyPropertiesDTO(
            id=str(entity.id),
            agent_id=entity.agent_id,
            property_id=entity.property_id,
            property_address=entity.property_address,
            property_city=entity.property_city,
            property_state=entity.property_state,
            property_zip=entity.property_zip,
            property_price=entity.property_price,
            property_bedrooms=entity.property_bedrooms,
            property_bathrooms=entity.property_bathrooms,
            property_square_feet=entity.property_square_feet,
            property_lot_size=entity.property_lot_size,
            property_type=entity.property_type
        )
        
    def dto_to_entity(self, dto: PropertyPropertiesDTO) -> Property:
        return Property(
            id=UUID(dto.id) if dto.id else None,
            agent_id=dto.agent_id,
            property_id=dto.property_id,
            property_address=dto.property_address,
            property_city=dto.property_city,
            property_state=dto.property_state,
            property_zip=dto.property_zip,
            property_price=dto.property_price,
            property_bedrooms=dto.property_bedrooms,
            property_bathrooms=dto.property_bathrooms,
            property_square_feet=dto.property_square_feet,
            property_lot_size=dto.property_lot_size,
            property_type=dto.property_type
        )