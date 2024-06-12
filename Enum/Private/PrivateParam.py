from enum import Enum


# "AdsPower Global.exe" --headless=true --api-key=ae65e480ad87ffa5653988b8f7148675 --api-port=18866 --no-sandbox
# github_token: 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
class PrivateParam(Enum):
    EMAIL = "mafrank9110@gmail.com"

    WINDOWS_PASSWORD = "123123"


NODE_JS_REQUEST_IP = "http://127.0.0.1:13001"


class ConnectPortReplace(Enum):
    """
    10000 + 原端口：10000 + 替换端口
    """
    REPLACE_DICT = {
        80: 10888,
        # 258: 11258
    }


class AdsParam:
    ADS_PORT = "18866"

    # ['', 'jghj1ht', 'jghj1hu', 'jghj1hw', 'jghj1hy', 'jghj1i0', 'jghj1i1', 'jghj1i2', 'jghj1i3', 'jghj1i4', 'jghj1i5', 'jghj1i6', 'jghj1i7', 'jghj1i8', 'jghj1ia', 'jghj1id', 'jghj1if', 'jghj1ig', 'jghj1ih', 'jghj1ij', 'jghj1ik', 'jghj1im', 'jghj1in', 'jghj1io', 'jghj1ip', 'jghj1ir', 'jghj1is', 'jghj1it', 'jghj1iu', 'jghj1iv', 'jghj1iw', 'jghj1iy', 'jghj1j0', 'jghj1j1', 'jghj1j2', 'jghj1j3', 'jghj1j4', 'jghj1j5', 'jghj1j6', 'jghj1j7', 'jghj1j8', 'jghj1j9', 'jghj1ja', 'jghj1jc', 'jghj1je', 'jghj1jf', 'jghj1jg', 'jghj1jh', 'jghj1ji', 'jghj1jj', 'jghj1jk', 'jghj1jm', 'jghj1jn', 'jghj1jo', 'jghj1jp', 'jghj1jq', 'jghj1jr', 'jghj1js', 'jghj1jt', 'jghj1ju', 'jghj1jw', 'jghj1k0', 'jghj1k2', 'jghj1k3', 'jghj1k4', 'jghj1k5', 'jghj1k7', 'jghj1kb', 'jghj1kc', 'jghj1kd', 'jghj1ke', 'jghj1kg', 'jghj1kh', 'jghj1ki', 'jghj1kj', 'jghj1kk', 'jghj1kl', 'jghj1kn', 'jghj1ko', 'jghj1kp', 'jghj1kq', 'jghj1kr', 'jghj1ks', 'jghj1kt', 'jghj1ku', 'jghj1kv', 'jghj1kw', 'jghj1kx', 'jghj1ky', 'jghj1l0', 'jghj1l2', 'jghj1l3', 'jghj1l4', 'jghj1l5', 'jghj1l6', 'jghj1l7', 'jghj1l8', 'jghj1la', 'jghj1lb', 'jghj1ld', 'jghj1le', 'jghj1lg', 'jghj1lh', 'jghj1li', 'jghj1lj', 'jghj1lk', 'jghj1ll', 'jghj1lm', 'jghj1ln', 'jghj1lp', 'jghj1lq', 'jghj1lr', 'jghj1lt', 'jghj1lu', 'jghj1lw', 'jghj1ly', 'jghj1m1', 'jghj1m2', 'jghj1m3', 'jghj1m5', 'jghj1m6', 'jghj1m7', 'jghj1m9', 'jghj1ma', 'jghj1mc', 'jghj1md', 'jghj1me', 'jghj1mg', 'jghj1mh', 'jghj1mi', 'jghj1mj', 'jghj1mk', 'jghj1ml', 'jghj1mm', 'jghj1mo', 'jghj1mq', 'jghj1mr', 'jghj1ms', 'jghj1mt', 'jghj1mu', 'jghj1mv', 'jghj1mw', 'jghj1mx', 'jghj1my', 'jghj1n0', 'jghj1n1', 'jghj1n2', 'jghj1n3', 'jghj1n4', 'jghj1n5', 'jghj1n6', 'jghj1n7', 'jghj1n8', 'jghj1n9', 'jghj1na', 'jghj1nc', 'jghj1nd', 'jghj1ne', 'jghj1nf', 'jghj1ng', 'jghj1nh', 'jghj1nj', 'jghj1nk', 'jghj1nl', 'jghj1nm', 'jghj1nn', 'jghj1np', 'jghj1nq', 'jghj1ns', 'jghj1nu', 'jghj1nv', 'jghj1nw', 'jghj1nx', 'jghj1ny', 'jghj1o0', 'jghj1o1', 'jghj1o2', 'jghj1o3', 'jghj1o4', 'jghj1o7', 'jghj1o9', 'jghj1oa', 'jghj1ob', 'jghj1oc', 'jghj1od', 'jghj1oe', 'jghj1of', 'jghj1og', 'jghj1oh', 'jghj1oi', 'jghj1ol', 'jghj1om', 'jghj1on', 'jghj1oo', 'jghj1op', 'jghj1oq', 'jghj1os', 'jghj1ov', 'jghj1ow', 'jghj1ox', 'jghj1oy', 'jghj1p1', 'jghj1p2', 'jghj1p4', 'jghj1p5', 'jghj1p6', 'jghj1p7', 'jghj1p9', 'jghj1pa', 'jghj1pc', 'jghj1pd', 'jghj1pf', 'jghj1pg', 'jghj1ph', 'jghj1pj', 'jghj1pk', 'jghj1pm', 'jghj1pn', 'jghj1pp', 'jghj1pr', 'jghj1pt', 'jghj1pv', 'jghj1pw', 'jghj1py', 'jghj1q0', 'jghj1q1', 'jghj1q3', 'jghj1q7', 'jghj1q8', 'jghj1qa', 'jghj1qb', 'jghj1qc', 'jghj1qd', 'jghj1qe', 'jghj1qf', 'jghj1qg', 'jghj1qh', 'jghj1qi', 'jghj1qj', 'jghj1qk', 'jghj1qn', 'jghj1qo', 'jghj1qp', 'jghj1qq', 'jghj1qr', 'jghj1qs', 'jghj1qt', 'jghj1qv', 'jghj1qw', 'jghj1qy', 'jghj1r1', 'jghj1r3', 'jghj1r4', 'jghj1r5', 'jghj1r8', 'jghj1ra', 'jghj1rc', 'jghj1rd', 'jghj1re', 'jghj1rf', 'jghj1rg', 'jghj1rh', 'jghj1ri', 'jghj1rk', 'jghj1rl', 'jghj1rm', 'jghj1rn', 'jghj1rp', 'jghj1rq', 'jghj1rr', 'jghj1rs', 'jghj1rt', 'jghj1ru', 'jghj1rv', 'jghj1rx', 'jghj1ry', 'jghj1s0', 'jghj1s1', 'jghj1s2', 'jghj1s4', 'jghj1s5', 'jghj1s6', 'jghj1s7', 'jghj1s8', 'jghj1sa', 'jghj1sb', 'jghj1sc', 'jghj1sd', 'jghj1se', 'jghj1sf', 'jghj1si', 'jghj1sj', 'jghj1sl', 'jghj1sm', 'jghj1so', 'jghj1sp', 'jghj1sq', 'jghj1ss', 'jghj1st', 'jghj1sv', 'jghj1sw']

    GROUP_ID = "3956536"

    ads_user_id_list = ['', 'jgiptip', 'jgiptir', 'jgiptit', 'jgiptiv', 'jgiptiy', 'jgiptj0', 'jgiptj3', 'jgiptj4',
                        'jgiptj6', 'jgiptjb', 'jgiptjf', 'jgiptjk', 'jgiptjp', 'jgiptjt', 'jgiptjy', 'jgiptk3',
                        'jgiptk8', 'jgiptkb', 'jgiptkg', 'jgiptkl', 'jgiptkq', 'jgiptku', 'jgiptl0', 'jgiptl4',
                        'jgiptl8', 'jgiptlc', 'jgiptlg', 'jgiptlj', 'jgiptlo', 'jgiptlt', 'jgiptlv', 'jgiptly',
                        'jgiptm1', 'jgiptm2', 'jgiptm4', 'jgiptm6', 'jgiptm8', 'jgiptma', 'jgiptmc', 'jgiptme',
                        'jgiptmg', 'jgiptmi', 'jgiptmj', 'jgiptml', 'jgiptmn', 'jgiptmp', 'jgiptmt', 'jgiptmv',
                        'jgiptmx', 'jgiptn0', 'jgiptn2', 'jgiptn5', 'jgiptn7', 'jgiptn9', 'jgiptnb', 'jgiptnc',
                        'jgiptne', 'jgiptng', 'jgiptni', 'jgiptnl', 'jgiptnn', 'jgiptnq', 'jgiptnr', 'jgiptnt',
                        'jgiptnv', 'jgiptnx', 'jgiptny', 'jgipto1', 'jgipto3', 'jgipto5', 'jgipto9', 'jgiptoa',
                        'jgiptod', 'jgiptof', 'jgiptoi', 'jgiptok', 'jgipton', 'jgiptoq', 'jgiptot', 'jgiptov',
                        'jgiptox', 'jgiptp0', 'jgiptp2', 'jgiptp5', 'jgiptp7', 'jgiptp9', 'jgiptpb', 'jgiptpd',
                        'jgiptpg', 'jgiptph', 'jgiptpj', 'jgiptpl', 'jgiptpo', 'jgiptpq', 'jgiptps', 'jgiptpu',
                        'jgiptpx', 'jgiptq0', 'jgiptq2', 'jgiptq4', 'jgiptq7', 'jgiptq9', 'jgiptqb', 'jgiptqd',
                        'jgiptqg', 'jgiptqj', 'jgiptqm', 'jgiptqo', 'jgiptqr', 'jgiptqt', 'jgiptqv', 'jgiptqw',
                        'jgiptqy', 'jgiptr2', 'jgiptr4', 'jgiptr6', 'jgiptr8', 'jgiptra', 'jgiptrc', 'jgiptrd',
                        'jgiptrf', 'jgiptrh', 'jgiptrk', 'jgiptrm', 'jgiptro', 'jgiptrq', 'jgiptrt', 'jgiptrv',
                        'jgiptrx', 'jgiptry', 'jgipts1', 'jgipts3', 'jgipts5', 'jgipts7', 'jgipts9', 'jgiptsc',
                        'jgiptse', 'jgiptsi', 'jgiptsl', 'jgiptsn', 'jgiptso', 'jgiptsq', 'jgiptst', 'jgiptsv',
                        'jgiptsx', 'jgiptt0', 'jgiptt2', 'jgiptt4', 'jgiptt6', 'jgiptt8', 'jgiptta', 'jgipttd',
                        'jgiptte', 'jgiptth', 'jgipttj', 'jgipttl', 'jgipttn', 'jgiptto', 'jgipttq', 'jgiptts',
                        'jgipttv', 'jgipttw', 'jgiptty', 'jgiptu2', 'jgiptu3', 'jgiptu5', 'jgiptu8', 'jgiptua',
                        'jgiptub', 'jgiptue', 'jgiptug', 'jgiptuh', 'jgiptuj', 'jgiptul', 'jgiptun', 'jgiptup',
                        'jgiptur', 'jgiptuu', 'jgiptuw', 'jgiptuy', 'jgiptv1', 'jgiptv2', 'jgiptv5', 'jgiptv7',
                        'jgiptv9', 'jgiptvb', 'jgiptvd', 'jgiptvf', 'jgiptvg', 'jgiptvj', 'jgiptvl', 'jgiptvn',
                        'jgiptvp', 'jgiptvr', 'jgiptvt', 'jgiptvw', 'jgiptvx', 'jgiptw0', 'jgiptw2', 'jgiptw5',
                        'jgiptw8', 'jgiptwa', 'jgiptwc', 'jgiptwf', 'jgiptwh', 'jgiptwk', 'jgiptwm', 'jgiptwn',
                        'jgiptwq', 'jgiptwt', 'jgiptwv', 'jgiptwy', 'jgiptx1', 'jgiptx3', 'jgiptx5', 'jgiptx7',
                        'jgiptx9', 'jgiptxb', 'jgiptxe', 'jgiptxg', 'jgiptxi', 'jgiptxm', 'jgiptxo', 'jgiptxq',
                        'jgiptxt', 'jgiptxw', 'jgiptxy', 'jgipty1', 'jgipty3', 'jgipty5', 'jgipty7', 'jgipty9',
                        'jgiptyb', 'jgiptyd', 'jgiptyf', 'jgiptyh', 'jgiptyj', 'jgiptyl', 'jgiptyn', 'jgiptyp',
                        'jgiptyq', 'jgiptys', 'jgiptyu', 'jgiptyw', 'jgipu02', 'jgipu07', 'jgipu0b', 'jgipu0f',
                        'jgipu0i', 'jgipu0k', 'jgipu0l', 'jgipu0o', 'jgipu0q', 'jgipu0s', 'jgipu0v', 'jgipu0x',
                        'jgipu10', 'jgipu12', 'jgipu14', 'jgipu16', 'jgipu18', 'jgipu1a', 'jgipu1d', 'jgipu1h',
                        'jgipu1j', 'jgipu1m', 'jgipu1o', 'jgipu1r', 'jgipu1x', 'jgipu24', 'jgipu28', 'jgipu2c',
                        'jgipu2g', 'jgipu2k', 'jgipu2o', 'jgipu2t', 'jgipu2y', 'jgipu34', 'jgipu38', 'jgipu3d',
                        'jgipu3i', 'jgipu3n', 'jgipu3r', 'jgipu3x', 'jgipu42', 'jgipu47', 'jgipu4c', 'jgipu4g',
                        'jgipu4k', 'jgipu4p', 'jgipu4t', 'jgipu4x', 'jgipu51', 'jgipu56', 'jgipu5a', 'jgipu5d',
                        'jgipu5h', 'jgipu5k', 'jgipu5n', 'jgipu5q']

    all_ads_user_id_list = ['', ]

    api_key = 'ae65e480ad87ffa5653988b8f7148675'


class FolderParam(Enum):
    ACCOUNT = "C:\\Users\\crypto\\Desktop\\Account"
    # ACCOUNT = "C:\\Users\\crypto\\Desktop\\share\\Account"


PROJECT = "C:/Users/crypto/PycharmProjects/gqgq"

if __name__ == '__main__':
    print(AdsParam.ads_user_id_list[225])
