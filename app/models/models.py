# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
# from sqlalchemy.ext.declarative import declarative_base
from . import db

# Base = declarative_base()
Base = db.Model

metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None)
            for c in self.__table__.columns}


Base.to_dict = to_dict


class Busines(Base):
    __tablename__ = 'business'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class ChannelSetting(Base):
    __tablename__ = 'channel_settings'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    device_id = Column(String(255))
    channel_index = Column(INTEGER(11))
    channel_type = Column(INTEGER(11))
    channel_alias = Column(String(255))
    created_at = Column(DateTime)


class City(Base):
    __tablename__ = 'city'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    name = Column(String(255))
    province_id = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))
    sys_code = Column(String(255))


class CollectorManagerSetting(Base):
    __tablename__ = 'collector_manager_settings'

    id = Column(INTEGER(11), primary_key=True)
    ping = Column(TIMESTAMP)
    online = Column(INTEGER(11))


class CollectorParam(Base):
    __tablename__ = 'collector_params'

    id = Column(String(255), primary_key=True)
    device_id = Column(String(255), unique=True)
    rate = Column(BIGINT(20))
    ct = Column(INTEGER(11))
    pt = Column(INTEGER(11))
    lct = Column(INTEGER(11))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))


class CollectorStatu(Base):
    __tablename__ = 'collector_status'

    id = Column(INTEGER(11), primary_key=True)
    device_id = Column(String(255))
    status = Column(INTEGER(11))


class CollectorType(Base):
    __tablename__ = 'collector_type'

    id = Column(INTEGER(11), primary_key=True)
    des = Column(String(255))
    des_code = Column(INTEGER(11))


class CommandQueue(Base):
    __tablename__ = 'command_queue'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    device_id = Column(String(255), index=True)
    command = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Company(Base):
    __tablename__ = 'company'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    name = Column(String(255))
    alias = Column(String(255))
    logo = Column(String(255))
    city_id = Column(String(255), index=True)
    address = Column(String(255))
    lat = Column(Float(asdecimal=True))
    lng = Column(Float(asdecimal=True))
    contact_name = Column(String(255))
    contact_phone = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))
    nav_flag = Column(TINYINT(4))
    platform = Column(INTEGER(11), server_default=text("'1'"))
    use_type = Column(INTEGER(11))
    main_total = Column(INTEGER(11))
    main_capacity = Column(Float(asdecimal=True))
    thermal_imager = Column(TINYINT(4))
    humiture_state = Column(TINYINT(4), server_default=text("'0'"))
    transformer_structure = Column(TINYINT(4), server_default=text("'0'"))
    power_period = Column(String(255))
    business_id = Column(String(255))


class DayEnergy(Base):
    __tablename__ = 'day_energy'

    id = Column(String(255), primary_key=True)
    device_no = Column(String(255))
    newest_value = Column(Float(asdecimal=True))
    use_value = Column(Float(asdecimal=True))
    updated_at = Column(DateTime)


class Device(Base):
    __tablename__ = 'device'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    device_id = Column(String(255))
    company_id = Column(String(255))
    group_id = Column(String(255))
    device_addr = Column(String(255))
    location = Column(String(255))
    name = Column(String(255))
    alias = Column(String(255))
    auto_tx = Column(TINYINT(1))
    enable = Column(TINYINT(1), index=True)
    online = Column(TINYINT(1), index=True, server_default=text("'0'"))
    state = Column(INTEGER(11), index=True, server_default=text("'1'"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_ping = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))
    port = Column(INTEGER(11))
    dindex = Column(INTEGER(11), server_default=text("'1'"))
    lat = Column(Float(asdecimal=True))
    lng = Column(Float(asdecimal=True))
    platform = Column(INTEGER(11), server_default=text("'1'"))
    can_break = Column(TINYINT(4))
    start = Column(TINYINT(4))
    discon_state = Column(TINYINT(4))
    collect_type = Column(INTEGER(11))
    hub_host = Column(String(255))
    hub_port = Column(INTEGER(11))
    type = Column(INTEGER(11))
    parent_id = Column(String(255))
    hardware_type = Column(INTEGER(11))
    device_type = Column(String(255))
    gateway_code = Column(INTEGER(255))
    gateway_type = Column(String(255))
    gateway_port = Column(INTEGER(11))
    calculate_status = Column(TINYINT(4))
    device_level = Column(INTEGER(11))
    device_parent = Column(String(255))


class DeviceDisconHistory(Base):
    __tablename__ = 'device_discon_history'

    id = Column(String(255), primary_key=True)
    device_id = Column(String(255))
    type = Column(INTEGER(11))
    created_at = Column(DateTime)


class DeviceGroup(Base):
    __tablename__ = 'device_group'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    company_id = Column(String(255), index=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))


class DeviceHourEnergy(Base):
    __tablename__ = 'device_hour_energy'
    __table_args__ = (
        Index('companyId_daydate', 'company_id', 'day_date'),
    )

    id = Column(INTEGER(10), primary_key=True)
    company_id = Column(String(255), index=True)
    device_id = Column(String(255), index=True)
    day_date = Column(DateTime, index=True)
    h0 = Column(Float(asdecimal=True))
    h1 = Column(Float(asdecimal=True))
    h2 = Column(Float(asdecimal=True))
    h3 = Column(Float(asdecimal=True))
    h4 = Column(Float(asdecimal=True))
    h5 = Column(Float(asdecimal=True))
    h6 = Column(Float(asdecimal=True))
    h7 = Column(Float(asdecimal=True))
    h8 = Column(Float(asdecimal=True))
    h9 = Column(Float(asdecimal=True))
    h10 = Column(Float(asdecimal=True))
    h11 = Column(Float(asdecimal=True))
    h12 = Column(Float(asdecimal=True))
    h13 = Column(Float(asdecimal=True))
    h14 = Column(Float(asdecimal=True))
    h15 = Column(Float(asdecimal=True))
    h16 = Column(Float(asdecimal=True))
    h17 = Column(Float(asdecimal=True))
    h18 = Column(Float(asdecimal=True))
    h19 = Column(Float(asdecimal=True))
    h20 = Column(Float(asdecimal=True))
    h21 = Column(Float(asdecimal=True))
    h22 = Column(Float(asdecimal=True))
    h23 = Column(Float(asdecimal=True))
    h24 = Column(Float(asdecimal=True))
    created_at = Column(DateTime)


class DeviceManufacturer(Base):
    __tablename__ = 'device_manufacturer'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class DeviceModel(Base):
    __tablename__ = 'device_model'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    model = Column(String(255))
    type = Column(INTEGER(11))
    manufacturer_id = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class DeviceParam(Base):
    __tablename__ = 'device_params'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    device_id = Column(String(255))
    params_type = Column(INTEGER(11))
    warn_up = Column(Float)
    warn_down = Column(Float)
    error_up = Column(Float)
    error_down = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))
    channel = Column(INTEGER(11))


class DeviceProtocol(Base):
    __tablename__ = 'device_protocol'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class DeviceSery(Base):
    __tablename__ = 'device_series'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class DeviceStatusLog(Base):
    __tablename__ = 'device_status_log'

    id = Column(String(100), primary_key=True, server_default=text("''"))
    device_no = Column(String(100), index=True)
    status = Column(INTEGER(1), index=True, server_default=text("'1'"))
    created_at = Column(DateTime)


class DeviceThreshold(Base):
    __tablename__ = 'device_threshold'

    id = Column(String(255), primary_key=True)
    device_id = Column(String(255))
    threshold_number = Column(INTEGER(11))
    threshold_value = Column(String(100))
    updated_at = Column(DateTime)


class DeviceType(Base):
    __tablename__ = 'device_type'

    id = Column(String(255), primary_key=True)
    type = Column(INTEGER(11))
    name = Column(String(255))
    series_id = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class Dtu(Base):
    __tablename__ = 'dtu'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    dtu_id = Column(String(255), index=True)
    company_id = Column(String(255), index=True)
    group_id = Column(String(255), index=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))


class EnergyLevel(Base):
    __tablename__ = 'energy_level'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    level = Column(INTEGER(11))
    city_id = Column(String(255), index=True)
    start_time = Column(String(255))
    end_time = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))


class EnergyMeasurement(Base):
    __tablename__ = 'energy_measurement'

    device_no = Column(String(255), primary_key=True)
    week_power = Column(Float(10, True))
    lastweek_power = Column(Float(10, True))
    power_range = Column(Float(10, True))
    power_rate = Column(Float(10, True))
    newest_value = Column(Float(10, True))
    updated_at = Column(DateTime)


class EnergyPrice(Base):
    __tablename__ = 'energy_price'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    city_id = Column(String(255), index=True)
    level = Column(INTEGER(11))
    price = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))


class EnergyReport(Base):
    __tablename__ = 'energy_report'

    device_no = Column(String(50), primary_key=True)
    newest_val = Column(Float(asdecimal=True), server_default=text("'0'"))
    today_val = Column(Float(asdecimal=True), server_default=text("'0'"))
    yesterday_val = Column(Float(asdecimal=True), server_default=text("'0'"))
    currMonth_val = Column(Float(asdecimal=True), server_default=text("'0'"))
    lastMonth_val = Column(Float(asdecimal=True), server_default=text("'0'"))
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
    remark = Column(String(255))


class ExceptionNotification(Base):
    __tablename__ = 'exception_notification'

    id = Column(String(255), primary_key=True)
    exception_id = Column(String(255))
    user_id = Column(String(255))
    content = Column(String(255))
    created_at = Column(DateTime)


class Exception(Base):
    __tablename__ = 'exceptions'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    device_id = Column(String(255), index=True)
    params_type = Column(INTEGER(11))
    value = Column(Float)
    warn_up = Column(Float)
    warn_down = Column(Float)
    error_up = Column(Float)
    error_down = Column(Float)
    type = Column(INTEGER(11))
    content = Column(String(255))
    disposed = Column(TINYINT(1))
    silent = Column(TINYINT(1))
    url = Column(String(255), server_default=text("''"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))
    memorandum = Column(String(255))
    operation_user = Column(String(255))
    inform = Column(TINYINT(1))


class GatewayDevice(Base):
    __tablename__ = 'gateway_device'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    gateway_type = Column(String(255))
    port = Column(INTEGER(11))
    collect_period = Column(INTEGER(11))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class GatewayType(Base):
    __tablename__ = 'gateway_type'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class IotTelecomSubsrcibe(Base):
    __tablename__ = 'iot_telecom_subsrcibe'

    id = Column(String(255), primary_key=True)
    subscribe_id = Column(String(255))
    subscribe_url = Column(String(255))
    callback_url = Column(String(255))
    notify_type = Column(String(255))
    _del = Column('del', TINYINT(4))
    created_at = Column(DateTime)


class LatestDatum(Base):
    __tablename__ = 'latest_data'

    id = Column(INTEGER(10), primary_key=True)
    device_id = Column(String(255), nullable=False, index=True, server_default=text("''"))
    type = Column(INTEGER(11), index=True)
    value = Column(Float(asdecimal=True))
    des = Column(String(255))
    unit = Column(String(255))
    updated_at = Column(DateTime)


class Message(Base):
    __tablename__ = 'message'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    title = Column(String(255))
    content = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))


t_message_read = Table(
    'message_read', metadata,
    Column('message_id', String(255), nullable=False, index=True, server_default=text("''")),
    Column('user_id', String(255), nullable=False, index=True, server_default=text("''"))
)


class OnetDevice(Base):
    __tablename__ = 'onet_device'

    id = Column(String(255), primary_key=True)
    device_name = Column(String(255))
    device_id = Column(String(255))
    device_alias = Column(String(255))
    location = Column(String(255))
    imei = Column(String(255))
    imsi = Column(String(255))
    device_type = Column(String(255))
    onet_id = Column(String(255))
    group_id = Column(String(255))
    company_id = Column(String(255))
    online_state = Column(TINYINT(4))
    device_status = Column(INTEGER(11))
    onet_type = Column(INTEGER(11))
    enable_state = Column(TINYINT(4))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class OnetDeviceDatum(Base):
    __tablename__ = 'onet_device_data'

    id = Column(String(255), primary_key=True)
    od_id = Column(String(255))
    temp_value = Column(Float(asdecimal=True))
    humi_value = Column(Float(asdecimal=True))
    valtage_value = Column(Float(asdecimal=True))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class OnetDeviceError(Base):
    __tablename__ = 'onet_device_error'

    id = Column(String(255), primary_key=True)
    od_id = Column(String(255))
    company_id = Column(String(255))
    data_type = Column(INTEGER(11))
    error_value = Column(Float(asdecimal=True))
    content = Column(String(255))
    error_status = Column(INTEGER(11))
    remark = Column(String(255))
    recover_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class OnetDeviceParam(Base):
    __tablename__ = 'onet_device_param'

    id = Column(String(255), primary_key=True)
    od_id = Column(String(255))
    temp_upper = Column(Float)
    temp_lower = Column(Float)
    humidness_upper = Column(Float)
    humidness_lower = Column(Float)
    voltage_error = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class OnetDeviceType(Base):
    __tablename__ = 'onet_device_type'

    id = Column(String(255), primary_key=True)
    type_name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class Province(Base):
    __tablename__ = 'province'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    type = Column(INTEGER(11))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))
    sys_code = Column(String(255))


class ReleaseVersion(Base):
    __tablename__ = 'release_version'

    id = Column(INTEGER(10), primary_key=True)
    android = Column(Float(255))
    ios = Column(Float(255))
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
    remark = Column(String(255))


class Role(Base):
    __tablename__ = 'role'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    name = Column(String(255))
    description = Column(String(500), server_default=text("''"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))


class ServiceLog(Base):
    __tablename__ = 'service_log'

    id = Column(String(255), primary_key=True)
    device_no = Column(String(255), server_default=text("''"))
    customer_name = Column(String(255), server_default=text("''"))
    type = Column(INTEGER(11))
    remark = Column(Text)
    event_date = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4))


class SetInterval(Base):
    __tablename__ = 'set_interval'

    id = Column(INTEGER(11), primary_key=True)
    hours = Column(INTEGER(11))
    type = Column(INTEGER(11))
    platform = Column(INTEGER(11), server_default=text("'3'"))
    company_id = Column(String(255))


class SysConfig(Base):
    __tablename__ = 'sys_config'

    id = Column(INTEGER(10), primary_key=True)
    android_version = Column(Float)
    android_content = Column(String(255), server_default=text("''"))
    android_link = Column(String(255), server_default=text("''"))
    ios_version = Column(Float(4))
    ios_content = Column(String(255), server_default=text("''"))
    ios_link = Column(String(255), server_default=text("''"))
    wechat_link = Column(String(255), server_default=text("''"))
    about = Column(String(255))
    run_env = Column(INTEGER(11), server_default=text("'1'"))
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
    remark = Column(String(255), server_default=text("''"))
    notice_email = Column(String(255), server_default=text("''"))
    notice_phone = Column(String(255), server_default=text("''"))


class SysNew(Base):
    __tablename__ = 'sys_news'

    id = Column(String(255), primary_key=True)
    title = Column(String(255))
    news_abstract = Column(String(255))
    cover = Column(String(255))
    xindex = Column(INTEGER(11))
    url = Column(String(255))
    user_id = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class ThermalImager(Base):
    __tablename__ = 'thermal_imager'

    id = Column(String(255), primary_key=True)
    device_no = Column(String(255))
    name = Column(String(255))
    alias = Column(String(255))
    model_id = Column(String(255))
    company_id = Column(String(255))
    group_id = Column(String(255))
    channel_ip = Column(String(255))
    http_port = Column(INTEGER(255))
    rtsp_port = Column(INTEGER(11))
    location = Column(String(255))
    enable = Column(TINYINT(4))
    protocol_id = Column(String(255))
    vendor_id = Column(String(255))
    type = Column(INTEGER(11))
    heat_status = Column(TINYINT(4))
    video_status = Column(TINYINT(4))
    nvr_id = Column(String(255))
    online = Column(TINYINT(4))
    hav_nvr = Column(TINYINT(4))
    hav_ptz = Column(TINYINT(4))
    network_type = Column(INTEGER(11))
    status = Column(INTEGER(11))
    video_nvr_stream = Column(String(255))
    heat_nvr_stream = Column(String(255))
    video_direct_stream = Column(String(255))
    heat_direct_stream = Column(String(255))
    camera_video_code = Column(String(255))
    camera_thermal_code = Column(String(255))
    _del = Column('del', TINYINT(4))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class ThermalImagerCoordinate(Base):
    __tablename__ = 'thermal_imager_coordinate'

    id = Column(String(255), primary_key=True)
    thermal_imager_id = Column(String(255))
    P_1 = Column(String(255))
    P_2 = Column(String(255))
    P_3 = Column(String(255))
    P_4 = Column(String(255))
    P_5 = Column(String(255))
    P_6 = Column(String(255))
    A_1 = Column(String(255))
    A_2 = Column(String(255))
    A_3 = Column(String(255))
    A_4 = Column(String(255))
    A_5 = Column(String(255))
    A_6 = Column(String(255))
    line = Column(String(255))
    collect_rate = Column(INTEGER(11))
    error_temp = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class ThermalImagerError(Base):
    __tablename__ = 'thermal_imager_error'

    id = Column(String(255), primary_key=True)
    thermal_imager_id = Column(String(255))
    type = Column(INTEGER(11))
    index = Column(INTEGER(11))
    param = Column(String(255))
    value = Column(Float)
    error_temp = Column(Float)
    status = Column(INTEGER(11))
    content = Column(String(255))
    recover_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class ThermalImagerTemp(Base):
    __tablename__ = 'thermal_imager_temp'

    id = Column(String(255), primary_key=True)
    thermal_imager_id = Column(String(255))
    type = Column(INTEGER(11))
    index = Column(INTEGER(11))
    param = Column(String(255))
    value = Column(Float)
    created_at = Column(DateTime)


class ThresholdParam(Base):
    __tablename__ = 'threshold_params'

    id = Column(String(255), primary_key=True)
    param_number = Column(INTEGER(11))
    param = Column(String(255))
    type = Column(INTEGER(11))
    pindex = Column(INTEGER(11))
    created_at = Column(DateTime)
    unit = Column(String(255))


class User(Base):
    __tablename__ = 'user'

    id = Column(String(255), primary_key=True, server_default=text("''"))
    name = Column(String(255))
    username = Column(String(255), index=True)
    password = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))
    company_id = Column(String(255), index=True)
    role_id = Column(String(255), index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    _del = Column('del', TINYINT(4), server_default=text("'0'"))
    url = Column(String(255))
    job = Column(String(255))
    platform = Column(INTEGER(11))
    area_id = Column(String(255))


class UserCompany(Base):
    __tablename__ = 'user_company'

    id = Column(INTEGER(10), primary_key=True)
    user_id = Column(String(250), nullable=False, index=True, server_default=text("''"))
    company_id = Column(String(250), nullable=False, index=True, server_default=text("''"))


class UserProduct(Base):
    __tablename__ = 'user_product'

    id = Column(String(255), primary_key=True)
    user_id = Column(String(255))
    product = Column(String(255))
    created_at = Column(DateTime)


class VideoRecorder(Base):
    __tablename__ = 'video_recorder'

    id = Column(String(255), primary_key=True)
    device_no = Column(String(255))
    name = Column(String(255))
    model_id = Column(String(255))
    vendor_id = Column(String(255))
    company_id = Column(String(255))
    group_id = Column(String(255))
    channel_ip = Column(String(255))
    channel_port = Column(INTEGER(11))
    location = Column(String(255))
    enable = Column(TINYINT(4))
    protocol_id = Column(String(255))
    online = Column(TINYINT(4))
    status = Column(INTEGER(11))
    _del = Column('del', TINYINT(4))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class WasionSyncInfo(Base):
    __tablename__ = 'wasion_sync_info'

    id = Column(INTEGER(10), primary_key=True)
    device_date = Column(DateTime)
    company_date = Column(DateTime)
    group_date = Column(DateTime)
    real_date = Column(DateTime)
