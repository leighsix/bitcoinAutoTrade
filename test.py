import pyupbit

access = "9kWM1i9h3ilfmhLxUYn0zfBQQE62quq0XNOmVZqz"          # 본인 값으로 변경
secret = "eUhjngwMJNLQkK0TU8jPS7jsJywL95bXRqbN9zFg"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회