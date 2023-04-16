from datetime import datetime
from app.jobs.store_in_firestore_job import StoreInFirestoreJob

CURRENT_TIMESTAMP = datetime.now()


def test_store_in_firestore_job(mocker):
    data_entry = {
        "ultima_consulta": CURRENT_TIMESTAMP,
        "dados": [
            {
                "data": CURRENT_TIMESTAMP,
                "vel": 15,
                "dir": 130,
                "alerta": False,
            },
        ]
    }

    execute_mock = mocker.patch(
        "app.jobs.store_in_firestore_job.StoreInFirestoreJob.execute",
        return_value=None
    )

    StoreInFirestoreJob.execute(data_entry)

    execute_mock.assert_called()
