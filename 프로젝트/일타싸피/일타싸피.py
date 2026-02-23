import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '서울18반_이동은'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6

# 좌하단이 (0,0) 기준 (기본 포켓 위치)
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


# =========================
# 1~3번 업그레이드용 함수들
# =========================

BALL_RADIUS = 2       # 대략값 (환경에 따라 약간 조정 가능)
POCKET_INSET = 0.0      # 포켓 중심을 테이블 안쪽으로 살짝 이동 (선택 안정화)

HOLES_INSET = [
    [0 + POCKET_INSET,   0 + POCKET_INSET],
    [127,                0 + POCKET_INSET],
    [254 - POCKET_INSET, 0 + POCKET_INSET],
    [0 + POCKET_INSET,   127 - POCKET_INSET],
    [127,                127 - POCKET_INSET],
    [254 - POCKET_INSET, 127 - POCKET_INSET],
]


def pick_target_idx(order, balls):
    # 일타싸피 기본(보통): 선공=1,3 / 후공=2,4 / 마지막=8(=idx 5)
    if order == 1:
        my_balls = [1, 3]
    else:
        my_balls = [2, 4]

    eight_ball = 5  # balls[5]가 8번 공

    # 1) 내 공이 남아있으면 내 공 중 살아있는 것 우선
    for b in my_balls:
        if balls[b][0] != -1:
            return b

    # 2) 내 공이 다 들어갔으면 8번 공
    if balls[eight_ball][0] != -1:
        return eight_ball

    # 3) fallback: 살아있는 아무 공(흰공 제외)
    for b in range(1, len(balls)):
        if balls[b][0] != -1:
            return b

    return 1


def dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def point_to_segment_distance(px, py, ax, ay, bx, by):
    abx = bx - ax
    aby = by - ay
    apx = px - ax
    apy = py - ay

    ab_len2 = abx * abx + aby * aby
    if ab_len2 == 0:
        return math.hypot(px - ax, py - ay)

    t = (apx * abx + apy * aby) / ab_len2
    if t < 0:
        cx, cy = ax, ay
    elif t > 1:
        cx, cy = bx, by
    else:
        cx = ax + t * abx
        cy = ay + t * aby

    return math.hypot(px - cx, py - cy)


def is_path_blocked(ax, ay, bx, by, balls, ignore_idxs, clearance):
    # 선분 A->B가 다른 공에 의해 막히는지 검사
    for i in range(1, NUMBER_OF_BALLS):  # 흰공(0)은 장애물로 보지 않음
        if i in ignore_idxs:
            continue
        if balls[i][0] == -1:
            continue
        px, py = balls[i][0], balls[i][1]
        d = point_to_segment_distance(px, py, ax, ay, bx, by)
        if d <= clearance:
            return True
    return False


def angle_between_vectors(ax, ay, bx, by):
    la = math.hypot(ax, ay)
    lb = math.hypot(bx, by)
    if la == 0 or lb == 0:
        return 180.0
    dot = ax * bx + ay * by
    cosv = dot / (la * lb)
    if cosv > 1:
        cosv = 1
    if cosv < -1:
        cosv = -1
    return math.degrees(math.acos(cosv))


def choose_best_hole(white_x, white_y, target_x, target_y, target_idx, balls):
    best_score = -1e18
    best_hole = HOLES_INSET[0]

    # 흰 -> 목적 벡터
    vwx = target_x - white_x
    vwy = target_y - white_y
    d_wt = math.hypot(vwx, vwy)

    for hx, hy in HOLES_INSET:
        # 목적 -> 홀 벡터
        vtx = hx - target_x
        vty = hy - target_y
        d_th = math.hypot(vtx, vty)

        # 컷각(0~180): 흰->목적 방향과 목적->홀 방향의 차이
        cut = angle_between_vectors(vwx, vwy, vtx, vty)

        # 목적->홀 라인 장애물 체크
        blocked_th = is_path_blocked(
            target_x, target_y, hx, hy,
            balls,
            ignore_idxs={target_idx},
            clearance=BALL_RADIUS * 2.0
        )

        score = 0.0

        # 막히면 제외급
        if blocked_th:
            score -= 10000.0

        # 거리 페널티
        score -= d_th * 3.0
        score -= d_wt * 0.8

        # 컷각 페널티(60도 넘어가면 급격히 어려움)
        if cut <= 60:
            score -= cut * 5.0
        else:
            score -= 60 * 5.0
            score -= (cut - 60) * 20.0

        # 너무 먼 포켓은 추가 페널티
        if d_th > 120:
            score -= (d_th - 120) * 2.0

        if score > best_score:
            best_score = score
            best_hole = [hx, hy]

    return best_hole[0], best_hole[1]


def calc_ghost_point(target_x, target_y, hole_x, hole_y, r):
    # 목적구 -> 홀 방향 단위벡터
    vx = hole_x - target_x
    vy = hole_y - target_y
    d = math.hypot(vx, vy)
    if d == 0:
        return target_x, target_y

    ux = vx / d
    uy = vy / d

    # 고스트볼: 목적구에서 홀 반대방향으로 2r
    ghost_x = target_x - ux * (2.0 * r)
    ghost_y = target_y - uy * (2.0 * r)
    return ghost_x, ghost_y


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.

    # 1) 타겟 공 선택
    idx = pick_target_idx(order, balls)

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표
    targetBall_x = balls[idx][0]
    targetBall_y = balls[idx][1]

    # 2) 홀 선택
    hole_x, hole_y = choose_best_hole(
        whiteBall_x, whiteBall_y,
        targetBall_x, targetBall_y,
        idx, balls
    )

    # 3) 고스트볼(접점) 계산
    ghost_x, ghost_y = calc_ghost_point(
        targetBall_x, targetBall_y,
        hole_x, hole_y,
        BALL_RADIUS
    )

    # 고스트볼이 극단적으로 테이블 밖이면 폭주 방지(간단 클램프)
    if ghost_x < 0:
        ghost_x = 0
    if ghost_x > TABLE_WIDTH:
        ghost_x = TABLE_WIDTH
    if ghost_y < 0:
        ghost_y = 0
    if ghost_y > TABLE_HEIGHT:
        ghost_y = TABLE_HEIGHT

    # 이제 흰공은 목적구 중심이 아니라 고스트볼을 향해 쏜다
    dx = ghost_x - whiteBall_x
    dy = ghost_y - whiteBall_y

    # ⚠️ 일타싸피 각도 정의에 맞춰 (기존 코드처럼) atan2(dx, dy) 형태 유지
    angle = math.degrees(math.atan2(dx, dy))
    if angle < 0:
        angle += 360

    # 파워는 아직 100 고정(4번/5번에서 업그레이드 예정)
    power = 100

    # 디버그
    print("ORDER:", order, "TARGET_IDX:", idx)
    print("TARGET:", targetBall_x, targetBall_y, "HOLE:", hole_x, hole_y, "GHOST:", ghost_x, ghost_y)
    print("ANGLE:", angle, "POWER:", power)

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')