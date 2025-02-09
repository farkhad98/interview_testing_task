from app.models.activity import Activity
from app.models.building import Building
from app.models.organization import Organization
from app.models.organization_activity import OrganizationActivity


async def create_initial_state(db):
    buildings = [
        {"address": "Lyubetsi 31", "longitude": 30.5234, "latitude": 50.4501},
        {"address": "Main St 45", "longitude": -74.0060, "latitude": 40.7128},
        {"address": "Baker St 221B", "longitude": -0.1586, "latitude": 51.5238},
        {"address": "Sunset Blvd 101", "longitude": -118.4912, "latitude": 34.0195},
        {"address": "Fifth Ave 789", "longitude": -73.9855, "latitude": 40.7580},
        {"address": "Rue de Rivoli 12", "longitude": 2.3364, "latitude": 48.8606},
        {"address": "Nevsky Prospekt 25", "longitude": 30.3351, "latitude": 59.9343},
        {"address": "Karl-Marx-Allee 88", "longitude": 13.4312, "latitude": 52.5200},
        {"address": "Via Roma 56", "longitude": 12.4964, "latitude": 41.9028},
        {"address": "Gran Via 23", "longitude": -3.7038, "latitude": 40.4168},
        {"address": "King St 77", "longitude": 144.9631, "latitude": -37.8136},
        {"address": "Ginza 6-10", "longitude": 139.7680, "latitude": 35.6895},
        {"address": "Broadway 123", "longitude": -74.0059, "latitude": 40.7127},
        {"address": "Market St 456", "longitude": -122.4194, "latitude": 37.7749},
        {"address": "Champs-Élysées 99", "longitude": 2.3030, "latitude": 48.8698}
    ]
    db.add_all(
        [
            Building(**building)
            for building in buildings
        ]
    )
    await db.commit()

    activities = [
        # Уровень 1
        {"name": "Construction", "parent_id": None},
        {"name": "Food", "parent_id": None},
        {"name": "Transport", "parent_id": None},
        {"name": "Electronics", "parent_id": None},
        {"name": "Furniture", "parent_id": None},
        {"name": "Testing activity", "parent_id": None}  # 6
    ]
    db.add_all(
        [
            Activity(**activity)
            for activity in activities
        ]
    )
    await db.commit()
    activities_children = [
        # Уровень 2
        {"name": "Bricks", "parent_id": 1},
        {"name": "Cement", "parent_id": 1},
        {"name": "Steel", "parent_id": 1},
        {"name": "Meat", "parent_id": 2},
        {"name": "Vegetables", "parent_id": 2},
        {"name": "Dairy", "parent_id": 2},
        {"name": "Cars", "parent_id": 3},
        {"name": "Bicycles", "parent_id": 3},
        {"name": "Motorcycles", "parent_id": 3},
        {"name": "Phones", "parent_id": 4},
        {"name": "Laptops", "parent_id": 4},
        {"name": "Tablets", "parent_id": 4},
        {"name": "Sofas", "parent_id": 5},
        {"name": "Chairs", "parent_id": 5},
        {"name": "Tables", "parent_id": 5},
        {"name": "testing child activity", "parent_id": 6},  # 22
        {"name": "testing child activity2", "parent_id": 6}  # 23
    ]
    db.add_all(
        [
            Activity(**activity)
            for activity in activities_children
        ]
    )
    await db.commit()
    activities_sub_children = [
        # Уровень 3
        {"name": "Red Bricks", "parent_id": 6},
        {"name": "White Bricks", "parent_id": 6},
        {"name": "Clay Bricks", "parent_id": 6},
        {"name": "Portland Cement", "parent_id": 7},
        {"name": "White Cement", "parent_id": 7},
        {"name": "Rapid Hardening Cement", "parent_id": 7},
        {"name": "Rebar Steel", "parent_id": 8},
        {"name": "Structural Steel", "parent_id": 8},
        {"name": "Stainless Steel", "parent_id": 8},
        {"name": "Beef", "parent_id": 9},
        {"name": "Chicken", "parent_id": 9},
        {"name": "Pork", "parent_id": 9},
        {"name": "Carrots", "parent_id": 10},
        {"name": "Potatoes", "parent_id": 10},
        {"name": "Onions", "parent_id": 10},
        {"name": "Milk", "parent_id": 11},
        {"name": "Cheese", "parent_id": 11},
        {"name": "Yogurt", "parent_id": 11},
        {"name": "Electric Cars", "parent_id": 12},
        {"name": "Gasoline Cars", "parent_id": 12},
        {"name": "Hybrid Cars", "parent_id": 12},
        {"name": "Mountain Bikes", "parent_id": 13},
        {"name": "Road Bikes", "parent_id": 13},
        {"name": "BMX Bikes", "parent_id": 13},
        {"name": "Sport Motorcycles", "parent_id": 14},
        {"name": "Cruiser Motorcycles", "parent_id": 14},
        {"name": "Dirt Bikes", "parent_id": 14},
        {"name": "Android Phones", "parent_id": 15},
        {"name": "iPhones", "parent_id": 15},
        {"name": "Gaming Laptops", "parent_id": 16},
        {"name": "Ultrabooks", "parent_id": 16},
        {"name": "Convertible Tablets", "parent_id": 17},
        {"name": "Drawing Tablets", "parent_id": 17},
        {"name": "Leather Sofas", "parent_id": 18},
        {"name": "Fabric Sofas", "parent_id": 18},
        {"name": "Office Chairs", "parent_id": 19},
        {"name": "Gaming Chairs", "parent_id": 19},
        {"name": "testing sub child", "parent_id": 22},  # 61
        {"name": "testing sub child2", "parent_id": 23},  # 62
        {"name": "testing sub child3", "parent_id": 22}  # 63
    ]
    db.add_all(
        [
            Activity(**activity)
            for activity in activities_sub_children
        ]
    )
    await db.commit()

    organizations = [
        {"name": "OOO RosNeft", "phone": "+78005052276", "building_id": 1},
        {"name": "GazProm", "phone": "+78005052345", "building_id": 2},
        {"name": "Lukoil", "phone": "+78005052456", "building_id": 3},
        {"name": "Sberbank", "phone": "+78005052567", "building_id": 4},
        {"name": "Yandex", "phone": "+78005052678", "building_id": 5},
        {"name": "Tinkoff", "phone": "+78005052789", "building_id": 6},
        {"name": "Mail.ru", "phone": "+78005052890", "building_id": 7},
        {"name": "MegaFon", "phone": "+78005052901", "building_id": 8},
        {"name": "MTS", "phone": "+78005053012", "building_id": 9},
        {"name": "Beeline", "phone": "+78005053123", "building_id": 10},
        {"name": "Rostelecom", "phone": "+78005053234", "building_id": 11},
        {"name": "Ozon", "phone": "+78005053345", "building_id": 12},
        {"name": "Wildberries", "phone": "+78005053456", "building_id": 13},
        {"name": "X5 Retail Group", "phone": "+78005053567", "building_id": 14},
        {"name": "Magnit", "phone": "+78005053678", "building_id": 15},
        {"name": "DNS", "phone": "+78005053789", "building_id": 1},
        {"name": "Eldorado", "phone": "+78005053890", "building_id": 3},
        {"name": "Technopark", "phone": "+78005053901", "building_id": 5},
        {"name": "Citylink", "phone": "+78005054012", "building_id": 7},
        {"name": "Avito", "phone": "+78005054123", "building_id": 9},
        {"name": "Otkritie Bank", "phone": "+78005054234", "building_id": 2},
        {"name": "Alfa Bank", "phone": "+78005054345", "building_id": 4},
        {"name": "VTB", "phone": "+78005054456", "building_id": 6},
        {"name": "Renaissance Credit", "phone": "+78005054567", "building_id": 8},
        {"name": "Pochta Bank", "phone": "+78005054678", "building_id": 10},
        {"name": "Pyaterochka", "phone": "+78005054789", "building_id": 12},
        {"name": "Lenta", "phone": "+78005054890", "building_id": 14},
        {"name": "FixPrice", "phone": "+78005054901", "building_id": 15},
        {"name": "Metro", "phone": "+78005055012", "building_id": 11},
        {"name": "Auchan", "phone": "+78005055123", "building_id": 13},
        {"name": "Sportmaster", "phone": "+78005055234", "building_id": 5},
        {"name": "Adidas", "phone": "+78005055345", "building_id": 7},
        {"name": "Nike", "phone": "+78005055456", "building_id": 9},
        {"name": "Decathlon", "phone": "+78005055567", "building_id": 3},
        {"name": "Teting activity company", "phone": "+78005055545", "building_id": 3},  # 35
        {"name": "Teting activity company2", "phone": "+780050555654", "building_id": 4}  # 36
    ]
    db.add_all(
        [
            Organization(**organization)
            for organization in organizations
        ]
    )
    await db.commit()

    organizationsactivities = [
        {"organization_id": 1, "activity_id": 1},
        {"organization_id": 1, "activity_id": 6},
        {"organization_id": 1, "activity_id": 19},
        {"organization_id": 2, "activity_id": 1},
        {"organization_id": 2, "activity_id": 8},
        {"organization_id": 2, "activity_id": 25},
        {"organization_id": 3, "activity_id": 3},
        {"organization_id": 3, "activity_id": 12},
        {"organization_id": 3, "activity_id": 36},
        {"organization_id": 4, "activity_id": 2},
        {"organization_id": 4, "activity_id": 9},
        {"organization_id": 4, "activity_id": 28},
        {"organization_id": 5, "activity_id": 4},
        {"organization_id": 5, "activity_id": 15},
        {"organization_id": 5, "activity_id": 45},
        {"organization_id": 6, "activity_id": 5},
        {"organization_id": 6, "activity_id": 18},
        {"organization_id": 6, "activity_id": 50},
        {"organization_id": 7, "activity_id": 4},
        {"organization_id": 7, "activity_id": 16},
        {"organization_id": 7, "activity_id": 47},
        {"organization_id": 8, "activity_id": 3},
        {"organization_id": 8, "activity_id": 14},
        {"organization_id": 8, "activity_id": 42},
        {"organization_id": 9, "activity_id": 4},
        {"organization_id": 9, "activity_id": 15},
        {"organization_id": 9, "activity_id": 46},
        {"organization_id": 10, "activity_id": 5},
        {"organization_id": 10, "activity_id": 20},
        {"organization_id": 10, "activity_id": 52},
        {"organization_id": 11, "activity_id": 2},
        {"organization_id": 11, "activity_id": 11},
        {"organization_id": 11, "activity_id": 34},
        {"organization_id": 12, "activity_id": 3},
        {"organization_id": 12, "activity_id": 13},
        {"organization_id": 12, "activity_id": 39},
        {"organization_id": 13, "activity_id": 1},
        {"organization_id": 13, "activity_id": 7},
        {"organization_id": 13, "activity_id": 22},
        {"organization_id": 14, "activity_id": 5},
        {"organization_id": 14, "activity_id": 17},
        {"organization_id": 14, "activity_id": 53},
        {"organization_id": 15, "activity_id": 2},
        {"organization_id": 15, "activity_id": 10},
        {"organization_id": 15, "activity_id": 31},
        #
        {"organization_id": 35, "activity_id": 6},  # 46 without child
        {"organization_id": 35, "activity_id": 22},  # 47 child
        {"organization_id": 35, "activity_id": 61},  # 48 sub child
        {"organization_id": 36, "activity_id": 22}  # 49 child

    ]
    db.add_all(
        [
            OrganizationActivity(**organizationactivity)
            for organizationactivity in organizationsactivities
        ]
    )
    await db.commit()
