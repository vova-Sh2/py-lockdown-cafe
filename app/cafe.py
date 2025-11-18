import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError"
                                     " should be raised with a message")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccineError"
                                       " should be raised with a message")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("NotWearingMaskError"
                                      " should be raised with a message")
        return f"Welcome to {self.name}"
