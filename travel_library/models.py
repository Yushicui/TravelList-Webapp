from dataclasses import dataclass, field

@dataclass 
class Trip:
    """
    A dataclass representing a trip, containing information about the destination, travel details, and user feedback.

    """
    _id: str
    attraction: str
    city: str
    country: str
    travel_days: list[str] = field(default_factory=list)
    best_season: list[str] = field(default_factory=list)
    rating: int = 0
    comments: list[dict] = field(default_factory=list)
    tags: list[str] = field(default_factory=list) 
    description: str = None
    video_link: str = None



