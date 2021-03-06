import logging
from typing import List, Type

from explainer.core.models import Fact, Message
from explainer.core.realize_slots import SlotRealizerComponent
from explainer.explainer_message_generator import Event
from explainer.resources.processor_resource import TaskResource

log = logging.getLogger("root")

TEMPLATE = """
en: The publication years, newspapers names and languages of the documents were extracted.
fi: Aineistosta etsittiin siinä esiintyvät julkaisuvuodet, sanomalehtien nimet ja kielet.
de: Die Erscheinungsjahre, Zeitungsnamen und Sprachen der Dokumente wurden extrahiert.
fr: Les années de publication, les titres des journaux et les langues des documents ont été extraits.
| name = ExtractFacets
"""


class ExtractFacetsResource(TaskResource):
    def templates_string(self) -> str:
        return TEMPLATE

    def parse_task(self, event: Event) -> List[Message]:
        task = event.task
        if not task or task.name != "ExtractFacets":
            return []

        return [Message(Fact("task", "ExtractFacets", None, event.id))]

    def slot_realizer_components(self) -> List[Type[SlotRealizerComponent]]:
        return []
