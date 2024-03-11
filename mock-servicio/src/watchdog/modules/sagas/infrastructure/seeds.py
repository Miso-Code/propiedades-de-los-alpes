from uuid import uuid4
import colorama
from .dto import TransactionDTO
from ....config.db import db


existing_records = db.query(TransactionDTO).count()


if existing_records == 0:
    print(colorama.Fore.LIGHTYELLOW_EX + '[Sagas] Seeding Transactions...', colorama.Style.RESET_ALL)
    db.bulk_save_objects(
        [
            TransactionDTO(
                id=str(uuid4()),
                event='PropertyIngestionCreatedEvent',
                error='PropertyIngestionFailedEvent',
                compensation='DeletePropertyIngestionCommand',
                compensation_topic='property-ingestion-delete-commands',
                order=1,
            ),
            TransactionDTO(
                id=str(uuid4()),
                event='PropertyIngestionValidatedEvent',
                error='PropertyIngestionRejectedEvent',
                compensation='DisapprovePropertyIngestionCommand',
                compensation_topic='data-control-commands',
                order=2,
            ),
            TransactionDTO(
                id=str(uuid4()),
                event='PropertyCreatedEvent',
                error='PropertyNotCreatedEvent',
                compensation='DeletePropertyEvent', #Not used
                compensation_topic='property-commands',
                order=3,
                is_last=True,
            ),
        ]
    )
    db.commit()
else:
    print(colorama.Fore.LIGHTYELLOW_EX + '[Sagas] Transactions already seeded.', colorama.Style.RESET_ALL)

