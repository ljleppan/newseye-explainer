from typing import List, Type

from explainer.core.models import Fact, Message
from explainer.core.realize_slots import SlotRealizerComponent
from explainer.explainer_message_generator import Event
from explainer.resources.processor_resource import ReasonResource

TEMPLATE = """
en: This step was taken to compare datasets that are of different languages, thus limiting the available options.
fi: Tämä tehtiin koska haluttiin verrata kahta eri kielistä aineistoa, mikä rajoittaa käytettävissä olevia analyysityökaluja.
| name = crosslingual_comparison
"""  # noqa: E501


class CrosslingualcomparisonResource(ReasonResource):
    def templates_string(self) -> str:
        return TEMPLATE

    def parse_reason(self, event: Event) -> List[Message]:
        task = event.reason
        if not task or task.name != "crosslingual comparison":
            return []

        return [Message(Fact("reason", "crosslingual_comparison", None, event.id))]

    def slot_realizer_components(self) -> List[Type[SlotRealizerComponent]]:
        return []
