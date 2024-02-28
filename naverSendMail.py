import smtplib
from email.mime.text import MIMEText

# 세션 생성
s = smtplib.SMTP('smtp.naver.com', 587)

# TLS 보안 시작
s.starttls()

# 로그인 인증
s.login('fermas0372', 'dohyun941086~')

# 보낼 메세지 설정
msg = MIMEText('내용 : 본문내용 테스트')
msg['Subject'] = '제목 : 메일 보내기 태스트'
msg['From'] = 'fermas0372@naver.com'
msg['To'] = 'kim46206758@gmail.com'

# 메일 보내기
s.sendmail(msg['From'], msg['To'], msg.as_string())

# 세션 종료
s.quit()