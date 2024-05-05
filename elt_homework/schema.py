from pandera import Column, DataFrameSchema

ProductSchema = DataFrameSchema(
    columns={
        "manufacturer_sku": Column(str),
        "ean13": Column(str, nullable=True),
        "cost_price": Column(float, nullable=True),
        "product__title": Column(str),
        "product__brand__name": Column(str),
        "product__product_class__name": Column(str),
        "attrib__outdoor_safe": Column(bool),
        "width": Column(float, nullable=True),
        "length": Column(float, nullable=True),
        "height": Column(float, nullable=True),
        "weight": Column(float, nullable=True),
        "attrib__material": Column(str, nullable=True),
        "attrib__finish": Column(str, nullable=True),
        "prop_65": Column(str, nullable=True),
        "product__styles": Column(str, nullable=True),
        "product__multipack_quantity": Column(int, nullable=True),
        "boxes__0__width": Column(float, nullable=True),
        "boxes__0__length": Column(float, nullable=True),
        "boxes__0__height": Column(float, nullable=True),
        "boxes__0__weight": Column(float, nullable=True),
        "boxes__1__width": Column(float, nullable=True),
        "boxes__1__length": Column(float, nullable=True),
        "boxes__1__height": Column(float, nullable=True),
        "boxes__1__weight": Column(float, nullable=True),
        "boxes__2__width": Column(float, nullable=True),
        "boxes__2__length": Column(float, nullable=True),
        "boxes__2__height": Column(float, nullable=True),
        "boxes__2__weight": Column(float, nullable=True),
        "attrib__kit": Column(bool, nullable=True),
        "attrib__ul_certified": Column(str, nullable=True),
        "attrib__number_bulbs": Column(int, nullable=True),
        "attrib__wattage": Column(float, nullable=True),
        "attrib__bulb_type": Column(str, nullable=True),
        "attrib__bulb_included": Column(bool, nullable=True),
        "attrib__switch_type": Column(str, nullable=True),
        "attrib__shade": Column(str, nullable=True),
        "attrib__cord_length": Column(float, nullable=True),
        "attrib__arm_height": Column(float, nullable=True),
        "attrib__seat_height": Column(float, nullable=True),
        "attrib__seat_width": Column(dtype="object", nullable=True),  #  20x24
        "attrib__weight_capacity": Column(float, nullable=True),
        "product__country_of_origin__alpha_3": Column(str, nullable=True),
        "product__bullets__1": Column(str, nullable=True),
        "product__bullets__2": Column(str, nullable=True),
        "product__bullets__3": Column(str, nullable=True),
        "product__bullets__4": Column(str, nullable=True),
        "product__bullets__5": Column(str, nullable=True),
        "product__bullets__6": Column(str, nullable=True),
    }
)

