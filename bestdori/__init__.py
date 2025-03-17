'''`bestdori`

Bestdori 的各种 API 调用整合，另外附带部分功能'''

from .user import User, Me

from .post import Post
from .charts import Chart

from .characters import Character
from .cards import Card
from .costumes import Costume
from .events import Event
from .eventarchives import EventArchive
from .gacha import Gacha
from .songs import Song
from .logincampaigns import LoginCampaign
from .miracleticket import MiracleTicketExchange
from .comics import Comic
from .missions import Mission

from .exceptions import (
    RequestInvalidError,
    LoginRequiredError,
    CredentialsInvalidError,
    UserInvalidError,
    PostHasNoChartError,
    PostHasNoSongError,
    ServerNotAvailableError,
    AssetsNotExistError,
)

from . import (
    user,
    post,
    charts,
    characters,
    cards,
    costumes,
    events,
    eventarchives,
    gacha,
    songs,
    songmeta,
    logincampaigns,
    miracleticket,
    comics,
    missions,
    models
)

from .settings import settings as settings

__all__ = [
    'User',
    'Me',
    'Post',
    'Chart',
    'Character',
    'Card',
    'Costume',
    'Event',
    'EventArchive',
    'Gacha',
    'Song',
    'LoginCampaign',
    'MiracleTicketExchange',
    'Comic',
    'Mission',
    'RequestInvalidError',
    'LoginRequiredError',
    'CredentialsInvalidError',
    'UserInvalidError',
    'PostHasNoChartError',
    'PostHasNoSongError',
    'ServerNotAvailableError',
    'AssetsNotExistError',
    'user',
    'post',
    'charts',
    'characters',
    'cards',
    'costumes',
    'events',
    'eventarchives',
    'gacha',
    'songs',
    'songmeta',
    'logincampaigns',
    'miracleticket',
    'comics',
    'missions',
    'models',
    'settings'
]