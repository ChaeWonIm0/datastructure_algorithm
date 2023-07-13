#include <bits10_1.h>
#define INF 1e9 

using namespace std;

/** 노드의 갯수 n 간선의 갯수 m */
int n, m;

/* 노드의 갯수는 최대 500개로 가정*/
/* 2차원 배열(그래프)*/
int graph[501][501];

int main(void) {
    cin >> n >> m;

    // 최단 거리 테이블을 모두 inf로 초기화
    for (int i = 0; i< 501; i ++) {
        fill(graph[i], graph[i] + 501, INF);
    }
    // 자기자신에게 오는 cost는 0으로 초기화
    for (int a = 1; a <= n; a++) {
        for (int b = 1; b <= n; b++) {
            if (a==b) graph[a][b] = 0;
        }
    }
    // 각 간선에 대한 정보를 입력받아 , 그 값으로 초기화
    for (int i=0; i <m; i++) {
        // A에서 B로 가는 비용은 C로 설정
        int a, b, c;
        cin >> a >> b>> c;
        graph[a][b]=c;
    }
    // 점화식에 따라 플로이드 워셜 알고리즘 수행
    for (int k = 1; k <= n; k++) {
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]);
            }
        }
    }

    /* 수행된 결과 출력 */
    for (int a = 1; a <= n; a++) {
        for (int b = 1; b<= n; b++) {
            /*도달 할 수 없는 경우 무한 출력*/
            if (graph[a][b] == INF) {
                cout << "무한" << ' ';
            }
            /* 도달가능하면 거리 출력*/
            else {
                cout << graph[a][b] << ' ';
            }
        }
        cout << '\n';
    }
}

