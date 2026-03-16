from enum import Enum


class PureCloudRegionHosts(str, Enum):
    us_east_1 = "mypurecloud.com"
    eu_west_1 = "mypurecloud.ie"
    ap_southeast_2 = "mypurecloud.com.au"
    ap_northeast_1 = "mypurecloud.jp"
    eu_central_1 = "mypurecloud.de"
    us_west_2 = "usw2.pure.cloud"
    ca_central_1 = "cac1.pure.cloud"
    ap_northeast_2 = "apne2.pure.cloud"
    eu_west_2 = "euw2.pure.cloud"
    ap_south_1 = "aps1.pure.cloud"
    us_east_2 = "use2.us-gov-pure.cloud"
    sa_east_1 = "sae1.pure.cloud"
    me_central_1 = "mec1.pure.cloud"
    ap_northeast_3 = "apne3.pure.cloud"
    eu_central_2 = "euc2.pure.cloud"

    def __init__(self, host: str, protocol: str = "https"):
        self._api_host = protocol + "://api." + host
        self._login_host = protocol + "://login." + host

    @property
    def api_host(self) -> str:
        return self._api_host

    @property
    def login_host(self) -> str:
        return self._login_host
