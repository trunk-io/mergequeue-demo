import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    CONF_NAME,
    DEVICE_CLASS_SOUND,
    STATE_CLASS_MEASUREMENT,
    UNIT_DECIBEL,
)
from esphome.core import CORE

# Remove the problematic import at module level
# import esphome.components.sensor as sensor

DEPENDENCIES = []
AUTO_LOAD = ["sensor"]

CONF_CUSTOM_MIC_SENSOR = "custom_mic_sensor"

custom_mic_sensor_ns = cg.esphome_ns.namespace("custom_mic_sensor")
CustomMicSensor = custom_mic_sensor_ns.class_("CustomMicSensor", cg.Component)


# Use lazy import inside the function
def sensor_schema():
    """Get the sensor schema with lazy import to avoid circular dependency."""
    import esphome.components.sensor as sensor

    return sensor.sensor_schema(
        CustomMicSensor,
        unit_of_measurement=UNIT_DECIBEL,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_SOUND,
        state_class=STATE_CLASS_MEASUREMENT,
    )


CONFIG_SCHEMA = sensor_schema().extend(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(CustomMicSensor),
            cv.Optional(CONF_NAME, default="Custom Mic Sensor"): cv.string,
        }
    ).extend(cv.polling_component_schema("60s"))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_NAME in config:
        cg.add(var.set_name(config[CONF_NAME]))

    # Add your custom mic sensor implementation here
    # Example:
    # cg.add(var.set_pin(config[CONF_PIN]))
