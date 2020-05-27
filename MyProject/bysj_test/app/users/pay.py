# from alipay import AliPay
import os
import app.config

# print(app.config.basepath)
app_private_key_string = open(app.config.basepath + '/static/key_file/app_private_key.pem').read()
alipay_public_key_string = open(app.config.basepath + '/static/key_file/alipay_public_key.pem').read()

# print(alipay_public_key_string)
# print(app_private_key_string)
from alipay import AliPay

ALIPAY_APP_ID = '2016102300747970'

ALIPAY_RETURN_URL = ''

ALIPAY_NOTIFY_URL = ''
# print(app_private_key_string)
# print(alipay_public_key_string)

ORDER_STATUS = 1

alipay = AliPay(
    appid=ALIPAY_APP_ID,
    # 默认回调url
    app_notify_url=None,
    # 应用私钥
    app_private_key_string=app_private_key_string,
    # 支付宝公钥
    alipay_public_key_string=alipay_public_key_string,
    # 指明签名算法
    sign_type="RSA2",
    # debug模式 会把请求发送至沙箱环境
    debug=True
)


def get_trade_url(order_id, amount, ALIPAY_RETURN_URL, ALIPAY_NOTIFY_URL):
    # pc网站支付地址  https://openapi.alipaydev.com/gateway.do? + querystring
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号
        out_trade_no=order_id,
        # 订单总金额
        total_amount=amount,
        subject=order_id,
        return_url=ALIPAY_RETURN_URL,
        notify_url=ALIPAY_NOTIFY_URL
    )
    return "https://openapi.alipaydev.com/gateway.do?" + order_string


def get_verify_result(data, sign):
    # 验签成功 返回 True   失败是 False
    return alipay.verify(data, sign)


def get_trade_result(order_id):
    # 查询支付结果
    result = alipay.api_alipay_trade_query(out_trade_no=order_id)
    print(result)
    if result.get("trade_status") == "TRADE_SUCCESS":
        return True
    return False
