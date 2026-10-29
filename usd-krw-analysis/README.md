# 원/달러 환율 트렌드 분석 (2020~2026)

원/달러 환율 일별 데이터(1,703개)로 추세, 급변, 변동성, 계절성을 분석하고 단순 예측의 한계를 확인한 프로젝트입니다.
분석 결과는 **[REPORT.md](REPORT.md)** 에 있습니다.

## 폴더 구조

```
usd-krw-analysis/
├── collect_data.py            # 데이터 수집 스크립트
├── analysis.ipynb             # 정제 · 분석 · 시각화 · 예측 (실행 결과 포함)
├── REPORT.md                  # 분석 리포트
├── stats.json                 # 리포트에 쓴 수치 (노트북이 자동 생성)
├── requirements.txt
├── data/
│   ├── usdkrw_daily_raw.csv   # 원본 (결측 포함)
│   └── usdkrw_daily_clean.csv # 정제 + 파생 컬럼 (노트북이 생성)
└── images/                    # 리포트용 그래프 6개 (노트북이 생성)
```

## 실행 방법

Python 3.10 이상이 필요합니다.

```bash
pip install -r requirements.txt

# 1) 데이터 수집 (data/usdkrw_daily_raw.csv 생성) — 저장소에 이미 포함되어 있어 생략 가능
python collect_data.py

# 2) 분석 노트북 실행 (images/, stats.json, clean.csv 생성)
jupyter notebook analysis.ipynb            # 위에서부터 순서대로 실행
# 또는 한 번에 실행:
jupyter nbconvert --to notebook --execute --inplace analysis.ipynb
```

> `collect_data.py`를 다시 실행하면 최신 날짜까지 받아오므로, 리포트의 수치와 조금 달라질 수 있습니다.

## 데이터 출처 및 라이선스

- 원천: Board of Governors of the Federal Reserve System, H.10 Foreign Exchange Rates → FRED 시리즈 [`DEXKOUS`](https://fred.stlouisfed.org/series/DEXKOUS) (뉴욕 정오 기준, 원/1달러)
- 수집 경로: [datasets/exchange-rates](https://github.com/datasets/exchange-rates) (FRED 데이터 미러, ODC-PDDL)
- 미국 정부 공개 통계로 자유롭게 사용할 수 있으나, 재배포 시 위 출처를 표기해 주세요. 투자 판단의 근거로 사용하지 마세요.
