# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from ...inboxes.types.inbox_id import InboxId
from ...messages.types.message import Message
from .thread_attachments import ThreadAttachments
from .thread_id import ThreadId
from .thread_labels import ThreadLabels
from .thread_message_count import ThreadMessageCount
from .thread_preview import ThreadPreview
from .thread_recipients import ThreadRecipients
from .thread_senders import ThreadSenders
from .thread_subject import ThreadSubject
from .thread_timestamp import ThreadTimestamp


class Thread(UncheckedBaseModel):
    inbox_id: InboxId
    thread_id: ThreadId
    labels: ThreadLabels
    timestamp: ThreadTimestamp
    senders: ThreadSenders
    recipients: ThreadRecipients
    subject: typing.Optional[ThreadSubject] = None
    preview: typing.Optional[ThreadPreview] = None
    attachments: typing.Optional[ThreadAttachments] = None
    message_count: ThreadMessageCount
    messages: typing.List[Message] = pydantic.Field()
    """
    Messages in thread. Ordered by `timestamp` ascending.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Time at which thread was last updated.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Time at which thread was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
