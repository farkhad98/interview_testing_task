from pydantic import BaseModel


class OrganizationsFilterSerializer(BaseModel):
    building_id: int | None = None
    activity_id: int | None = None
    name: str | None = None
    left_top_coordinates_x: float | None = None
    left_top_coordinates_y: float | None = None
    right_top_coordinates_x: float | None = None
    right_top_coordinates_y: float | None = None
    right_bottom_coordinates_x: float | None = None
    right_bottom_coordinates_y: float | None = None
    left_bottom_coordinates_x: float | None = None
    left_bottom_coordinates_y: float | None = None
