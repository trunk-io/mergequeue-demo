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

DEPENDENCIES = []
AUTO_LOAD = ["sensor"]

CONF_CUSTOM_MIC_SENSOR = "custom_mic_sensor"

custom_mic_sensor_ns = cg.esphome_ns.namespace("custom_mic_sensor")
CustomMicSensor = custom_mic_sensor_ns.class_("CustomMicSensor", cg.Component)

# Define schema manually to avoid circular import
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(CustomMicSensor),
        cv.Optional(CONF_NAME, default="Custom Mic Sensor"): cv.string,
        cv.Optional("unit_of_measurement", default=UNIT_DECIBEL): cv.string,
        cv.Optional("accuracy_decimals", default=1): cv.int_range(min=0, max=10),
        cv.Optional("device_class", default=DEVICE_CLASS_SOUND): cv.string,
        cv.Optional("state_class", default=STATE_CLASS_MEASUREMENT): cv.string,
    }
).extend(cv.polling_component_schema("60s"))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_NAME in config:
        cg.add(var.set_name(config[CONF_NAME]))

    # Add your custom mic sensor implementation here
    # Example:
    # cg.add(var.set_pin(config[CONF_PIN]))
