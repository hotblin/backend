# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, DateTime, String, Table, Text, Time, VARBINARY, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CmsHelp(Base):
    __tablename__ = 'cms_help'

    id = Column(BIGINT(20), primary_key=True)
    category_id = Column(BIGINT(20))
    icon = Column(String(500))
    title = Column(String(100))
    show_status = Column(INTEGER(1))
    create_time = Column(DateTime)
    read_count = Column(INTEGER(1))
    content = Column(Text)


class CmsHelpCategory(Base):
    __tablename__ = 'cms_help_category'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    icon = Column(String(500))
    help_count = Column(INTEGER(11))
    show_status = Column(INTEGER(2))
    sort = Column(INTEGER(11))


t_cms_member_report = Table(
    'cms_member_report', metadata,
    Column('id', BIGINT(20)),
    Column('report_type', INTEGER(1)),
    Column('report_member_name', String(100)),
    Column('create_time', DateTime),
    Column('report_object', String(100)),
    Column('report_status', INTEGER(1)),
    Column('handle_status', INTEGER(1)),
    Column('note', String(200))
)


class CmsPrefrenceArea(Base):
    __tablename__ = 'cms_prefrence_area'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255))
    sub_title = Column(String(255))
    pic = Column(VARBINARY(500))
    sort = Column(INTEGER(11))
    show_status = Column(INTEGER(1))


class CmsPrefrenceAreaProductRelation(Base):
    __tablename__ = 'cms_prefrence_area_product_relation'

    id = Column(BIGINT(20), primary_key=True)
    prefrence_area_id = Column(BIGINT(20))
    product_id = Column(BIGINT(20))


class CmsSubject(Base):
    __tablename__ = 'cms_subject'

    id = Column(BIGINT(20), primary_key=True)
    category_id = Column(BIGINT(20))
    title = Column(String(100))
    pic = Column(String(500))
    product_count = Column(INTEGER(11))
    recommend_status = Column(INTEGER(1))
    create_time = Column(DateTime)
    collect_count = Column(INTEGER(11))
    read_count = Column(INTEGER(11))
    comment_count = Column(INTEGER(11))
    album_pics = Column(String(1000))
    description = Column(String(1000))
    show_status = Column(INTEGER(1))
    content = Column(Text)
    forward_count = Column(INTEGER(11))
    category_name = Column(String(200))


class CmsSubjectCategory(Base):
    __tablename__ = 'cms_subject_category'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    icon = Column(String(500))
    subject_count = Column(INTEGER(11))
    show_status = Column(INTEGER(2))
    sort = Column(INTEGER(11))


class CmsSubjectComment(Base):
    __tablename__ = 'cms_subject_comment'

    id = Column(BIGINT(20), primary_key=True)
    subject_id = Column(BIGINT(20))
    member_nick_name = Column(String(255))
    member_icon = Column(String(255))
    content = Column(String(1000))
    create_time = Column(DateTime)
    show_status = Column(INTEGER(1))


class CmsSubjectProductRelation(Base):
    __tablename__ = 'cms_subject_product_relation'

    id = Column(BIGINT(20), primary_key=True)
    subject_id = Column(BIGINT(20))
    product_id = Column(BIGINT(20))


class CmsTopic(Base):
    __tablename__ = 'cms_topic'

    id = Column(BIGINT(20), primary_key=True)
    category_id = Column(BIGINT(20))
    name = Column(String(255))
    create_time = Column(DateTime)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    attend_count = Column(INTEGER(11))
    attention_count = Column(INTEGER(11))
    read_count = Column(INTEGER(11))
    award_name = Column(String(100))
    attend_type = Column(String(100))
    content = Column(Text)


class CmsTopicCategory(Base):
    __tablename__ = 'cms_topic_category'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    icon = Column(String(500))
    subject_count = Column(INTEGER(11))
    show_status = Column(INTEGER(2))
    sort = Column(INTEGER(11))


class CmsTopicComment(Base):
    __tablename__ = 'cms_topic_comment'

    id = Column(BIGINT(20), primary_key=True)
    member_nick_name = Column(String(255))
    topic_id = Column(BIGINT(20))
    member_icon = Column(String(255))
    content = Column(String(1000))
    create_time = Column(DateTime)
    show_status = Column(INTEGER(1))


class OmsCartItem(Base):
    __tablename__ = 'oms_cart_item'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    product_sku_id = Column(BIGINT(20))
    member_id = Column(BIGINT(20))
    quantity = Column(INTEGER(11))
    price = Column(DECIMAL(10, 2))
    sp1 = Column(String(200))
    sp2 = Column(String(200))
    sp3 = Column(String(200))
    product_pic = Column(String(1000))
    product_name = Column(String(500))
    product_sub_title = Column(String(500))
    product_sku_code = Column(String(200))
    member_nickname = Column(String(500))
    create_date = Column(DateTime)
    modify_date = Column(DateTime)
    delete_status = Column(INTEGER(1), server_default=text("'0'"))
    product_category_id = Column(BIGINT(20))
    product_brand = Column(String(200))
    product_sn = Column(String(200))
    product_attr = Column(String(500))


class OmsCompanyAddres(Base):
    __tablename__ = 'oms_company_address'

    id = Column(BIGINT(20), primary_key=True)
    address_name = Column(String(200))
    send_status = Column(INTEGER(1))
    receive_status = Column(INTEGER(1))
    name = Column(String(64))
    phone = Column(String(64))
    province = Column(String(64))
    city = Column(String(64))
    region = Column(String(64))
    detail_address = Column(String(200))


class OmsOrder(Base):
    __tablename__ = 'oms_order'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20), nullable=False)
    coupon_id = Column(BIGINT(20))
    order_sn = Column(String(64))
    create_time = Column(DateTime)
    member_username = Column(String(64))
    total_amount = Column(DECIMAL(10, 2))
    pay_amount = Column(DECIMAL(10, 2))
    freight_amount = Column(DECIMAL(10, 2))
    promotion_amount = Column(DECIMAL(10, 2))
    integration_amount = Column(DECIMAL(10, 2))
    coupon_amount = Column(DECIMAL(10, 2))
    discount_amount = Column(DECIMAL(10, 2))
    pay_type = Column(INTEGER(1))
    source_type = Column(INTEGER(1))
    status = Column(INTEGER(1))
    order_type = Column(INTEGER(1))
    delivery_company = Column(String(64))
    delivery_sn = Column(String(64))
    auto_confirm_day = Column(INTEGER(11))
    integration = Column(INTEGER(11))
    growth = Column(INTEGER(11))
    promotion_info = Column(String(100))
    bill_type = Column(INTEGER(1))
    bill_header = Column(String(200))
    bill_content = Column(String(200))
    bill_receiver_phone = Column(String(32))
    bill_receiver_email = Column(String(64))
    receiver_name = Column(String(100), nullable=False)
    receiver_phone = Column(String(32), nullable=False)
    receiver_post_code = Column(String(32))
    receiver_province = Column(String(32))
    receiver_city = Column(String(32))
    receiver_region = Column(String(32))
    receiver_detail_address = Column(String(200))
    note = Column(String(500))
    confirm_status = Column(INTEGER(1))
    delete_status = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    use_integration = Column(INTEGER(11))
    payment_time = Column(DateTime)
    delivery_time = Column(DateTime)
    receive_time = Column(DateTime)
    comment_time = Column(DateTime)
    modify_time = Column(DateTime)


class OmsOrderItem(Base):
    __tablename__ = 'oms_order_item'

    id = Column(BIGINT(20), primary_key=True)
    order_id = Column(BIGINT(20))
    order_sn = Column(String(64))
    product_id = Column(BIGINT(20))
    product_pic = Column(String(500))
    product_name = Column(String(200))
    product_brand = Column(String(200))
    product_sn = Column(String(64))
    product_price = Column(DECIMAL(10, 2))
    product_quantity = Column(INTEGER(11))
    product_sku_id = Column(BIGINT(20))
    product_sku_code = Column(String(50))
    product_category_id = Column(BIGINT(20))
    sp1 = Column(String(100))
    sp2 = Column(String(100))
    sp3 = Column(String(100))
    promotion_name = Column(String(200))
    promotion_amount = Column(DECIMAL(10, 2))
    coupon_amount = Column(DECIMAL(10, 2))
    integration_amount = Column(DECIMAL(10, 2))
    real_amount = Column(DECIMAL(10, 2))
    gift_integration = Column(INTEGER(11), server_default=text("'0'"))
    gift_growth = Column(INTEGER(11), server_default=text("'0'"))
    product_attr = Column(String(500))


class OmsOrderOperateHistory(Base):
    __tablename__ = 'oms_order_operate_history'

    id = Column(BIGINT(20), primary_key=True)
    order_id = Column(BIGINT(20))
    operate_man = Column(String(100))
    create_time = Column(DateTime)
    order_status = Column(INTEGER(1))
    note = Column(String(500))


class OmsOrderReturnApply(Base):
    __tablename__ = 'oms_order_return_apply'

    id = Column(BIGINT(20), primary_key=True)
    order_id = Column(BIGINT(20))
    company_address_id = Column(BIGINT(20))
    product_id = Column(BIGINT(20))
    order_sn = Column(String(64))
    create_time = Column(DateTime)
    member_username = Column(String(64))
    return_amount = Column(DECIMAL(10, 2))
    return_name = Column(String(100))
    return_phone = Column(String(100))
    status = Column(INTEGER(1))
    handle_time = Column(DateTime)
    product_pic = Column(String(500))
    product_name = Column(String(200))
    product_brand = Column(String(200))
    product_attr = Column(String(500))
    product_count = Column(INTEGER(11))
    product_price = Column(DECIMAL(10, 2))
    product_real_price = Column(DECIMAL(10, 2))
    reason = Column(String(200))
    description = Column(String(500))
    proof_pics = Column(String(1000))
    handle_note = Column(String(500))
    handle_man = Column(String(100))
    receive_man = Column(String(100))
    receive_time = Column(DateTime)
    receive_note = Column(String(500))


class OmsOrderReturnReason(Base):
    __tablename__ = 'oms_order_return_reason'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    sort = Column(INTEGER(11))
    status = Column(INTEGER(1))
    create_time = Column(DateTime)


class OmsOrderSetting(Base):
    __tablename__ = 'oms_order_setting'

    id = Column(BIGINT(20), primary_key=True)
    flash_order_overtime = Column(INTEGER(11))
    normal_order_overtime = Column(INTEGER(11))
    confirm_overtime = Column(INTEGER(11))
    finish_overtime = Column(INTEGER(11))
    comment_overtime = Column(INTEGER(11))


class PmsAlbum(Base):
    __tablename__ = 'pms_album'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(64))
    cover_pic = Column(String(1000))
    pic_count = Column(INTEGER(11))
    sort = Column(INTEGER(11))
    description = Column(String(1000))


class PmsAlbumPic(Base):
    __tablename__ = 'pms_album_pic'

    id = Column(BIGINT(20), primary_key=True)
    album_id = Column(BIGINT(20))
    pic = Column(String(1000))


class PmsBrand(Base):
    __tablename__ = 'pms_brand'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(64))
    first_letter = Column(String(8))
    sort = Column(INTEGER(11))
    factory_status = Column(INTEGER(1))
    show_status = Column(INTEGER(1))
    product_count = Column(INTEGER(11))
    product_comment_count = Column(INTEGER(11))
    logo = Column(String(255))
    big_pic = Column(String(255))
    brand_story = Column(Text)


class PmsComment(Base):
    __tablename__ = 'pms_comment'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    member_nick_name = Column(String(255))
    product_name = Column(String(255))
    star = Column(INTEGER(3))
    member_ip = Column(String(64))
    create_time = Column(DateTime)
    show_status = Column(INTEGER(1))
    product_attribute = Column(String(255))
    collect_couont = Column(INTEGER(11))
    read_count = Column(INTEGER(11))
    content = Column(Text)
    pics = Column(String(1000))
    member_icon = Column(String(255))
    replay_count = Column(INTEGER(11))


class PmsCommentReplay(Base):
    __tablename__ = 'pms_comment_replay'

    id = Column(BIGINT(20), primary_key=True)
    comment_id = Column(BIGINT(20))
    member_nick_name = Column(String(255))
    member_icon = Column(String(255))
    content = Column(String(1000))
    create_time = Column(DateTime)
    type = Column(INTEGER(1))


class PmsFeightTemplate(Base):
    __tablename__ = 'pms_feight_template'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(64))
    charge_type = Column(INTEGER(1))
    first_weight = Column(DECIMAL(10, 2))
    first_fee = Column(DECIMAL(10, 2))
    continue_weight = Column(DECIMAL(10, 2))
    continme_fee = Column(DECIMAL(10, 2))
    dest = Column(String(255))


class PmsMemberPrice(Base):
    __tablename__ = 'pms_member_price'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    member_level_id = Column(BIGINT(20))
    member_price = Column(DECIMAL(10, 2))
    member_level_name = Column(String(100))


class PmsProduct(Base):
    __tablename__ = 'pms_product'

    id = Column(BIGINT(20), primary_key=True)
    brand_id = Column(BIGINT(20))
    product_category_id = Column(BIGINT(20))
    feight_template_id = Column(BIGINT(20))
    product_attribute_category_id = Column(BIGINT(20))
    name = Column(String(64), nullable=False)
    pic = Column(String(255))
    product_sn = Column(String(64), nullable=False)
    delete_status = Column(INTEGER(1))
    publish_status = Column(INTEGER(1))
    new_status = Column(INTEGER(1))
    recommand_status = Column(INTEGER(1))
    verify_status = Column(INTEGER(1))
    sort = Column(INTEGER(11))
    sale = Column(INTEGER(11))
    price = Column(DECIMAL(10, 2))
    promotion_price = Column(DECIMAL(10, 2))
    gift_growth = Column(INTEGER(11), server_default=text("'0'"))
    gift_point = Column(INTEGER(11), server_default=text("'0'"))
    use_point_limit = Column(INTEGER(11))
    sub_title = Column(String(255))
    description = Column(Text)
    original_price = Column(DECIMAL(10, 2))
    stock = Column(INTEGER(11))
    low_stock = Column(INTEGER(11))
    unit = Column(String(16))
    weight = Column(DECIMAL(10, 2))
    preview_status = Column(INTEGER(1))
    service_ids = Column(String(64))
    keywords = Column(String(255))
    note = Column(String(255))
    album_pics = Column(String(255))
    detail_title = Column(String(255))
    detail_desc = Column(Text)
    detail_html = Column(Text)
    detail_mobile_html = Column(Text)
    promotion_start_time = Column(DateTime)
    promotion_end_time = Column(DateTime)
    promotion_per_limit = Column(INTEGER(11))
    promotion_type = Column(INTEGER(1))
    brand_name = Column(String(255))
    product_category_name = Column(String(255))


class PmsProductAttribute(Base):
    __tablename__ = 'pms_product_attribute'

    id = Column(BIGINT(20), primary_key=True)
    product_attribute_category_id = Column(BIGINT(20))
    name = Column(String(64))
    select_type = Column(INTEGER(1))
    input_type = Column(INTEGER(1))
    input_list = Column(String(255))
    sort = Column(INTEGER(11))
    filter_type = Column(INTEGER(1))
    search_type = Column(INTEGER(1))
    related_status = Column(INTEGER(1))
    hand_add_status = Column(INTEGER(1))
    type = Column(INTEGER(1))


class PmsProductAttributeCategory(Base):
    __tablename__ = 'pms_product_attribute_category'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(64))
    attribute_count = Column(INTEGER(11), server_default=text("'0'"))
    param_count = Column(INTEGER(11), server_default=text("'0'"))


class PmsProductAttributeValue(Base):
    __tablename__ = 'pms_product_attribute_value'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    product_attribute_id = Column(BIGINT(20))
    value = Column(String(64))


class PmsProductCategory(Base):
    __tablename__ = 'pms_product_category'

    id = Column(BIGINT(20), primary_key=True)
    parent_id = Column(BIGINT(20))
    name = Column(String(64))
    level = Column(INTEGER(1))
    product_count = Column(INTEGER(11))
    product_unit = Column(String(64))
    nav_status = Column(INTEGER(1))
    show_status = Column(INTEGER(1))
    sort = Column(INTEGER(11))
    icon = Column(String(255))
    keywords = Column(String(255))
    description = Column(Text)


class PmsProductCategoryAttributeRelation(Base):
    __tablename__ = 'pms_product_category_attribute_relation'

    id = Column(BIGINT(20), primary_key=True)
    product_category_id = Column(BIGINT(20))
    product_attribute_id = Column(BIGINT(20))


class PmsProductFullReduction(Base):
    __tablename__ = 'pms_product_full_reduction'

    id = Column(BIGINT(11), primary_key=True)
    product_id = Column(BIGINT(20))
    full_price = Column(DECIMAL(10, 2))
    reduce_price = Column(DECIMAL(10, 2))


class PmsProductLadder(Base):
    __tablename__ = 'pms_product_ladder'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    count = Column(INTEGER(11))
    discount = Column(DECIMAL(10, 2))
    price = Column(DECIMAL(10, 2))


class PmsProductOperateLog(Base):
    __tablename__ = 'pms_product_operate_log'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    price_old = Column(DECIMAL(10, 2))
    price_new = Column(DECIMAL(10, 2))
    sale_price_old = Column(DECIMAL(10, 2))
    sale_price_new = Column(DECIMAL(10, 2))
    gift_point_old = Column(INTEGER(11))
    gift_point_new = Column(INTEGER(11))
    use_point_limit_old = Column(INTEGER(11))
    use_point_limit_new = Column(INTEGER(11))
    operate_man = Column(String(64))
    create_time = Column(DateTime)


class PmsProductVertifyRecord(Base):
    __tablename__ = 'pms_product_vertify_record'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    create_time = Column(DateTime)
    vertify_man = Column(String(64))
    status = Column(INTEGER(1))
    detail = Column(String(255))


class PmsSkuStock(Base):
    __tablename__ = 'pms_sku_stock'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    sku_code = Column(String(64), nullable=False)
    price = Column(DECIMAL(10, 2))
    stock = Column(INTEGER(11), server_default=text("'0'"))
    low_stock = Column(INTEGER(11))
    sp1 = Column(String(64))
    sp2 = Column(String(64))
    sp3 = Column(String(64))
    pic = Column(String(255))
    sale = Column(INTEGER(11))
    promotion_price = Column(DECIMAL(10, 2))
    lock_stock = Column(INTEGER(11), server_default=text("'0'"))


class SmsCoupon(Base):
    __tablename__ = 'sms_coupon'

    id = Column(BIGINT(20), primary_key=True)
    type = Column(INTEGER(1))
    name = Column(String(100))
    platform = Column(INTEGER(1))
    count = Column(INTEGER(11))
    amount = Column(DECIMAL(10, 2))
    per_limit = Column(INTEGER(11))
    min_point = Column(DECIMAL(10, 2))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    use_type = Column(INTEGER(1))
    note = Column(String(200))
    publish_count = Column(INTEGER(11))
    use_count = Column(INTEGER(11))
    receive_count = Column(INTEGER(11))
    enable_time = Column(DateTime)
    code = Column(String(64))
    member_level = Column(INTEGER(1))


class SmsCouponHistory(Base):
    __tablename__ = 'sms_coupon_history'

    id = Column(BIGINT(20), primary_key=True)
    coupon_id = Column(BIGINT(20), index=True)
    member_id = Column(BIGINT(20), index=True)
    coupon_code = Column(String(64))
    member_nickname = Column(String(64))
    get_type = Column(INTEGER(1))
    create_time = Column(DateTime)
    use_status = Column(INTEGER(1))
    use_time = Column(DateTime)
    order_id = Column(BIGINT(20))
    order_sn = Column(String(100))


class SmsCouponProductCategoryRelation(Base):
    __tablename__ = 'sms_coupon_product_category_relation'

    id = Column(BIGINT(20), primary_key=True)
    coupon_id = Column(BIGINT(20))
    product_category_id = Column(BIGINT(20))
    product_category_name = Column(String(200))
    parent_category_name = Column(String(200))


class SmsCouponProductRelation(Base):
    __tablename__ = 'sms_coupon_product_relation'

    id = Column(BIGINT(20), primary_key=True)
    coupon_id = Column(BIGINT(20))
    product_id = Column(BIGINT(20))
    product_name = Column(String(500))
    product_sn = Column(String(200))


class SmsFlashPromotion(Base):
    __tablename__ = 'sms_flash_promotion'

    id = Column(BIGINT(20), primary_key=True)
    title = Column(String(200))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(INTEGER(1))
    create_time = Column(DateTime)


class SmsFlashPromotionLog(Base):
    __tablename__ = 'sms_flash_promotion_log'

    id = Column(INTEGER(11), primary_key=True)
    member_id = Column(INTEGER(11))
    product_id = Column(BIGINT(20))
    member_phone = Column(String(64))
    product_name = Column(String(100))
    subscribe_time = Column(DateTime)
    send_time = Column(DateTime)


class SmsFlashPromotionProductRelation(Base):
    __tablename__ = 'sms_flash_promotion_product_relation'

    id = Column(BIGINT(20), primary_key=True)
    flash_promotion_id = Column(BIGINT(20))
    flash_promotion_session_id = Column(BIGINT(20))
    product_id = Column(BIGINT(20))
    flash_promotion_price = Column(DECIMAL(10, 2))
    flash_promotion_count = Column(INTEGER(11))
    flash_promotion_limit = Column(INTEGER(11))
    sort = Column(INTEGER(11))


class SmsFlashPromotionSession(Base):
    __tablename__ = 'sms_flash_promotion_session'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(200))
    start_time = Column(Time)
    end_time = Column(Time)
    status = Column(INTEGER(1))
    create_time = Column(DateTime)


class SmsHomeAdvertise(Base):
    __tablename__ = 'sms_home_advertise'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    type = Column(INTEGER(1))
    pic = Column(String(500))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(INTEGER(1))
    click_count = Column(INTEGER(11))
    order_count = Column(INTEGER(11))
    url = Column(String(500))
    note = Column(String(500))
    sort = Column(INTEGER(11), server_default=text("'0'"))


class SmsHomeBrand(Base):
    __tablename__ = 'sms_home_brand'

    id = Column(BIGINT(20), primary_key=True)
    brand_id = Column(BIGINT(20))
    brand_name = Column(String(64))
    recommend_status = Column(INTEGER(1))
    sort = Column(INTEGER(11))


class SmsHomeNewProduct(Base):
    __tablename__ = 'sms_home_new_product'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    product_name = Column(String(64))
    recommend_status = Column(INTEGER(1))
    sort = Column(INTEGER(1))


class SmsHomeRecommendProduct(Base):
    __tablename__ = 'sms_home_recommend_product'

    id = Column(BIGINT(20), primary_key=True)
    product_id = Column(BIGINT(20))
    product_name = Column(String(64))
    recommend_status = Column(INTEGER(1))
    sort = Column(INTEGER(1))


class SmsHomeRecommendSubject(Base):
    __tablename__ = 'sms_home_recommend_subject'

    id = Column(BIGINT(20), primary_key=True)
    subject_id = Column(BIGINT(20))
    subject_name = Column(String(64))
    recommend_status = Column(INTEGER(1))
    sort = Column(INTEGER(11))


class UmsAdmin(Base):
    __tablename__ = 'ums_admin'

    id = Column(BIGINT(20), primary_key=True)
    username = Column(String(64))
    password = Column(String(64))
    icon = Column(String(500))
    email = Column(String(100))
    nick_name = Column(String(200))
    note = Column(String(500))
    create_time = Column(DateTime)
    login_time = Column(DateTime)
    status = Column(INTEGER(1), server_default=text("'1'"))


class UmsAdminLoginLog(Base):
    __tablename__ = 'ums_admin_login_log'

    id = Column(BIGINT(20), primary_key=True)
    admin_id = Column(BIGINT(20))
    create_time = Column(DateTime)
    ip = Column(String(64))
    address = Column(String(100))
    user_agent = Column(String(100))


class UmsAdminPermissionRelation(Base):
    __tablename__ = 'ums_admin_permission_relation'

    id = Column(BIGINT(20), primary_key=True)
    admin_id = Column(BIGINT(20))
    permission_id = Column(BIGINT(20))
    type = Column(INTEGER(1))


class UmsAdminRoleRelation(Base):
    __tablename__ = 'ums_admin_role_relation'

    id = Column(BIGINT(20), primary_key=True)
    admin_id = Column(BIGINT(20))
    role_id = Column(BIGINT(20))


class UmsGrowthChangeHistory(Base):
    __tablename__ = 'ums_growth_change_history'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20))
    create_time = Column(DateTime)
    change_type = Column(INTEGER(1))
    change_count = Column(INTEGER(11))
    operate_man = Column(String(100))
    operate_note = Column(String(200))
    source_type = Column(INTEGER(1))


class UmsIntegrationChangeHistory(Base):
    __tablename__ = 'ums_integration_change_history'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20))
    create_time = Column(DateTime)
    change_type = Column(INTEGER(1))
    change_count = Column(INTEGER(11))
    operate_man = Column(String(100))
    operate_note = Column(String(200))
    source_type = Column(INTEGER(1))


class UmsIntegrationConsumeSetting(Base):
    __tablename__ = 'ums_integration_consume_setting'

    id = Column(BIGINT(20), primary_key=True)
    deduction_per_amount = Column(INTEGER(11))
    max_percent_per_order = Column(INTEGER(11))
    use_unit = Column(INTEGER(11))
    coupon_status = Column(INTEGER(1))


class UmsMember(Base):
    __tablename__ = 'ums_member'

    id = Column(BIGINT(20), primary_key=True)
    member_level_id = Column(BIGINT(20))
    username = Column(String(64), unique=True)
    password = Column(String(64))
    nickname = Column(String(64))
    phone = Column(String(64), unique=True)
    status = Column(INTEGER(1))
    create_time = Column(DateTime)
    icon = Column(String(500))
    gender = Column(INTEGER(1))
    birthday = Column(Date)
    city = Column(String(64))
    job = Column(String(100))
    personalized_signature = Column(String(200))
    source_type = Column(INTEGER(1))
    integration = Column(INTEGER(11))
    growth = Column(INTEGER(11))
    luckey_count = Column(INTEGER(11))
    history_integration = Column(INTEGER(11))


class UmsMemberLevel(Base):
    __tablename__ = 'ums_member_level'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    growth_point = Column(INTEGER(11))
    default_status = Column(INTEGER(1))
    free_freight_point = Column(DECIMAL(10, 2))
    comment_growth_point = Column(INTEGER(11))
    priviledge_free_freight = Column(INTEGER(1))
    priviledge_sign_in = Column(INTEGER(1))
    priviledge_comment = Column(INTEGER(1))
    priviledge_promotion = Column(INTEGER(1))
    priviledge_member_price = Column(INTEGER(1))
    priviledge_birthday = Column(INTEGER(1))
    note = Column(String(200))


class UmsMemberLoginLog(Base):
    __tablename__ = 'ums_member_login_log'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20))
    create_time = Column(DateTime)
    ip = Column(String(64))
    city = Column(String(64))
    login_type = Column(INTEGER(1))
    province = Column(String(64))


class UmsMemberMemberTagRelation(Base):
    __tablename__ = 'ums_member_member_tag_relation'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20))
    tag_id = Column(BIGINT(20))


class UmsMemberProductCategoryRelation(Base):
    __tablename__ = 'ums_member_product_category_relation'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20))
    product_category_id = Column(BIGINT(20))


class UmsMemberReceiveAddres(Base):
    __tablename__ = 'ums_member_receive_address'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20))
    name = Column(String(100))
    phone_number = Column(String(64))
    default_status = Column(INTEGER(1))
    post_code = Column(String(100))
    province = Column(String(100))
    city = Column(String(100))
    region = Column(String(100))
    detail_address = Column(String(128))


class UmsMemberRuleSetting(Base):
    __tablename__ = 'ums_member_rule_setting'

    id = Column(BIGINT(20), primary_key=True)
    continue_sign_day = Column(INTEGER(11))
    continue_sign_point = Column(INTEGER(11))
    consume_per_point = Column(DECIMAL(10, 2))
    low_order_amount = Column(DECIMAL(10, 2))
    max_point_per_order = Column(INTEGER(11))
    type = Column(INTEGER(1))


class UmsMemberStatisticsInfo(Base):
    __tablename__ = 'ums_member_statistics_info'

    id = Column(BIGINT(20), primary_key=True)
    member_id = Column(BIGINT(20))
    consume_amount = Column(DECIMAL(10, 2))
    order_count = Column(INTEGER(11))
    coupon_count = Column(INTEGER(11))
    comment_count = Column(INTEGER(11))
    return_order_count = Column(INTEGER(11))
    login_count = Column(INTEGER(11))
    attend_count = Column(INTEGER(11))
    fans_count = Column(INTEGER(11))
    collect_product_count = Column(INTEGER(11))
    collect_subject_count = Column(INTEGER(11))
    collect_topic_count = Column(INTEGER(11))
    collect_comment_count = Column(INTEGER(11))
    invite_friend_count = Column(INTEGER(11))
    recent_order_time = Column(DateTime)


class UmsMemberTag(Base):
    __tablename__ = 'ums_member_tag'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    finish_order_count = Column(INTEGER(11))
    finish_order_amount = Column(DECIMAL(10, 2))


class UmsMemberTask(Base):
    __tablename__ = 'ums_member_task'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    growth = Column(INTEGER(11))
    intergration = Column(INTEGER(11))
    type = Column(INTEGER(1))


class UmsPermission(Base):
    __tablename__ = 'ums_permission'

    id = Column(BIGINT(20), primary_key=True)
    pid = Column(BIGINT(20))
    name = Column(String(100))
    value = Column(String(200))
    icon = Column(String(500))
    type = Column(INTEGER(1))
    uri = Column(String(200))
    status = Column(INTEGER(1))
    create_time = Column(DateTime)
    sort = Column(INTEGER(11))


class UmsRole(Base):
    __tablename__ = 'ums_role'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100))
    description = Column(String(500))
    admin_count = Column(INTEGER(11))
    create_time = Column(DateTime)
    status = Column(INTEGER(1), server_default=text("'1'"))
    sort = Column(INTEGER(11), server_default=text("'0'"))


class UmsRolePermissionRelation(Base):
    __tablename__ = 'ums_role_permission_relation'

    id = Column(BIGINT(20), primary_key=True)
    role_id = Column(BIGINT(20))
    permission_id = Column(BIGINT(20))
