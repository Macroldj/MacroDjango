import hashlib

from macroDjango import settings


def get_sign(params=None, mch_key=''):
    """
    :param params: 统一下单参数
    :param mch_key: 商户api_key
    :return:
    """
    tmp_sign = '&'.join([
            '{}={}'.format(key, params.get(key)) for key in sorted(
                params.keys()) if params.get(key)
        ]) + "&key={}".format(mch_key)
    pay_sign = hashlib.md5(tmp_sign.encode("utf-8")).hexdigest().upper()
    return pay_sign


def check_sign(params=None):
    """
    https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=20_1
    支付回调签名验证
    :param params:
    :return:
    """
    sign = params.pop('sign')
    pay_sign = get_sign(params=params, mch_key=settings.WECHAT_MCH_ID)
    if not sign:
        return False
    return sign == pay_sign
