#問題1 幅優先探索迷路
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#ハッシュ値取得　とりあえずこういうもの
    def __hash__(self):
        return (self.x << 16) | self.y
#同値性判定　とりあえずこういうもの
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def bfs(h, w, t, sx, sy, gx, gy):#(マップ縦、マップ横、マップ本体、スタート横軸、スタート縦軸、ゴール横軸、ゴール縦軸)
    open_list = []#未調査リスト
    closed = set()#調査済みリスト
    initial_state = State(sx, sy)#初期位置指定
    open_list.append(initial_state)#初期位置を未調査リストに入れる

    #初期位置
    cost = 1
    while True:
        #一時保管場所
        tmp_q = []
        while open_list:
            #現在位置から見て、まだ進んでない道を取得
            st = open_list.pop(0)

            if st.x == gx and st.y == gy:
                return cost
            #壁を飛ばす処理
            if t[st.y][st.x] == 1:
                continue
            #通ってきた場所は飛ばす処理➡同地性判定、ハッシュ値取得が必要？
            if st in closed:
                continue
            #調査済みリストに投げる処理
            closed.add(st)
            for i in range(4):
                nx = st.x + dx[i]
                ny = st.y + dy[i]

                #座標が外れるものを排除する処理
                if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                    continue

                #一時保管の処理
                tmp_q.append(State(nx, ny))

        #次の未調査リストに追加
        open_list = tmp_q
        #現在位置からの調査が全て終わるとcostを追加
        cost += 1


h, w = map(int, input().split())
t = [[int(x) for x in input().split()] for _ in range(h)]

cost = bfs(h, w, t, 0, 0, w - 1, h - 1)
print(cost)