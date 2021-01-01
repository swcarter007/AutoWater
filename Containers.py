from dependency_injector import providers, containers

from FileService import FileService
from PlantFileService import PlantFileService
from IOService import IOService
from WaterService import WaterService
from PlantService import PlantService

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    FileService = providers.Singleton(FileService)
    IOService = providers.Singleton(IOService)
    PlantFileService = providers.Singleton(PlantFileService)
    PlantService = providers.Singleton(PlantService)

    WaterService = providers.Factory(WaterService)
