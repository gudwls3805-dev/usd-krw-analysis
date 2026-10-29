"""
원/달러 환율 일별 데이터 수집 스크립트

출처: 미국 연방준비제도(Fed) H.10 통계 → FRED 시리즈 DEXKOUS
      (South Korean Won to U.S. Dollar Spot Exchange Rate, 뉴욕 정오 기준)
수집 경로: FRED 데이터를 국가별로 정리한 공개 미러 저장소 datasets/exchange-rates (GitHub)
      https://github.com/datasets/exchange-rates

실행:  python collect_data.py
결과:  data/usdkrw_daily_raw.csv  (2020-01-01 이후, 원본 그대로·결측 포함)
"""
from pathlib import Path

import pandas as pd

SOURCE_URL = "https://raw.githubusercontent.com/datasets/exchange-rates/main/data/daily.csv"
START = "2020-01-01"
OUT = Path(__file__).parent / "data" / "usdkrw_daily_raw.csv"


def main() -> None:
    df = pd.read_csv(SOURCE_URL)
    krw = df[df["Country"] == "South Korea"][["Date", "Exchange rate"]].copy()
    krw.columns = ["date", "usdkrw"]
    krw["date"] = pd.to_datetime(krw["date"])
    krw = krw[krw["date"] >= START].sort_values("date")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    krw.to_csv(OUT, index=False)
    print(f"saved {len(krw)} rows → {OUT}  ({krw['date'].min():%Y-%m-%d} ~ {krw['date'].max():%Y-%m-%d})")


if __name__ == "__main__":
    main()

# 대안 경로 (같은 데이터):
#   FRED에서 직접 받기: https://fred.stlouisfed.org/series/DEXKOUS  → "Download" → CSV
#   pandas_datareader 사용:  web.DataReader("DEXKOUS", "fred", START)
