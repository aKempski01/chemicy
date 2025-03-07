from enum import Enum

class ItemStatus(Enum):
    Ordered = "Ordered"
    Delivered = "Delivered"
    Opened = "Opened"
    Disposed = "Disposed"
    Missing = "Missing"
    LowLevel = "LowLevel"
    Empty = "Empty"