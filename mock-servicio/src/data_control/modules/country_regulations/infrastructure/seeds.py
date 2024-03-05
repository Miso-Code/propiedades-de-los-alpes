from uuid import uuid4
import colorama
from .dto import CountryRegulationDTO
from ..domain.value_objects import CountryRegulationConditionType
from ....config.db import db


existing_records = db.query(CountryRegulationDTO).count()


if existing_records == 0:
    print(colorama.Fore.LIGHTYELLOW_EX + '[Country Regulations] Seeding country regulations...', colorama.Style.RESET_ALL)
    db.bulk_save_objects(
        [
            CountryRegulationDTO(
                id=str(uuid4()),
                country_code='US',
                country_name='United States',
                fields='location_coordinates_latitude,location_coordinates_longitude',
                regulation_condition_type=CountryRegulationConditionType.IS_NOT_EMPTY.value,
                regulation_condition_value=''
            ),
            CountryRegulationDTO(
                id=str(uuid4()),
                country_code='US',
                country_name='United States',
                fields='location_coordinates_latitude,location_coordinates_longitude',
                regulation_condition_type=CountryRegulationConditionType.LESS_THAN.value,
                regulation_condition_value='40'
            ),
            CountryRegulationDTO(
                id=str(uuid4()),
                country_code='US',
                country_name='United States',
                fields='location_floor',
                regulation_condition_type=CountryRegulationConditionType.GREATER_THAN_OR_EQUALS.value,
                regulation_condition_value='1'
            ),
            CountryRegulationDTO(
                id=str(uuid4()),
                country_code='CO',
                country_name='Colombia',
                fields='location_floor',
                regulation_condition_type=CountryRegulationConditionType.LESS_THAN.value,
                regulation_condition_value='20'
            ),
            CountryRegulationDTO(
                id=str(uuid4()),
                country_code='CO',
                country_name='Colombia',
                fields='location_floor',
                regulation_condition_type=CountryRegulationConditionType.GREATER_THAN_OR_EQUALS.value,
                regulation_condition_value='1'
            ),
        ]
    )
    db.commit()
else:
    print(colorama.Fore.LIGHTYELLOW_EX + '[Country Regulations] Country regulations already seeded.', colorama.Style.RESET_ALL)

