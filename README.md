# 🧩 8-puzzle-solver

> A\*알고리즘을 통해 퍼즐의 최적해를 찾아서 최소 이동횟수로 퍼즐을 푸는 프로그램

![ex1](https://user-images.githubusercontent.com/76832861/176325797-2ddfe55d-ead3-4095-a67d-e8371adcc2ba.gif)

#### A\*알고리즘
> 출발 지점에서 목표 지점까지의 최적의 경로를 찾는 최단 경로 알고리즘
- 각 지점에 대해 그 지점을 통과하는 최상의 경로를 추정하는 휴리스틱 추정값을 사용함
- 8퍼즐에서는 퍼즐이 정렬된 상태가 목표지점이 되고 (현재 이동횟수 + 각 숫자가 목표위치까지의 맨해튼 거리)를 더한 값으로 우선순위를 정함
